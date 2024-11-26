class Network {

    static BASE_URL = "http://127.0.0.1:8000/";
    static instance = null;
    static getInstance() {
        if (!Network.instance) {
            Network.instance = new Network();
            Network.instance.BASE_URL = Network.BASE_URL;
        }
        return Network.instance;
    }

    request(url, method, data = {}) {
        const path = `${Network.BASE_URL}${url}`;
        switch (method.toLowerCase()) {
            case "get":
                return this.get(path);
            case "post":
                return this.post(path, data);
            default:
                return Promise.reject(new Error("Unsupported request method"));
        }
    }

    ajaxRequest(url, method, data = {}) {
        return new Promise((resolve, reject) => {
            $.ajax({
                url: url,
                type: method.toUpperCase(),
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: data,
                success: (response) => {
                    data = JSON.parse(response);
                    console.log(data);
                    resolve({ status: "response", data: data });
                    return { status: "response", data: data };
                },
                error: (jqXHR, textStatus, errorThrown) => {
                    return reject({ status: "error", message: textStatus, details: errorThrown });
                }
            });
        });
    }

    get(url) {
        return this.ajaxRequest(url, "GET");
    }

    post(url, data) {
        return this.ajaxRequest(url, "POST", data);
    }
}

const network = Network.getInstance();

function isAlphanumeric(str) {
    // 正则表达式匹配数字和字母
    const regex = /^[a-zA-Z0-9]+$/;
    return regex.test(str);
}
