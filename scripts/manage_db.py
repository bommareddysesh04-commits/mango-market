"""
One-off DB maintenance script for Mango Market Platform
- Backs up the SQLite database file
- Removes duplicate `order_id` entries from `weighments` (keeps earliest `created_at`)
- Drops any non-unique index that targets `order_id` on `weighments`
- Creates a unique index `ux_weighments_order_id` on `weighments(order_id)`

Usage:
    python manage_db.py --db instance/database.db

Run this script from the repository root (where `instance/` is located).
"""

import argparse
import shutil
import sqlite3
import sys
import time
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def backup_db(db_path: Path) -> Path:
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    backup_path = db_path.with_name(f"{db_path.stem}.backup-{timestamp}{db_path.suffix}")
    shutil.copy2(db_path, backup_path)
    return backup_path


def find_duplicate_order_ids(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("SELECT order_id, COUNT(*) as c FROM weighments GROUP BY order_id HAVING c > 1")
    return [row[0] for row in cur.fetchall()]


def delete_duplicates_keep_earliest(conn: sqlite3.Connection, order_id: str):
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM weighments WHERE order_id=? ORDER BY created_at ASC, id ASC",
        (order_id,),
    )
    ids = [r[0] for r in cur.fetchall()]
    if len(ids) <= 1:
        return 0
    keep = ids[0]
    to_delete = ids[1:]
    cur.executemany("DELETE FROM weighments WHERE id=?", [(i,) for i in to_delete])
    return len(to_delete)


def drop_non_unique_order_index(conn: sqlite3.Connection):
    cur = conn.cursor()
    # List indexes on weighments
    cur.execute("PRAGMA index_list('weighments')")
    indexes = cur.fetchall()  # (seq, name, unique, origin, partial)
    dropped = []
    for idx in indexes:
        name = idx[1]
        unique = idx[2]
        if unique:  # skip unique indexes
            continue
        # Inspect index columns
        cur.execute(f"PRAGMA index_info('{name}')")
        cols = [r[2] for r in cur.fetchall()]  # (seqno, cid, name)
        if 'order_id' in cols:
            logger.info(f"Dropping non-unique index '{name}' on weighments(order_id)")
            cur.execute(f"DROP INDEX IF EXISTS '{name}'")
            dropped.append(name)
    return dropped


def create_unique_index(conn: sqlite3.Connection):
    cur = conn.cursor()
    logger.info("Creating unique index 'ux_weighments_order_id' ON weighments(order_id)")
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS ux_weighments_order_id ON weighments(order_id)")


def run_migration(db_path: Path):
    if not db_path.exists():
        logger.error(f"Database file not found: {db_path}")
        return 2

    logger.info(f"Backing up database: {db_path}")
    backup_path = backup_db(db_path)
    logger.info(f"Backup created at: {backup_path}")

    conn = sqlite3.connect(str(db_path))
    try:
        conn.execute('PRAGMA foreign_keys = OFF')
        conn.isolation_level = None
        conn.execute('BEGIN')

        duplicates = find_duplicate_order_ids(conn)
        total_deleted = 0
        logger.info(f"Found {len(duplicates)} duplicate order_id groups")
        for oid in duplicates:
            deleted = delete_duplicates_keep_earliest(conn, oid)
            if deleted:
                logger.info(f"Deleted {deleted} duplicate rows for order_id={oid}")
            total_deleted += deleted

        dropped = drop_non_unique_order_index(conn)
        if dropped:
            logger.info(f"Dropped indexes: {dropped}")

        try:
            create_unique_index(conn)
        except sqlite3.IntegrityError as e:
            logger.error("Failed to create unique index - duplicates may still exist: %s", e)
            conn.execute('ROLLBACK')
            return 3

        conn.execute('COMMIT')
        logger.info(f"Migration completed. Total duplicate rows removed: {total_deleted}")
        return 0
    except Exception as e:
        logger.exception("Migration failed: %s", e)
        try:
            conn.execute('ROLLBACK')
        except Exception:
            pass
        return 1
    finally:
        conn.execute('PRAGMA foreign_keys = ON')
        conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DB maintenance script for Mango Market')
    parser.add_argument('--db', default='instance/database.db', help='Path to the SQLite DB file')
    args = parser.parse_args()
    db_path = Path(args.db)
    code = run_migration(db_path)
    sys.exit(code)
