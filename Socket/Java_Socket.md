
# java Socket 통신

### SocketClint

```java

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

import com.google.gson.Gson;

import UserManagement.dto.RequestDto;


//단일 양방향
public class SockerClient {
	
	public static void main(String[] args) {
		
		try {
			Socket socket = new Socket("127.0.0.1",9090);//client의 socket은 ip와 server랑 연결시키는 port를 담아서 생성을한다.
			System.out.println("서버에 접속 성공!");
			
			InputStream inputStream = socket.getInputStream();
			InputStreamReader streamReader = new InputStreamReader(inputStream);
			//buffer -> 데이터를 한 덩어리씩 주고받고 할 때 필요하다. 안그러면 문자열을 하나씩 다 잘라서 받아야함
			BufferedReader reader = new BufferedReader(streamReader);
			
			//System.out.println(reader.readLine());
			
			OutputStream outputStream = socket.getOutputStream();
			PrintWriter printWriter = new PrintWriter(outputStream,true);
			
			
			Gson gson = new Gson();
			RequestDto<String> dto = new RequestDto<String>("test","테스트데이터");
			
			printWriter.println(gson.toJson(dto));
			
		} catch (UnknownHostException e) {
			//ip를 잡지 못했을때
			e.printStackTrace();
		} catch (IOException e) {
			//socket의 input output이 전달 못했을때 인터넷이 끊기거나 등등
			e.printStackTrace();
		}
	}
	
}

```


### SocketServer

``` java

package j25_소켓;

import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
//단일 양방향
public class SocketServer {
	
	public static final int PORT = 9090;
	
	public static void main(String[] args) {
		List<Socket> clients = new ArrayList<>();//client에서 보낸 socket을 담는 list
		try {
			ServerSocket serverSocket = new ServerSocket(PORT);//port가 정해져 있음 port가 담겨져 있는체로 serversocket을 생성
			while(true) {
				
				System.out.println("클라이언트의 접속을 기다리고 있습니다.");
				Socket socket = serverSocket.accept();//client의 접속을 기다리는 method client의 요청이 오면 socket에 담음
				clients.add(socket);//client의 socket을 list의 추가 이것으로 client를 구별하거나 데이터를 구분함.
				System.out.println("클라이언트가 연결되었습니다.");
				System.out.println(clients);
				
				OutputStream outputStream = socket.getOutputStream();//
				PrintWriter out = new PrintWriter(outputStream,true);//printwriter -> 문자열을 보내주는 객체, 버퍼기능 탑재
				out.println("___server에 접속한 것을 환영합니다.");
			}
			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
}

```