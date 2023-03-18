  # Java day 19
  
  ## 백엔드의 간단한 구조
  
  +
  ![Spring 기본적인 구조](https://user-images.githubusercontent.com/51119920/215367676-f6219cbb-1375-471a-9370-a70bfcea4ea2.png)


  ## 배열 복습
  
  ```java
  package J12_배열.복습;



public class Array1 {
	
	public static void main(String[] args) {
		int num1 = 10;
		int num2 = 20;
		int num3 = 30;
		int num4 = 40;
		int num5 = 50;
		
		
		int[] nums = new int[5];
		
		nums[0] = 10;
		nums[1] = 20;
		nums[2] = 30;
		nums[3] = 40;
		nums[4] = 50;
		
		
		//new int [] {10,20,30,40,50}; 초기화때만 쓸 수 있음
		
		System.out.println((new int [] {10,20,40,40,50})[0]);//배열안에 데이터를 바꾸면 다른 배열로 바뀐다. 그래서 배열을 변수안에 넣어서 쓴다.
		System.out.println((new int [] {10,20,30,40,50})[1]);
		
		
		
	}
	
}

  ```
  
  ```java
package J12_배열.복습;

import java.util.Arrays;
import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Data;

@AllArgsConstructor
@Data
class User{
	private String username;
	private String password;
}


public class Array2 {
	
	public static void main(String[] args) {
		
		User[] users = new User[] {
				new User("aaa", "1234"),
				new User("bbb", "1234"),
				new User("ccc", "1234")
		};
		
		for(int i = 0; i<users.length; i++) {
			 users[i].setPassword("2222");
			 System.out.println(users[i].getPassword());
		}
		
		for(User u : users) {
			System.out.println(u);
		}
		List<User>userList = Arrays.asList(users);//배열을 List형식으로 바꾸는 asList 메소드
		System.out.println(userList);
		
	}
	
}

  ```
  
  ## 제네릭
  ? 와일드 카드
  
  ## collection
  
  ### List
  - 중복 O, 순서 O
  - List == Array
  - 배열 int [] nums
  - List<integer> nums


  ### Map
  - key와 value로 이루어진 collection이다.
  - key는 중복이 허용되지않는다, 순서는 없다
  - value는 중복이 허용된다.
	
```java
	package j22_익명클래스;

public class Main {
	
	public static void main(String[] args) {
		Calculator c1 = new Addition();
		
		System.out.println(c1.calc(10, 20));
		
		//인터페이스라서 생성을 할 수가 없음
		//Calculator c3 = new Calculator();
		
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
		
		//람다
		Calculator c3 = (x,y) -> x * y;
		
		
		System.out.println(c2.calc(200, 100));
		
		System.out.println(c3.calc(10, 20));
	}
}

```
### lamda

## 람다식

익명클래스 : 객체생성 + 클래스 정의  
정의된 것으로 바로 생성함  
람다도 똑같이 작동한다.  

람다식을 쓸 수 있는 인터페이스는 추상메소드가 딱 하나만 있는 인터페이스만 쓸 수 있다.  
람다식은 코드의 질을 올려준다. 람다는 메소드가 주체가 된다. 인터페이스나 추상클래스안에 메소드가 하나만 존재해야 쓸 수 있다.  
람다식은 앞에 대상이 있어야 사용가능 하다. (독립적으로 사용이 불가능하다)  
익명클래스는 여러개의 추상메소드를 익명클래스로 활용가능하지만 람다식은 불가능하다 그래서 상황에 따라 익명클래스를 쓸지  
람다식을 쓸지 잘 생각해야한다.  

### 익명클래스와 람다
```java
	Instrument instrument = new Instrument() {

			@Override
			public String play(String instrument) {

				return instrument + "를 연주합니다.";
			}
		};

		Instrument instrument2 = (String item) -> {
			return item + "을(를) 연주합니다";
		};
```
### 람다사용법

```java
// 매개변수 자료형을 생략할 수 있다.
		// 매개변수의 이름을 바꿀 수 있다.
		Instrument instrument3 = (item) -> {
			return item + "을(를) 부순다";
		};

		// 매개변수가 하나이면 감싸는 괄호를 생략할 수 있다.
		Instrument instrument4 = item -> {
			return item + "을(를) 부순다";
		};

		// 구현부의 명령이 하나일 때 중괄호를 생략할 수 있다.
		// 이때 return자료형이 정해져있으면 리턴값으로 사용이 된다.
		// 중괄호를 생략하는 것은 람다식에서 return반드시 생략을 해야한다.
		Instrument instrument5 = item -> item + "을(를) 부순다";

		int result = 10 + 20;
		Instrument instrument6 = item -> item + "을(를) 부순다" + result;

		System.out.println(instrument.play("기타"));
		// System.out.println(instrument1.play("기타"));
		System.out.println(instrument2.play("트럼펫"));
		System.out.println(instrument6.play("피아노"));
```

### 람다를 쓰는 이유
1. 지역변수를 람다에서 쓸 수가 있다. -> 자유도가 생긴다.
2. 코드가 간결해진다.
3. 익명클래스와 동일한 한번 만 정의해서 쓴다(생성하지않고 쓰는것)

### 람다 기본 함수형 인터페이스
> 출저 : https://bangu4.tistory.com/215  
![람다 형식](https://user-images.githubusercontent.com/51119920/215641768-a114108d-7501-49b4-bb26-27713f51c34e.png)

### Runnable
```java
	Runnable a = () -> System.out.println("실행");
		Runnable b = () -> {
			System.out.println("여");
			System.out.println("러");
			System.out.println("명");
			System.out.println("령");
			System.out.println("실");
			System.out.println("행");
		};

		a.run();
		b.run();
```
### Supplier
```java
// 2. Supplier<T> - T get()
		Supplier<LocalDate> c = () -> LocalDate.now();
		Supplier<String> d = () -> {
			LocalDate now = LocalDate.now();
			return now.format(DateTimeFormatter.ofPattern("yyyy년 MM월 dd일"));
		};

		System.out.println(c.get());
		System.out.println(d.get());
```

### Consumer
```java
Consumer<String> e = name -> {
			System.out.println("이름: " + name);
			System.out.println("오늘날짜: " + d.get());
		};
		e.accept("이종현");

		// 메소드 참조 표현식([인스턴스]::[메소드명 또는 new])
		Consumer<String> f = System.out::println;
		f.accept("출력");

```
### Consumer를 이용한 List와 Map forEach Method 활용

``` java
List<String> names = new ArrayList<>();

		names.add("김동민");
		names.add("김두영");
		names.add("장진원");
		names.add("조병철");
		
		Consumer<String> g = name->System.out.println("이름: " + name + "님");
		
		names.forEach(g);
		
		names.forEach(name -> {
			System.out.println("이름을 출력합니다.");
			System.out.println("이름: " + name);
			System.out.println();
		});
		
		Map<String,String> userMap = new HashMap<>();
		userMap.put("username", "aaa");
		userMap.put("password", "1234");
		
		userMap.forEach((k,v) -> {
			System.out.println("key: " + k);
			System.out.println("value: " + v);
			System.out.println();
		});
```