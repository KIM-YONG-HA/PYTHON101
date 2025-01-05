# 데이터프레임(DataFrame) 연산



## 컬럼 시프트 

 동일 컬럼 위 아래를 연산 


 df['컬럼명'].shift(1)

 특정 컬럼의 데이터를 아래로 하나씩 이동 


 df['close_shift1] = df['close'].shift(1)