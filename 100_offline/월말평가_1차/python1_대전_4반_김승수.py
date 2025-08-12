def strip_and_lowercase(text):
    """
    문자열의 앞뒤 공백을 제거하고, 소문자로 변환한 문자열을 반환한다.
    """
    # strip method를 통해 문자열 앞뒤 공백 제거
    strip_text = text.strip()

    # lower method를 통해 문자열을 소문자로 변환
    strip_and_lowercase_text = strip_text.lower()
    return strip_and_lowercase_text


def is_valid_log(text):
    """
    로그 항목이 유효한지 검사한다.
    유효하지 않은 경우는 다음 조건 중 하나라도 해당되는 경우이다.
    - 공백 문자열
    - "error" 또는 "none" 이 포함된 문자열
    - 숫자로만 구성된 문자열
    """
    # 받은 문자열이 공백이거나, error와 none을 포함하거나, 숫자로만 구성됐다면 False 반환
    # 그렇지 않다면 True 반환
    if (text == '') or (text.find('error') != -1 or text.find('none') != -1) or (text.isnumeric()):
        return False
    else: return True


def clean_log(text):
    """
    '_'가 포함된 경우 이를 ' '로 바꾸고,
    각 단어의 첫 글자를 대문자로 바꾼다. (Title Case)
    """
    # replace method를 통해 '_' 를 ' '로 변환
    clean_text = text.replace('_', ' ')

    # split method를 통해 공백을 기준으로 단어 나누기
    split_text = clean_text.split(' ')

    # 나눈 단어들의 첫 단어를 대문자로 변환하여 저장할 리스트
    capital_text = []

    # capitalize method를 통해 각 단어의 첫 글자를 대문자로 변환
    for i in range(len(split_text)):
        capitalize_text = split_text[i].capitalize()

        # 변환한 문자열을 리스트에 저장
        capital_text.append(capitalize_text)

    # 리스트에 저장된 문자열들을 공백으로 연결
    clean_capital_text = ' '.join(capital_text)
    return clean_capital_text


def process_logs(log_list):
    """
    전체 로그 리스트를 받아 유효한 항목만 정제하여 리스트로 반환한다.
    위 함수들을 적절히 활용해야 한다.
    """
    # 정제된 문자열들을 저장할 리스트
    result_log = []

    # 전달받은 리스트를 순회하여 모든 문자열에 대해 위에서 정의한 함수들 실행
    for i in range(len(log_list)):
        # 공백 제거, 소문자 변환
        strip_lower_log = strip_and_lowercase(log_list[i])
        
        # 유효성 검사를 통과하면 각 단어의 첫글자를 대문자로 변환
        if is_valid_log(strip_lower_log):
            valid_clean_log = clean_log(strip_lower_log)

            # 최종 정제된 문자열을 리스트에 저장
            result_log.append(valid_clean_log)

    return result_log

# 아래 코드는 수정 할 수 없음
raw_logs = [
    "  user_login  ",
    "ERROR_404",
    "   page_viewed",
    "None",
    "signup_success ",
    "  1234 ",
    "   ",
]

result = process_logs(raw_logs)
print(result)

# ['User Login', 'Page Viewed', 'Signup Success']