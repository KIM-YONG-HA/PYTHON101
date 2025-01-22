# pandas
판다스 라이브러리는 행과 열로 구성된 데이터를 수집 및 정리에 최적화 되어있는 파이썬의 패키지이다. 
<br><br>

## import
```
import pandas as pd
```
※ 별칭은 pd를 많이 사용한다. 
<br><br>

## 자료구조 

대표적으로 Series(시리즈), DataFrame(데이터프레임)이 있다. 

<br><br>

## Series

순차적으로 나열된 1차원 자료구조로 index(행), value(열)로 구성되며 1:1 대응한다.

파이썬 자료구조 중 딕셔너리와 유사하다.
<br><br>






## Series 클래스의 파라미터 
``` python
pd.Series(data, index, dtype, name, copy, fastpath)
```
### data 
```
저장할 데이터를 지정하며 리스트, 딕셔너리, 스칼라 값 등이 가능하다. 
```

### index
```
데이터의 키나 위치를 지정하여 레이블 역할을 한다
```

### dtype
```
데이터 타입을 지정

int : 정수형 데이터
float : 부동소수점(실수)형 데이터 
bool : 논리값
object : 문자열 또는 혼합데이터
category : 범주형 데이터
datetime64[ns]: 날짜 및 시간 데이터
timedelta65[ns]: 시간 간격 데이터 
```

### name
```
시리즈의 이름을 지정하며 데이터 분석시 컬럼 이름으로 사용 가능하다.
```

### copy
```
데이터의 복사 여부를 결정한다

True : 데이터를 복사하여 Series 객체를 독립적으로 생성

False : 데이터를 참조하여 Series 객체 생성하여 원본 데이터와 연동될 수 있음

성능최적화를 위해 사용되며 default는 false
```

※ 데이터가 매우 클 때 복사 대신 참조를하면 메모리 사용량과 실행시간이 줄어들어 효율적이지만 원본이 변경될 수도 있다. 

※ copy=False를 지정해도 복사가 발생할 수 있는데 이는 내부적으로 판다스가 데이터를 안전하게 다루기 위한 수행동작이다.

### fastpath
```
내부적으로 성능 최적화를 위해 사용되며 자동으로 설정되어 지정할 필요가 없다. 
```

<br><br>


## Series 객체 생성

### 딕셔너리로 생성
``` python 
dict_data = {'a':1, 'b':2, 'c':3}
sr = pd.Series(dict_data)
print(type(sr))
print(sr)
```

```
#  결과 
<class 'pandas.core.series.Series'>
a    1
b    2
c    3
dtype: int64 #  value값의 타입 
```
``` python 
print(sr.index)
print(sr.values)
```
```
#  결과
Index(['a', 'b', 'c'], dtype='object')
[1 2 3]
```


### 리스트로 생성

``` python 
list_data = [3.141582,0,True,'2025-01-03','python']
sr2 = pd.Series(list_data)
print(sr2)
```
```
#  결과
0      3.141582
1             0
2          True
3    2025-01-03
4        python
dtype: object
```
``` python
print(sr2.index)
print(sr2.values)

```
```
#  결과 
RangeIndex(start=0, stop=5, step=1)
[3.141582 0 True '2025-01-03' 'python']
```


### 튜플로 생성 

``` python
tup_data = ('가', '나', '다', '라')
sr = pd.Series(tup_data)
print(sr)
```

```
#  결과 
0    가
1    나
2    다
3    라
dtype: object

```
<br><br>








## Series.index

시리즈 생성 시 별도의 인덱스를 지정하지 않았다면 0부터 순차적인 값(RangeIndex)이 부여된다.


### 인덱스 지정 없이 객체 생성
``` python 
list_data = ['가', '나', '다', '라']
sr = pd.Series(list_data)
print(sr)
print(sr.index)
```
```
#  결과 
0    가
1    나
2    다
3    라
dtype: object
RangeIndex(start=0, stop=4, step=1)
```

### 시리즈 생성 후 인덱스 추가 

``` python
sr.index = ['A', 'B', 'C', 'D']
print(sr)
print(sr.index)
```

```
0    가
1    나
2    다
3    라
dtype: object
RangeIndex(start=0, stop=4, step=1)
```

### 시리즈 생성 시 인덱스 추가 

``` python 
sr = pd.Series(data=['가', '나', '다', '라'], index=['A','B','C','D'])
print(sr)
print(sr.index)
```
```
#  결과 
A    가
B    나
C    다
D    라
dtype: object
```


### 인덱스 수정하기 

``` python
sr = pd.Series(data=['가', '나', '다', '라'], index=['A','B','C','D'])
sr.index = ['a', 'b', 'c', 'd']
print(sr.index)
```
```
Index(['a', 'b', 'c', 'd'], dtype='object')
```
※ sr.index = ['a', 'b', 'c', 'd']와 sr.index = list('abcd')의 결과는 같으며 리스트 함수도 알아두면 도움이 된다.





## 인덱싱과 슬라이싱

시리즈 생성 시 별도의 인덱스를 지정하지 않았다면 0부터 순차적인 값(RangeIndex)이 부여된다.

``` python 
sr = pd.Series(['가', '나', '다', '라'])
print(sr.index)
```

### 원소 한 개 선택

``` python
print(sr[0])
```
```
가
```

### 특정 원소 여러 개 선택(fancy indexing)
``` python
print(sr[[1,3]])
```

```
1    나
3    라
dtype: object
```


### 키 지정 후 숫자 인덱스로 선택 

``` python 
sr = pd.Series(['가', '나', '다', '라'], index=['A', 'B', 'C', 'D'])
print(sr[0])
```
```
가
FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
  print(sr[0])
```
※ 인덱스 지정 후 sr[0]은 출력은 되지만 ser.iloc[pos]를 권장한다는 오류가 출력된다.


### 불리언 인덱싱(boolean indexing)
조건식을 만들어 True에 해당하는 값만 필터링한다

``` python 
sr = pd.Series([10, 20, 30, 40], index=list('ABCD'))
print(sr[sr > 20])
```
```
C    30
D    40
dtype: int64
```

``` python
sr = pd.Series(['가', '나', '다', '라'], index=list('ABCD'))
print(sr[sr > '가'])
```
```
B    나
C    다
D    라
dtype: object
```
※ 문자의 경우 아스키 코드값을 비교한다.




### 슬라이싱 
``` python
sr = pd.Series([10, 20, 30, 40])
print(sr[0:3])
```
```
0    10
1    20
2    30
dtype: int64
```

``` python
sr = pd.Series([10, 20, 30, 40], index=list('ABCD'))
print(sr['A':'D'])
```
```
A    10
B    20
C    30
D    40
dtype: int64
```

※ 문자 인덱스의 경우 A, B, C, D(마지막 인덱스 D 포함)
※ 숫자 인덱스의 경우 0, 1, 2(마지막 인덱스 3 미포함)
