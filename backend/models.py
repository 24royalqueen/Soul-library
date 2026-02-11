from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_date = Column(DateTime, default=datetime.utcnow)
    isbn = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Book(title={self.title}, author={self.author}, isbn={self.isbn})>'

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Member(name={self.name}, email={self.email})>'

class Borrowing(Base):
    __tablename__ = 'borrowings'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime)

    book = relationship('Book', backref='borrowings')
    member = relationship('Member', backref='borrowings')

class Return(Base):
    __tablename__ = 'returns'

    id = Column(Integer, primary_key=True)
    borrowing_id = Column(Integer, ForeignKey('borrowings.id'), nullable=False)
    return_date = Column(DateTime, default=datetime.utcnow)

    borrowing = relationship('Borrowing', backref='returns')

class Fine(Base):
    __tablename__ = 'fines'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    date_issued = Column(DateTime, default=datetime.utcnow)

    member = relationship('Member', backref='fines')

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    reservation_date = Column(DateTime, default=datetime.utcnow)

    book = relationship('Book', backref='reservations')
    member = relationship('Member', backref='reservations')

