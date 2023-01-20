# MySQL
 : ->컬러명, 테이블명, 데이터베이스명을 벡커터안에 넣어줘야한다.  
하지만 해당 DB안에 use 상태일시 생략이 가능하다.  

쿼리는 명령어를 항상 줄여야함

 

## insert 
```sql
select * from student_mst;

insert into `db_study2_explain.student_mst`
(`student_id`,`student_name`,`mentor_id`)//위치가 같아야함
values(4,'손지호',3);//위치가 같아야함
//만약 NotNull일 경우 반드시 값을 넣어줘야함

insert into 
`db_study2_explain`.`student_mst`
values(4,'손지호');
//이렇게 넣으면 null값이 있어도 하나하나 다 null값으로 넣어줘야한다. 그렇지 않으면 오류가 남

insert into student_mst //insert 명령어가 하나이고 값은 여러개 넣을 때 
values
	 (5,'이강용'),
	 (6,'김준경'),
	 (7,'이현수'),
	 (8,'정의현');
```

## update

```sql
update student_mst //바꿀 테이블 이름
set
	mentor_id = 15 // update 할 컬럼명과 데이터
where //이게 없으면 해당 테이블에 컬럼명에 전부 update 된다. where에 조건을 달아 줘야함
	student_id = 5;//조건은 key값으로 하는게 좋다. 신뢰성이 높다.
  
  /////////////////////////////
  update student_mst
set
	student_name = '김재영',//여러개를 바꾸고 싶다면 ,(쉼표)로 구분한다.
	mentor_id = 15
where
	student_id = 5;
  
  /////////////////////
  /*멘토 아이디가 10인 학생들의 멘토아이디를 1로 바꿔라 */
  update student_mst
set	
	  mentor_id = 1
where mentor_id = 10;//이렇게 update를 하면 에러가 뜬다. 왜냐하면 mysql에서 워크벤치가 row의 값이 한번에 바꾸는걸 위험하다고 생각하기 때문에 그래서 edit에서 수정이 필요하다. 하지만 가급적으로는 key값으로 조건을 주는게 좋다.
  
```

## delete

```sql
delete // 삭제할 테이블 이름
from 
	student_mst 
where //조건,and,or,in 키워드가 있음
	student_id = 4
and student_name = '손지호';
```
## select

```sql
/*==================<< selete >>==================*/

select * from student_mst;

/*전체 컬럼 조회(test code를 할 때 사용)*/
select
	*
from
	student_mst;
    
/*지정 컬럼 조회(유지보수를 위해 전체컬럼을 조회하더라도 다 적어주는게 좋다)*/
select
	student_id,
    student_name
from
	student_mst;
    
    
/*  컬럼명을 임시로 바꾸는 방법(java랑 sql이랑 표기법이 다르기 때문에 중요)
	as(alias)알리아스
	as는 생략가능하다 하지만 컬럼명은 생략을 안하고 보통 테이블명에서 생략함
*/
/* 정석    
select
	sm.student_id as studentId
from
	student_mst sm
*/
select
	student_id as studentId
from
	student_mst sm;

/* 조회 조건 where */
select
	*
from
	student_mst
where
	mentor_id = 1;

 /*서브 쿼리(서브쿼리를 쓰면 항상 ()를 해줘야한다.),서브쿼리를 쓸려면 타당한 이유가 필요하다*/
select
	*
from
	student_mst
where
	mentor_id = (select   /*서브 쿼리(서브쿼리를 쓰면 항상 ()를 해줘야한다.),서브쿼리를 쓸려면 타당한 이유가 필요하다*/
					mentor_id//서브쿼리는 대부분 하나의 값을 꺼내서 비교해야한다.
				from 
					mentor_mst
				where
					mentor_name = '문자영');

select 
    student_id,
    student_name,
    mentor_id,
    (select 
	mentor_name
    from 
	mentor_mst
    where
	mentor_id = student_mst.mentor_id) as mentor_name
from
	student_mst;

/* 그룹으로 묶어서 조회(연산을 통한 통계 처리를 할 때 쓴다.) */

select
	count(mentor_id),
    min(student_id),
    max(student_id),
    avg(student_id),
    sum(student_id),
	mentor_id
from
	student_mst
group by
	mentor_id;

/* 중복 제거 */
select distinct
	mentor_id
from
	student_mst;

/* 그룹으로 묶어서 조회한 결과에 조건주는 방법 */

select
	count(mentor_id) as mentor_count,
    min(student_id),
    max(student_id),
    avg(student_id),
    sum(student_id),
	mentor_id
from
	student_mst
group by
	mentor_id
having
	mentor_count = 5;
    
/* 정렬(default값은 오름차순 정렬) */
select
	*
from
	student_mst
order by
	mentor_id ,
    student_id desc;/*내리차순 정렬*/
```

## 공공데이터 연습

``` sql
likeㅣ
   %나를% 이 있는 모든것
    %나를 로 시작하는것
    나를%로 끝나는 것
```
