const API_URL = "http://127.0.0.1:5000/api"


document.getElementById("btn_sign_up").addEventListener("click", check_sign_up_form)
window.addEventListener("keypress", function(event){
    if(event.key == "Enter"){
        event.preventDefault()
        document.getElementById("btn_sign_up").click()
        this.document.getElementById("email").click()
    }
})


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
            position: "bottom-end",
            icon: "error",
            title: "Password and verify password must match.",
            showConfirmButton: false,
            timer: 1500
        })
        document.getElementById("verify_password").value = ""
    }

    else{
        validation(email, password)
    }
}



function validation (email, password) {
    if (validate_email(email) === false){
        document.getElementById("email").value = ""
        swal.fire({
            position: "bottom-end",
            icon: "error",
            title: "Invalid email adress.",
            showConfirmButton: false,
            timer: 1500
        })
        return false
    }
    
    else if (validate_password(password) === false){
        document.getElementById("password").value = ""
        document.getElementById("verify_password").value = ""
        swal.fire({
            position: "bottom-end",
            icon: "error",
            title: "password shuld be 4-12 character",
            showConfirmButton: false,
            timer: 1500
        })
        return false
    }
    else{
            post_signup_form()
    }
}



function validate_password(password){
    if(password.length >= 12 || password.length < 4){
        return false
    }
    return true
}


function validate_email(emailAddress) {
    var sQtext = '[^\\x0d\\x22\\x5c\\x80-\\xff]';
    var sDtext = '[^\\x0d\\x5b-\\x5d\\x80-\\xff]';
    var sAtom = '[^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+';
    var sQuotedPair = '\\x5c[\\x00-\\x7f]';
    var sDomainLiteral = '\\x5b(' + sDtext + '|' + sQuotedPair + ')*\\x5d';
    var sQuotedString = '\\x22(' + sQtext + '|' + sQuotedPair + ')*\\x22';
    var sDomain_ref = sAtom;
    var sSubDomain = '(' + sDomain_ref + '|' + sDomainLiteral + ')';
    var sWord = '(' + sAtom + '|' + sQuotedString + ')';
    var sDomain = sSubDomain + '(\\x2e' + sSubDomain + ')*';
    var sLocalPart = sWord + '(\\x2e' + sWord + ')*';
    var sAddrSpec = sLocalPart + '\\x40' + sDomain; // complete RFC822 email address spec
    var sValidEmail = '^' + sAddrSpec + '$'; // as whole string
  
    var reValidEmail = new RegExp(sValidEmail);
  
    return reValidEmail.test(emailAddress);
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
        if(response_value["response"] === true){
            swal.fire({
                position: "top-end",
                icon: "success",
                title: "Succes",
                showConfirmButton: false,
                timer: 1100
            })
            .then((redirect_login) => {
                if (redirect_login){
                    window.location.replace("http://127.0.0.1:5500/login/login.html")
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