import sqlalchemy
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from models import create_table, Publisher, Book, Shop, Stock, Sale

DSN = '...'
engine = sqlalchemy.create_engine(DSN)

create_table(engine)

Session = sessionmaker(bind=engine)
session=Session()

session.close_all()
# The Session.close_all() method is deprecated and will be removed in a future release. Please refer to session.close_all_sessions()

# pr = Publisher(name = 'Пушкин')
# b = Book(title = 'Капитанская дочка', publisher = pr)
# sh = Shop(name = "Буквоед")
# st = Stock(book = b, shop = sh, count = 10)
# s = Sale(price = 600, date_sale = '09.11.2022', stock = st, count = 1)
#
# session.add(pr)
# session.add(b)
# session.add(sh)
# session.add(st)
# session.add(s)
# session.commit()

sel = select([Book, Shop, Sale, Stock]).select_from(Stock.join(Shop, Stock.c.id_shop == Shop.c.id).join(Book, Stock.c.id_book == Book.c.id).join(Sale, Sale.c.id_stock == Stock.c.id))
for i in session.query(sel).all():
    print(i)


