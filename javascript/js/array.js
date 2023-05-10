let numbers1 = [1,2,3,4,5];
let numbers2 = [6,7,8,9,10];
let numbers3 = new Array();

let numbers4 = numbers1.concat(numbers2);

console.log(numbers1);
console.log(typeof numbers2);
console.log(typeof numbers3);
console.log(typeof numbers4);
console.log(numbers4);

function odd(num){
    return num % 2 != 0;
}

let numbers5 = numbers4.filter(odd);
console.log(numbers5);

let numbers6 = numbers4.filter(n => n % 2 != 0);
console.log(numbers6);

for(let i = 0; i<numbers5.length; i++){
    console.log("i: " + numbers5[i]);
}

for(let num of numbers5){
    console.log(`forEach: ${num}`);//표현식
}

numbers5.forEach(n => console.log(`ArrayforEach: ${n}`));

console.log(numbers5.indexOf(5));
console.log(numbers5.lastIndexOf(2));
console.log(numbers5.join(";"));
console.log(numbers5.push(11));
console.log(numbers5);
console.log(numbers5.unshift(13));
console.log(numbers5);
console.log(numbers5.pop());//맨 마지막 요소 제거.last index delete stack과 비슷.
console.log(numbers5);
console.log(numbers5.splice(2,1,15,17));//start,count,insert 시작지점부터 count만큼 지울수 있고 중간에 insert가 가능, array추가도 가능
console.log(numbers5);
console.log(numbers5.slice(3,6));//python slice index와 같음
console.log(numbers5);

function compare(n1,n2){
    if(n1 > n2) return 1;
    if(n1 === n2) return 0;
    if(n1 < n2) return -1;
}

console.log(numbers5.sort((a,b)=> a - b));
console.log(numbers5.reverse());
console.log(numbers5.toString());


const backButton = document.getElementsByTagName("button");
backButton[0].onclick = ()=>{
    history.back();
}