import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QComboBox, QListWidget, QLineEdit, QMessageBox, QTextEdit, QInputDialog, QStackedWidget
)
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
import pygame

CATEGORY_FILE = "data/category_example.json"
AUDIO_DIR = "data/"

class StartScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()
        title = QLabel("노래 맞추기 게임")
        title.setFont(QFont("맑은 고딕", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        btn_layout = QHBoxLayout()
        self.single_btn = QPushButton("싱글 플레이")
        self.multi_btn = QPushButton("멀티 플레이")
        self.settings_btn = QPushButton()
        self.settings_btn.setIcon(QIcon.fromTheme("preferences-system"))
        self.settings_btn.setFixedSize(40, 40)
        self.settings_btn.clicked.connect(self.open_settings)
        self.login_btn = QPushButton()
        self.login_btn.setIcon(QIcon.fromTheme("user-identity"))
        self.login_btn.setFixedSize(40, 40)
        self.login_btn.clicked.connect(self.open_login)
        self.single_btn.clicked.connect(lambda: self.parent.show_game(mode="single"))
        self.multi_btn.clicked.connect(lambda: self.parent.show_game(mode="multi"))
        btn_layout.addWidget(self.single_btn)
        btn_layout.addWidget(self.multi_btn)
        btn_layout.addWidget(self.settings_btn)
        btn_layout.addWidget(self.login_btn)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def open_settings(self):
        QMessageBox.information(self, "환경설정", "여기서 환경설정(음량, 테마 등)을 구현할 수 있습니다.")

    def open_login(self):
        QMessageBox.information(self, "로그인", "여기서 로그인/회원가입 기능을 구현할 수 있습니다.")

class SongGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("노래 맞추기 게임")
        self.setGeometry(200, 200, 500, 350)  # 시작 화면 크기 축소
        self.setWindowIcon(QIcon())
        pygame.mixer.init()
        self.init_data()
        self.stacked = QStackedWidget()
        self.start_screen = StartScreen(self)
        self.stacked.addWidget(self.start_screen)
        self.setCentralWidget(self.stacked)
        self.favorites = []
        self.score = 0

    def init_data(self):
        with open(CATEGORY_FILE, encoding="utf-8") as f:
            self.categories = json.load(f)
        self.category_names = list(self.categories.keys())
        self.songs = []
        self.nickname = ""
        self.avatar_path = ""

    def show_game(self, mode="single"):
        self.game_widget = GameWidget(self, mode)
        if self.stacked.count() == 2:
            self.stacked.removeWidget(self.stacked.widget(1))
        self.stacked.addWidget(self.game_widget)
        self.stacked.setCurrentWidget(self.game_widget)
        # 창 크기 고정 해제 (사용자 자유 조절)
        self.setMinimumSize(400, 320)
        self.setMaximumSize(16777215, 16777215)
        self.setSizePolicy(self.sizePolicy().Expanding, self.sizePolicy().Expanding)
        # 멀티플레이 안내
        if mode == "multi":
            QMessageBox.information(self, "멀티플레이", "서버와 연결 중입니다. 곡/카테고리 목록을 불러옵니다.")

class GameWidget(QWidget):
    def __init__(self, parent, mode):
        super().__init__()
        self.parent = parent
        self.mode = mode
        self.categories = parent.categories
        self.category_names = parent.category_names
        self.songs = []
        self.favorites = []
        self.score = 0
        self.nickname = ""
        self.avatar_path = ""
        self.init_ui()


    def init_ui(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        center_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # 아바타/닉네임
        self.avatar_label = QLabel()
        self.avatar_label.setFixedSize(80, 80)
        self.avatar_label.setStyleSheet("border: 2px solid #aaa; border-radius: 40px;")
        self.nickname_input = QLineEdit()
        self.nickname_input.setPlaceholderText("닉네임 입력")
        self.avatar_btn = QPushButton("아바타 선택")
        self.avatar_btn.clicked.connect(self.select_avatar)
        left_layout.addWidget(self.avatar_label)
        left_layout.addWidget(self.nickname_input)
        left_layout.addWidget(self.avatar_btn)

        # 싱글/멀티플레이 분기 안내
        if self.mode == "multi":
            left_layout.addWidget(QLabel("[멀티플레이 모드] 서버와 연동됩니다."))
        else:
            left_layout.addWidget(QLabel("[싱글플레이 모드] 로컬에서 진행됩니다."))

        # 카테고리 선택만 표시 (싱글/멀티 분기)
        self.category_box = QComboBox()
        self.category_box.addItems(self.category_names)
        self.category_box.currentIndexChanged.connect(self.load_songs)
        left_layout.addWidget(QLabel("카테고리 선택"))
        left_layout.addWidget(self.category_box)
        self.song_list = QListWidget()  # 항상 생성
        if self.mode == "multi":
            left_layout.addWidget(QLabel("곡 목록"))
            left_layout.addWidget(self.song_list)
            self.song_list.currentRowChanged.connect(self.update_song_info)
        else:
            self.song_list.hide()  # 싱글모드에서는 숨김

        # 중앙: 곡 정보/음원 재생/정답 입력
        self.song_info = QLabel("곡 정보")
        self.song_info.setFont(QFont("맑은 고딕", 14))
        if self.mode == "single":
            self.song_info.hide()
            # 싱글플레이 UI: 중앙 세로 정렬, 불필요한 공간 최소화
            single_layout = QVBoxLayout()
            single_layout.setAlignment(Qt.AlignCenter)
            self.random_btn = QPushButton("랜덤 노래 재생")
            self.random_btn.setFixedHeight(40)
            self.random_btn.setStyleSheet("font-size:16px; margin-bottom:10px;")
            self.random_btn.clicked.connect(self.play_random_song)
            single_layout.addWidget(self.random_btn)

            self.answer_input = QLineEdit()
            self.answer_input.setPlaceholderText("곡명을 입력하세요")
            self.answer_input.setFixedHeight(32)
            self.answer_input.setStyleSheet("font-size:15px; margin-bottom:10px;")
            single_layout.addWidget(self.answer_input)

            self.check_btn = QPushButton("정답 확인")
            self.check_btn.setFixedHeight(36)
            self.check_btn.setStyleSheet("font-size:15px; margin-bottom:10px;")
            self.check_btn.clicked.connect(self.check_answer)
            single_layout.addWidget(self.check_btn)

            self.result_label = QLabel("")
            self.result_label.setAlignment(Qt.AlignCenter)
            self.result_label.setStyleSheet("font-size:16px; margin-top:10px;")
            single_layout.addWidget(self.result_label)

            center_layout.addStretch(1)
            center_layout.addLayout(single_layout)
            center_layout.addStretch(1)
        else:
            center_layout.addWidget(self.song_info)
            self.preview_btn = QPushButton("음원 미리듣기 (5초)")
            self.preview_btn.clicked.connect(self.preview_audio)
            self.section_btn = QPushButton("특정 구간 재생")
            self.section_btn.clicked.connect(self.select_audio_section)
            self.play_btn = QPushButton("전체 재생")
            self.play_btn.clicked.connect(self.play_audio)
            center_layout.addWidget(self.preview_btn)
            center_layout.addWidget(self.section_btn)
            center_layout.addWidget(self.play_btn)
            self.answer_input = QLineEdit()
            self.answer_input.setPlaceholderText("곡명을 입력하세요")
            center_layout.addWidget(self.answer_input)
            self.check_btn = QPushButton("정답 확인")
            self.check_btn.clicked.connect(self.check_answer)
            center_layout.addWidget(self.check_btn)
            self.result_label = QLabel("")
            center_layout.addWidget(self.result_label)

        # 즐겨찾기/업적/랭킹/통계/채팅
        self.favorite_btn = QPushButton("즐겨찾기 추가")
        self.favorite_btn.clicked.connect(self.add_favorite)
        right_layout.addWidget(self.favorite_btn)
        self.fav_list = QListWidget()
        right_layout.addWidget(QLabel("즐겨찾기 목록"))
        right_layout.addWidget(self.fav_list)
        self.badge_label = QLabel("업적/뱃지: 없음")
        right_layout.addWidget(self.badge_label)
        self.score_label = QLabel("점수: 0")
        right_layout.addWidget(self.score_label)
        if self.mode == "multi":
            self.chat_box = QTextEdit()
            self.chat_box.setReadOnly(True)
            self.chat_input = QLineEdit()
            self.chat_input.setPlaceholderText("채팅 입력")
            self.send_btn = QPushButton("채팅 전송")
            self.send_btn.clicked.connect(self.send_chat)
            right_layout.addWidget(QLabel("채팅"))
            right_layout.addWidget(self.chat_box)
            right_layout.addWidget(self.chat_input)
            right_layout.addWidget(self.send_btn)
        self.admin_btn = QPushButton("관리자 모드")
        self.admin_btn.clicked.connect(self.admin_mode)
        right_layout.addWidget(self.admin_btn)
        # 뒤로가기 버튼
        self.back_btn = QPushButton("뒤로가기")
        self.back_btn.clicked.connect(self.go_back)
        right_layout.addWidget(self.back_btn)

        main_layout.addLayout(left_layout, 2)
        main_layout.addLayout(center_layout, 3)
        main_layout.addLayout(right_layout, 2)
        self.setLayout(main_layout)
        self.load_songs()

    def go_back(self):
        # 첫 화면(StartScreen)으로 복귀 및 창 크기 원래대로 복원
        self.parent.stacked.setCurrentWidget(self.parent.start_screen)
        self.parent.resize(500, 350)

    def select_avatar(self):
        path, _ = QInputDialog.getText(self, "아바타 이미지 경로", "이미지 파일 경로 입력:")
        if path and os.path.exists(path):
            pixmap = QPixmap(path).scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.avatar_label.setPixmap(pixmap)
            self.avatar_path = path

    def load_songs(self):
        cat = self.category_box.currentText()
        self.songs = self.categories[cat]
        self.song_list.clear()
        if self.mode == "multi":
            for song in self.songs:
                self.song_list.addItem(f"{song['title']} / {song['artist']}")
            self.update_song_info(0)

    def update_song_info(self, idx):
        if self.mode == "single":
            self.song_info.hide()
            return
        if idx < 0 or idx >= len(self.songs):
            self.song_info.setText("곡 정보")
            return
        song = self.songs[idx]
        self.song_info.setText(f"아티스트: {song['artist']}\n파일: {song['file']}")

    def select_avatar(self):
        path, _ = QInputDialog.getText(self, "아바타 이미지 경로", "이미지 파일 경로 입력:")
        if path and os.path.exists(path):
            pixmap = QPixmap(path).scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.avatar_label.setPixmap(pixmap)
            self.avatar_path = path

    def load_songs(self):
        cat = self.category_box.currentText()
        self.songs = self.categories[cat]
        self.song_list.clear()
        for song in self.songs:
            self.song_list.addItem(f"{song['title']} / {song['artist']}")
        self.update_song_info(0)

    def update_song_info(self, idx):
        if idx < 0 or idx >= len(self.songs):
            self.song_info.setText("곡 정보")
            return
        song = self.songs[idx]
        self.song_info.setText(f"아티스트: {song['artist']}\n파일: {song['file']}")

    def preview_audio(self):
        idx = self.song_list.currentRow()
        if idx < 0: return
        song = self.songs[idx]
        audio_path = os.path.join(AUDIO_DIR, song['file'])
        if not os.path.exists(audio_path):
            QMessageBox.warning(self, "오류", "음원 파일이 없습니다.")
            return
        try:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            QApplication.processEvents()
            import time; time.sleep(5)
            pygame.mixer.music.stop()
        except Exception as e:
            QMessageBox.warning(self, "오류", f"음원 재생 오류: {e}")

    def select_audio_section(self):
        idx = self.song_list.currentRow()
        if idx < 0: return
        song = self.songs[idx]
        audio_path = os.path.join(AUDIO_DIR, song['file'])
        start, ok1 = QInputDialog.getInt(self, "구간 재생", "시작 초 입력:", 0, 0, 60)
        end, ok2 = QInputDialog.getInt(self, "구간 재생", "종료 초 입력:", 5, 1, 120)
        if ok1 and ok2 and end > start:
            try:
                pygame.mixer.music.load(audio_path)
                pygame.mixer.music.play(start)
                QApplication.processEvents()
                import time; time.sleep(end - start)
                pygame.mixer.music.stop()
            except Exception as e:
                QMessageBox.warning(self, "오류", f"구간 재생 오류: {e}")

    def play_audio(self):
        idx = self.song_list.currentRow()
        if idx < 0: return
        song = self.songs[idx]
        audio_path = os.path.join(AUDIO_DIR, song['file'])
        if not os.path.exists(audio_path):
            QMessageBox.warning(self, "오류", "음원 파일이 없습니다.")
            return
        try:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
        except Exception as e:
            QMessageBox.warning(self, "오류", f"음원 재생 오류: {e}")

    def check_answer(self):
        import random
        idx = self.song_list.currentRow()
        if self.mode == "single":
            # 싱글플레이: 랜덤 곡에서 정답 체크
            if not hasattr(self, 'current_random_idx'):
                self.result_label.setText("먼저 랜덤 노래를 재생하세요!")
                self.result_label.setStyleSheet("color: orange;")
                return
            song = self.songs[self.current_random_idx]
        else:
            if idx < 0: return
            song = self.songs[idx]
        answer = self.answer_input.text().strip()
        if answer == song['title']:
            self.result_label.setText("정답! 🎉")
            self.result_label.setStyleSheet("color: green; font-weight: bold;")
            self.score += 1
            self.score_label.setText(f"점수: {self.score}")
            self.award_badge()
        else:
            # 오답 시 힌트(제목의 한 글자만 랜덤 위치로 제공)
            title = song['title']
            if len(title) > 0:
                hint_idx = random.randint(0, len(title)-1)
                hint_char = title[hint_idx]
                hint = ["_" for _ in title]
                hint[hint_idx] = hint_char
                hint_str = "힌트: " + " ".join(hint)
            else:
                hint_str = "힌트 없음"
            self.result_label.setText(f"오답! {hint_str}")
            self.result_label.setStyleSheet("color: orange; font-weight: bold;")
    def play_random_song(self):
        import random
        if not self.songs:
            self.result_label.setText("카테고리를 먼저 선택하세요!")
            self.result_label.setStyleSheet("color: orange;")
            return
        self.current_random_idx = random.randint(0, len(self.songs)-1)
        song = self.songs[self.current_random_idx]
        audio_path = os.path.join(AUDIO_DIR, song['file'])
        if not os.path.exists(audio_path):
            QMessageBox.warning(self, "오류", "음원 파일이 없습니다.")
            return
        try:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            self.result_label.setText("노래가 재생 중입니다. 정답을 입력하세요!")
            self.result_label.setStyleSheet("color: blue;")
        except Exception as e:
            QMessageBox.warning(self, "오류", f"음원 재생 오류: {e}")

    def add_favorite(self):
        idx = self.song_list.currentRow()
        if idx < 0: return
        song = self.songs[idx]
        if song not in self.favorites:
            self.favorites.append(song)
            self.fav_list.addItem(f"{song['title']} / {song['artist']}")
            QMessageBox.information(self, "즐겨찾기", "즐겨찾기에 추가되었습니다.")

    def award_badge(self):
        if self.score == len(self.songs):
            self.badge_label.setText("업적/뱃지: 음악 천재")
        elif self.score >= len(self.songs) // 2:
            self.badge_label.setText("업적/뱃지: 음악 애호가")
        else:
            self.badge_label.setText("업적/뱃지: 참가상")

    def send_chat(self):
        msg = self.chat_input.text().strip()
        if msg:
            self.chat_box.append(f"{self.nickname_input.text()}: {msg}")
            self.chat_input.clear()

    def admin_mode(self):
        QMessageBox.information(self, "관리자 모드", "곡/카테고리 삭제, 수정, 추가 등은 별도 관리 화면에서 구현 가능합니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SongGame()
    app.setStyleSheet("""
        QWidget { font-family: '맑은 고딕'; font-size: 13px; }
        QPushButton { background: #4F8EF7; color: white; border-radius: 6px; padding: 6px 12px; }
        QPushButton:hover { background: #357AE8; }
        QLineEdit, QComboBox, QListWidget, QTextEdit { background: #F5F7FA; border-radius: 4px; }
        QLabel { color: #222; }
    """)
    window.show()
    sys.exit(app.exec_())
