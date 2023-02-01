# java day 20

## Function
```java
//Function <T,R>
		Function<String, Integer> h = num -> Integer.parseInt(num);
		
		int coverStrNum1 = h.apply("10000");
		int coverStrNum2 = h.apply("20000");
		
		System.out.println(coverStrNum1+coverStrNum2);
```

## Predicate

```java
Function<Predicate<String>, Boolean> function1 = predeicate -> predeicate.or(str -> str.startsWith("이"))
				.test("김준일");

		boolean rs = function1.apply(str -> str.startsWith("김"));
		System.out.println(rs);

		List<String> nameList = new ArrayList<>();
		nameList.add("김종환1");
		nameList.add("고종환2");
		nameList.add("김종환3");
		nameList.add("김종환4");
```

## Stream

```java
//Stream -> 일회용
		Stream<String> stream = nameList.stream().filter(name -> name.startsWith("김"));
		//stream.forEach(name -> System.out.println(name));
		List<String> newList = stream.collect(Collectors.toList());
		
		System.out.println(newList);
		
		System.out.println("=====================================================");
		
		nameList.stream()
			.filter(name -> name.startsWith("김"))
			.collect(Collectors.toList())
			.forEach(name -> System.out.println(name));
```
