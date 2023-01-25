# 서브쿼리와 조인

```sql
/*===================<<서브쿼리>>=================*
select
	*
from
	library_mst;

select//
	순번,
    도서관명,
    구분,
    도서명,
    저작자,
    (select author_name from author_mst where author_id = 저작자) as 저작자명,
    출판사,
    (select publisher_name from publisher_mst where publisher_id = 출판사) as 출판사명, //->조건이 두개면 오류가 난다.
    발행연도,
    청구기호
from
	library_mst;
	
```
