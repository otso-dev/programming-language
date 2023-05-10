# Java_Day_9

# Object 클래스
최상위 클래스이다.  
java에서 클래스를 만들 때 항상 Object클래스를 상속 받는다.  
근데 java에서는 다중 상속이 불가능하다. 하지만 다중상속 개념이아니라  
Object and A -> B X  Object -> A -> B  O
Object는 어차피 최상위 클래스이기 때문에 제일 위에서 타고 내려가는 개념이다.  
Object 내에 있는 메소드들을 오버라이드를 해서 재정의 할 수 있다.

# Object 클래스 안에 있는 메소드 활용 (오버라이드)

## ToString

Object class 안에 있는 원형 toString 메소드
```java
 public String toString() {
        return getClass().getName() + "@" + Integer.toHexString(hashCode());
    }
    //class의 이름과 주소값을 String으로 값을 리턴함
```

Object는 모든 클래스의 상위클래스이므로 오버라이드가 가능  
toString 메소드를 오버라이드하여 재정의
```java
@Override
	public String toString() {

		return "이름" + name + "\n나이 : " + age;
	}
```

## Equals

원형 equals 메소드
```java
public boolean equals(Object obj) {
        return (this == obj);
    }
    //외부로 받은 객체를 자기의 주소값과 같은지 비교한 값을 리턴함.
```

equals 재정의

```java
@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (obj == null) {
			return false;
		}
		if (!(obj.getClass() == Student.class)) {
			return false;
		}
    // instance는 상속관계를 가질 때 문제가 생기기 때문에 사라졌다.
    // a b c 가 상속관계에 있을 때 b객체인지 아닌지 알고싶은데 c라는 클래스가 b와 a를 포함하는 관계성 때문에 true가 반환된다.
    // 그래서 instance가 아닌 getclass와 class.class를 쓴다.
    
		Student s = (Student) obj;//다운캐스팅을 할 떄에는 정확하게 타입을 지정해라.
		boolean result = name.equals(s.name) && age == s.age;

		return result;
	}

```

## HashCode

원형 HashCode 메소드
```java
  public native int hashCode();
  //클래스.hashcode를 하면 클래스의 주소값을 반환한다.
```
HashCode 재정의

```java
@Override
	public int hashCode() {

		return Objects.hash(name, age); // java.util -> 데이터를 관리할 수 있는 도구들이 있음.
    
    //name과 age를 hash알고리즘을 이용해 정수로된 값을 리턴 시켜줌
    //해쉬코드를 쓰는 이유는 두 객체를 비교 할 때 비용을 절감 시켜준다.
	}
```
## getclass

원형 getclass

```java
@IntrinsicCandidate
    public final native Class<?> getClass();
//객체로 생성된 class의 정보가 담겨져 있다.
```

## finalize
garbage collection로 동적할당을 한 객체가 소멸할 때 호출이 되는 메소드이다.
```java
package j16_Object;

// 이 패키지 안에서만 참조가 가능 하지만 이렇게 쓰지 말 것.
class Test {
	private int num;

	public Test(int num) {
		super();
		this.num = num;
		System.out.println(num + "생성");
	}

	@Override
	protected void finalize() throws Throwable {// 가비지 콜렉터로 소멸이 됐을 때 호출이 된다.
		// 이것을 언제 써야하는가. 데이터를 보존하고 싶을 때
		System.out.println(num + "객체 소멸");
	}
}

public class ObjectFinalize {

	public static void main(String[] args) {

		Test test = null;

		for (int i = 0; i < 10; i++) {
//			try {
//				Thread.sleep(500);
//			} catch (InterruptedException e) {
//				
//				e.printStackTrace();
//			}

			test = new Test(i);

			test = null;

			System.gc();// 강제로 가비지 컬렉터를 호출하는 것 , JVM이 여유가 있을 떄 호출됨
		}
	}

}

//얕은 복사
//같은 놈
//user u = new user()
//user u1 = u;
//스텍 메모리에 변수를 만들어 복사를 한 것

//깊은 복사
//다른 놈
//객체를 새로 만들어 객체 안에 있는 데이터까지 복사를 하는 것

/* finalize를 쓰는 이유 (오버라이드)
 * 소멸한 데이터가 나중에 쓰기 위해 만들었는데 가비지 콜렉터가 소멸을 하였을 때
 * finalize를 이용해 옮기기 위해 쓰인다.
 * */
 
```


# .class
getclass()메소드와 똑같은 기능을 하지만 getclass()메소드는 객체를 생성해야지만 쓸 수있다.  
.class는 객체를 생성하지 않아도 해당 클래스의.class를 붙여주면 해당 클래스의 정보를 확인 할 수 있다.
equals를 할 때 getclass와 같이 해당 클래스가 일치하는지 안하는지 사용가능하다.
```java
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (obj == null) {
			return false;
		}
		if (!(obj.getClass() == Student.class)) {// instance는 상속관계를 가질 때 문제가 생기기 때문에 사라졌다.
			return false;
		}

		Student s = (Student) obj;//다운캐스팅을 할 떄에는 정확하게 타입을 지정해라.
		boolean result = name.equals(s.name) && age == s.age;

		return result;
	}

```

