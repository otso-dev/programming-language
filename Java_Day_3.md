
# Java_Day_3

## 연산자
항과 연산자  
ex) (5>3) ? 1:0  
연산에 사용되어지는 기호를 연산자라고 한다.  
항은 연산에 사용되어지는 값을 항이라 한다.  

## 단항 연산자
ex) ++num;, --num;
항이 하나인 연산자

## 이항 연산자
항이 두개인 연산자
ex) num1 + num2;
ex) num3 - num4;

## 삼항 연산자
항이 세개인 연산자
ex) (5>3) ? 1:0;  
ex) (100 > 1000) ? "참" : "거짓";

## 대입 연산자
변수에 값을 대입하는 연산자
ex) int age = 26;

## 부호 연산자
- **+** ex) +(6)  
- **-** ex) -(6)
양수와 음수를 표현하기위해 사용한다.

## 산술 연산자
- + : 두 항을 더한다.  
- - : 앞에 있는 항에서 뒤에 있는 항을 뺍니다.  
- * : 두 항을 곱한다.  
- / : 앞에 있는 항에서 뒤에있는 항을 나누어 몫을 구합니다.  
- % : 앞에 있는 항에서 뒤에있는 항을 나누어 나머지를 구합니다.

## 증감 연산자
- **++** ex) iNum = ++Num;, iNum = Num++;  
- **--** ex) iNum = --Num;, iNum = Num--;  
전위와 후위의 차이
전위 계산을 먼저함
후위 계산을 나중에 함

## 관계 연산자
- > : 왼쪽 항이 크면 참, 아니면 거짓
- < : 왼쪽 항이 작으면 참, 아니면 거짓
- >= : 왼쪽 항이 크거나 같으면 참, 아니면 거짓
- <= : 왼쪽 항이 작거나 같으면 참, 아니면 거짓
- == : 두 항이 같으면 참, 아니면 거짓
- != : 두 항이 다르면 참, 아니면 거짓

## 복합 대입 연산자
- +=
- -=
- *=
- /=
- %=
## 조건 연산자
조건식 ? 결과1: 결과2
조건식의 결과가 참이면 결과1를 반환, 거짓이면 결과2를 반환

## 문자열 
여러 문자를 하나로 묶은 것  
String class -> String은 기본 자료형이 아닌 class이다.  
API에서 제공하는 String class라는 것을 이용한다.  
문자 자료형 char은 다른 특징을 가지고 있다.  
'A' -> 문자, "Hello World" -> 문자열  
문자열 합치기는 + 연산자로 합칠 수 있다.
## 입력
Scanner Class
콘솔에서 키보드 입력을 받는 클래스

## Scanner Class Method

