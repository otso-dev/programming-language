# java_Thread


### Thread

```java

package j26_스레드;

public class ThreadTest {

	public static void main(String[] args) {
		LoopThread loopThread1 = new LoopThread("김상현");
		LoopThread loopThread2 = new LoopThread("강대협");
		LoopThread loopThread3 = new LoopThread("손지호");
		LoopThread loopThread4 = new LoopThread("김재영");
		
		
		//우선순위 설정
		loopThread1.setPriority(6);
		loopThread4.setPriority(7);
		//thread의 우선순위를 알려줌
		System.out.println(loopThread1.getPriority());
		System.out.println(loopThread2.getPriority());
		System.out.println(loopThread3.getPriority());
		System.out.println(loopThread4.getPriority());
		
		
		//thread는 우선순위별로 실행시킨다 근데 우선순위가 다 같기 때문에 순서별로 출력이 안됨
		//thread의 우선순위는 숫자가 큰게 우선수위가 높다.
		loopThread1.start();
		loopThread2.start();
		loopThread3.start();
		loopThread4.start();
		
		
	}

}


```


### LoopThread

```java
package j26_스레드;

public class LoopThread extends Thread {

	private String threadName;

	public LoopThread(String threadName) {
		this.threadName = threadName;
	}

	@Override
	public void run() {

		for (int i = 0; i < 10; i++) {
			System.out.println(threadName + ": " + i);
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

	}
}


```