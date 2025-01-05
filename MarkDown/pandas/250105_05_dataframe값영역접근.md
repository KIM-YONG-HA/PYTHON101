# 데이터프레임(DataFrame) 값, 영역 접근



``` python 
import pandas as pd

data = [
    ['3R', 1510, 7.46],
    ['3SOFT', 1790, 1.65],
    ['ACTS', 1185, 1.28],
]

index = ['037730', '036365', '005760']
columns = ['종목명', '현재가', '등락률']

df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
```

```
          종목명   현재가   등락률
037730     3R  1510  7.46
036365  3SOFT  1790  1.65
005760   ACTS  1185  1.28
```



## df.iloc[행번호, 열번호] 

``` python 
print(df.iloc[0,0])
```

```
3R
```


## df.loc[인덱스, 컬럼명]

``` python 
print(df.loc['037730', '종목명'])
```

```
3R
```




## 영역 가져오기 

데이터프레임에서 특정 영역 접근 


### df.iloc[행번호 리스트, 열번호 리스트]


``` python 
print(df.iloc[[0, 1], [0, 1]])
```
```
          종목명   현재가
037730     3R  1510
036365  3SOFT  1790
```



``` python 
print(df.iloc[0:2, [0, 1]])
```

```
          종목명   현재가
037730     3R  1510
036365  3SOFT  1790
```



### df.loc[인덱스 리스트, 컬럼명 리스트 ]


``` python 
print(df.loc[['037730', '036365'], ['종목명', '현재가']])
```

```
          종목명   현재가
037730     3R  1510
036365  3SOFT  1790
```



``` python 
print(df.loc['037730':'036365', '종목명':'현재가'])
```

```
          종목명   현재가
037730     3R  1510
036365  3SOFT  1790
```



## 연속적이지 않은 영역 선택 

### df.iloc
``` python 
print(df.iloc[[0, 1], [0, 2]])
```
```
          종목명   등락률
037730     3R  7.46
036365  3SOFT  1.65
```

## df.loc


``` python 
print(df.loc[['037730','036365'] , ['종목명','등락률']])
```

```
```













``` python 
```

```
```



