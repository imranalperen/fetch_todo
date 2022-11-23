const API_URL = "http://127.0.0.1:5000/api"


document.getElementById("btn_login").addEventListener("click", check_login_form)
window.addEventListener("keypress", function(event){
    if(event.key == "Enter"){
        event.preventDefault()
        document.getElementById("btn_login").click()
        this.document.getElementById("password").focus()
    }
})


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
        if(response_value["response"] === true){
            const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 1000,
                timerProgressBar: true,
                didOpen: (toast) => {
                  toast.addEventListener('mouseenter', Swal.stopTimer)
                  toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
            })
            Toast.fire({
                icon: 'success',
                title: 'Signed in successfully'
                })
            const access_token = response_value["access_token"]
            console.log(access_token["token"])
            window.localStorage.clear("access_token")
            window.localStorage.setItem("access_token", access_token["token"])
            window.setTimeout(function(){
                window.location.replace("http://127.0.0.1:5500/index/index.html")
            }, 1100)
        }
        else{
            swal.fire({
                position: "bottom-end",
                icon: "error",
                title: "Wrong password or email.",
                showConfirmButton: false,
                timer: 1500
            })
        }
    })
}