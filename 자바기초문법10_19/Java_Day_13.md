# Java_Day_13

## 예외 처리
>자바에서 예외(exception) 란 사용자의 잘못된 조작이나 개발자의 코딩 실수로 인해 발생하는 프로그램 오류를 말합니다. 예외가 발생되면 프로그램은 곧바로 종료된다는 점에서 에러와 동일하나,  
>예외는 예외 처리를 통해 프로그램을 종료하지 않고 정상 실행 상태가 유지되도록 할 수 있습니다.

### 예외 처리 2가지
**일반 예외**
> Checked Exception이라고 부르고, 개발자가 반드시 예외 처리를 직접 진행해야한다.
> ex) input output이 있는 값, 파일 입출력 등등
> Checked Exception은 예외 클래스의 상위 클래스가 Exception을 상속받으면 무조건 Checked Exception이다.
> > **실해 예외**
> > Unchecked Exception이라고 부르고, 개발자가 예외처리를 직접 하지 않아도 된다. 명시적인 예외 처리가 강제되는 것이 아니므로  
> > Unchecked 라고 부른다.

### 실행 예외 처리 종류
1. NullPointerException
2. ArrayIndexOutOfBoundsException 
3. NumberFormatException 
4. ClassCastException 

### NullPointerException
> 객체 참조가 없는 상태일 때 발생하고 null값을 갖는 참조 변수로 객체 접근 연산자인 .을 사용했을 때 발생한다.  
> 객체가 없는 상태에서 객체를 사용하기 때문에 당연히 예외가 발생한다.

### ArrayIndexOutOfBoundsException
> 배열에서 인덱스 범위를 초과하여 사용할 때 발생합니다. 
> ex) int [] Array = new int[4] -> Array[5] = 5;

### NumberFormatException
> 자열로 되어 있는 데이터를 숫자로 변경하는 경우가 많은데, 문자열을 숫자로 변환하는 방법 중 가장 많이 사용되는 코드는  
> Integer.parseInt(String s) 메소드와 Double.parseDouble(String s) 메소드입니다. 매개값인 문자열이 숫자로 변환될 수 있다면 숫자를 정상적으로 리턴하지만, 
>  숫자로 변환할 수 없는 문자열이 포함되어 있으면 NumberFormatException을 발생 시킨다.

### ClassCastException 
> 허용되지 않는데 억지로 타입 변환을 시도할 경우 발생합니다.
> ex) A class B class가 있고 두 개의 class 관계성이 없는데 A a = new (A)b();를 하려 할 때 발생함.

### 예외 떠넘기기(throw)
> 메소드 내부에서 예외가 발생할 수 있는 코드를 작성할 때, try-catch로 할 수 있지만, 경우에 따라서 메소드를 호출한 곳으로 예외 처리를  
> 떠넘길 수도 있다. 이 때 사용하는 키워드가 throws이다.
> throws를 이용해서 예외를 떠넘기기 할때는 checked Exception를 할 때 주로 쓰인다. 왜냐하면 강제성이 띄워지기 때문이다. 물로 unchecked Exception도  
> 예외를 떠넘길수 있지만, 강제성이 부여되지 않기 때문이다.

### 사용자 정의 예외
> 개발자가 직접 정의하여 만드는 예외를 말한다.
### CustomErrorException class
```java
package j21_예외;


//사용자 정의 예외처리를 할 때는 RuntimeException을 상속으면 unchecked 가 되고
//Exception을 상속받으면 checked가 된다.
public class CustomErrorException extends RuntimeException{
	
	public CustomErrorException() {
		System.out.println("내가 만든 예외 생성");
	}
	public CustomErrorException(String message) {
		super(message);//RuntimeException안에는 생성자 오버로딩이 많음
	}

}
```

## 익명클래스
> 추상클래스나 인터페이스에서 메소드의 기능이 굳이 class를 만들어 상속을 받아서 메소드 오버라이드를 할 필요가 없이  
> 한 곳에서만 쓰는 상황이거나 한번 만 쓰는 기능일 때 익명 클래스를 만들어서 사용한다.
### main
```java
package j22_익명클래스;

public class Main {
	
	public static void main(String[] args) {
		Calculator c1 = new Addition();
		
		System.out.println(c1.calc(10, 20));
		
		
		
		/////////////////////////////////////
		
		//임시적으로 구현된 객체 -> 익명클래스라고 함 (한번만 쓰는 경우 익명클래스를 이용한다)
		//다른 곳에서는 쓰지 못함 딱 여기서만 쓸 수 있다. 1회성
		//인터페이스와 추상클래스 또한 익명클래스를 쓸 수 있다.
		Calculator c2 = new Calculator() { 
			
			@Override
			public int calc(int x, int y) {
				// TODO Auto-generated method stub
				return x - y;
			}
		};
		System.out.println(c2.calc(200, 100));
	}
}

```

## window bulider
> 이클립스에서 지원하는 java로 만들 수 있는 GUI툴이다.
