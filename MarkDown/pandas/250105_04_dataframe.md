# 데이터프레임(DataFrame)

2차원 데이터를 효과적으료 표현한 판다스 자료구조  
2차원 표에서 컬럼 또는 인덱스 단위로 데이터를 표현   
컬럼명:key, 데이터:values



## 컬럼 단위로 데이터 표현

``` python 
import pandas as pd

data = {
    "종가": [156000, 51300, 68800, 140000],
    "PER": [39.88, 8.52, 10.03, 228.38],
    "PBR": [3.52, 1.14, 0.88, 2.15]
}

index = ['naver', '삼성전자', 'LG전자', '카카오']

df = pd.DataFrame(data, index)

print(df)
```

```
           종가     PER   PBR
naver  156000   39.88  3.52
삼성전자    51300    8.52  1.14
LG전자    68800   10.03  0.88
카카오    140000  228.38  2.15
```

## 행 단위로 표현 


``` python
import pandas as pd


data = [
    [156000, 39.88, 3.52],
    [51300, 8.52, 1.14],
    [68800, 10.03, 0.88],
    [140000, 228.38, 2.15],
]

index = ['naver', '삼성전자', 'LG전자', '카카오']
columns = ['종가', 'PER', 'PBR']

df = pd.DataFrame(data=data, index=index, columns=columns)

print(df)

```

```
           종가     PER   PBR
naver  156000   39.88  3.52
삼성전자    51300    8.52  1.14
LG전자    68800   10.03  0.88
카카오    140000  228.38  2.15
```

## 행 단위 데이터를 딕셔너리로 표현 


``` python 
import pandas as pd


data = [
    {"종가":156000, "PER":39.88, "PBR":3.52},
    {"종가":51300, "PER":8.52, "PBR":1.14},
    {"종가":68800, "PER":10.03, "PBR":0.88},
    {"종가":140000, "PER":228.38, "PBR":2.15}
]

index = ['naver', '삼성전자', 'LG전자', '카카오']

df = pd.DataFrame(data=data, index=index)

print(df)
```

```
           종가     PER   PBR
naver  156000   39.88  3.52
삼성전자    51300    8.52  1.14
LG전자    68800   10.03  0.88
카카오    140000  228.38  2.15
```



## DataFrame 인덱싱


### 컬럼 선택


``` python 

import pandas as pd

data = [
    [156000, 39.88, 3.52],
    [51300, 8.52, 1.14],
    [68800, 10.03, 0.88],
    [140000, 228.38, 2.15],
]

index = ['naver', '삼성전자', 'LG전자', '카카오']
columns = ['종가', 'PER', 'PBR']

df = pd.DataFrame(data=data, index=index, columns=columns)

print(df['종가'])
```

```
naver    156000
삼성전자      51300
LG전자      68800
카카오      140000
Name: 종가, dtype: int64
```


## 멀티 컬럼 선택 

``` python 
print(df[['종가','PBR']])
```

```
           종가   PBR
naver  156000  3.52
삼성전자    51300  1.14
LG전자    68800  0.88
카카오    140000  2.15
```




## 로우 단위 선택

loc 인덱스, ### iloc 행번호로 선택 



### loc

``` python 
print(df.loc['삼성전자'])
```

```
종가     51300.00
PER        8.52
PBR        1.14
Name: 삼성전자, dtype: float64
```

### iloc

``` python 
print(df.iloc[1])
```

```
종가     51300.00
PER        8.52
PBR        1.14
Name: 삼성전자, dtype: float64
```





## 멀티 로우 선택 


### loc 

``` python 
print(df.loc[['삼성전자', '카카오']])
```
```
          종가     PER   PBR
삼성전자   51300    8.52  1.14
카카오   140000  228.38  2.15
```


### iloc

``` python
print(df.iloc[[1, 3]])
```

```
          종가     PER   PBR
삼성전자   51300    8.52  1.14
카카오   140000  228.38  2.15
```






## 로우 슬라이싱 

### loc

``` python 
print(df.loc['삼성전자':'카카오'])
```

```

          종가     PER   PBR
삼성전자   51300    8.52  1.14
LG전자   68800   10.03  0.88
카카오   140000  228.38  2.15
```


### iloc

``` python 
print(df.iloc[1:])
```

```
          종가     PER   PBR
삼성전자   51300    8.52  1.14
LG전자   68800   10.03  0.88
카카오   140000  228.38  2.15
```







``` python 
```

```
```



