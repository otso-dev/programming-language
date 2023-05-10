window.onload = () =>{
    
}

function a (){
    console.log("a 함수 호출");
}

a();

console.log(typeof a);

//화살표 함수 -> 화살표가 function이라고 생각하면 쉽다.
let b = (f) => {
    console.log("test가 프린트 되기 전에 무조건 실행");
    f();
}

b(a)

b(function(){console.log("test")});

//정의와 동시에 같이 호출하는 함수 -> 즉시 실행 함수
(function(){console.log("test2")}());