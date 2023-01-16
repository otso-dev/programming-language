# Java_Day_12

## Set
>set도 list와 똑같은 메소드들을 가지고 있다.  
set은 get 메소드가 없다. 왜냐하면 set은 키값이 없다.  
그래서 무조건 forEach를 써서 값을 하나씩 가져오거나 탐색을 해야한다.  
```java
package j19_컬렉션;

import java.util.Set;

public class SetStringMain {
	
	public static void main(String[] args) {
		Set<String> setStr = new HashSet<>();
		
		setStr.add("김상현");
		setStr.add("강대협");
		setStr.add("손지호");
		setStr.add("최해혁");
		
		System.out.println(setStr);
		String searchName = "손지호";
		
		for(String name : setStr) {//값을 직접 꺼내서 비교해야한다.
			if(name.equals(searchName)) {
				System.out.println(name);
			}
		}
		
	}

}
```
### Set addAll
```java
	Set<String> setStr = new HashSet<>();//중복 X
		List<String> listStr = new ArrayList<>();//중복 O
		
		listStr.add("임나영");
		listStr.add("이강용");
		listStr.add("임나영");
		listStr.add("임나영");
		
		System.out.println(listStr);
		
		setStr.add("김상현");
		setStr.add("강대협");
		setStr.add("손지호");
		setStr.add("최해혁");
		setStr.add("최해혁");
		setStr.addAll(listStr);//매개변수가 Collection이라서 list, set과 같은 것들도 넣을 수 있다.
		//set은 값의 중복을 허용하지 않기 때문에 list의 중복된 값은 하나만 들어가게 된다.
```


### Set Iterator
```java
Iterator<String> iterator = setStr.iterator();
		
		while(iterator.hasNext()) {
			String n = iterator.next();
			if(n.equals(searchName)) {
				System.out.println(n);
			}
		}
```

### HashSet
> hashcode의 값으로 정렬된 Set  
```java
package j19_컬렉션;

import java.util.HashSet;
import java.util.Set;

public class StudentHashSet {

	
	private static Student searchStudent(Set<Student> students, String searchName) {
		Student student = null;
		
		for(Student s : students) {
			if(s.getName().equals(searchName)) {
				student = s;
				break;
			}
		}
		return student;
	}
	
	public static void main(String[] args) {
		Set<Student> students = new HashSet<>();
		
		students.add(new Student("이현수", 26));
		students.add(new Student("정의현", 24));
		students.add(new Student("김수현", 31));
		students.add(new Student("이종현", 32));
		
		System.out.println(students);
		
		Student student = searchStudent(students, "김수현");
		
		if(student == null) {
			System.out.println("검색실패");
		}else {
			System.out.println("검색성공" + student);
		}
		
	}
	
	
}

```
## map
```java
package j19_컬렉션;


import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class MapStringMain {

	public static void main(String[] args) {

		// Map은 Key는 Set, Value는 List 형식이다.
		Map<String, String> strMap = new HashMap<>();

		// Map add가 아닌 put이 있다.
		strMap.put("이종현", "a");
		strMap.put("진채희", "b");
		strMap.put("김재영", "c");
		strMap.put("이상현", "d");

		System.out.println(strMap);

		// map은 키값이 있기 때문에 get이 존재함
		System.out.println(strMap.get("a"));
		System.out.println(strMap.get("e"));

		// Map은 Key값이 지정해서 넣어주기 때문에 for문을 쓸 수 없다.
		// forEach도 Map은 Key와 Value를 한쌍으로 가지기 때문에 쓸 수 없다.

		// 그래서 keySet을 이용해 키값만 꺼내와서 forEach를 쓸 수 있다.
		for (String k : strMap.keySet()) {
			System.out.println("Key: " + k);
			System.out.println(strMap.get(k));// 꺼낸 Key값을 이용해 Value를 꺼낼 수 있음.
		}

		
		//key값이 hash값으로 정렬이 되서 나오기 때문에 순서대로 안나온다.
		for(String v : strMap.values()) {
			System.out.println("Value: " + v);
		}
		
		//key와 value를 한번에 들고오고 싶을 때 Entry를 쓴다.
		//Entry는 key와 value의 값을 다 가지고 있는 하나의 객체이다.
		System.out.println(strMap.entrySet());
		
		//Set<Entry<String, String>> s = null;
		
		for(Entry<String,String> entry : strMap.entrySet()) {
			System.out.println(entry);
			System.out.println("key: " + entry.getKey()); 
			System.out.println("value: " + entry.getValue()); 
		}
		
		System.out.println("==================================");
		
		//람다식
		strMap.forEach((k,v) -> {
			System.out.println("key: " + k);
			System.out.println("value: " + v);
		});
		
	}

}

```
### HashMap
>Map의 Key값이 Hashcode로 정렬된 Map
```java
package j19_컬렉션;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class HashMapTest {

	
	public static void main(String[] args) {
		Map<String, Object> dataMap = new HashMap<>();
		dataMap.put("username", "aaa");
		dataMap.put("password", "1234");
		dataMap.put("name", "김준일");
		dataMap.put("email", "aaa@gmail.com");
		
		
		List<String> hobby = new ArrayList();
		hobby.add("골프");
		hobby.add("축구");
		hobby.add("농구");
		hobby.add("음악감상");
		
		dataMap.put("hobbys", hobby);
		
		System.out.println(dataMap);
		
		
		List<String> list = (List<String>)dataMap.get("hobbys");
		System.out.println(list.get(0));
		
		for(Entry<String, Object> entry : dataMap.entrySet()) {
			System.out.println("key : " + entry.getKey());
			System.out.println("value : " + entry.getValue() );
		}
		
	}
	
}


```

