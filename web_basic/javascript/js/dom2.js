const box = document.getElementsByClassName("box");
box[0].style.backgroundColor = "black";

const container = document.getElementsByClassName("container");

const addBox = document.getElementsByClassName("add");
const addBox2 = document.getElementsByClassName("add2");

function addEvent(doc){
    console.log(doc);
    const redButton = document.getElementsByClassName("red-button");
    const blueButton = document.getElementsByClassName("blue-button");
    for(let i = 0; i<doc.length; i++){
        redButton[i].onclick = () =>{
            console.log("red");
            doc[i].style.backgroundColor = "red";
            
        }
        blueButton[i].onclick = () =>{
            doc[i].style.backgroundColor = "blue";
            console.log("blue");
        }
    }
}

addBox[0].onclick = () =>{
    
    container[0].innerHTML += `
        <div class="box"></div>
        <button class="red-button">빨간색</button>
        <button class="blue-button">파란색</button>
    `;
    box[box.length-1].style.backgroundColor = "black";

    addEvent(box);
}

addBox2[0].onclick = () =>{
    const newbox = document.createElement("div");
    const newredButton = document.createElement("button");
    const newBlueButton = document.createElement("button");
    const newredButtonText = document.createTextNode("빨간색");
    const newBlueButtonText = document.createTextNode("파란색");
    const setboxclass = document.createAttribute("class");
    const setRedButtonClass = document.createAttribute("class");
    const setBlueButtonClass = document.createAttribute("class");
    const setBackgroundColor = document.createAttribute("style");

    container[0].appendChild(newbox);
    container[0].appendChild(newredButton);
    container[0].appendChild(newBlueButton);
    newbox.setAttributeNode(setboxclass);
    newbox.setAttribute("class","box");

    newredButton.appendChild(newredButtonText);
    newredButton.setAttributeNode(setRedButtonClass);
    newredButton.setAttribute("class","red-button");

    newBlueButton.appendChild(newBlueButtonText);
    newBlueButton.setAttributeNode(setBlueButtonClass);
    newBlueButton.setAttribute("class","blue-button");

    newbox.setAttributeNode(setBackgroundColor);
    newbox.setAttribute("style","background-color: black");

    const box2 = document.getElementsByClassName("box");

    addEvent(box2);
}
