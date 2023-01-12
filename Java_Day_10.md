# Java_Day_10

## static
생성될 때 생기는 게 아니라 클래스를 정의하였을 때 static이 붙어있으면 공유하는 메모리가 할다이 된다.  
공유하는 메모리 영역이다.  


## TestA
```java
package j17_스태틱;

public class TestA {
	
	private static int num;
	
	
	public static void setNum(int num) {
		TestA.num = num;
	}
	
	public static int getNum() {
		return num;
	}

}

```

## StaticMain

```java
package j17_스태틱;

public class StaticMain {
	
	public static void main(String[] args) {
		
		
		
		//객체가 생성을 안했는데 메소드를 호출하고 있다.
		System.out.println("출력 1 : " + TestA.getNum());
		System.out.println();
		
		TestA.setNum(100);
		System.out.println("출력 2 : " + TestA.getNum());
	}

}

```

## Student

```java
package j17_스태틱;

public class Student {

		private static final int CODE = 20230000;
		
		private static int ai = 1; //auto_increment
		
		private int studentCode;
		private String name;
		
		public Student(String name) {
			studentCode = CODE + ai;
			ai++;
			this.name = name;
		}
		
		public static int getAutoIncrement() {
			System.out.println("현재 AI : " + 6);
			
			//static 메소드에 꼭 생성이 되어야지만 쓸 수 있는 변수들은 쓸 수 가 없다.
			//static은 class를 선연하고 컴파일 됐을 때 이미 메모리에 할당이 되어 있기 때문에
			//static 메소드 안에서는 static 변수만 가능 단 메소드 안에 있는 변수는 사용가능하다.
//			System.out.println("학생이름 : " + name);
			return ai;
		}
		
		@Override
		public String toString() {//생략가능 단 String 변수에 대입할 때는 toString을 붙여야한다.
			return "Student [studentCode=" + studentCode + ", name=" + name + "]";
		}
		
		
		
		
}

```

## StudentMain
```java
package j17_스태틱;

public class StudentMain {
	
	
	public static void main(String[] args) {
		
		Student[] students = new Student[5];
		Teacher[] teachers = new Teacher[5];
		
		students[0] = new Student("손지호");
		students[1] = new Student("김재영");
		students[2] = new Student("이상현");
		students[3] = new Student("박성진");
		students[4] = new Student("윤선영");
		
		teachers[0] = new Teacher("김준일1");
		teachers[1] = new Teacher("김준일2");
		teachers[2] = new Teacher("김준일3");
		teachers[3] = new Teacher("김준일4");
		teachers[4] = new Teacher("김준일5");
		
		for(int i = 0; i<students.length; i++) {
			System.out.println(students[i]);
			System.out.println(teachers[i]);
			System.out.println();
		}
		 System.out.println(Student.getAutoIncrement()); 
		 
		 int j = 0;
		 
		 for(Student s : students) {//하나씩 꺼내는 용도
			 System.out.println(s);
			 System.out.println(teachers[j]);
			 System.out.println();
			 j++;
		 }
		
	}

}

```
## 동기화
두개의 상태를 동일하게 해주는 것

## 싱글톤
싱글톤은 하나만 존재하여야 하기 때문에 생성자가 private으로 생성한다.  
싱글톤으로 생성된 객체는 모든 곳에서 접근이 가능하다.  
같은 객체를 써야하고 or 하나의 객체로 기능을 조작할 때 쓴다.  
하나의 객체로 공유를 해야할 때 쓴다.  



