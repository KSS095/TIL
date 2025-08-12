class Book:
    # 2. 클래스 변수 생성
    book_count = 0

    # 1. title, author, year, price를 인자로 받아 인스턴스 변수로 저장하는 생성자
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        
        # 가격은 0 이상만 허용, 0 미만일 경우 ValueError
        if price >= 0:
            self.price = price
        # else: ValueError()

        # 2. Book의 인스턴스 생성 시 클래서 변수 1씩 증가
        Book.book_count += 1

    # 3. 인스턴스 메서드 get_info()
    # f-string 이용하여 적절한 문자열 반환
    def get_info(self):
        return f'[{self.title} - {self.author}, {self.year}년, {self.price}원]'

    # 4. 정적 메서드 is_expensive()
    @staticmethod
    def is_expensive(price):
        if price >= 30000: return True
        else: return False

    # 5. 클래스 메서드 get_book_count()
    @classmethod
    def get_book_count(cls):
        return cls.book_count
    
    # 6. 클래스 메서드 from_string()
    # info_str 문자열을 적절히 변환하여 새로운 Book의 인스턴스 반환
    @classmethod
    def from_string(cls, info_str):
        book_str = info_str.split('/')
        return cls(book_str[0], book_str[1], int(book_str[2]), int(book_str[3]))

# 아래 코드는 수정 할 수 없음
book1 = Book("파이썬 완벽 가이드", "홍길동", 2023, 35000)
book2 = Book.from_string("자료구조의 이해/이순신/2021/28000")

print(book1.get_info())
# [파이썬 완벽 가이드 - 홍길동, 2023년, 35000원]
print(Book.is_expensive(35000))  # True
print(Book.get_book_count())     # 2