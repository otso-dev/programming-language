# Java_Day_4

## 반복문(while)

package j07_반복;

import java.util.Scanner;

public class Menu {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		
		boolean loopFlag1 = true;
		
		while(loopFlag1) {
			char select = '\0';
			
			System.out.println("========<<식당메뉴>>========");
			System.out.println("1. 김밥천국");
			System.out.println("2. 탄탄면");
			System.out.println("3. 홍대개미");
			System.out.println("4. 밥앤밥");
			System.out.println("========================");
			System.out.println("q. 프로그램 종료");
			System.out.println("========================");
			
			System.out.println("식당 번호 선택");
			select = scanner.next().charAt(0);//next().charAt(0) 함수는 char형으로 위치값에 해당하는 값을 가져옴
			
			if(select == 'q' || select == 'Q') {
				loopFlag1 = false;
			}else if(select == '1') {
				boolean loopFlag2 = true;
				while(loopFlag2) {
					System.out.println();
					System.out.println("========<<김밥천국>>========");
					System.out.println("1. 라면");
					System.out.println("2. 돌솥비빔밥");
					System.out.println("3. 오므라이스");
					System.out.println("4. 김치볶음밥");
					System.out.println("========================");
					System.out.println("b. 뒤로가기");
					System.out.println("q. 프로그램 종료");
					System.out.println("========================");
					
					System.out.println("메뉴 번호 선택");
					select = scanner.next().charAt(0);//next().charAt(0) 함수는 char형으로 위치값에 해당하는 값을 가져옴
					if(select == 'b') {
						loopFlag2 = false;
					}else if(select == 'q' || select == 'Q') {
						loopFlag1 = false;
						loopFlag2 = false;
					}else if(select == '1') {
						System.out.println();
						System.out.println("라면을 선택했습니다.");
					}else if(select == '2') {
						System.out.println();
						System.out.println("돌솥비빔밥을 선택했습니다.");
					}else if(select == '3') {
						System.out.println();
						System.out.println("오므라이스를 선택했습니다.");
					}else if(select == '4') {
						System.out.println();
						System.out.println("김치볶음밥을 선택했습니다.");
					}else {
						System.out.println();
						System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
						System.out.println("사용할 수 없는 번호입니다.");
						System.out.println("다시 입력하세요");
						System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
					}
					System.out.println();
				}
				
				
			}else if(select == '2') {
				boolean loopFlag2 = true;
				while(loopFlag2) {
					System.out.println();
					System.out.println("========<<탄탄면>>========");
					System.out.println("1. 탄탄면");
					System.out.println("2. 비빔탄탄면");
					System.out.println("3. 마파탄탄면");
					System.out.println("4. 훈육탕면");
					System.out.println("========================");
					System.out.println("b. 뒤로가기");
					System.out.println("q. 프로그램 종료");
					System.out.println("========================");
					
					System.out.println("메뉴 번호 선택");
					select = scanner.next().charAt(0);//next().charAt(0) 함수는 char형으로 위치값에 해당하는 값을 가져옴
					if(select == 'b') {
						loopFlag2 = false;
					}else if(select == 'q' || select == 'Q') {
						loopFlag1 = false;
						loopFlag2 = false;
					}else if(select == '1') {
						System.out.println();
						System.out.println("탄탄면을을 선택했습니다.");
					}else if(select == '2') {
						System.out.println();
						System.out.println("비빔탄탄면을 선택했습니다.");
					}else if(select == '3') {
						System.out.println();
						System.out.println("마파탄탄면을 선택했습니다.");
					}else if(select == '4') {
						System.out.println();
						System.out.println("훈육탕면을 선택했습니다.");
					}else {
						System.out.println();
						System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
						System.out.println("사용할 수 없는 번호입니다.");
						System.out.println("다시 입력하세요");
						System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
					}
					System.out.println();
				}
				
			}else if(select == '3') {
				boolean loopFlag2 = true;
				while(loopFlag2) {
					System.out.println();
					System.out.println("========<<홍대개미>>========");
					System.out.println("1. 대창 덮밥");
					System.out.println("2. 스테이크 덮밥");
					System.out.println("3. 연어 덮밥");
					System.out.println("4. 불닭 덮밥");
					System.out.println("========================");
					System.out.println("b. 뒤로가기");
					System.out.println("q. 프로그램 종료");
					System.out.println("========================");
					
					System.out.println("메뉴 번호 선택");
					select = scanner.next().charAt(0);//next().charAt(0) 함수는 char형으로 위치값에 해당하는 값을 가져옴
					if(select == 'b') {
						loopFlag2 = false;
					}else if(select == 'q' || select == 'Q') {
						loopFlag1 = false;
						loopFlag2 = false;
					}else if(select == '1') {
						System.out.println();
						System.out.println("대창 덮밥을 선택했습니다.");
					}else if(select == '2') {
						System.out.println();
						System.out.println("스테이크 덮밥을 선택했습니다.");
					}else if(select == '3') {
						System.out.println();
						System.out.println("연어 덮밥을 선택했습니다.");
					}else if(select == '4') {
						System.out.println();
						System.out.println("불닭 덮밥을 선택했습니다.");
					}else {
						System.out.println();
						System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
						System.out.println("사용할 수 없는 번호입니다.");
						System.out.println("다시 입력하세요");
						System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
					}
					System.out.println();
				}
				
			}else if(select == '4') {
				boolean loopFlag2 = true;
				while(loopFlag2) {
					System.out.println();
					System.out.println("========<<밥앤밥>>========");
					System.out.println("1. 소고기 미역국");
					System.out.println("2. 제육볶음");
					System.out.println("3. 순두부 찌개");
					System.out.println("4. 순두부 된장찌개");
					System.out.println("========================");
					System.out.println("b. 뒤로가기");
					System.out.println("q. 프로그램 종료");
					System.out.println("========================");
					
					System.out.println("메뉴 번호 선택");
					select = scanner.next().charAt(0);//next().charAt(0) 함수는 char형으로 위치값에 해당하는 값을 가져옴
					if(select == 'b') {
						loopFlag2 = false;
					}else if(select == 'q' || select == 'Q') {
						loopFlag1 = false;
						loopFlag2 = false;
					}else if(select == '1') {
						System.out.println();
						System.out.println("소고기미역국을 선택했습니다.");
						loopFlag1 = false;
						loopFlag2 = false;
					}else if(select == '2') {
						System.out.println();
						System.out.println("제육볶음을 선택했습니다.");
						loopFlag1 = false;
						loopFlag2 = false;
					}else if(select == '3') {
						System.out.println();
						System.out.println("순두부 찌개를 선택했습니다.");
						loopFlag1 = false;
						loopFlag2 = false;
					}else if(select == '4') {
						System.out.println();
						System.out.println("순두부 된장찌개를 선택했습니다.");
						loopFlag1 = false;
						loopFlag2 = false;
					}else {
						System.out.println();
						System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
						System.out.println("사용할 수 없는 번호입니다.");
						System.out.println("다시 입력하세요");
						System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
					}
					System.out.println();
				}
				
			}else {
				System.out.println();
				System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
				System.out.println("사용할 수 없는 번호입니다.");
				System.out.println("다시 입력하세요");
				System.out.println("xxxxxxxxxxxxxxxxxxxxxxxxxx");
			}
			
			System.out.println();
			
		}

