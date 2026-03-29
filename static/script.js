function login() {
    let email = document.querySelector("input[type='email']").value;
    let password = document.querySelector("input[type='password']").value;

    if (email !== "" && password !== "") {
        localStorage.setItem("isLoggedIn", "true");
        window.location.href = "/home";
    } else {
        alert("Please enter email and password");
    }
}

function signup() {
    localStorage.setItem("isLoggedIn","true")
    window.location.href = "/home";
}

function analyze_job() {
    window.location.href = "/detect";
}

function home() {
    window.location.href = "/";
}

function report() {
    window.location.href = "/report";
}

// check login
const currentPage = window.location.pathname;

if (localStorage.getItem("isLoggedIn") !== "true" && currentPage !== "/login") {
    window.location.href = "/login";
}
function logout() {
    localStorage.removeItem("isLoggedIn");
    window.location.href = "/login";
}