## java bulid tool
Maven
- Ant의 대안으로 만들어진 자바용 프로젝트 관리 도구
- 표준화된 포맷을 제공(Pom.xml)
- 외부 저장소에서 필요한 라이브러리와 플러그인들을 로컬시스템의 캐시하여 관리
- 프로젝트의 전체적인 라이프사이클을 관리
- 상속구조를 이용한 멸티 모듈 구현

MVN -> java라이브러리를 모아둔 사이트.  
Group id -> 도메인을 뒤집은 형식  
Version -> 0.0.0 -> 주버전.부버전.수버전  
주버전 대규모 업데이트  
부버전 기능을 추가 or 삭제  
수버전 에러 수정  


## JSON
> JSON 개발자라면 무조건 알아야하는 데이터 포맷이다.(공통 자료형)  
> JSON은 모든 언어가 가지고 있는 데이터 형식이다.  
> JSON은 value가 Object인 Map과 같은 형식이라고 볼 수 있다.  
> JSON을 -> 객체로 , 객체를 -> JSON 형태로 바꿀 수 있어야한다.  
> JSON은 시작부터 끝까지 모두 문자열이다.  
> ex) JSON 형식  
``` JSON
//JSON 형식
//key값은 무조건 문자열
 "{
 "key" : "value"
 }"
 
 ex)[user]
 
  
 "{
   "username" : "junil",
   "password" : "1234",
   "name" : "김준일",
   "email" :"aaa@gmail.com"
   "age" : 30 ->숫자는 그냥 숫자로
   "hobby" : [
		"골프",
		"농구",
		"축구"
	     ],
	  	"school" : {
			"schoolName" : "부산교육대학원",
			"address" : "부산시"
			}
  }"
```
## Gson
> Gson은 Java 개체를 JSON 표현으로 또는 그 반대로 변환하는 데 사용할 수 있는 Java 라이브러리입니다. Google에서 개발했으며 JSON 데이터 작업을 위해 Java 커뮤니티에서 널리 사용됩니다. Gson은 Java 개체를 JSON으로 직렬화 및 역직렬화하기 위한 간단하고 사용하기 쉬운 API를 제공합니다. 또한 복잡한 데이터 구조와 중첩된 개체를 처리할 수 있으며 다양한 유형의 JSON과 Java 개체 간에 자동으로 변환할 수 있습니다. 또한 객체가 직렬화 및 역직렬화되는 방식을 사용자 정의할 수 있는 강력한 구성 옵션 세트가 있습니다. 전반적으로 Gson은 단순성, 성능 및 유연성으로 인해 Java에서 JSON으로 작업하는 데 널리 사용됩니다.

### Gson을 이용해 JSON -> Object로 Object -> JSON Code
```java
package j20_JSON;

import java.util.HashMap;
import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;

import j20_JSON.builder.User;

public class JsonMap {
	
	public static void main(String[] args) {
		
		//Gson을 기본 생성자로 생성했을때는 JSON에 맞게 출력을 안해줌
		Gson gson = new Gson();
		
		//JSON 형식으로 출력을 해줌
		//serializeNulls은 null을 출력해주는 메소드
		gson = new GsonBuilder().setPrettyPrinting().serializeNulls().create();
		
		//Object(Map) -> JSON
		Map<String,Object> user = new HashMap<>();
		user.put("username", "aaa");
		user.put("password", "1234");
		user.put("name", null);
		
		String userJson = gson.toJson(user);
		System.out.println(user);
		System.out.println(userJson);
		
		//JSON -> Object(Map)
		Map<String,Object> userMap = gson.fromJson(userJson, Map.class);
		//JSON -> Object(class)
		User userObj = gson.fromJson(userJson, User.class);
		
		System.out.println(userMap);
		System.out.println(userObj);
		
		JsonObject jsonObject = new JsonObject();
		jsonObject.addProperty("test1", "aaa");
		jsonObject.addProperty("test2", "bbb");
		jsonObject.addProperty("test3", "ccc");
		
		String jsonObjectStr = jsonObject.toString();
		System.out.println(jsonObjectStr);
		
		
	}

}

```

