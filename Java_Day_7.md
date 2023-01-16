# Java_Day_7

## DI 
>의존성 주입(Dependency Injection)  
>객체의 생성과 사용을 분리하는 프로그래밍 설계방식이다.  
>아래의 class 세개가 있다. 만약 A class를 생성할 때 생성자에서 B class를 생성하게 해주고 B class를 생성할 때 C class를  
>생성해준다면 A B C 간에 B는 A에 의존성도 높고 결합도 또한 높아진다. C class도 마찬가지이다. 왜냐하면 B class를 생성 할려면  
>A class를 생성해주어야 하기 때문이다. 그래서 의존성과 결합도를 낮추기 위해 DI를 이용한다. 그리고  
>의존성을 주입하는 이유는 바로 생성과 사용에 대한 관심을 분리하게 되면 생성에 대한 책임을 다른 누군가에 위임할 수 있는 동시에 필요에 따라 객체 생성 방식을 선택할 수 있기 때문입니다. 최종적으로는 객체들이 가지는 강한 결합을 느슨하게 만들 수 있고 이는 설계의 유연성을 부여합니다.




### A class
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
### B class

```java
package J12_배열.di;

public class Test_B {
	
	private Test_C tc;
	
	public Test_B(Test_C tc) {
		this.tc = tc;
	}
	
	public void testB1() {
		System.out.println("\tTest_B1 메소드 호출!");

		tc.testC1();
	}

}

```

### C class

```java
package J12_배열.di;

public class Test_C {
	
	public void testC1() {
		System.out.println("\tTest_C1 메소드 호출!");
	}

}

```


### main

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
