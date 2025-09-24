


import psycopg2
import re

# PostgreSQL ga ulanish
conn = psycopg2.connect(
    dbname="contact_db",
    user="postgres",
    password="1234",  # o'zingizning parolingizni yozing
    host="localhost",
    port="5432"
)


import psycopg2

# PostgreSQL ga ulanish
conn = psycopg2.connect(
    dbname="contact_db",
    user="postgres",
    password="1234",   # o'zingizning parolingiz
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# contact jadvalini yaratish
cur.execute("""
CREATE TABLE IF NOT EXISTS contact (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
)
""")

# sms jadvalini yaratish
cur.execute("""
CREATE TABLE IF NOT EXISTS sms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    message TEXT NOT NULL
)
""")

conn.commit()
print("✅ Jadvallar yaratildi (agar mavjud bo'lmasa)")


class Contact:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def info(self):
        print(f"name: {self.__name}, phone: {self.__phone}")


class SMS:
    def __init__(self, name, phone, message):
        self.__name = name
        self.__phone = phone
        self.__message = message

    def info(self):
        print(f"name: {self.__name}, phone: {self.__phone}, message: {self.__message}")


def contact_manager():
    while True:
        kod = input("\n1. add contact\n2. view contact\n3. del contact\n4. quit\n> ")

        if kod == "1":  # add contact
            name = input("name: ")
            phone = input("phone: ")
            r_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
            if re.match(r_phone, phone):
                cur.execute("INSERT INTO contact (name, phone) VALUES (%s, %s)", (name, phone))
                conn.commit()
                print("✅ kontakt qo‘shildi")
            else:
                print("❌ raqam noto‘g‘ri")

        elif kod == "2":  # view contacts
            cur.execute("SELECT name, phone FROM contact")
            rows = cur.fetchall()
            if rows:
                print("\n📒 kontaktlar ro‘yxati:")
                for row in rows:
                    c = Contact(row[0], row[1])
                    c.info()
            else:
                print("❌ kontakt yo‘q")

        elif kod == "3":  # delete contact
            name = input("name: ")
            cur.execute("DELETE FROM contact WHERE LOWER(name) = LOWER(%s)", (name,))
            conn.commit()
            if cur.rowcount > 0:
                print("🗑 kontakt o‘chirildi")
            else:
                print("❌ bunday kontakt topilmadi")

        elif kod == "4":
            break
        else:
            print("❌ noto‘g‘ri tanlov")


def sms_manager():
    while True:
        kod = input("\n1. sms yuborish\n2. sms tarixi\n3. sms ochirish\n4. quit\n> ")

        if kod == "1":  # send sms
            name = input("name: ")
            phone = input("phone: ")
            r_phone = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
            if not re.match(r_phone, phone):
                print("❌ raqam noto‘g‘ri")
                continue

            # kontakt borligini tekshirish
            cur.execute("SELECT * FROM contact WHERE LOWER(name)=LOWER(%s) AND phone=%s", (name, phone))
            row = cur.fetchone()
            if not row:
                print("❌ bu kontakt yo‘q, sms yuborilmaydi")
                continue

            text = input("sms: ")
            cur.execute("INSERT INTO sms (name, phone, message) VALUES (%s, %s, %s)", (name, phone, text))
            conn.commit()
            print("📨 sms yuborildi")

        elif kod == "2":  # view sms
            cur.execute("SELECT name, phone, message FROM sms")
            rows = cur.fetchall()
            if rows:
                print("\n📜 sms tarixi:")
                for row in rows:
                    s = SMS(row[0], row[1], row[2])
                    s.info()
            else:
                print("❌ sms tarixi yo‘q")

        elif kod == "3":  # delete sms
            name = input("name: ")
            cur.execute("DELETE FROM sms WHERE LOWER(name)=LOWER(%s)", (name,))
            conn.commit()
            if cur.rowcount > 0:
                print("🗑 sms o‘chirildi")
            else:
                print("❌ bunday sms yo‘q")

        elif kod == "4":
            break
        else:
            print("❌ noto‘g‘ri tanlov")


def main():
        while True:
            print("\n--asosiy menyu--")
            tanlov = input("1. contact manager\n2. sms manager\n3. chiqish\n> ")

            if tanlov == "1":
                contact_manager()
            elif tanlov == "2":
                sms_manager()
            elif tanlov == "3":
                print("👋 dastur tugadi")

                # faqat shu yerda ulanishni yopamiz
                cur.close()
                conn.close()
                break
            else:
                print("❌ noto‘g‘ri tanlov")
main()


















