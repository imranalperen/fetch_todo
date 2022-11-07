const API_URL = "http://localhost:5000/api"
const access_token = window.localStorage.getItem("access_token")


document.getElementById("btn_add_todo").addEventListener("click", add_todo_db)
document.getElementById("btn_logout").addEventListener("click", function () {
    window.localStorage.clear()
    window.location.replace("http://127.0.0.1:5500/frontend/login/login.html")
})


function list_todos() {
    fetch(`${API_URL}/index/list_todo`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Access-Token": access_token
        }
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
    })
}



async function add_todo_db() {
    const todo_body = document.getElementById("todo_body").value
    let request_body = {"todo": todo_body}

    await fetch(`${API_URL}/index/add_todo`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Access-Token": access_token
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
                text: "Todo added the list",
                showConfirmButton: false,
                timer: 1100
            })
            document.getElementById("todo_body").value = ""
            list_todos()
        }
        else{
            console.error("Error when todo inserting db")
        }
    })
}