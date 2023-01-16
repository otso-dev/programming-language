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
### 기본 생성자

### 필수 생성자

### 전체 생성자

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
