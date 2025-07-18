# 멀티 플레이 진입점

def main():
    import json
    import os
    print("멀티 플레이 모드 시작")
    # 카테고리 데이터 로딩
    data_path = os.path.join(os.path.dirname(__file__), '../data/category_example.json')
    with open(data_path, encoding='utf-8') as f:
        categories = json.load(f)

    print("[카테고리 목록]")
    for idx, cat in enumerate(categories.keys()):
        print(f"{idx+1}. {cat}")

    sel = input("카테고리 번호를 선택하세요: ")
    try:
        sel_idx = int(sel) - 1
        cat_name = list(categories.keys())[sel_idx]
    except:
        print("잘못된 입력입니다.")
        return

    print(f"선택된 카테고리: {cat_name}")
    print("[곡 리스트]")
    for song in categories[cat_name]:
        print(f"- {song['title']} / {song['artist']}")
    # TODO: 서버/클라이언트 및 카테고리 동기화 구현

if __name__ == "__main__":
    main()
