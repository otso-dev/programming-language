# Java_Day_5
## Class
### User Class
> User라는 class를 만들고 User에 필요한 변수와 메소드들을 만듬
``` java
package j09_클래스;

public class J09_User {

	String username;
	int password;
	String name;
	String email;
	
	void printUserInfo() {
		
		System.out.println("아이디 : " + username);
		System.out.println("비밀번호 : " + password);
		System.out.println("이름 : " + name);
		System.out.println("이메일 : " + email);
	}
	
}

```
### UserMain
>User class 객체를 생성해서 정보를 입력하고 입력된 정보를 User class 안에있는 멤버 메소드 printInfo를 호출함
``` java
package j09_클래스;

public class J09_UserMain {
	
	
	
	public static void main(String[] args) {
		J09_User u1 = new J09_User();
		J09_User u2 = new J09_User();
		J09_User u3 = new J09_User();
		
		u1.username = "user1";
		u1.password = 1234;
		u1.name = "홍길동";
		u1.email = "useremail1@naver.com";
		
		u2.username = "user2";
		u2.password = 123456; 
		u2.name = "김민수";
		u2.email = "useremail2@gmail.com";
		
		u3.username = "user3";
		u3.password = 1234567;
		u3.name = "황철수";
		u3.email = "useremail3@naver.com";
		
		u1.printUserInfo();
		System.out.println();
		u2.printUserInfo();
		System.out.println();
		u3.printUserInfo();
		
	}
	
}

```

## 생성자(Constructor)
> 생성자는 new 연산자를 통해서 인스턴스를 생성할 때 반드시 호출이 되고 제일 먼저 실행되는 일종의 메소드지만 메소드와는 다르다.   
생성자는 멤버변수의 초기화를 시키는 역할을 한다  
### 기본 생성자(No argument constructor)
>class를 만들 때 기본적으로 만들어지는 생성자이고 생략되어있다.  
>멤버변수에 final이 있다면 만들 수 없다.
```java
	J10_Student(){ //NO argument constructor
		System.out.println("기본 생성자 호출");
}
```
### 필수 생성자(required argument constructor)
>class에 final이란 변수가 있다면 무조건 생성자를 만들어야하는 생성자가 바로 Required Argument Costructor이다.
```java
J10_Student(int a) {//required argument constructor
		// TODO Auto-generated constructor stub
		this.a = a;
	}
```
### 전체 생성자(all argument constructor)
>class의 모든 변수를 매개변수로 받는 생성자이다.
```java
J10_Student(String name, int age, int a) {//all argument constructor
		
		//클래스내의 멤버변수의 지역변수들은 이름이 같아도 구분을 해줌
		//하지만 이름이 같아지기 때문에 this를 이용해준다.
		//this 자기자신의 주소를 가지고 있음.
		this.name = name;
		this.age = age;
		this.a = a;
	}
```
## 접근지정자
> 클래스내에 멤버변수나 메소드의 접근을 지정하는 키워드이다. 만약 변수나 메소드에 아무것도 입력을 안한다면 default상태가 된다.  
### public
> 접근제한 없음
### proteced
> 동일 패키지와 상속받은 클래스 내부
### private
> 클래스 내부만
### default
> 동일 패키지 내에서만

### StudentDefault
```java
package j11_접근지정자.default1;

 public class J11_StudentDefault {
	
	 
	//클래스내의 멤버변수는 private로 지정 -> 데이터의 은닉
	//메서드를 활용해 멤버변수를 값을 전달해줘야한다.
	private String name;
	private int age;
	
	public J11_StudentDefault() {
		
	}
	
	public J11_StudentDefault(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	public void printInfo() {
		System.out.println("이름: " + name);
		System.out.println("나이: " + age);
	}
	
	
	//클래스내에서 작동하는 메소드들은 private로 지정 -> 캡슐화
	
	//Getter -> 값을 가지고 오는 메서드
	public String getName() {
		return name;
	}
	
	//Setter -> 값을 대입 해주는 메서드
	public void setName(String name) {
		this.name = name;
	}
	
	//알트 쉬프트 s -> Getter , Setter, 생성자를 자동으로 만들어주는 단축키
	//컨트롤 쉬프트 f -> 자동 줄정리 단축키
	
	
	// ${name} -> 하나의 표현식이고 Getter를 호출함
	
}

```

## 배열

동일한 자료형(Data Type)의 데이터를 연속된 공간에 저장하기 위한 자료구조이다. 즉, 연관된 데이터를 그룹화하여 묶어준다고 생각하면 된다. 
참조형 자료형이다.

``` java
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

### 배열에 값을 넣는 방법 3가지

```java
package J12_배열;

public class Array2 {
	
	public static void printNames(String[] names) {
		
		for(int i = 0; i< names.length; i++) {
			System.out.println("이름[" + (i + 1) + "]" + names[i]);
		}
		
		System.out.println();
	}
	public static void main(String[] args) {
		
		//배열에 값을 넣는 방법 세가지                                                                                                                           
		String[] names = new String[3];//들어갈 값이 정해져 있지 않을 때 or 들어가는 공간이 확실할 때

		names[0] = "김종환";
		names[1] = "김상현";
		names[2] = "임나영";

		String[] names2 = new String[] { "이상현", "손지호", "이강용" };//둘다 크기를 지정하지 않음
		
		String[] names3 = { "김두영", "강대협", "이현수", "김재영" }; // ==
		
		
		printNames(names);
		printNames(new String[] { "이상현", "손지호", "이강용" });
		printNames(names3);
		
	}

}

```
### class를 배열로 만들었을 경우

```java
package J12_배열;



public class Array4 {

	public static void main(String[] args) {
		
		J12_User[] users = new J12_User[3];
		
		J12_User[] users2 = new J12_User[]  {
				new J12_User("aaa","1234","김종환","aaa@gmail.com"),
				new J12_User("bbb","1234","이종현","bbb@gmail.com"),
				new J12_User("ccc","1234","진채희","ccc@gmail.com")
		};
		
		J12_User[] users3 = {
				new J12_User("aaa","1234","김종환","aaa@gmail.com"),
				new J12_User("bbb","1234","이종현","bbb@gmail.com"),
				new J12_User("ccc","1234","진채희","ccc@gmail.com")
		};
		
		users[0] = new J12_User("aaa","1234","김종환","aaa@gmail.com");
		users[1] = new J12_User("bbb","1234","이종현","bbb@gmail.com");
		users[2] = new J12_User("ccc","1234","진채희","ccc@gmail.com");
		
	
		
		for(int i = 0; i < users.length; i++) {
			System.out.println(users[i].toString());
		}
		
	}
	
}

```
