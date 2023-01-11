# Java_Day_2


# 변수
변수 : 변하는 수  
자료형 + 변수명 => ex) int level;  
## 변수명 제약사항
1. 변수 이름은 영문자나 숫자를 사용할 수 있고 구분하며, 특수 문자 중에는 $, _ 만 사용할 수 있다.  
2. 변수 이름은 숫자로 시작할 수 없다.  
3. 자바에서 이미 사용 중인 예약어는 사용할 수 없다.(키워드) 

## 자료형 크기

![자료형 크기](https://user-images.githubusercontent.com/51119920/211733648-0fa33104-8680-4904-a88e-58c19448618c.png)

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
