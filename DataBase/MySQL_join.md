# 서브쿼리와 조인

``` sql
/*===================<<서브쿼리>>=================*/
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

## join

innner join -> a와 b의 공통된(조건에 맞는) 데이터들만 뽑겠다.   

### inner join(교집합)
``` sql
insert into library_mst
values (0,'테스트도서관','999(테스트)','테스트도서명','9999','9999','2023','999.9-테99ㅌ');


-- inner join은 양쪽의 동일한 데이터값만 조회한다.
select
	* 
from
	library_mst lm
    inner join publisher_mst pm on (pm.publisher_id = lm.출판사)
order by
	lm.순번 desc; 
```
outer join -> left와 right 두개가 있다. left는 왼쪽에 기준을 두는거고, right는 오른쪽에 기준을 두는 것이다.  

### left outer join
``` sql
select
	* 
from
	library_mst lm
    left outer join publisher_mst pm on (pm.publisher_id = lm.출판사)

order by
	lm.순번 desc;
```

### left outer join

```sql
select
	* 
from
	library_mst lm
    left outer join publisher_mst pm on (pm.publisher_id = lm.출판사)
where 
	pm.publisher_id is null
order by
	lm.순번 desc;
```
