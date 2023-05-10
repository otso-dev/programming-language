const divs = document.getElementsByTagName("div");

console.log(divs[0]);

divs[0].innerHTML += `<button type="button">버튼</button>`;

console.log(divs[0].innerHTML);

const newbutton = document.createElement("button");
const newbuttonText = document.createTextNode("버튼2");
const buttonTypeAttribute = document.createAttribute("type");
newbutton.setAttributeNode(buttonTypeAttribute);
newbutton.setAttribute("type","button");
newbutton.appendChild(newbuttonText);
divs[0].appendChild(newbutton);