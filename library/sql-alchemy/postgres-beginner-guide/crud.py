from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from config import DATABASE_URI
from models import Base, Book
from datetime import datetime
# import yaml
# yaml.warnings({'YAMLLoadWarning': False})

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def recreateDB():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


book1 = Book(
    title='Deep Learning',
    author='Ian Goodfellow',
    pages=775,
    published=datetime(2016, 11, 18)
)

book2 = Book(
    title="An Introduction to Statistical Learning: with Applications in R",
    author="Gareth James",
    pages=436,
    published=datetime(2013, 12, 21)
)

recreateDB()
s = Session()

# Inserting Rows
s.add(book1)
s.add(book2)
s.commit()

# Quering
first_book = s.query(Book).first()
print(first_book)

# for data in yaml.load_all(open('books.yaml'), Loader=yaml.FullLoader):
#     book = Book(**data)
#     s.add(book)

# s.commit()

all_books = s.query(Book).all()
print(all_books)

# Filtering basics: WHERE
r = s.query(Book).filter_by(title='Deep Learning').first()
print("filter_by:", r)

r = s.query(Book).filter(Book.title == 'Deep Learning').first()
print("filter:", r)

start_date = datetime(2009, 1, 1)
end_date = datetime(2012, 1, 1)

print(s.query(Book).filter(Book.published.between(start_date, end_date)).all())


# AND OR
print(s.query(Book).filter(
    and_(
        Book.pages > 750,
        Book.published > datetime(2016, 1, 1)
    )
).all()
)


# ORDER BY
print(s.query(Book).order_by(Book.pages.desc()).all())


# LIMIT
print(s.query(Book).limit(2).all())