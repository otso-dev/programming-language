# Java_Day_5

## 생성자(Constructor)
> 생성자는 new 연산자를 통해서 인스턴스를 생성할 때 반드시 호출이 되고 제일 먼저 실행되는 일종의 메소드지만 메소드와는 다르다.   
생성자는 멤버변수의 초기화를 시키는 역할을 한다
### 기본 생성자

### 필수 생성자

### 전체 생성자

## 접근지정자
클래스내에 멤버변수나 메소드의 접근을 지정하는 키워드이다.
## public
> 어디서든 접근이 가능함
## proteced

## private

## default


## 배열

동일한 자료형(Data Type)의 데이터를 연속된 공간에 저장하기 위한 자료구조이다. 즉, 연관된 데이터를 그룹화하여 묶어준다고 생각하면 된다. 
참조형 자료형이다.

```java
public class ArrayEx01 {
	public static void main(String[] args) {
		String[] beer = {"Kloud", "Cass", "Asahi", "Guinness", "Heineken"};
		    // 인덱스 번호 :   0  ,    1   ,   2   ,     3      ,     4
		System.out.println(beer[0]); // Kloud
		System.out.println(beer[1]); // Cass
		System.out.println(beer[2]); // Asahi
		System.out.println(beer[3]); // Guinness
		System.out.println(beer[4]); // Heineken
	}
}
```
