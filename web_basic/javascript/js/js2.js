window.onload=()=>{
    console.log("onload test");
    let calc = new Calc("정성현",29);
    calc.showInfo();
    Calc.statcPrint();
    console.log(Calc.testNumber2);

    TestService.getInstace().showTestPrint();
}

function add(a,b){
    return a+b;
}

// Python
// def add(a,b)
//    return a+b

// java
// int add(a,b){
//     return a+b;
// }


console.log(add(10,20));

/*
    javascript의 class

    #은 private을 의미한다.
    자료형은 선언하지 않는다.
    멤버변수 또는 멤버메소드를 참조할 때는 항상 this를 붙인다.
    멤버메소드를 정의할 때는 function 키워드를 사용하지 않는다.
    생성자는 constructor로 정의한다.
*/


class Calc{
    #PI = null;                 // private -> # 없으면 public
    testNumber = 10;
    static testNumber2 = 20;
    name = null;
    age = null;

    constructor(name,age){
        if(typeof name == "string" && typeof age == "number"){
            this.name = name;
            this.age = age;
        }else if(typeof name == "string"){
            this.name = name;
            this.age = null;
        }else if(typeof age == "number"){
            this.name = null;
            this.age = age;
        }else{
            this.name = null;
            this.age = null;
        }
    }

    showInfo(){
        console.log(this.#PI);
        console.log(this.testNumber);
        console.log(this.testNumber2);
        console.log(this.name);
        console.log(this.age)
    }

    static statcPrint(){
        console.log("static test");
    }

}

let calc2 = {
    name: "김준일",
    age: 30,
    showInfo: function(){
        console.log(calc2.name);
        console.log(calc2.age);
    }
}


//javascript 싱글톤
class TestService{
    static #instace = null;

    static getInstace(){
        if(this.#instace == null){
            this.#instace = new TestService();;
        }
        return this.#instace;
    }

    showTestPrint(){
        console.log("싱글톤 테스트");
    }
}