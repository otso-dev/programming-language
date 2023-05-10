# Java_Day_2


# 변수
**변수 : 변하는 수  
자료형 + 변수명 => ex) int level;**  

## 변수명 제약사항
1. 변수 이름은 영문자나 숫자를 사용할 수 있고 구분하며, 특수 문자 중에는 $, _ 만 사용할 수 있다.  
2. 변수 이름은 숫자로 시작할 수 없다.  
3. 자바에서 이미 사용 중인 예약어는 사용할 수 없다.(키워드) 

## 변수와 메모리의 관계
변수는 컴퓨터 내부의 메모리 공간에 저장된다.

## 컴퓨터에서 수를 표현하는 방법

![진수](https://user-images.githubusercontent.com/51119920/211734142-b7bafe0b-48b3-4922-8e07-a7f46bafea58.png)

## 자료형 크기

![자료형 크기](https://user-images.githubusercontent.com/51119920/211733648-0fa33104-8680-4904-a88e-58c19448618c.png)

## 데이터 단위
1. 비트(bit)  
0 또는 1의 값을 저장하기 위한 최소단위  
1bit가 가지는 총 경우의 수는 0과1, 두 가지이다.  
2. 바이트(Byte)  
8bit를 한 단위로 표준화한 요량 단위  
1byte가 나타낼 수 있는 총 경우의 수  
00000000 ~ 11111111 -> 2^7개

## 정수 자료형
- byte   
- short  
- int  
- long  

## 문자 자료형
- char
- 아스키코드 -> 'A' == 65 컴퓨터는 각각의 문자를 숫자형태로 기억하고 있다.

## 실수 자료형
- flaot
- double

## 논리 자료형
- true
- false


## 변수 선언과 초기화

```java

package j02_변수;

public class Variable1 {

	public static void main(String[] args) {
		int num = 0; // 선언과 초기화를 동시에 명시
		
		int num2; // 4byte의 메모리 공간을 할당할 것이고 그 공간의 이름을 num2라 하겠다! 선언
		num2 = 10; // num2변수명을 가진 메모리 공간의 데이터를 비우고 10의 값을 대입하겠다. 초기화
		
		
		System.out.println(num + 1);
		

	}

}

```

## char 자료형
```java
package j02_변수;

public class Variable2 {

	public static void main(String[] args) {
		char firstName1 = '가';
		char firstName2 = '일';
		
		char alphabetA = 'A';
		
		System.out.println("김" + firstName1 + firstName2);
		System.out.println("알파벳A: " + alphabetA);
		
		System.out.println(alphabetA + 'B');
		System.out.println(alphabetA);
		System.out.println("\uAC00");
		System.out.println(firstName1 + 0);

	}

}

```

## 상수와 final

상수 : 변하지 않는 수
```java

package j02_변수;

public class Variable3 {

	public static void main(String[] args) {
		// 상수: 자료형 앞에 final이 붙는다.
		// 상수는 상수명을 무조건 대문자로 사용을 한다.
		final int NOW_AGE = 0;
		
		System.out.println(NOW_AGE);

	}

}
```

## 형변환
**자료형을 다른 자료형으로 변환시키는 것**
## 업캐스팅

**문자->정수->실수**
값이 작은 범위에서 큰 범위로의 형변환  
묵시적 형 변환(형 변환 타입 생략이 가능)

## 다운 캐스팅
**실수->정수->문자**
값이 큰 범위에서 작은 범위로의 형변환  
명시적 형 변환(형 변환 타입 생략 불가능)

```java
package j03_형변환;

public class Casting1 {

	public static void main(String[] args) {
		char a = 'a';
		int num1 = a;//char 자료형을 int형으로 형변환
		
		System.out.println((double) a);
		System.out.println((char) 97.0);
		System.out.println((byte) 300);
		

	}

}

```

```java
package j03_형변환;

public class Casting2 {
	public static void main(String[] args) {
		char char_a = 'a';
		int num = (int) char_a;
		
		char char_b = (char) (num + 1);
		
		System.out.println('a' + 1);
		System.out.println(char_b);
	}
}
```java
package j03_형변환;

public class Casting3 {
	public static void main(String[] args) {
		double kor = 87.5;
		double eng = 95.7;
		double math = 80.5;
		
		int total = (int) kor + (int) eng + (int) math;
		double avg = (double) total / 3.0;
		
		System.out.println("합계: " + total);
		System.out.println("평균: " + avg);
		
	}
}
```
