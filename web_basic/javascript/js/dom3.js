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

const statusList = new Array();
const addButton = document.getElementsByClassName("add");
addButton[0].onclick = () =>{
    const todoText = document.getElementsByClassName("todo-text");
    const todoList = document.getElementsByClassName("todo-list");
    todoList[0].innerHTML += `
    <li><span class="todo-content">${todoText[0].value}</span> <button class="ok-button">확인</button> </li>
    `;
    statusList.push(false);
    todoText[0].value = null;
    addEvent()
}
function addEvent(){
    const okButton = document.getElementsByClassName("ok-button");
    const todoContent = document.getElementsByClassName("todo-content");
    for(let i = 0; i<okButton.length; i++){
        okButton[i].onclick = () =>{
            if(statusList[i]){
                todoContent[i].style.color = "black";
                todoContent[i].style.textDecoration = "none";
                statusList[i] = false;
            }else{
                todoContent[i].style.color = "red";
                todoContent[i].style.textDecoration = "Line-through";
                statusList[i] = true;
            }
        }
    }
}