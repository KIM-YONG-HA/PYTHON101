[OSI - 참고 블로그](https://velog.io/@jeongs/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-OSI-7-%EA%B3%84%EC%B8%B5-%EA%B7%B8%EB%A6%BC%EA%B3%BC-%ED%95%A8%EA%BB%98-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)

# OSI(Open System Interconnection)

## A7-P-S-T-N-D-Phy1
(아파서 탈났다 피식)

## 응7표, 세전네, 데물1


## 1. Physical Layer(물리)
* 단위는 비트 
* 전기적 신호
※ 장비 : 케이블, 리피터, 허브

## 2. Data Link Layer(데이터 링크)
* 단위는 프레임
* 이웃 컴퓨터와의 통신만
* 직접적으로 연결된 두개의 노드사이에 데이터 전송
* 물리층의 오류를 수정하기도 함 
* 프레이밍
* 흐름제어
* 오류제어
* 접근제어
* 동기화
* 안전하게 데이터를 보낸다 
※ 장비 : 브릿지, 스위치

## 3. Network Layer
* 단위는 패킷 
* IP 프로토콜이 대표적 
* 라우팅 : IP정하고, 경로 선택, 패킷 전달
* 라우팅은 네트워크에서 목적지까지 보낼 패킷의 경로를 설정
※ 장비 : 라우터, 공유기, L3 스위치 

## 4. Transport Layer(전송)
* End to End 신뢰성 있는 연결 
* 데이터 단위는 TCP는세그먼트 UDP는 Datagram
* 포트를 사용한다 
* 전송 속도를 조절하거나
* 오류가 발생하면 맞춰줌 
* 데이터 용량, 속도, 목적지 처리 
* TCP, UDP가 있음 

※ TCP프로토콜 : 신뢰성 보장, 연결 유지를 위한 리소스
※ UDP프로토콜 : 도착여부 상관없이 빠른데이터 전송(스트리밍)
※ 장비 : L4 스위치(3계층에서 온 트래픽을 분석해 구분), 게이트웨이, 로드 밸런서 


## 5. Session Layer


세션 계층(Session Layer)은 양 끝단의 **응용 프로세스**가 통신을 관리하기 위한 방법을 제공하며, **통신 세션을 구성하고 유지하며 종료**하는 역할을 합니다.

- **데이터 전송 단위**: 세션 계층의 데이터 전송 단위는 **메시지(Message)**입니다. 세션 계층은 데이터를 논리적인 단위로 나누어 관리하고, 양 끝단의 응용 프로세스 간의 **세션 관리**를 담당합니다.
- **통신 세션 관리**: 세션 계층은 두 응용 프로그램 간의 세션을 설정하고, 세션을 유지하면서 **동기화 및 오류 복구** 기능을 제공합니다.
- **프로토콜**:
  - **NetBIOS**: 네트워크에서 응용 프로그램 간에 세션을 설정하고 유지하는 프로토콜.
  - **SSH (Secure Shell)**: 보안이 강화된 원격 통신 프로토콜로, 세션 계층에서 안전한 연결을 제공.
  - **RPC (Remote Procedure Call)**: 원격 프로시저 호출을 통해 원격 시스템에서 함수나 프로시저를 실행하는 프로토콜.

**참고**: 포트 번호는 **전송 계층**에서 다루는 개념으로, 세션 계층은 세션을 관리하는 역할을 합니다. 세션 계층은 세션 ID와 같은 고유 식별자를 사용하여 통신을 관리합니다.


## 6. Presentation Layer(표현계층)


* ASCII, MPEG, JPEG, MIDI, AFP, PAP

## 7. Appication Layer 

* HTTP, FTP, SMTP, POP3




## 데이터 단위 
```
Application / Data(Message) /FTP, HTTP
Presentation / Data(Message) /JPEG,MPEG
Session / Data(Message) / NetBIOS

Transport / Segment / TCP, UDP

Network / Packet/ IP
Data Link / Frame / MAC, PPP
Physical / Bit /Ethernet, RS232c
```