## builder 패턴
> class 안에 class가 있는 구조  
> AllArgsConstructor가 필수이다.  
> class를 생성할 때 원하는 변수 값을 넣고 싶은데 생성자 오버라이딩이 불가능 할 때 쓴다.  
> lombok을 이용하여 @builder를 이용하면 쉽게 구현이 가능하다

### User class
```java
package j20_JSON.builder;

import lombok.AllArgsConstructor;
import lombok.Data;

//builder 패턴
//class 안에 class
//AllArgsConstructor가 필수다.
//생성할 때 원하는 변수 값만 넣고 싶을 때 
@Data
//@Builder //AllArgsConstructor도 같이 import된다.
@AllArgsConstructor
public class User {

	private String username;
	private String password;
	private String name;
	private String email;
	
	

//	public static UserBuilder builder() {
//
//		return new UserBuilder();// User class안에있는 UserBuider를 생성
//	}
//
//	// 내부 class
//	// class 안에 있는 class를 쓸려면 user를 생성해야 쓸 수있다. 그래서 static을 활용해 생성
//	// 하지 않고도 쓸 수 있도록 하였다.
//	@Data
//	public static class UserBuilder {
//		private String username;
//		private String password;
//		private String name;
//		private String email;
//
//		public UserBuilder username(String username) {
//			this.username = username;
//			return this;
//		}
//
//		public UserBuilder password(String password) {
//			this.password = password;
//			return this;
//		}
//
//		public UserBuilder name(String name) {
//			this.name = name;
//			return this;
//		}
//
//		public UserBuilder email(String email) {
//			this.email = email;
//			return this;
//		}
//
//		public User build() {// 생성된 UserBuider객체 안에 User를 생성하는 build를 쓸 수있다.
//			// User를 생성하면 User안에 있는 멤버변수에 접근할 수 있다.
//			return new User(username, password, name, email);
//		}
//	}

}

```

### UserBuilder class
> class안에 class를 만들어도 되지만 이렇게 따로 빼도 상관은 없다.  
```java
package j20_JSON.builder;

public class UserBuilder {

	
	private String username;
	private String password;
	private String name;
	private String email;

	public UserBuilder username(String username) {
		this.username = username;
		return this;
	}

	public UserBuilder password(String password) {
		this.password = password;
		return this;
	}

	public UserBuilder name(String name) {
		this.name = name;
		return this;
	}

	public UserBuilder email(String email) {
		this.email = email;
		return this;
	}

	public User build() {// 생성된 UserBuider객체 안에 User를 생성하는 build를 쓸 수있다.
		// User를 생성하면 User안에 있는 멤버변수에 접근할 수 있다.
		return new User(username, password, name, email);
	}
}

```

### UserMain

```java
package j20_JSON.builder;

public class UserMain {

	public static void main(String[] args) {
		
		//User user = new User();
		
		 
		//User.UserBuilder userBuilder = new User.UserBuilder();
		
		User user2 = new UserBuilder()
				.username("aaa")
				.password("1234")
				.name("정성현")
				.build();
		
		System.out.println(user2);
	}
}

```
## 예외처리
>프로그램의 오류를 예외라고 한다. 프로그램이 예외처리를 하지 않고 예외를 만나면 프로그램이 팅기는 현상이 발생한다.  
>프로그램이 갑자기 종료될 때 임시저장을 하거나 예외를 처리하는 것을 예외처리라고 한다.

```java
package j21_예외;

//예외처리
//프로그램의 오류를 예외라고 한다.
//
public class ArrayException {

	public static void main(String[] args) {

		Integer[] nums = { 1, 2, 3, 4, 5 };

		try {// if else와 비슷 try -> 예외가 일어날수도 있는 부분
			throw new NullPointerException();// 강제로 예외를 일어나게 하는 것.
//			for (int i = 0; i < 6; i++) {
//				System.out.println(nums[i]);
//			}
		} catch (IndexOutOfBoundsException e) {// 예외가 일어난 부분을 받는 부분
			System.out.println("예외 처리함");
		} catch (NullPointerException e) {
			System.out.println("빈값 처리함");
		} catch (Exception e) {// 마지막에는 Exception을 해주는게 좋다.(모든 예외처리를 다 예상 못하기 때문에)
			System.out.println("예상 못한 예외 처리함");
		}

		System.out.println("프로그램 정상 종료");

	}

}

```
