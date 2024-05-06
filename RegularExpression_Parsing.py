import re

def parse_filename(filename):
    # 파일명에서 필요한 정보를 파싱하기 위한 정규식 정의
    pattern = r"(\w+)-(\w+-\d+-\d+)_([^_]+)-BASE.*_(\d{14})_.*\.dat"
    
    # 정규식을 사용하여 파일명 매칭
    match = re.match(pattern, filename)
    if match:
        vehicle_type, management_number, management_number2, date = match.groups()
        
        # 관리번호2 부분에 'VM'이 포함되어 있는지 확인
        if 'VM' in management_number2:
            # 날짜 포맷 변경 (YYYYMMDDHHMMSS -> YYYY-MM-DD HH:MM:SS)
            formatted_date = f"{date[:4]}-{date[4:6]}-{date[6:8]} {date[8:10]}:{date[10:12]}:{date[12:]}"
            return vehicle_type, management_number, formatted_date
        else:
            return "관리번호2에 'VM'이 포함되어 있지 않습니다."
    else:
        return "파일명 형식이 잘못되었습니다."

# 파일명 예제
filename = "ME-N23-12-563_VM-21C-0209-BASE_27_3_-1_CCP_20240226193112_227414.dat"

# 함수 실행 및 결과 출력
result = parse_filename(filename)
print(result)