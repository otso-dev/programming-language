# Java_Day_6

## 2차원배열
>2차원배열이라고 하지만 배열을 담는 배열이라고 생각하면 된다. 형태는 int[][] nums = new int[3][2]; 이다.

```java
package J12_배열;

public class DoubleArray1 {
	
	public static void main(String[] args) {
		
		int num = 0;
		
		int [] nums = new int[2];
		
		int[][] d_nums = new int[3][2];
		
		d_nums[0][0] = 1;
		d_nums[0][1] = 4;
		
		d_nums[1][0] = 2;
		d_nums[1][1] = 5;
		
		d_nums[2][0] = 3;
		d_nums[2][1] = 6;
		
		for(int i = 0; i < 2; i++) {
			for(int j = 0; j < 3; j++) {
				System.out.println(d_nums[j][i]);
				
			}
		}
		
		int[][] d_nums2 = new int[][] {{1,2,3},{5,6}};
		
//		for(int i = 0; i < 2; i++) {
//			for(int j = 0; j < 3; j++) {
//				System.out.println(d_nums2[i][j]);
//				
//			}
//		}
		
		System.out.println(d_nums2.length);//바깥쪽 길이
		System.out.println(d_nums2[1].length);//안쪽 길이
		
		
		for(int i = 0; i<d_nums2.length; i++) {
			for(int j = 0; j < d_nums2[i].length; j++) {
				System.out.println(d_nums2[i][j]);
			}
		}
		
		
	}
}

```

## User class

### class를 활용한 회원관리 프로그램
```java
package J12_배열;

public class J12_User {
	
	
	//Entity -> 정보를 담는 객체
	private String username;
	private String password;
	private String name;
	private String email;
	
	public J12_User() { // ctrl + space
	
	}
	
	//alt +shitf + s
	public J12_User(String username, String password, String name, String email) {
		super();
		this.username = username;
		this.password = password;
		this.name = name;
		this.email = email;
	}
	
	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	@Override
	public String toString() {
		return "J12_User [username=" + username + ", password=" + password + ", name=" + name + ", email=" + email
				+ "]";
	}
	
	
	
}

```

## UserRepositoty class

```java
package J12_배열;


//저장소
public class J12_UserRepositoty {
	
	private J12_User[] userTable;

	public J12_UserRepositoty(J12_User[] userTable) {
		this.userTable = userTable;
	}
	
	public J12_User[] getUserTable() {
		return userTable;
	}
	
	public void saveUser(J12_User user) {
		extendArrayOne();
		userTable[userTable.length - 1] = user;
	}
	
	private void extendArray(int length) {
		J12_User[] newArray = new J12_User[userTable.length + length];
		transferDataToNewArray(userTable, newArray);
		userTable = newArray;
	}
	
	private void extendArrayOne() {
		J12_User[] newArray = new J12_User[userTable.length + 1];
		transferDataToNewArray(userTable, newArray);
		userTable = newArray;
	}
	
	private void transferDataToNewArray(J12_User[] oldArray, J12_User[] newArray) {
		for(int i = 0; i < oldArray.length; i++) {
			newArray[i] = oldArray[i];
		}
	}
	
	
}

```

## UserService class

```java
package J12_배열;

import java.util.Scanner;
/*	
 * 프로세서 => cpu
 * 프로세스는 여러개의 쓰레드를 가지고 있음
 */
public class J12_UserService {

	private Scanner scanner;

	public J12_UserService() {//초기값을 지정할 때는 생성자에 한다. 메모리 절약
	 scanner = new Scanner(System.in);
	}

	public void run() {
		boolean loopFlag = true;
		char select = '\0';
		while (loopFlag) {
			showMainMenu();
			select = inputSelect("메인");
			loopFlag = mainMenu(select);
		}
	}

	public void stop() {
		for(int i = 0; i < 10; i++) {
			try {
				Thread.sleep(500);
				System.out.println("프로그램 종료중....(" + ( i + 1 ) +"/10)");
			} catch (InterruptedException e) {
				
				e.printStackTrace();
			}
		}
		System.out.println("프로그램 종료");
	}
	
	private char inputSelect(String menuName) {
		System.out.print(menuName + " 메뉴선택 : ");
		char select = scanner.next().charAt(0);
		scanner.nextLine();// 버퍼를 비워주기
		return select;
	}

	private void showMainMenu() {
		System.out.println("========<< MainMenu >>========");
		System.out.println("1. 회원 전체 조회");
		System.out.println("2. 회원 등록");
		System.out.println("3. 사용자이름으로 회원 조회");
		System.out.println("4. 회원 정보 수정");
		System.out.println("==============================");
		System.out.println("q. 프로그램 종료");
		System.out.println();
	}
	
	private boolean mainMenu(char select) {
		boolean flag = true;
		
		if(isExit(select)) {
			flag = false;
		}else {
			if(select == '1') {
				
			}else if(select == '2') {
				
			}else if(select == '3') {
				
			}else if(select == '4') {
				
			}else {
				System.out.println(getSelectErrorMessage());
				
			}
		}
		System.out.println();
		
		return flag;
	}
	
	private boolean isExit(char select) {
		return select == 'q' || select == 'Q';
	}
	
	private String getSelectErrorMessage() {
		return "###<< 잘못된 입력입니다. 다시 입력하세요. >>###";
	}
}


```

## UserMain class

```java
package J12_배열;

public class J12_UserMain {
	
		public static void main(String[] args) {
			J12_UserService service = new J12_UserService();
			
			service.run();
			service.stop();
		}
		
}


```
