# Windows HTTP Time Synchronizer
> **Solution for NTP (UDP 123) Port Blocking and Time Sync Infinite Loading**
> **NTP(UDP 123) 포트 차단 및 윈도우 시간 동기화 무한 로딩 해결 도구**

This project solves the issue where Windows time synchronization fails due to ISP firewalls (e.g., LGU+ in Korea) or corporate network restrictions that block the standard NTP port (UDP 123).
이 프로젝트는 LG 유플러스 등 특정 ISP의 회선 방화벽이나 사내 보안망에서 표준 NTP 포트(UDP 123)를 차단하여 발생하는 윈도우 시간 동기화 실패 문제를 해결합니다.

---

## Symptoms (문제 증상)

If your PC clock is inaccurate and you see these issues, your network might be blocking NTP:
PC 시간이 맞지 않고 아래 현상이 있다면 회선 차단을 의심해야 합니다:

1. **Infinite Loading**: The "Sync now" button in Windows settings keeps spinning forever.
   (윈도우 설정의 [지금 동기화] 버튼이 무한 로딩됨.)
2. **Sync Error**: "Windows could not synchronize with the time server... no time data available."
   (제어판 동기화 시도 시 "사용 가능한 시간 데이터가 없어 동기화하지 못했습니다" 메시지 출력.)
3. **Chain Reaction**: Crypto exchange API (Binance, BitMEX) errors, SSL certificate issues.
   (거래소 API 연결 실패, 웹사이트 SSL 인증서 에러 발생.)

## The Solution (해결 방식)

This tool bypasses the blocked UDP 123 port and uses **HTTPS (TCP 443)**. It extracts standard time from Google server's response headers to force-sync your system clock.
본 도구는 차단된 UDP 123 포트 대신 **HTTPS (TCP 443 포트)**를 이용합니다. Google 서버 응답 헤더에서 표준 시간을 추출하여 시스템 시계를 강제 동기화합니다.

---

## Key Features (주요 기능)

* **NTP Bypass**: Uses HTTP/HTTPS to bypass ISP and corporate firewalls. (포트 차단 무력화)
* **Standalone**: Works as a single `.exe` file without needing Python. (독립 실행 지원)
* **Auto-Admin**: Automatically requests UAC (Administrator) privileges. (관리자 권한 자동 요청)
* **Process Persistence**: The window stays open until you press Enter. (결과 확인용 창 유지)

---

## How to Use (사용 방법)

### 1. Executable (.exe) - Recommended (일반 사용자)
1. Download `sync_time.exe` from this repository. (`sync_time.exe` 다운로드)
2. Double-click to run. (더블 클릭하여 실행)
3. Select **[Yes]** for Administrator privileges. (관리자 권한 [예] 선택)
4. Confirm "Success" and press Enter to exit. (성공 메시지 확인 후 엔터)

### 2. Python (.py) - For Developers (개발자용)
1. Install dependency: (필수 라이브러리 설치)
   ```bash
   pip install requests
   ```
2. Run the script: (스크립트 실행)
   ```bash
   python sync_time.py
   ```

---

## License (라이선스)

This project is licensed under the **MIT License**.
이 프로그램은 자유로운 수정 및 배포가 가능한 MIT License를 따릅니다.

**Designed by [ GAUNTER-O-DIMM ]**