		System.out.println("프로그램 정상 종료!");
	}

}

## 메소드

package j08_메소드;

public class Method1 {
	
	public static int sum(int x, int y) {
		int result = x + y;
		
		return result;
	}
	
	public static void main(String[] args) {
		int a1 = 10;
		int b1 = 20;
		
		int a2 = 20;
		int b2 = 30;
		
		int a3 = 30;
		int b3 = 40;
		
		int total1 = 0;
		int total2 = 0;
		int total3 = 0;
		
		total1 = a1 + b1;
		total2 = a2 + b2;
		
		total1 = sum(a1,b1);
		total2 = sum(a2,b2);
		total3 = sum(a3,b3);
		
		System.out.println(total1);
		System.out.println(total2);
		System.out.println(total3);
	}
}

package j08_메소드;

public class Method2 {
	
	//클래스 안에서 정의한것을 메소드라 부르고 바깥에서 정의한 것을 함수라고 한다.
	// 매개변수 : x, 반환 x
	// 매개변수 -> 입력
	// void -> 반환이 없다.
	// 호이스팅 -> 실행전에 소스코드를 분석하고 정의한다.
	public static void method1() {
		System.out.println("단순 실행");
		System.out.println();
	}
	
	//매개변수: int 하나 입력, 반환 x
	public static void method2(int num) {
		System.out.println("num: " + num);
		System.out.println();
	}
	
