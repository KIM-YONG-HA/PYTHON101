# 데이터프레임(DataFrame) 추가 삭제 



## 컬럼 추가 


df['컬럼명']


``` python 

import pandas as pd

# 예제 데이터프레임 생성
data = {
    "Name": ["유재석", "박명수", "정형돈"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)

```

```
  Name  Age
0  유재석   25
1  박명수   30
2  정형돈   35
```



``` python 
df['addr'] = "NULL"
print(df)
```
```
  Name  Age  addr
0  유재석   25  NULL
1  박명수   30  NULL
2  정형돈   35  NULL
```



## 컬럼 삭제 
원본에 적용되지 않으므로 변수에 재저장 또는 inplace=True 사용 

axis(축) 1은 열을 뜻한다 

``` python
print(df.drop('addr', axis=1))
```

```

  Name  Age
0  유재석   25
1  박명수   30
2  정형돈   35
```





## 시계열 데이터와 인덱스 

``` python 
date = ["2025-01-01"]
index = pd.to_datetime(date)

print(type(date))
print(type(index))
```
```
<class 'list'>
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
```


``` python 
date = "2025-01-01"
index = pd.to_datetime(date)

print(type(date))
print(type(index))
```
```
<class 'str'>
<class 'pandas._libs.tslibs.timestamps.Timestamp'>
```



## 로우 추가 

``` python 
date = "2025-01-05 09:00:00"
dt = pd.to_datetime(date)

df.loc[dt] = [1,2,3,4]
df

```


## 로우 삭제 

df.drop(로우 인덱스, axis=0, inplace=True)

``` python 
df.drop(df.index[-1], axis=0, inplace=True)
```
