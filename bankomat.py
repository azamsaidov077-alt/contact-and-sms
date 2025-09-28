import psycopg2


conn = psycopg2.connect(
    dbname="bankdb",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);
""")


cur.execute("""
CREATE TABLE IF NOT EXISTS cards (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    pin VARCHAR(10) NOT NULL,
    seria VARCHAR(20) UNIQUE NOT NULL,
    balans INT DEFAULT 0,
    sms BOOLEAN DEFAULT FALSE,
    sms_phone VARCHAR(20)
);
""")

conn.commit()
cur.close()
conn.close()

print(" Jadvalar yaratildi!")

import psycopg2
import re

class Banko:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="bankdb",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()


    def add_user(self):
        name = input("Ism: ")
        phone = input("Telefon: ")
        self.cur.execute(
            "INSERT INTO users (fullname, phone) VALUES (%s, %s) RETURNING id",
            (name, phone)
        )
        user_id = self.cur.fetchone()[0]
        self.conn.commit()
        print(f"User qo'shildi. ID: {user_id}")


    def all_users(self):
        self.cur.execute("SELECT * FROM users")
        for row in self.cur.fetchall():
            print(row)


    def add_card(self):
        self.all_users()
        user_id = int(input("User ID tanlang: "))
        pin = input("PIN: ")
        seria = input("Seria: ")
        balans = int(input("Balans: "))
        self.cur.execute(
            "INSERT INTO cards (user_id, pin, seria, balans) VALUES (%s, %s, %s, %s)",
            (user_id, pin, seria, balans)
        )
        self.conn.commit()
        print(" Karta qo'shildi")

    def all_cards(self):
        self.cur.execute(
            """SELECT c.id, u.fullname, c.seria, c.balans, c.sms, c.sms_phone
               FROM cards c JOIN users u ON c.user_id = u.id"""
        )
        for row in self.cur.fetchall():
            sms = "yoqilgan" if row[4] else "ochirilgan"
            phone = row[5] if row[5] else "nomer yo'q"
            print(f"id:{row[0]}, ism:{row[1]}, seria:{row[2]}, balans:{row[3]}, sms:{sms}, phone:{phone}")


    def find_card(self):
        seria = input("Seria: ")
        pin = input("PIN: ")
        self.cur.execute("SELECT * FROM cards WHERE seria=%s AND pin=%s", (seria, pin))
        return self.cur.fetchone()


    def balans_qoshish(self):
        card = self.find_card()
        if card:
            summa = int(input("Summa: "))
            self.cur.execute(
                "UPDATE cards SET balans = balans + %s WHERE id=%s RETURNING balans",
                (summa, card[0])
            )
            new_balans = self.cur.fetchone()[0]
            self.conn.commit()
            print(f" Yangi balans: {new_balans}")


    def balans_yechish(self):
        card = self.find_card()
        if card:
            summa = int(input("Summa: "))
            if card[4] >= summa:
                self.cur.execute(
                    "UPDATE cards SET balans = balans - %s WHERE id=%s RETURNING balans",
                    (summa, card[0])
                )
                new_balans = self.cur.fetchone()[0]
                self.conn.commit()
                print(f" Yangi balans: {new_balans}")
            else:
                print(" Pul yetarli emas")


    def sms_toggle(self):
        card = self.find_card()
        if card:
            s = input("1 - yoqish, 0 - ochirish: ")
            if s == "1":
                phone = input("Telefon raqam: ")
                if re.match(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", phone):
                    self.cur.execute(
                        "UPDATE cards SET sms=True, sms_phone=%s WHERE id=%s",
                        (phone, card[0])
                    )
                    self.conn.commit()
                    print(" SMS yoqildi")
                else:
                    print(" Telefon formati noto‘g‘ri")
            elif s == "0":
                self.cur.execute(
                    "UPDATE cards SET sms=False, sms_phone=NULL WHERE id=%s",
                    (card[0],)
                )
                self.conn.commit()
                print(" SMS o‘chirildi")



banko = Banko()
while True:
    tanlov = input("""
1. User qo'shish
2. Userlarni ko‘rish
3. Karta qo‘shish
4. Kartalarni ko‘rish
5. Balans qo‘shish
6. Balans yechish
7. SMS yoqish/ochirish
8. Chiqish
>>> """)
    if tanlov == "1":
        banko.add_user()
    elif tanlov == "2":
        banko.all_users()
    elif tanlov == "3":
        banko.add_card()
    elif tanlov == "4":
        banko.all_cards()
    elif tanlov == "5":
        banko.balans_qoshish()
    elif tanlov == "6":
        banko.balans_yechish()
    elif tanlov == "7":
        banko.sms_toggle()
    elif tanlov == "8":
        print("Dastur tugadi")
        break
    else:
        print(" Noto‘g‘ri tanlov")
