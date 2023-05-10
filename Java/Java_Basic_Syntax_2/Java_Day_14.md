# Java Day 14


## window builder tool

### class 계층도
![화면 캡처 2023-01-26 002500](https://user-images.githubusercontent.com/51119920/214605444-46b1ab7c-5bad-43f6-9070-840e82b06b00.png)

### JFrame

### JPanel

### JButton

### JLabel

### JFieldText

### JPasswordField

### CardLayout

### 어댑터 패턴
어댑터 패턴 -> 구현하고 싶은 메소드만 골라서 구현 할 수 있다.  
인터페이스안에 메소드들을 쓸려면 모든 메소드들을 오버라이드 해야하는데  
익명클래스를 이용해 자기가 쓰고 싶은 메소드들만 오버라이드 해서 쓸 수 있다.  

### 어댑터 패턴을 이용해 로그인 구현부분
mouseClicked의 메소드를 오버라이드해서 클릭할때만 이 메소드가 호출되기 때문에 호출되는 메소드만 어댑터 패턴을 이용해  
로그인 버튼을 클릭시 로그인을 하는 코드를 구현하였음.
```java
LoginButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JsonObject loginUser = new JsonObject();
				loginUser.addProperty("usernameAndEmail", UsernameTextField.getText());
				loginUser.addProperty("password", passwordField.getText());
				
				UserService userService = UserService.getInstance();
				
				Map<String,String> response = userService.authorize(loginUser.toString());
				
				if(response.containsKey("error")) {
					JOptionPane.showMessageDialog(null, response.get("error"),"error",JOptionPane.ERROR_MESSAGE);
					return;
				}
				JOptionPane.showMessageDialog(null, response.get("ok"),"ok",JOptionPane.INFORMATION_MESSAGE);
				
			}
		});
```

### 회원가입

```java
JButton RegisterButton = new JButton("Register");
		RegisterButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JsonObject userJson = new JsonObject();
				userJson.addProperty("username", registerUsernameField.getText());
				userJson.addProperty("password", registerPasswordField.getText());
				userJson.addProperty("name", registerNameField.getText());
				userJson.addProperty("email", registerEmailField.getText());
			
				UserService userService = UserService.getInstance();
				
				Map<String,String> response = userService.register(userJson.toString());
				
				if(response.containsKey("error")) {
					JOptionPane.showMessageDialog(null, response.get("error"),"error",JOptionPane.ERROR_MESSAGE);
					return;
				}
				
				JOptionPane.showMessageDialog(null, response.get("ok"),"ok",JOptionPane.INFORMATION_MESSAGE);
				mainCard.show(MainPanel, "loginPanel");
				clearFields(registerFeilds);
				
			}
		});
```

### 로그인
```java
LoginButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JsonObject loginUser = new JsonObject();
				loginUser.addProperty("usernameAndEmail", UsernameTextField.getText());
				loginUser.addProperty("password", passwordField.getText());
				
				UserService userService = UserService.getInstance();
				
				Map<String,String> response = userService.authorize(loginUser.toString());
				
				if(response.containsKey("error")) {
					JOptionPane.showMessageDialog(null, response.get("error"),"error",JOptionPane.ERROR_MESSAGE);
					return;
				}
				JOptionPane.showMessageDialog(null, response.get("ok"),"ok",JOptionPane.INFORMATION_MESSAGE);
				
			}
		});
```
