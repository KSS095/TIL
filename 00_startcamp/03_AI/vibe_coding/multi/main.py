# 멀티 플레이 진입점

def main():
    import requests
    print("멀티 플레이 모드 시작 (서버와 통신)")
    SERVER_URL = "http://localhost:5000"

    # 카테고리 목록 받아오기
    res = requests.get(f"{SERVER_URL}/categories")
    categories = res.json()
    print("[카테고리 목록]")
    for idx, cat in enumerate(categories):
        print(f"{idx+1}. {cat}")

    sel = input("카테고리 번호를 선택하세요: ")
    try:
        sel_idx = int(sel) - 1
        cat_name = categories[sel_idx]
    except:
        print("잘못된 입력입니다.")
        return

    print(f"선택된 카테고리: {cat_name}")
    # 곡 리스트 받아오기
    res = requests.get(f"{SERVER_URL}/songs", params={"category": cat_name})
    songs = res.json()
    print("[곡 리스트]")
    for song in songs:
        print(f"- {song['title']} / {song['artist']}")
    # TODO: 서버/클라이언트 및 카테고리 동기화 구현

if __name__ == "__main__":
    main()
