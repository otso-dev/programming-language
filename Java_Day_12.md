# Java_Day_12

## Set
>set도 list와 똑같은 메소드들을 가지고 있다.  
set은 get 메소드가 없다. 왜냐하면 set은 키값이 없다.  
그래서 무조건 forEach를 써서 값을 가져오거나 탐색을 해야한다.  
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

## map

