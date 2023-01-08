# Java_Day_2


## 변수

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
