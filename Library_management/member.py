# member.py
from abc import ABC, abstractmethod

class LibraryMember(ABC):
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    @abstractmethod
    def borrow_book(self, book):
        pass
