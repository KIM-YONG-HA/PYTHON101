# DataFrame

Series가 여러 개 있는 2차원의 데이터구조를 가지며 행과 열로 구성되어있다.

<br><br>

## DataFrame 파라미터 

``` python 
pandas.DataFrame(data, index, columns, copy)
```

### data
DataFrame을 채울 원본 데이터이며 리스트, 딕셔너리, 배열, numpy배열, 다른 데이터프레임 


### index
데이터프레임의 행 레이블을 지정하며 기본 값은 RangeIndex(0, 1, 2, ...)

### columns
데이터프레임의 열 레이블을 지정하며 기본 값은 데이터에 따라 자동 생성되며 명시적으로 지정할 수 있다.


### dtype
데이터프레임의 타입을 지정하며 명시하지 않으면 pandas가 자동으로 추론하여 지정


### copy
데이터 원본을 복사할지 여부 

## DataFrame 속성

### index

### columns

### values 


### T | transpose()


### shape 

데이터 프레임의 행과 열을 튜플로 반환

### ndim 

### dtypes

### size




### info()

### head()

### tail()



### isnull() | isna()

### notnull() | notna()

### describe()

### memory_usage()


<br><br>

## DataFrame 생성 

### 리스트로 생성 

``` python 
import numpy as np
import pandas as pd

list_data = [
    [1, 2, 3], 
    ['A', 'B', 'C'],
    [True, True, False],
]


df = pd.DataFrame(data=list_data)
```
```
      0     1      2
0     1     2      3
1     A     B      C
2  True  True  False
```

### 딕셔너리로 생성

딕셔너리로 생성시 키가 컬럼이 된다 

``` python 
data = {'A': [1,2], 'B': [3,4]}
df = pd.DataFrame(data=data)
print(df)
```
```
   A  B
0  1  3
1  2  4
```









## index, columns 지정

### 데이터프레임 생성 시 지정 
``` python 
member_data = [
    ['홍길동', 40, '남', '서울'],
    ['정길동', 30, '여', '부산'],
    ['박길동', 29, '남', '광주'],
    ['최길동', 55, '여', '제주'],
]

df = pd.DataFrame(data=member_data, index=['A','B','C','D'], columns=['name', 'age', 'gender','addr'])
print(df)
print(df.index)
print(df.columns)
```
```
  name  age gender addr
A  홍길동   40      남   서울
B  정길동   30      여   부산
C  박길동   29      남   광주
D  최길동   55      여   제주
Index(['A', 'B', 'C', 'D'], dtype='object')
Index(['name', 'age', 'gender', 'addr'], dtype='object')
```

### 데이터프레임 생성 후 지정 또는 수정 

``` python 
df.index = ['가', '나', '다', '라']
df.columns = ['이름', '나이', '성별', '거주지']
print(df)
print(df.index)
print(df.columns)
```

```
    이름  나이 성별 거주지
가  홍길동  40  남  서울
나  정길동  30  여  부산
다  박길동  29  남  광주
라  최길동  55  여  제주
Index(['가', '나', '다', '라'], dtype='object')
Index(['이름', '나이', '성별', '거주지'], dtype='object')
```






## 인덱싱과 슬라이싱 



## 컬럼 조회

### 열 1개 조회
``` python
print(df['이름'])
```
```
가    홍길동
나    정길동
다    박길동
라    최길동
Name: 이름, dtype: object
```

### 열 여러개 조회 

``` python
print(df[['이름', '거주지']])
```
```
    이름 거주지
가  홍길동  서울
나  정길동  부산
다  박길동  광주
라  최길동  제주
```

## 컬럼 이름 변경 

### 특정 컬럼만 변경하기 
``` python 
df.rename(columns={'이름':'성명', '거주지':'거주지역'}, inplace=True)
print(df)
```
```
    성명  나이 성별 거주지역
가  홍길동  40  남   서울
나  정길동  30  여   부산
다  박길동  29  남   광주
라  최길동  55  여   제주
```

### 열 이름을 가져온 후 수정하기 

``` python 
columns = df.columns.tolist()
columns[0] = '성명'
columns[3] = '거주지역'
df.columns = columns
print(df)
```
※ df.columns에 리스트로 전체를 다시 재지정도 가능





## 데이터 삭제 
drop() 메소드를 사용하여 삭제한다. 
원본 데이터는 수정되지 않으므로 변수에 재저장 또는 inplace=True 옵션을 사용한다.

axis=0은 행, axis=1은 열을 의미하며 행을 삭제 시 1

### 1개 열 삭제 
``` python 
df.drop('거주지역', axis=1)
```

### 여러개 열 삭제 
``` python 
df.drop(['나이', '거주지역'], axis=1)
```



### 인덱스 '가' 삭제

``` python 
df.drop('가', axis=0)
```


## 데이터 추가 


### row 추가


### column 추가 



## 불리언 인덱싱(Boolean Indexing)




## 컬럼 위치 변경 

### 열 순서 재지정 
``` python 
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})
```
### 열을 직접 지정 

``` python 
df = df[['C', 'A', 'B']]
print(df)
```

### 특정 열을 맨 앞으로 
``` python 
col_to_move = df.pop('B')  # 'B' 열을 제거하면서 반환
df.insert(0, 'B', col_to_move)  # 'B'를 첫 번째 위치에 삽입
print(df)
```

``` python 
cols = ['C'] + [col for col in df.columns if col != 'C']
# 앞으로 이동시킬 C 와 C 제외 나머지를 리스트화
df = df[cols]
print(df)
```

### 특정 열을 맨 뒤로 

``` python
col_to_move = df.pop('B')  # 'B' 열 제거 및 반환
df['B'] = col_to_move      # 'B' 열을 맨 뒤에 추가
```

### 열 위치 교환

``` python 
columns = list(df.columns)
columns[0], columns[2] = columns[2], columns[0]  # 'A'와 'C' 교환
df = df[columns]
print(df)
```




df_copy = df #  참조복사 
df_copy = df[:] #  얕은 복사
df_copy = df.copy() #  깊은 복사


## loc, iloc




