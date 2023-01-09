# Java_Day_7

## 생성자
RequiredArgsConstructor
특별한 처리가 필요한 각 필드에 대해 1개의 매개변수가 있는 생성자를 생성합니다.  
초기화되지 않은 모든 필드는 매개변수를 가져 오며 선언된 곳에서 초기화되지 않은 final것으로 표시된 필드도 가져옵니다 .  
@NonNull로 표시된 필드 @NonNull의 경우 명시적 null 검사도 생성됩니다. 생성자는 포함 NullPointerException으로 표시된 필드를 위한 매개변수가 있는 경우 를 발생시킵니다 .  
매개변수의 순서는 클래스에 필드가 나타나는 순서와 일치합니다.  

```java
package J12_배열.di;

public class Test_A {
	//값을 주는 방법은 두 가지 생성자의 매개변수와 Setter
	
	private final Test_B tb;//final은 상수 그리고 초기화를 무조건 해야함. 프로그램이 돌아가는 와중에 값이 변하지 않아야 하는 값에 final을 붙여준다.
	
	public Test_A(Test_B tb) {//생성자에서 변수를 초기화 하거나 생성을 해야하는 것이 좋다. 하지만 Test_B는 Test_A에 의존성이 높고 
							  //결합도도 높다.
		this.tb = tb;		  //final을 붙이면 필수 매개변수 생성자 
	}
	
//	public void setTb(Test_B tb) {
//		this.tb = tb;
//	}
	
	public void testA1() {
		System.out.println("Test_A1 메소드 호출!");
		//Test_B tb = new Test_B();

		tb.testB1();
	}

	public void testA2() {
		System.out.println("Test_A2 메소드 호출!");
		//Test_B tb = new Test_B();

		tb.testB1();

	}

}


```


NoArgsConstructor
NoArgsConstructor매개변수가 없는 생성자를 생성합니다.  
이것이 가능하지 않은 경우(final 필드 때문에) 대신 컴파일러 오류가 발생합니다.   
를 사용하지 않으면 모든 final 필드가 / / @NoArgsConstructor(force = true)로 초기화됩니다.  
필드와 같이 제약 조건이 있는 필드의 경우 검사 가 생성되지 않으므로 이러한 제약 조건은 일반적으로 해당 필드가 나중에 적절하게 초기화될 때까지 충족되지 않는다는 점에 유의하십시오.   
최대 절전 모드 및 서비스 제공자 인터페이스와 같은 특정 Java 구성에는 인수 없는 생성자가 필요합니다. 이 주석은 주석을 생성하는 다른 생성자 중 하나 또는 하나와 조합하여 주로 유용합니다  

AllArgsConstructor  

클래스의 각 필드에 대해 1개의 매개변수가 있는 생성자를 생성합니다.   로 표시된 필드는 @NonNull해당 매개변수에 대해 null 검사를 수행합니다.
## DI 
의존성 주입(Dependency Injection)


```java

package J12_배열.di;

public class Test_A {
	//값을 주는 방법은 두 가지 생성자의 매개변수와 Setter
	
	private final Test_B tb;//final은 상수 그리고 초기화를 무조건 해야함. 프로그램이 돌아가는 와중에 값이 변하지 않아야 하는 값에 final을 붙여준다.
	
	public Test_A(Test_B tb) {//생성자에서 변수를 초기화 하거나 생성을 해야하는 것이 좋다. 하지만 Test_B는 Test_A에 의존성이 높고 
							  //결합도도 높다.
		this.tb = tb;		  //final을 붙이면 필수 매개변수 생성자 
	}
	
//	public void setTb(Test_B tb) {
//		this.tb = tb;
//	}
	
	public void testA1() {
		System.out.println("Test_A1 메소드 호출!");
		//Test_B tb = new Test_B();

		tb.testB1();
	}

	public void testA2() {
		System.out.println("Test_A2 메소드 호출!");
		//Test_B tb = new Test_B();

		tb.testB1();

	}

}
```


```java
package J12_배열.di;

public class Main {
	//dependency injection DI
	public static void main(String[] args) {
		//Test_C tc = new Test_C();
		Test_C tc2 = new Test_C();
		Test_B tb = new Test_B(tc2);//결합도와 의존도를 낮추기 위해 Test_B를 생성
		
		Test_A ta = new Test_A(tb);//객체 주입은 항상 외부에서 해야함
		
				
		ta.testA1();
		ta.testA2();
		tb.testB1();
		
		
	}
}

```
