# 싱글 플레이 진입점

def main():
    import json
    import os
    print("싱글 플레이 모드 시작")
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
    # 게임 로직: 첫 번째 곡 음원 재생 및 정답 입력
    import pygame
    pygame.mixer.init()
    first_song = categories[cat_name][0]
    audio_path = os.path.join(os.path.dirname(__file__), f"../data/{first_song['file']}")
    print(f"\n[음원 재생] {first_song['title']} / {first_song['artist']}")
    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        input("엔터를 누르면 정답 입력 화면으로 이동합니다...")
        pygame.mixer.music.stop()
    except Exception as e:
        print(f"음원 파일 재생 오류: {e}")
        return

    answer = input("곡명을 입력하세요: ")
    if answer.strip() == first_song['title']:
        print("정답입니다!")
    else:
        print(f"오답입니다. 정답: {first_song['title']}")

if __name__ == "__main__":
    main()