	//매개변수 : 매개변수 두개 입력, 반환 x
	public static void method3(int num, int num2) {
		System.out.println("num : " +num);
		System.out.println("num2 : " +num2);
		System.out.println();
	}
	
	//반환값은 하나만 가능하다.
	public static String method4() {
		return "데이터 반환";
	}
	
	public static String method5(int age) {
		return age + "살";
	}
	
	public static void main(String[] args) {
		method1();//함수 호출
		method2(100);
		method3(200,300);
		System.out.println(method4());
		System.out.println();
		
		String data1 = method4();
		System.out.println(data1);
		System.out.println();
		
		System.out.println(method5(29));
		System.out.println();
	}
}

package j08_메소드;

public class Method3 {
	
	
	//메소드 오버로딩 : 메소드의 이름을 똑같지만 매개변수의 갯수와 순서가 다름, 호출 할 떄 달라짐
	//메소드의 자료형이 달라도 오버로딩이 안된다
	public static void ov1() {
		System.out.println("매개변수 없음");
	}
	
	public static void ov1(int x) {
		System.out.println("int 매개변수 하나 매개변수 x: " + x);
	}
	
	public static void ov1(int a, String b) {
		System.out.println("int 먼저 그다음 String");
	}
	
	public static void ov1(String a, int b) {
		System.out.println("String 먼저 그 다음  int");
	}
	
	public static void main(String[] args) {
		ov1();
		ov1(100);
		ov1(100,"b");
		ov1("a",100);

	}

}

## 클래스

Java는 객체지향 언어이다.
객체지향 언어(OOP)

Object-Oriented-Programming
객체란 세상에 존재하는 모든 것을 의미 즉, 주변의 사물, 생명등을 말한다.
프로그래밍 관점에서는 객체들의 관계성을 사용하여 순차적으로 수행되는 프로그램내에서 간에 관계를 형성하여 프로그램을 동작하게함

객체의 예시
객체 = 데이터 + 기능
객체 = 컴퓨터(PC)
데이터(변수) = 모니터, 본체, 키보드, 마우스, 스피커 등등
기능(메소드) = 화면출력, 프로그램 실행, 입력, 소리출력 등등

객체지향 언어의 특징
1. 상속
2. 캡슐화
3. 추상화
4. 다형성

## 상속
의미 그대로 상위 클래스의 모든 것을 상속받아 사용하는 것
부모와 자식 관계(데이터의 관계성)

## 캡슐화
데이터와 기능을 외부로부터 접근은 차단하고, 권한 또는 절차없이 데이터를 변경 또는 기능 수행을 할 수 없게
캡슐처럼 보호함(데이터의 은닉성) 키워드 private

## 추상화
추상적인 요소들을 묶어서 분류하는 것
학생, 선생, 학부모 등 사람이라는 추상적인 요소로 분류할 수 있음
(데이터의 구조화)

## 다형성
객체의 기능이 다양한 형태를 가질 수 있음 상속과 깊은 관계를 가진다.
한 부모 밑에서 태어난 자식이 완전히 같을 수 없듯이 객체 또한 부모 클래스로 부터 상속받은 데이터와 기능을
자식 클래스에서 재정의하여 사용할 수 있음

## 객체지향 언어의 장점(절차지향언어와 상대적으로 장점을 얘기하는 것)
1. 재사용성 : 상속을 통해 코드의 재사용을 높일 수 있음.
2. 생상성 향상 : 클래스 단위의 부품들을 조립
3. 유지보수의 우수성 : 구조화된 소스코드 클래스 단위로 소스코드를 관리할 수 있음.

## 객체지향 언어의 단점
1. 객체를 세분화하여 설계하여야한다.
2. 실행 속도가 절차지향 언어 대비 느리다.
3. 상속으로 인하여 관계가 많이 형성되면 코딩의 난이도가 높아진다.

## 절차 VS 객체지향 언어
절차 지향언어의 반대가 객체지향 언어가 아니다!
객체 지향 언어도 절차지향언어에 속하지만 객체라는 녀석들의 관계가 추가된 것이다.

## class
객체에 대하여 정의해 놓은 설계도 혹은 틀
## Object
클래스를 통해 구현 할 수 있는 모든 대상 즉, 해당 클래스로 구현한 인스터스를 대표하는 의미
## instance
객체가 실제로 구현된 것
클래스의 인스턴스라고 표현함.
