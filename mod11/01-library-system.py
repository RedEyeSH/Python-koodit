class Publication:
    def __init__(self, name: str):
        self.name = name

    def print_information(self):
        pass

class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}\n")

class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"\nMagazine name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}\n")

mag = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

mag.print_information()
book.print_information()
