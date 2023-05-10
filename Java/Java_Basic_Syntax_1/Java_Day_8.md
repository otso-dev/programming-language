# Java_Day_8


## 상속

키워드 : extend 클래스명

클래스를 메모리 공간으로 본다면 확장하는 개념.  

부모 클래스와 상속된 클래스의 메모리 공간은 나눠져 있지만  
상속된 클래스를 생성하면 부모클래스 메모리도 같이 메모리가 생성됨  
부모클래스는 상속된 자식클래스를 포함하는 관계이다.  
```java
package j13_상속;

public class Car {

	private String company;
	private String model;
	private int price;

	public Car() {
		System.out.println("부모");
	}

	public String getCompany() {
		return company;
	}

	public void setCompany(String company) {
		this.company = company;
	}

	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public int getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}

	public int discountPrice(int percentage) {
		return price - (price * percentage / 100);
	}

}


```
## 오버라이드
부모가 가진 메소드를 자식 클래스에서 똑같이 재정의를 하는 것  
가능한 이유 : 부모클래스와 자식클래스의 메모리주소는 다르기 때문에 자식클래스를 생성할 떄 같이 생성될 뿐 메모리공간은 다르다.  
재정의 : 부모의 메소드 주소를 끊어버리고 정의하는 것  

오버라이드시 메소드가 달라지면은 안됨  
메소드가 달라지는 것 : 메소드명 or 매개변수 자료형이 달라짐  


```java
package j13_상속;

public class KiaCar extends Car{
	
	public KiaCar() {
		super();//나의 상위 객체를 의미한다. kiaCar -> Car의 생성자가 호출됨 super는 생성자 제일 상위에 있어야함
		//부모클래스가 먼저 생성 되어야 함
		System.out.println("자식");
		
	}
	
	
	@Override//오버라이드를 하지 않는다면 부모 클래스에서 바로 들고오고,
	//오버라이드를 한다면 자식 클래스 메소드를 통해서 가져오는 것 -> 주소가 다르기 때문에 오버로딩과는 다른 개념이다.
	public int discountPrice(int percentage) {
		
		return super.discountPrice(percentage);
	}
	
	public void test() {
		KiaCar kc = this;//자신의 주소를 변수로 쓰고 싶을 때
	}
}

```

## 클래스 형변환

클래스들이 상속관계에 있을때 업캐스팅과 다운캐스팅이 가능하다.  
다운캐스팅을 할 때에는 자료형의 형변환처럼 명시를 해줘야한다.  

상속 관계
A -> B,C 일 때
A a = new B(); 업캐스팅  
B b = (A)a; 다운캐스팅

### 업캐스팅
B라는 클래스로 생성을 했지만 A의 메소드만 쓸 수 있다. 그래서 B 클래스에서 부모의 메소드를 오버라이드 하여  
B클래스에서 쓸 수 있게 해주면 된다.

### 다운캐스팅
자료형의 다운캐스팅 처럼 클래스에서도 다운캐스팅이 가능하다. 똑같이 명시적으로 알려줘야지만 다운캐스팅을 할 수 있다. 하지만  
부모클래스만 생성해서 자식클래스로 다운캐스팅이 불가능하고, 상속관계가 없는 클래스도 불가능 하다.

```java
package j13_상속.casting2;

public class Main {

	public static void main(String[] args) {
		Taxi taxi = new Taxi();
		Subway subway = new Subway();
		
		
		Transportation transportation = new Transportation();
//		Taxi t1 = (Taxi) transportation; //다운캐스팅이 안된다. 왜?? -> 부모클래스를 생성했을시 메모리 공간이
//		//부모 클래스의 메모리 공간만 생성되고 자식클래스는 부모와 자기자신의 메모리공간이 같이 생성되기 때문에
//		//담을 공간이 없기 때문에 안된다.
//		
//		
//		Transportation transportation1 = taxi;
//		Subway s1 = (Subway) transportation1; //다운 캐스팅이 안된다. 부모클래스는 같지만 택시와 지하철은 관계가 없기
//		//때문에 다운캐스팅이 되지 않는다.
//		
//		Transportation transportation2 = subway;
		
		//instanceof는 포함관계를 보고, getclass(), class는 명확하게 어떤 객체가 생성되었는지 보는 것

		Transportation[] transportations = new Transportation[6];
		
		//업캐스팅
		transportations[0] = taxi;
		transportations[1] = subway;
		transportations[2] = taxi;
		transportations[3] = subway;
		transportations[4] = taxi;
		transportations[5] = subway;
		
		
		//다운캐스팅
		for (int i = 0; i < transportations.length; i++) {
			
			if(transportations[i] instanceof Taxi) {
				Taxi tx = (Taxi)transportations[i];
				tx.checkTaxiNumber();
			}else if(transportations[i] instanceof Subway) {
				Subway sw = (Subway)transportations[i];
				sw.checkRoute();
			}
			
			
			transportations[i].go();
		}

		for(Transportation trans : transportations ) {
			trans.stop();
		}
		
	}

}
```


