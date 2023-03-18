

class TodoEvent {
    static #instance = null;
    static getInstance() {
        if (this.#instance == null) {
            this.#instance = new TodoEvent();
        }
        return this.#instance;
    }

    addEventAddTodoClick() {
        const addTodoButton = document.querySelector(".add-todo-button");
        const todoInput = document.querySelector(".todo-input");
        addTodoButton.onclick = () => {
            TodoService.getInstance().addTodo();
            todoInput.value = "";
        }
    }

    addEventAddTodoKeyUp() {
        const todoInput = document.querySelector(".todo-input");
        todoInput.onkeyup = () => {
            if (window.event.keyCode == 13) {
                const addTodoButton = document.querySelector(".add-todo-button");
                addTodoButton.click();
            }
        }
    }

    addEventRemoveTodoClick(){
        const removeButtons = document.querySelectorAll(".content-footer .remove-button");
        removeButtons.forEach((removeButton,index)=>{
            removeButton.onclick = () =>{
                ModalService.getInstance().showRemoveModal(index);
            }
        });
    }

    addEventModifyTodoClick(){
        const ModifyButtons = document.querySelectorAll(".content-footer .modify-button");
        ModifyButtons.forEach((modifybutton, index) => {
            modifybutton.onclick = () =>{
                ModalService.getInstance().showModifyModal(index);
            }
        });
    }
}

class TodoService {
    static #instance = null;
    static getInstance() {
        if (this.#instance == null) {
            this.#instance = new TodoService();
        }
        return this.#instance;
    }

    todoList = null;

    constructor() {
        if(localStorage.getItem("todoList") == null){
            this.todoList = new Array();
        }else{
            // JSON.stringify -> javascript Obj -> JSON
            // JSON.parse -> JSON -> javascript Obj
            this.todoList = JSON.parse(localStorage.getItem("todoList"));
        }
        this.loadTodoList();
    }
    updateLocalStorage() {
        localStorage.setItem("todoList", JSON.stringify(this.todoList));
        this.loadTodoList();
    }

    addTodo() {
        const todoInput = document.querySelector(".todo-input");
        const nowDate = new Date();
        // console.log(`년: ${nowDate.getFullYear()}`);
        // console.log(`월: ${nowDate.getMonth()}`);
        // console.log(`일: ${nowDate.getDate()}`);
        // console.log(`요일: ${nowDate.getDay()}`);
        // console.log(`시: ${nowDate.getHours()}`);
        // console.log(`분: ${nowDate.getMinutes()}`);
        // console.log(`초: ${nowDate.getSeconds()}`);

        const convertDay = (day) => {
            return day == 0 ? "일"
                : day == 1 ? "월"
                    : day == 2 ? "화"
                        : day == 3 ? "수"
                            : day == 4 ? "목"
                                : day == 5 ? "금" : "토";
        }

        const todoObj = {
            todoDate: `${nowDate.getFullYear()}.${nowDate.getMonth() + 1}.${nowDate.getDate()}(${convertDay(nowDate.getDay())})`,
            todoDateTime: `${nowDate.getHours()}:${nowDate.getMinutes()}:${nowDate.getSeconds()}`,
            todoContent: todoInput.value
        }
        this.todoList.push(todoObj);
        this.updateLocalStorage();
        
    }

    loadTodoList() {
        const todoContentList = document.querySelector(".todo-content-list");
        todoContentList.innerHTML = ``;

        this.todoList.forEach(todoObj => {
            todoContentList.innerHTML += `
                <li class="content-container">
                    <div class="content-header">
                        <div class="todo-date">${todoObj.todoDate}</div>
                        <div class="todo-date-time">${todoObj.todoDateTime}</div>
                    </div>
                    <div class="content-main">
                        ${todoObj.todoContent}
                    </div>
                    <div class="content-footer">
                        <button class="modify-button">
                            <i class="fa-regular fa-pen-to-square"></i>
                        </button>
                        <button class="remove-button">
                            <i class="fa-regular fa-trash-can"></i>
                        </button>
                    </div>
                </li>`;
        });
        TodoEvent.getInstance().addEventRemoveTodoClick();
        TodoEvent.getInstance().addEventModifyTodoClick();
    }
    
}