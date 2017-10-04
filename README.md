# Network 대역 내 취약점 Port Scanning Tool

대역 설정과 수집하고나 하는 포트를 수동 세팅함으로서 네트워크 내 취약점 조사가 가능한 도구

## Getting Started

본 체계는 Python3 기반으로 제작되었습니다.

### Prerequisites

실행하기 전 필요한 소프트웨어 목록 및 설치법

```
python3 (>= 3.3.0)
python-nmap (>= 0.6.0)
nmap (>= 7.12)
PyWin32 (>= 219)
```

###
Network 대역폭 및 스캐닝 포트 설정

코드 내
```
IP = "{IP}";
SUBNET = "/20";
PORT = "21, 22, .... "

변경 필요

```

## Running the tests

### cmd 창에서 수행

```
 > python3 scan_to_csv(Internet).py
```

