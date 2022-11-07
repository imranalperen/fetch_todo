const API_URL = "http://localhost:5000/api"


document.getElementById("btn_login").addEventListener("click", check_login_form)


function check_login_form() {
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    let request_body = {
        "email": email,
        "password": password
    }

    fetch(`${API_URL}/login`, {
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
                position: "bottom-end",
                icon: "success",
                title: "Success",
                text: "Successfuly logged in",
                showConfirmButton: false,
                timer: 1100
            })
        }
        else{
            swal.fire({
                position: "bottom-end",
                icon: "error",
                title: "Wrong password or email.",
                showConfirmButton: false,
                timer: 1000
            })
        }
    })
}