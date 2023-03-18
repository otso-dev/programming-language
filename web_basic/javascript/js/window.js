// window.alert(); window 생략가능
console.log(document);// document  => html object
console.log(location.href)
// location.href = "https://www.naver.com";

const naverButton = document.getElementsByTagName("button");
naverButton[0].onclick = () =>{
    // location.href = "https://www.naver.com";
    location.replace("https://www.naver.com");
}

naverButton[1].onclick = () =>{
    location.href = "http://127.0.0.1:5500/javascript/array.html";
}