## 추상클래스
공통된 것을 묶어놓은 것을 추상화라고 한다. 추상 클래스는 하나의 추상 메소드만 가져도 추상클래스로 인식 한다.  
추상클래스는 생성자는 있지만 생성이 불가능하고 설계도 역할만 한다. 그 외에는 일반클래스와 동일한 기능을 가진다.  
추상클래스를 상속 받으면 자식 클래스에서 부모의 추상 메소드를 전부 재정의를 하여야한다.

```java
package j14_추상;


//추상클래스
//공통된 것들을 모아두는 것을 추상화라고 한다.
//추상 메소드가 하나라도 있으면 추상클래스라고 정의함.
//생성이 불가능하다.
//설계도 역할
//그 외에는 일반클래스와 동일한 기능을 가진다.
public abstract class Transportation {

	
	// 추상 메소드
	public abstract void go();
	
	public abstract void stop();
	
}
```

```java
package j14_추상;

//추상클래스를 상속받으면 추상클래스로 만들던지
//추상 메소드를 다 구현해야한다.
//설계도
public class Airplane extends Transportation{

	@Override
	public void go() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void stop() {
		// TODO Auto-generated method stub
		
	}
}

```

## 인터페이스
interface도 class와 동일한 기능을 가지고 있다. 하지만 메소드는 전부 abstract로 추상메소드이고, 일반 메소드를 쓸려면, default를 써줘야한다.  
또한 interface는 멤버변수들은 가질 수 없지만, 상수는 가질 수 있다.  
추상클래스와 차이점은 관계성과 멤버변수를 가질 수 있고, 없고의 차이점이 있다.  

```java
package j15_인터페이스;


//interface == class
//메소드 전부 abstract 메소드이다.
//일반메소드를 쓸러면 default를 써줘야한다.
//멤버 변수들은 가질수 없지만, 상수는 가질 수 있다.
//추상클래스와 차이점 관계성과 멤버변수를 가질수 있고 없고의 차이점
public interface Calculator {

	public int ERROR = -9999999;
	
	public double plus(double x, double y);
	
	public double minus(double x, double y);
	
	public default double multiplication(double x, double y) {
		return x * y;
	}
	
	public double division(double x, double y);
}

```
### 인터페이스의 활용법과 형변환
```java
package j15_인터페이스;

public class Main {

	public static void main(String[] args) {
		Equipment[] equipments = new Equipment[2];

		equipments[0] = new GeneralCalculator(); //eq랑 gen 같이 생성
		equipments[1] = new SmartPhone(); //

		Calculator[] calculators = new Calculator[2];
		
		calculators[0] = new GeneralCalculator();
		calculators[1] = new SmartPhone();
		
		System.out.println("모든 장비 전원 켜기");
		for (Calculator c : calculators) {
			Equipment eq = (Equipment) c;
			eq.powerOn();
		}//반대로 가능
		System.out.println();

		System.out.println("모든 장비 전원 켜기");
		for (Equipment eq : equipments) {
			eq.powerOn();
		}
		System.out.println();

		System.out.println("모든 장비에서 10과 20을 더하기");

		for (Equipment eq : equipments) {
			Calculator c = (Calculator) eq;//다운캐스팅을 한후 업캐스팅을 한다.
			double result = c.plus(10, 20);
			System.out.println("결과 : " + result);
		}

		System.out.println("모든 장비에서 10과 0을 나누기");

		for (Equipment eq : equipments) {
			Calculator c = (Calculator) eq;
			double result = c.division(10, 2);
			System.out.println("결과 : " + result);
		}

		System.out.println("모든 장비 전원 끄기");
		for (Equipment eq : equipments) {
			eq.powerOff();
		}
		System.out.println();
	}
}

```
