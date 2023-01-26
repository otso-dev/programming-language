# Java day 17

## pool

![pool의 구조](https://user-images.githubusercontent.com/51119920/214733801-f29f942e-e46e-4145-85b2-745d3a4174f6.png)

## java와 DB연결 구조
![java_db 연결 전체구조](https://user-images.githubusercontent.com/51119920/214733804-54140462-fc05-4fec-a7d0-b769f73e7878.png)

# 회원가입 DB연동

## UserRepository class
DB와 연동하기 위해 DBConnectionMgr를 선언
```java
  public class UserRepository {

	
	private static UserRepository instance;
	
	public static UserRepository getInstance() {
		if(instance == null) {
			instance = new UserRepository();
		}
		
		return instance;
	}
	
	private DBConnectionMgr pool;
	
	private UserRepository() {
		pool = DBConnectionMgr.getInstance();
	}
```
## saveUser 메소드
```java
public int saveUser(User user) {
		int successCount = 0;
		
		Connection con = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		String sql = null;
		
		try {
			con = pool.getConnection();
			
			sql = "insert into user_mst\r\n"
					+ "values(0, ?, ?, ?, ?);";
			
			pstmt = con.prepareStatement(sql,Statement.RETURN_GENERATED_KEYS);
			pstmt.setString(1, user.getUsername());
			pstmt.setString(2, user.getPassword());
			pstmt.setString(3, user.getName());
			pstmt.setString(4, user.getEmail());
			
			successCount = pstmt.executeUpdate();
			
			rs = pstmt.getGeneratedKeys();
			
			if(rs.next()) {
				user.setUserId(rs.getInt(1));
			}

		} catch (Exception e) {
			
			e.printStackTrace();
		} finally {
			pool.freeConnection(con,pstmt,rs);
		}
		
		return successCount;
	}
	
	public int saveRoleDtl(RoleDtl roleDtl) {
		int successCount = 0;
		
		Connection con = null;
		PreparedStatement pstmt = null;
		
		String sql = null;
		try {
			con = pool.getConnection();
			sql = "insert into role_dtl values"
					+ "(0,?,?)";
			
			pstmt = con.prepareStatement(sql);
			pstmt.setInt(1, roleDtl.getRoleId());
			pstmt.setInt(2, roleDtl.getUserId());
			
			successCount = pstmt.executeUpdate();
			
//			ResultSet rs = null; key값을 쓸일이 없으면 필요없음
//			rs = pstmt.getGeneratedKeys();
//			 Statement.RETURN_GENERATED_KEYS
//			if(rs.next()) {
//				roleDtl.setRoleDtlId(rs.getInt(1));
//			}
		} catch (Exception e) {
			
			e.printStackTrace();
		} finally {
			pool.freeConnection(con,pstmt);
		}
		
		return successCount;
	}
```
