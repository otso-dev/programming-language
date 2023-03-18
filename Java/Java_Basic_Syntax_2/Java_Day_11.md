# Java_Day_11

## Generic
- 형태 class 클래스명<>
- Generic은 wrapper class 자료형만 쓸 수 있다. 일반 자료형은 쓸 수 없다.(wrapper classs는 String과 같이 자료형을 클래스화 시킨 것)
- 자료형을 바꾸고 싶을 때 쓴다.
- Generic은 생성될 때 자료형을 판단하기 때문에 자료형을 마음대로 바꿀 수 있다.
- ?키워드는 생성시 자동으로 자료형을 가져온다. 하지만 가능한 자료형을 명시하는 것이 좋다. ex) TestData<?,?> td = new TestData<> ("정성현",30);
- Generic은 Generic안에 있는 타입의 자료형을 가져 올 수 있다.
- ? -> 와일드카드라고 부른다.(어떠한 형태든지 쓸 수 있다.)
- ? extends class명 대상 하위 객체
- ? super class명 대상 상위 

## TestData class

```java
package j18_제네릭;

public class TestData<T,E> {
	
	//제네릭은 래퍼 클래스 자료형만 쓸 수 있다. ->일반 자료형은 쓸 수 없다.
	//자료형을 바꾸고 싶을 때 쓴다.
	//자료형을 클래스화 시킨 것을 wrapper Class라고 한다.
	private T data1;//char
	private E data2;//int
	
	public  TestData(T data1, E data2) {
		this.data1 = data1;
		this.data2 = data2;
	}

	@Override
	public String toString() {
		return "TestData [data1=" + data1 + ", data2=" + data2 + "]";
	}
	

}

```

## CMRespDto class

Commit Message Response Data Transfer Object
클라이언트가 서버에게 요청을 날리면 동일한 형식으로 응답해주는 응답인터페이스

```java
package j18_제네릭;


//Commit Message Response Data Transfer Object
//클라이언트가 서버에게 요청을 날리면 동일한 형식으로 응답해주는 응답인터페이스

public class CMRespDto<T> {
	
	private int code;
	private String message;
	private T data;
	
	public CMRespDto(int code, String message, T data) {
		super();
		this.code = code;
		this.message = message;
		this.data = data;
	}
	
	@Override
	public String toString() {
		return "CMRespDto [code=" + code + ", message=" + message + ", data=" + data + "]";
	}
	
	
	
	
	
}

```

## main class

``` java
package j18_제네릭;

public class Main {

	//?는 생성시 자동으로 자료형을 가져옴
	//가능한 자료형을 명시하는 것이 좋음
	//TestData<?,?> td = new TestData<> ("정성현",30);
	
	public static void main(String[] args) {
		TestData<String, Integer> td = new TestData<String, Integer>("jsh", 100);
		TestData<String, Double> td2 = new TestData<String, Double>("jsh", 100.05);// 제네릭은 생성될 때 타입을 결정한다.

		
		
		System.out.println(td);
		System.out.println(td2);
		
		
	//generic 안에 generic 타입의 자료형을 가져올 수 있음
	//data안에 td의 자료형인 TestData<String,Integer>를 넣음
		
		CMRespDto<TestData<String, Integer>> cm = 
				new CMRespDto<TestData<String, Integer>>(200, "김준일", td);
	
		//td의 자료형을 ?을 이용해 자동으로 가져옴
//		CMRespDto<TestData<?,?>> cm =
//				new CMRespDto<TestData<?,?>>(20, "성공", td);
//		CMRespDto<?> cm =
//				new CMRespDto<>(200, "성공", td);

		System.out.println(cm);
		
	}

}

```
## collection 

- collection framework 주요 인터페이스
- List
- Set
- Map

## 주요 인터페이스 간의 상속 관계
![collection_주요 인터페이스 상속관계](https://user-images.githubusercontent.com/51119920/212228854-a25b374f-4073-489d-b310-86cc9a6b7f48.png)

## 구조
### List(배열)  
 - 순서 O, 중복 O  

>![List_구조](https://user-images.githubusercontent.com/51119920/212241237-e357c0d9-12e7-4820-9dc5-e310a25033c1.png)


### Set(집합) 
 - 순서 X, 중복 X  
>![Set_구조](https://user-images.githubusercontent.com/51119920/212241276-56680343-bc1d-4464-be4b-0b3150e400a0.png)


### map   
 - Key와 Value를 가진다.
 - Key -> Set과 같은 구조(순서 X, 중복 X) value -> 중복 O
>![map_구조](https://user-images.githubusercontent.com/51119920/212241391-9aab3b91-1efb-47c8-b63c-b0cc3a66c6f9.png)

### collection framework

> ***framework*** -> 틀 안에서 일을 하는 것. (틀 안에서 자유롭게 개발해라)  
필요한 이유 -> 각자의 개발 방식이 다를 수 있기때문에 틀을 정해주고 그 안에서 개발을 자유롭게 하기 위해서.  
collection framework -> java안에서 쓰는 다수의 데이터를 쉽고 표준화된 방법을 제공하는 클래스의 집합을 의미  
즉, 데이터를 저장하는 자료구조 와 데이터를 처리하는 알고리즘을 구조화하여 클래스로 구현해 놓은 것이다.  
이러한 collection framework는 java의 interface를 사용하여 구현이 되어있다.


