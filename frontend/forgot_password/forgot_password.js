const API_URL = "http://localhost:5000/api"


document.getElementById("btn_send_mail").addEventListener("click", send_mail)
const backend_verify_code = {}

function send_mail() {
    //we need instantly block otherwise process wil take less then 1 sec and it is enough to click more then 1 time
    document.getElementById("email").disabled = true
    document.getElementById("btn_send_mail").disabled = true
    const email = document.getElementById("email").value
    if(email !== ""){
        fetch(`${API_URL}/forgot_password`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"email": email})
        })
        .then((response) => response.json())
        .then((response_value) => {
            if(response_value["response"] === true){
                const verify_code = response_value["verify_code"]
                backend_verify_code["code"] = verify_code
                create_verify_inputs()
            }
            else{
                document.getElementById("email").disabled = false
                document.getElementById("btn_send_mail").disabled = false
                document.getElementById("email").value = ""
                swal.fire({
                    position: "bottom-end",
                    icon: "error",
                    title: "Invalid email adress.",
                    showConfirmButton: false,
                    timer: 1500
                })
            }
        })
    }
}


function create_verify_inputs() {
    const parent = document.getElementById("new_psw")
    const notice = document.createElement("h4")
    notice.innerHTML = "Verify code sended your email adress..."
    const verify_code_input = document.createElement("input")
    verify_code_input.className = "form-control"
    verify_code_input.id = "verify_code_input"
    verify_code_input.placeholder= "####"
    const password = document.createElement("input")
    password.className = "form-control"
    password.id = "password"
    password.type = "password"
    password.placeholder = "*******"
    const verify_password = document.createElement("input")
    verify_password.className = "form-control"
    verify_password.id = "verify_password"
    verify_password.type = "password"
    verify_password.placeholder = "*******"
    const verify_code_label = document.createElement("label")
    verify_code_label.innerHTML = "Verify Code"
    const password_label = document.createElement("label")
    password_label.innerHTML = "Password"
    const verify_password_label = document.createElement("label")
    verify_password_label.innerHTML = "Verfiy Password"
    const ok_btn = document.createElement("button")
    ok_btn.innerHTML = "Change Password"
    ok_btn.className = "btn btn-success"
    ok_btn.addEventListener("click", post_forgot_form)
    const br = document.createElement("br")

    parent.appendChild(notice)
    parent.appendChild(br)
    parent.appendChild(verify_code_label)
    parent.appendChild(verify_code_input)
    parent.appendChild(password_label)
    parent.appendChild(password)
    parent.appendChild(verify_password_label)
    parent.appendChild(verify_password)
    parent.appendChild(br)
    parent.appendChild(ok_btn)
}


function post_forgot_form() {
    const verify_code = document.getElementById("verify_code_input").value
    const password = document.getElementById("password").value
    const verify_password = document.getElementById("verify_password").value

    if(verify_code == backend_verify_code["code"]){// == and === are differenet stuffs
        if(password === verify_password){
            const req_body = {
                "email": document.getElementById("email").value,
                "new_password": password
            }
            fetch(`${API_URL}/forgot_password_endpoint`, {
                method: "POSt",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(req_body)
            })
            .then((resp) => resp.json())
            .then((resp_val) => {
                console.log(resp_val)
                window.location.replace("http://127.0.0.1:5500/login/login.html")
            })
        }
        else{
            console.log("passwordlar eşleşmedi")
            document.getElementById("verify_password").value = ""
            swal.fire({
                position: "bottom-end",
                icon: "error",
                title: "Passwords must match.",
                showConfirmButton: false,
                timer: 1500
            })
        }
    }
    else{
        console.log("hatalı kod")
        document.getElementById("verify_code_input").value = ""
        swal.fire({
            position: "bottom-end",
            icon: "error",
            title: "Invalid verify code",
            showConfirmButton: false,
            timer: 1500
        })
    }
}