![Scanner_Method](https://user-images.githubusercontent.com/51119920/211741896-641fc4f4-abd3-4263-b032-55565d4b3383.png)


```java
package j05.입력;

import java.util.Scanner;

public class Input2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		System.out.print("문자열1: ");
		String str1 = scanner.nextLine();//이것을 제외하고 띄어쓰기 허용안함
		System.out.print("문자열2: ");
		String str2 = scanner.next();
		System.out.print("정수 : ");
		int number1 = scanner.nextInt();
		System.out.print("실수 : ");
		double number2 = scanner.nextDouble();
		
		System.out.println("문자열1 " + str1);
		System.out.println("문자열2 " + str2);
		System.out.println("정수 " + number1);
		System.out.println("실수 " + number2);
		
		
	}

}
```


```java
package j05.입력;

import java.util.Scanner;

public class Input3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in); //system => 운영체제를 뜻함
		
		String str1 = null;
		int age = 0;
		String str2 = null;
		String str3 = null;
		
		System.out.print("이름 : ");
		str1 = scanner.next();//nextLine() 함수를 제외하고 엔터와 스페이스바를 포함하지 않는다. 그러므로
		//버퍼안에 문자열이나 스페이스바 엔터가 남아있기 때문에 한번더 nextLine()해준다.
		System.out.print("나이 :  ");
		age = scanner.nextInt();
		scanner.nextLine();
		System.out.print("주소 : ");
		str2 = scanner.nextLine();
		System.out.print("연락처 : ");
		str3 = scanner.next();
		
		System.out.println("사용자의 이름은 " + str1 +"이고 "+ "나이는 " + age +"살입니다.");
		System.out.println("주소는 " + str2 + "에 거주중입니다.");
		System.out.println("연락처는 " + str3 + " 입니다");
		
	}

}
```

```java
package j05.입력;

import java.util.Scanner;

public class Input4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in); //system => 운영체제를 뜻함
		
		int a = 0;
		int b = 0;
		int c = 0;
		
		int max = 0;
		int min = 0;
		
		System.out.print("정수 3개 입력 : ");
		a = scanner.nextInt();
		b = scanner.nextInt();
		c = scanner.nextInt();
		
		//max = a > b ? a : b > c ? b : c > a ? c : 0;
		//min = a < b ? a : b < c ? b : c < a ? a : 0;
		
		max = a;
		max = b > max ? b : max;
		max = c > max ? c : max;
		
		min = a;
		min = b < min ? b : min;
		min = c < min ? c : min;
		
		System.out.println("a : " + a);
		System.out.println("b : " + b);
		System.out.println("c : " + c);
		
		
		
		System.out.println("최대값: " + max);
		System.out.println("최소값: " + min);
		
	}

}
```

## 조건문

### if

```java
package j06_조건;

public class Conditional1 {

	public static void main(String[] args) {
		
		int num = 10;
		int num2 = 5;
		
		if(num > num2)
		{ 
			System.out.println("num이 num2보다 큽니다.");
			System.out.println("num" + num);
		}else if (num == num2) {
			System.out.println("num과 num2가 같습니다.");
		} else {
			System.out.println("num이 num2보다 작습니다.");
		}
		
	}

}

```
```java

package j06_조건;

import java.util.Scanner;

public class Conditional2 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		int a = 0;
		int b = 0;
		int c = 0;
		int max = 0;
		int min = 0;
		
		System.out.println("정수 3개 입력 : ");
		a = scanner.nextInt();
		b = scanner.nextInt();
		c = scanner.nextInt();
		
		max = a;
		min = a;
		if(b > max)max = b;
		if(c > max) max = c;
		
		if(b < min) min = b;
		if(c < min) min = c;
		
		System.out.println("최대값 : " + max);
		System.out.println("최소값 : " + min);
		
	}

}
```

```java
package j06_조건;

import java.util.Scanner;

public class Conditional3 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		int score = 0;
		String grade = null;
		
		System.out.print("점수 입력 : ");
		score = scanner.nextInt();
		
		//0점보다 작거나 100점보다 크면 계산불가
		//90 ~ 100 A
		//80 ~ 89 B
		//70 ~ 79 C
		//60 ~ 69 D
		//0 ~ 59 F
		
		//내 코드
		if(score > 89) {
			//if(score > 94) grade = "A+";
			 grade = "A";
		}
		else if(score > 79) {
			//if(score > 84) grade = "B+";
			 grade = "B";
		}
		else if(score > 69) {
			//if(score > 74) grade = "C+";
			 grade = "C";
		}
		else if(score > 59) {
			//if(score > 64) grade = "D+";
			 grade ="D";
		}
		else {
			//if(score > 54) grade = "F+";
			 grade ="F";
		}
		
		if(score % 10 > 4 || score == 100) {//F학점은 +가 없다라는 조건을 추가 안함
			grade = grade + "+";
		}
		
		if(score > 0 && score < 101)
		System.out.print("점수(" + score + "): " + grade + "학점");
		else System.out.println("계산 불가");
		
		//강사코드
		if(score < 0 || score > 100) {
			grade = null;
		}else if(score > 89) {
			grade = "A";
		}else if(score > 89) {
			grade = "B";
		}else if(score > 89) {
			grade = "C";
		}else if(score > 89) {
			grade = "D";
		}else {
			grade = "F";
		}
		
		if((score > 59 && score < 101) && (score % 10 > 4 || score == 100)) {
			grade += "+";
		}
		
		if(grade == null) {
			System.out.println("계산불가");
		}else {
			System.out.print("점수(" + score + "): " + grade + "학점");
		}
		
	}

}
```


### switch문


```java
package j06_조건;

public class Switch1 {

	public static void main(String[] args) {
		String select = "B선택";
		
		switch(select) {
			case "A선택" : 
				System.out.println("PC(A)를 연결합니다.");
				break;
			case "B선택" : 
				System.out.println("PC(B)를 연결합니다.");
				break;
			case "C선택" : 
				System.out.println("PC(C)를 연결합니다.");
				break;
			case "D선택" : 
				System.out.println("PC(D)를 연결합니다.");
		}

	}

}
```
## 반복문
### for문

```java
package j07_반복;

public class Loop1 {

	public static void main(String[] args) {
		//지역 변수 = 지역 내에서만 사용가능
		//전역 변수 = 전역으로 사용가능
		int sum = 0;
		
		for(int i = 0; i < 100; i++) {
			sum += i + 1; 
		}
		System.out.println("1 ~ 100까지 총합: " + sum);

	}

}
```

```java
package j07_반복;

import java.util.Scanner;

public class Loop2 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int startNumber = 0;
		int endNumber = 0;
		int sum = 0;
		
		System.out.print("시작 : ");
		startNumber = scanner.nextInt();
		
		System.out.println("끝 : ");
		endNumber = scanner.nextInt();
		
		//내 코드
		for(int i = 0; i < endNumber + 1; i++) {
				if(i > startNumber - 1) {
					sum += i;
				}
		}
		
		
		//강사코드
		for(int i = 0; i < endNumber - startNumber + 1; i++)
		{
			sum += i + startNumber;
		}
		System.out.println("startNumber ~ endNumber까지 총합: " + sum);
		//반복횟수를 생각해보자.

	}

}
```

```java
package j07_반복;

import java.util.Scanner;

public class Loop3 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int count = 0;
		int sum = 0;
		int total = 0;
		System.out.print("반복횟수 : ");
		count = scanner.nextInt();
		
		for(int i = 0; i < count; i++) {
			int num1 = 0;
			int num2 = 0;
			sum = 0;
			System.out.println( i + 1+"번 반복");
			System.out.print("a : ");
			num1 = scanner.nextInt();
			System.out.print("b : ");
			num2 = scanner.nextInt();
			sum = num1 + num2;
			System.out.println(i + 1 + "번 합 : " + sum);
			System.out.println();
			total += sum;
		}
		System.out.println("총합 : " + total);
	}

}
````

```java

### 별찍기

package j07_반복;

public class Star1 {

	public static void main(String[] args) {
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < i + 1; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < 10 - i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < 9 - i; j++) {
				System.out.print(" ");
			}
			for(int j = 0; j < i + 1; j++) {
				System.out.print("*");
			}
			
			for(int j = 0; j < i; j++) {
				System.out.print("*");
			}
			
			System.out.println();
		}
		
	}

}
```

