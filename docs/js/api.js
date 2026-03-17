// ====== API CONFIGURATION ======
const API_BASE_URL = "https://mango-market-qssw.onrender.com";

// Expose current base for debugging
window.API_BASE_URL = API_BASE_URL;

// Expose helper so pages can check backend status & trigger retry
window.ensureApiReady = () => Promise.resolve(API_BASE_URL);

// ====== API CLIENT HELPER ======
const APIClient = {
    getHeaders: function() {
        const headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        };
        const token = localStorage.getItem('session_token');
        if (token) {
            headers['Authorization'] = 'Bearer ' + token;
        }
        return headers;
    }
};

// ====== REQUEST HANDLER ======
async function apiFetch(endpoint, opts = {}) {
    return fetch(`${API_BASE_URL}${endpoint}`, opts);
}

async function postData(endpoint, data) {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: 'POST',
            headers: APIClient.getHeaders(),
            credentials: 'include',
            body: JSON.stringify(data)
        });
            method: 'POST',
            headers: APIClient.getHeaders(),
            credentials: 'include',
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            let errorMsg = `Server error: ${response.status} ${response.statusText}`;
            try {
                const errData = await response.json();
                if (errData && errData.message) errorMsg = errData.message;
            } catch (e) {}
            return { success: false, message: errorMsg };
        }

        const json = await response.json();
        if (json && json.session_token) localStorage.setItem('session_token', json.session_token);
        return { success: true, ...json };

    } catch (error) {
        console.error("API Network Error:", error);
        return { success: false, message: "Network error. Is the server running? Check console for details." };
    }
}
