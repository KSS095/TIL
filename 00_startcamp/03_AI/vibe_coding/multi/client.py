# 멀티 플레이 클라이언트 예시 (서버와 실시간 동기화)
import requests
import threading
import time

SERVER_URL = "http://localhost:5000"

class GameClient:
    def set_profile(self, nickname):
        avatar_path = input(f"{nickname}님의 아바타 이미지 경로를 입력하세요(예: ./avatar.png): ")
        self.profile = {'nickname': nickname, 'avatar': avatar_path}
        print(f"프로필 설정 완료! 닉네임: {nickname}, 아바타: {avatar_path}")
    def set_problem_master(self):
        master = input("문제 출제자 닉네임을 입력하세요(관리자만 가능): ")
        print(f"문제 출제자가 {master}로 지정되었습니다.")
        self.problem_master = master

    def add_favorite(self, song):
        if not hasattr(self, 'favorites'):
            self.favorites = []
        self.favorites.append(song)
        print(f"즐겨찾기에 추가: {song['title']} / {song['artist']}")

    def show_favorites(self):
        if hasattr(self, 'favorites') and self.favorites:
            print("[즐겨찾기 곡 목록]")
            for s in self.favorites:
                print(f"- {s['title']} / {s['artist']}")
        else:
            print("즐겨찾기 곡이 없습니다.")

    def award_badge(self, score):
        if score == len(self.songs):
            print("[업적] 만점! '음악 천재' 뱃지 획득!")
        elif score >= len(self.songs) // 2:
            print("[업적] 절반 이상 성공! '음악 애호가' 뱃지 획득!")
        else:
            print("[업적] 도전 완료! '참가상' 뱃지 획득!")

    def preview_audio(self, audio_path, seconds=5):
        import pygame
        print(f"음원 미리듣기 {seconds}초...")
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            time.sleep(seconds)
            pygame.mixer.music.stop()
        except Exception as e:
            print(f"미리듣기 오류: {e}")

    def select_audio_section(self, audio_path):
        import pygame
        start = int(input("재생 시작 초(예: 10): "))
        end = int(input("재생 종료 초(예: 20): "))
        print(f"{start}초~{end}초 구간 재생...")
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play(start)
            time.sleep(end - start)
            pygame.mixer.music.stop()
        except Exception as e:
            print(f"구간 재생 오류: {e}")
    def upload_audio(self, file_path, dest_name):
        # 실제 파일 업로드는 서버에 파일 저장 API 필요
        import shutil
        try:
            shutil.copy(file_path, f"../data/{dest_name}")
            print("음원 파일이 업로드되었습니다.")
        except Exception as e:
            print(f"업로드 실패: {e}")

    def delete_song(self):
        category = input("삭제할 곡의 카테고리: ")
        title = input("삭제할 곡명: ")
        res = requests.post(f"{SERVER_URL}/delete_song", json={"category": category, "title": title})
        if res.status_code == 200:
            print("곡 삭제 완료.")
        else:
            print("곡 삭제 실패.")

    def edit_song(self):
        category = input("수정할 곡의 카테고리: ")
        title = input("수정할 곡명: ")
        new_title = input("새 곡명(변경 없으면 Enter): ")
        new_artist = input("새 아티스트(변경 없으면 Enter): ")
        new_file = input("새 음원 파일명(변경 없으면 Enter): ")
        res = requests.post(f"{SERVER_URL}/edit_song", json={
            "category": category,
            "title": title,
            "new_title": new_title,
            "new_artist": new_artist,
            "new_file": new_file
        })
        if res.status_code == 200:
            print("곡 수정 완료.")
        else:
            print("곡 수정 실패.")

    def show_stats(self, nickname):
        res = requests.get(f"{SERVER_URL}/stats", params={"nickname": nickname})
        if res.status_code == 200:
            stats = res.json()
            print(f"[플레이어 통계] 정답률: {stats.get('accuracy', 0)}%, 플레이 횟수: {stats.get('plays', 0)}")
        else:
            print("통계 조회 실패.")

    def chat(self, nickname):
        msg = input("채팅 메시지 입력: ")
        res = requests.post(f"{SERVER_URL}/chat", json={"nickname": nickname, "msg": msg})
        if res.status_code == 200:
            print("메시지 전송 완료.")
        else:
            print("메시지 전송 실패.")

    def admin_mode(self):
        print("[관리자 모드]")
        print("1. 곡 삭제  2. 곡 수정  3. 카테고리 삭제")
        sel = input("번호 선택: ")
        if sel == '1':
            self.delete_song()
        elif sel == '2':
            self.edit_song()
        elif sel == '3':
            category = input("삭제할 카테고리명: ")
            res = requests.post(f"{SERVER_URL}/delete_category", json={"category": category})
            if res.status_code == 200:
                print("카테고리 삭제 완료.")
            else:
                print("카테고리 삭제 실패.")

    def show_highlight(self, ranking):
        if ranking:
            print(f"[최고 점수: {ranking[0]['nickname']} - {ranking[0]['score']}점]")

    def get_hint(self, song):
        print(f"힌트: 아티스트는 {song['artist']}입니다.")

    def timer_mode(self, seconds):
        import time
        print(f"제한 시간: {seconds}초")
        time.sleep(seconds)
        print("시간 종료!")
    def add_song(self):
        print("[곡 추가]")
        category = input("카테고리명: ")
        title = input("곡명: ")
        artist = input("아티스트: ")
        file = input("음원 파일명(mp3 등): ")
        res = requests.post(f"{SERVER_URL}/add_song", json={
            "category": category,
            "title": title,
            "artist": artist,
            "file": file
        })
        if res.status_code == 200:
            print("곡이 성공적으로 추가되었습니다.")
        else:
            print("곡 추가 실패.")
    def __init__(self):
        self.category = None
    def run(self):
        admin = input("관리자 모드로 시작하시겠습니까? (y/n): ")
        if admin.lower() == 'y':
            self.admin_mode()
            return
        add_song_mode = input("곡을 직접 추가하시겠습니까? (y/n): ")
        if add_song_mode.lower() == 'y':
            file_path = input("음원 파일 경로: ")
            dest_name = input("서버에 저장할 파일명: ")
            self.upload_audio(file_path, dest_name)
            self.add_song()
            return
        import pygame
        nickname = input("닉네임을 입력하세요: ")
        self.set_profile(nickname)
        categories = self.fetch_categories()
        print("[카테고리 목록]")
        for idx, cat in enumerate(categories):
            print(f"{idx+1}. {cat}")
        sel = input("카테고리 번호를 선택하세요: ")
        try:
            sel_idx = int(sel) - 1
            self.category = categories[sel_idx]
        except:
            print("잘못된 입력입니다.")
            return
        self.songs = self.fetch_songs(self.category)
        # 세션 등록
        requests.post(f"{SERVER_URL}/session", json={"nickname": nickname, "category": self.category})
        score = 0
        print(f"\n{nickname}님, 게임을 시작합니다! (아바타: {self.profile['avatar']})")
        # 문제 출제자 지정(관리자만)
        if input("문제 출제자를 지정하시겠습니까? (y/n): ").lower() == 'y':
            self.set_problem_master()
        for idx in range(len(self.songs)):
            # 랜덤 문제 출제
            res = requests.get(f"{SERVER_URL}/songs", params={"category": self.category, "random": "1"})
            song_list = res.json()
            if not song_list:
                print("문제가 없습니다.")
                break
            song = song_list[0]
            # 즐겨찾기/추천
            if input("이 곡을 즐겨찾기에 추가하시겠습니까? (y/n): ").lower() == 'y':
                self.add_favorite(song)
            if input("즐겨찾기 곡 목록을 보시겠습니까? (y/n): ").lower() == 'y':
                self.show_favorites()
            # 서버에 현재 문제 번호 동기화
            requests.post(f"{SERVER_URL}/current_problem", json={"category": self.category, "problem_idx": idx})
            print(f"\n[{idx+1}번 문제] {song['artist']}의 곡 전주를 듣고 곡명을 맞춰보세요!")
            # 힌트/타이머/난이도
            hint_mode = input("힌트가 필요합니까? (y/n): ")
            if hint_mode.lower() == 'y':
                self.get_hint(song)
            timer_mode = input("타이머 모드로 진행합니까? (y/n): ")
            if timer_mode.lower() == 'y':
                self.timer_mode(10)
            # 음원 미리듣기/구간 선택
            audio_path = f"../data/{song['file']}"
            if input("음원 미리듣기(5초) 하시겠습니까? (y/n): ").lower() == 'y':
                self.preview_audio(audio_path)
            if input("특정 구간만 재생하시겠습니까? (y/n): ").lower() == 'y':
                self.select_audio_section(audio_path)
            # 음원 전체 재생
            try:
                import pygame
                pygame.mixer.init()
                pygame.mixer.music.load(audio_path)
                pygame.mixer.music.play()
                input("엔터를 누르면 정답 입력 화면으로 이동합니다...")
                pygame.mixer.music.stop()
            except Exception as e:
                print(f"음원 파일 재생 오류: {e}")
            answer = input("곡명을 입력하세요: ")
            if answer.strip() == song['title']:
                print("정답!")
                score += 1
            else:
                print(f"오답! 정답: {song['title']}")
            chat_mode = input("채팅 메시지를 보내시겠습니까? (y/n): ")
            if chat_mode.lower() == 'y':
                self.chat(nickname)
        print(f"\n게임 종료! {nickname}님의 점수: {score} / {len(self.songs)}")
        self.award_badge(score)
        # 점수 서버 전송
        try:
            res = requests.post(f"{SERVER_URL}/score", json={"nickname": nickname, "score": score, "category": self.category})
            if res.status_code == 200:
                print("점수가 서버에 저장되었습니다.")
            else:
                print("점수 저장 실패.")
        except Exception as e:
            print(f"점수 서버 전송 오류: {e}")
        # 랭킹 조회
        try:
            res = requests.get(f"{SERVER_URL}/ranking", params={"category": self.category})
            if res.status_code == 200:
                ranking = res.json()
                print(f"\n[{self.category} 랭킹]")
                for idx, item in enumerate(ranking):
                    print(f"{idx+1}. {item['nickname']} - {item['score']}점")
                self.show_highlight(ranking)
            else:
                print("랭킹 조회 실패.")
        except Exception as e:
            print(f"랭킹 서버 통신 오류: {e}")
        self.show_stats(nickname)

    def fetch_categories(self):
        res = requests.get(f"{SERVER_URL}/categories")
        return res.json()

    def fetch_songs(self, category):
        res = requests.get(f"{SERVER_URL}/songs", params={"category": category})
        return res.json()
    def run(self):
        admin = input("관리자 모드로 시작하시겠습니까? (y/n): ")
        if admin.lower() == 'y':
            self.admin_mode()
            return
        add_song_mode = input("곡을 직접 추가하시겠습니까? (y/n): ")
        if add_song_mode.lower() == 'y':
            file_path = input("음원 파일 경로: ")
            dest_name = input("서버에 저장할 파일명: ")
            self.upload_audio(file_path, dest_name)
            self.add_song()
            return
        import pygame
        nickname = input("닉네임을 입력하세요: ")
        categories = self.fetch_categories()
        print("[카테고리 목록]")
        for idx, cat in enumerate(categories):
            print(f"{idx+1}. {cat}")
        sel = input("카테고리 번호를 선택하세요: ")
        try:
            sel_idx = int(sel) - 1
            self.category = categories[sel_idx]
        except:
            print("잘못된 입력입니다.")
            return
        self.songs = self.fetch_songs(self.category)
        # 세션 등록
        requests.post(f"{SERVER_URL}/session", json={"nickname": nickname, "category": self.category})
        score = 0
        print(f"\n{nickname}님, 게임을 시작합니다!")
        for idx in range(len(self.songs)):
            # 랜덤 문제 출제
            res = requests.get(f"{SERVER_URL}/songs", params={"category": self.category, "random": "1"})
            song_list = res.json()
            if not song_list:
                print("문제가 없습니다.")
                break
            song = song_list[0]
            # 서버에 현재 문제 번호 동기화
            requests.post(f"{SERVER_URL}/current_problem", json={"category": self.category, "problem_idx": idx})
            print(f"\n[{idx+1}번 문제] {song['artist']}의 곡 전주를 듣고 곡명을 맞춰보세요!")
            # 힌트/타이머/난이도
            hint_mode = input("힌트가 필요합니까? (y/n): ")
            if hint_mode.lower() == 'y':
                self.get_hint(song)
            timer_mode = input("타이머 모드로 진행합니까? (y/n): ")
            if timer_mode.lower() == 'y':
                self.timer_mode(10)
            # 음원 재생
            audio_path = f"../data/{song['file']}"
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(audio_path)
                pygame.mixer.music.play()
                input("엔터를 누르면 정답 입력 화면으로 이동합니다...")
                pygame.mixer.music.stop()
            except Exception as e:
                print(f"음원 파일 재생 오류: {e}")
            answer = input("곡명을 입력하세요: ")
            if answer.strip() == song['title']:
                print("정답!")
                score += 1
            else:
                print(f"오답! 정답: {song['title']}")
            chat_mode = input("채팅 메시지를 보내시겠습니까? (y/n): ")
            if chat_mode.lower() == 'y':
                self.chat(nickname)
        print(f"\n게임 종료! {nickname}님의 점수: {score} / {len(self.songs)}")
        # 점수 서버 전송
        try:
            res = requests.post(f"{SERVER_URL}/score", json={"nickname": nickname, "score": score, "category": self.category})
            if res.status_code == 200:
                print("점수가 서버에 저장되었습니다.")
            else:
                print("점수 저장 실패.")
        except Exception as e:
            print(f"점수 서버 전송 오류: {e}")
        # 랭킹 조회
        try:
            res = requests.get(f"{SERVER_URL}/ranking", params={"category": self.category})
            if res.status_code == 200:
                ranking = res.json()
                print(f"\n[{self.category} 랭킹]")
                for idx, item in enumerate(ranking):
                    print(f"{idx+1}. {item['nickname']} - {item['score']}점")
                self.show_highlight(ranking)
            else:
                print("랭킹 조회 실패.")
        except Exception as e:
            print(f"랭킹 서버 통신 오류: {e}")
        self.show_stats(nickname)
