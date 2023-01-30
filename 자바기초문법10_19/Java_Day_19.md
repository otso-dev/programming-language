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
