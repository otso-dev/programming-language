/*
    1. 추가버튼 클릭시 input에 들어있는 value의 값을 list에 추가
    2. 확인버튼 클릭시 todo-content의 색상을 red로 변경, 취소선 적용
    3. 확인버튼 다시 클릭시 todo-content의 색상을 black로 변경, 취소선 미적용
*/

//내 코드
/*
const button = document.getElementsByClassName("add");

const todoList = document.getElementsByClassName("todo-list");

button[0].onclick = () =>{
    todoList[0].innerHTML += `
    <li><span class="todo-content">${document.getElementsByClassName("todo-text")[0].value}</span> <button class="ok-button">확인</button> </li>
    `
    console.log("add");
    let check = true;
    const okButton = document.getElementsByClassName("ok-button");
    const todoContent = document.getElementsByClassName("todo-content");
        for(let i = 0; i <todoContent.length; i++){
            okButton[i].onclick = () =>{
                if(check){
                    todoContent[i].style.color = "red";
                    todoContent[i].style.textDecoration = "Line-through";
                }else{
                    todoContent[i].style.color = "black";
                    todoContent[i].style.textDecoration = "none";
                }
                check = !check;
            }
    }
}
*/

const addButton = document.getElementsByClassName("add");
addButton[0].onclick = () =>{
    const todoText = document.getElementsByClassName("todo-text");
    const todoList = document.getElementsByClassName("todo-list");
    const li = document.createElement("li");
    if(todoText[0].value != ''){
        li.innerHTML = `<li><input type="checkbox" class="ok-check"> <span class="todo-content">${todoText[0].value}</span> </li>`;
        todoList[0].appendChild(li)
        todoText[0].value = null;
        addEvent()
    }
}
function addEvent(){
    const okCheck = document.getElementsByClassName("ok-check");
    const todoContent = document.getElementsByClassName("todo-content");
    for(let i = 0; i<okCheck.length; i++){
        okCheck[i].onchange = () =>{
            if(okCheck[i].checked){
                todoContent[i].style.color = "red";
                todoContent[i].style.textDecoration = "Line-through";
            }else{
                todoContent[i].style.color = "black";
                todoContent[i].style.textDecoration = "none";
            }
        }
    }
}