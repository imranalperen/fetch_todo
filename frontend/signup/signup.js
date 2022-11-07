const API_URL = "http://localhost:5000/api"


document.getElementById("btn_sign_up").addEventListener("click", check_sign_up_form)


function check_sign_up_form() {
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    const verify_password = document.getElementById("verify_password").value

    if(email === "" || password === "" || verify_password === ""){
        swal.fire({
            title: "Warning",
            text: "Please fill all the form...",
            icon: "warning",
        })
    }
    else if(password !== verify_password){
        swal.fire({
            title: "Verify Passwrod",
            text: "Password and verify password fileds must be same...",
            icon: "warning",
        })
        document.getElementById("verify_password").value = ""
    }
    else{
        post_signup_form()
    }
}


function post_signup_form() {
    let request_body = {
        "email": document.getElementById("email").value,
        "password": document.getElementById("password").value,
        "verify_password": document.getElementById("verify_password").value
    }
    
    fetch(`${API_URL}/signup`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(request_body)
    })
    .then((response) => response.json())
    .then((response_value) => {
        if(response_value["response"] === "success"){
            swal.fire({
                position: "top-end",
                icon: "success",
                title: "Succes",
                showConfirmButton: false,
                timer: 1100
            })
            .then((redirect_login) => {
                if (redirect_login){
                    window.location.replace("http://127.0.0.1:5500/frontend/login/login.html")
                }
            })
        }
        else{
            swal.fire({
                title: "Warning",
                text: "Invalid email. This email already registered.",
                icon: "error"
            })
            document.getElementById("email").value = ""
        }
    })
    .catch((error) => {
        console.error("Error: ", error)
    })
}