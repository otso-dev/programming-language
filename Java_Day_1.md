# Java_Day_1

### 프로그램이란
순서대로 진행되는것.

### 프로그래밍 언어
컴퓨터와 의사소통에 필요한 언어

### 컴퓨터 언어
기계어를 쓴다. 0 or 1(2 진수)

### 고급언어(사람이 이해하기 쉬운 언어)
C, Java, Python

### 저급언어(컴퓨터가 이해하기 쉬운 언어)
기계어, 어셈블리어 

### 컴파일러
고급언어를 컴퓨터가 이해하기 위해서 번역하는 역할을 수행

### Java란
제임스 고슬링이 만든 언어로 JVM(자바란 언어를 컴파일 할 수 있는 가상기계)을 이용해서
운영체제가 달라도 상관없이 java를 쓸 수 있다.

객체 지향 언어이다.

클래스 단위로 컴파일을 한다.

안정적인 언어이다.(가비지 컬렉터 : 동적 메모리 관리에 따른 쓰레기값 자동수거)

### 개발환경 
https://sites.google.com/view/kji-java/index  - jdk  
https://spring.io/tools - spring boot  
jdk 환경변수 설정하기  
JAVA_HOME 새로만들기  
CLASS_PATH 새로만들기  
path 편집  
 
cmd로 java버젼 확인하기  
java파일이 알집이면 jarfix 설치  
java실행파일 .jar로 시작  

클래스 이름은 항상 대문자  
혹시 틀렸을시 클릭하고 F2를 누르고 이름을 변경  


영역 복사 컨틀롤 + 알트 방향키  

중복 수정시 알트 + 원하는 곳에 클릭  

JVM 자바 가상 기계(자바란 언어를 컴파일 하는 것)  
JDK 자바 개발 환경  
Java Runtime Environment 환경 해당되는 언어를 실행할수있는 환경  
IDE 통합개발환경  

```java
/code HelloJava  
package j01_출력;

public class HelloJava { 
	// class는 모두 대문자로 시작한다.
	// 주석: 함수 설명이나 코드 내부에 메모를 할 때 쓴다.
	// 주석처리 된 것은 컴파일시 무시
	// 한 줄 주석
	// 들여쓰기 (tab)
	/*
	 * 여러줄 주석
	 */
	/**
	 * 
	 * 클래스, 메소드 등의 정보를 설명하기 위한 주석
	 */
	
	
	// 프로그램의 시작점
	public static void main(String[] args) {
		
		System.out.println("Hello,Java!!"); //println : 한줄의 문자열을 출력후 끝에 줄바꿈을 해라.
		System.out.println("주소 : 부산 동래구 온천동");
		System.out.println("이름 : 정성현");
		System.out.print("연락처 : 010-4758-8028"); //print : 줄바꿈 없이 출력
		System.out.println("수업 : AWS기반 공공빅데이터 활용 웹개발자 양성");
	}

}
```
```java
/code OutPut1

package j01_출력;

public class OutPut1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.print("이름 : ");
		System.out.println("정성현");
		System.out.print("나이 : ");
		System.out.println(28 + "1"); //28과 "28"의 차이는 숫자와 문자열의 차이다. 문자열은 " "안에 넣어야함
		System.out.println("이름 : " + "정성현");
		//"문자" + 1은 하면 자동으로 숫자 1이 문자열로 바뀜
	}

}
```

```java

/code OutPut2

package j01_출력;

public class OutPut2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int year = 10; // 자료형 변수명(
		
		System.out.println("이름 : 정성현");
		System.out.println("나이 : " +(20 + year));
		System.out.println("이름 : 정성현");
		System.out.println("나이 : " +(21 + year));
		System.out.println("이름 : 정성현");
		System.out.println("나이 : " +(22 + year));
		System.out.println("이름 : 정성현");
		System.out.println("나이 : " +(23 + year));
		
	}

}
```
- 변수와 메모리의 관계  
10진수 0 ~ 9  
2진수 0 ~ 1  
8진수 0 ~ 8  
16진수 0 ~ F  

