import os
import sys
import ctypes

try:
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if not is_admin():
        if getattr(sys, 'frozen', False):
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
        else:
            script = os.path.abspath(sys.argv[0])
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}"', None, 1)
        sys.exit()


    import requests 
    from datetime import datetime, timedelta

    print("==================================================")
    print("    시간 동기화 엔진 v1.0")
    print("==================================================")
    
    url = 'https://www.google.com'
    print(f"\n {url} 서버에서 표준 시간 수신 중...")
    
    response = requests.head(url, timeout=5)
    server_date_str = response.headers.get('Date')
    
    if not server_date_str:
        print(" 서버 응답에서 시간 데이터를 찾지 못했습니다.")
    else:
        gmt_time = datetime.strptime(server_date_str, '%a, %d %b %Y %H:%M:%S %Z')
        kst_time = gmt_time + timedelta(hours=9)
        
        print(f" 서버 시간(KST): {kst_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        new_date = kst_time.strftime('%Y-%m-%d')
        new_time = kst_time.strftime('%H:%M:%S')

        print("\n 시스템 시간 동기화 처리 중...")
        os.system(f'date {new_date}')
        os.system(f'time {new_time}')

        print("\n [성공] 시간 동기화 완료!")
        print(f" 변경된 PC 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

except ModuleNotFoundError:
    print("\n [오류] 필요한 파이썬 패키지(requests)가 설치되지 않았습니다!")
    print("   해결법: 명령 프롬프트(CMD)를 열고 아래 명령어를 쳐주세요.")
    print("   pip install requests")
except Exception as e:
    print(f"\n [알 수 없는 오류 발생] {e}")

print("\n==================================================")
input("  종료하려면 [엔터] 키를 누르세요...")
