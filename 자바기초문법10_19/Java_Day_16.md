# java day 16

## java와 MySQL(DB)연결

### DB


### roleinsert class

```java
package j23_database;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class RoleInsert {
	
	//DB를 연결하기위해 pool이라는 전역변수로 설정
	private DBConnectionMgr pool;
	
	//생성자에 DBConnectionMgr를 생성 (싱글톤)
	public RoleInsert() {
		pool = DBConnectionMgr.getInstance();
	}
	
	//DB에 role_mst 테이블에 데이터를 집어넣기위해 메소드를 만듬
	public int saveRole(String roleName) {
		int successCount = 0;
		
		//쿼리문을 문자열로 받아야하기 때문에 String으로 잡음
		String sql = null;
		
		//Connection이라는 인터페이스로 DB와 연결
		Connection con = null;
		//PreparedStatement 작성한 쿼리문을 DB에 넣기 위해서 pstmt로 잡음
		PreparedStatement pstmt = null;
		
		try {
			
			//직접적인 DB와 연결
			con = pool.getConnection();
			//sql에 작성할 쿼리문 values(0 == pk값(db에 AI를 체크해줬기 때문에 자동으로 증가함),? == (?를 한 이유 자기가 원하는 데이터 값을 넣기 위해서)
			sql = "insert into role_mst values(0,?)";
			//Connection으로 연결된 DB에 prepareStatement() 메소드 안에 작성한 쿼리문과 DB상에 자동으로 생성된 key값을 넣어서 쓰겠다.
			pstmt = con.prepareStatement(sql,Statement.RETURN_GENERATED_KEYS);
			
			//pstmt안에있는 setString메소드를 써서 첫번째 인자는 ?의 순번을 나타내고,두번째 인자는 ?에 넣을 데이터를 넣는다)
			pstmt.setString(1, roleName);
			
			//insert, update, delete를 DB에 적용시키기 위해 executeUpdate() 메소드를 호출함
			//데이터를 집어 넣으면 변수에 성공한 갯수만큼 변수에 집어넣음
			successCount = pstmt.executeUpdate();
			
			//새로운 키값 설정
			int newKey = 0;
			
			//테이블안에 있는 자동적으로 넣은 키값을 추적하기 위해getGeneratedKeys()를 이용
			ResultSet rs = pstmt.getGeneratedKeys();
			//rs에 담겨진 키값을 next
			if(rs.next()) {
				newKey = rs.getInt(1);//
			}
			
			System.out.println(newKey != 0 ? "새로운 키값: " + newKey : "키가 생성되지 않음");
			
		} catch (Exception e) {
			
			e.printStackTrace();
		}
		
		return successCount;
	}
	
	public static void main(String[] args) {
		RoleInsert roleInsert = new RoleInsert();
		
		int successCount = roleInsert.saveRole("ROLE_TESTER");
		
		System.out.println("insert 성공 건수: " + successCount);
		
		
		
	}

}

```
