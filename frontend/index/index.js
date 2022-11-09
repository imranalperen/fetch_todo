const API_URL = "http://localhost:5000/api"
const access_token = window.localStorage.getItem("access_token")


document.getElementById("btn_add_todo").addEventListener("click", add_todo_db)
document.getElementById("btn_logout").addEventListener("click", function () {
    window.localStorage.clear()
    window.location.replace("http://127.0.0.1:5500/frontend/login/login.html")
})

list_todos()


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
        if(data["response"] === true){
            refresh_todos(data["todo_list"])
        }
        else{
            console.log("there is no todo")
        }
    })
}


function refresh_todos(todos) {
    document.getElementById("todo_table_body").innerHTML = ""
    for (let i = 0; i < todos.length; i++){
        const table = document.getElementById("todo_table_body")
        const tr_element = document.createElement("tr")
        const td_text_element = document.createElement("td")
        const td_done_element = document.createElement("td")
        const td_update_element = document.createElement("td")

        const done_button = document.createElement("button")
        done_button.className = "btn btn-success"
        done_button.id = "btn_done"
        done_button.addEventListener("click", done_todo)

        const update_button = document.createElement("button")
        update_button.className = "btn btn-warning"
        update_button.id = "btn_update"
        update_button.addEventListener("click", update_todo)

        const td_hidden = document.createElement("td")
        td_hidden.id = "todo_id"
        td_hidden.style.display = "none"
        td_hidden.innerHTML = todos[i]["id"]

        td_text_element.innerHTML = todos[i]["todo_body"]
        done_button.innerHTML = "Done"
        update_button.innerHTML = "Update"

        //show todolar aktif ise aç kapa
        if(todos[i]["done"]){
            done_button.disabled = true
            update_button.disabled = true
            td_text_element.style.color = "#D8D9CF"
        }

        td_done_element.appendChild(done_button)
        td_update_element.appendChild(update_button)

        tr_element.appendChild(td_text_element)
        tr_element.appendChild(td_done_element)
        tr_element.appendChild(td_update_element)
        tr_element.appendChild(td_hidden)

        table.appendChild(tr_element)
        document.getElementById("todo_body").value = ""
    }
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
        if(response_value["response"] === true){
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


function done_todo() {
    let todo_id = this.parentElement.parentElement.lastChild.innerHTML
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Done it'
      }).then((result) => {
        if (result.isConfirmed) {
            done_todo_endpoint(todo_id)
        }
      })
}


async function done_todo_endpoint(todo_id) {
    await fetch(`${API_URL}/index/done_todo`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            "Access-Token": access_token
        },
        body: JSON.stringify({"todo_id": todo_id})
    })
    .then((response) => response.json())
    .then((response_value) => {
        if(response_value["response"] === true){
            list_todos()
            Swal.fire({
                position: "bottom-end",
                icon: "success",
                title: "Deleted",
                text: "Your file has been deleted.",
                showConfirmButton: false,
                timer: 1100
            })
        }
    })
}


function update_todo() {
    let old_body = this.parentElement.parentElement.firstChild.innerHTML
    let todo_id = this.parentElement.parentElement.lastChild.innerHTML
    Swal.fire({
        title: "Update",
        input: "text",
        inputValue: old_body,
        showCancelButton: true,
        confirmButtonText: "Update",
        showLoaderOnConfirm: true,
        preConfirm: (update_body) => update_body_endpoint(update_body, todo_id)
    })
}


function update_body_endpoint(update_body, todo_id) {
    let request_body = {
        "update_body": update_body,
        "todo_id": todo_id
    }
    fetch(`${API_URL}/index/update_todo`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
            "Access-Token": access_token
        },
        body: JSON.stringify(request_body)
    })
    .then((response) => response.json())
    .then((response_value) => {
        if(response_value["response"] === true){
            list_todos()
            Swal.fire({
                position: "bottom-end",
                icon: "success",
                title: "Updated",
                text: "Your file updated successfully.",
                showConfirmButton: false,
                timer: 1000
            })
        }
        else{
            console.error("Error", error)
        }
    })
}