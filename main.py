# import psycopg2
# import re
#
# # PostgreSQL ga ulanish
# conn = psycopg2.connect(
#     dbname="contact_db",
#     user="postgres",
#     password="1234",  # o'zingizni parolingiz
#     host="localhost"
# )
# cur = conn.cursor()
#
# # Jadval mavjud bo'lmasa yaratamiz
# cur.execute("""
# CREATE TABLE IF NOT EXISTS contact (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     phone VARCHAR(20) NOT NULL
# )
# """)
# conn.commit()
#
#
# class Contact:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#     def __str__(self):
#         return self.phone
#
#     def info(self):
#         print(f"name: {self.name} phone: {self.phone}")
#
#
# def contact_manager():
#     while True:
#         kod = input("\n 1. add contact\n 2. view contacts\n 3. delete contact\n 4. quit\nTanlang: ")
#
#         if kod == "1":
#             name = input("Name: ")
#             phone = input("Phone: ")
#             r_name = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
#             if re.match(r_name, phone):
#                 cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
#                 conn.commit()
#                 print("✅ Contact added")
#             else:
#                 print("❌ Telefon raqam noto‘g‘ri kiritilgan")
#
#         elif kod == "2":
#             cur.execute("SELECT name, phone FROM contacts")
#             rows = cur.fetchall()
#             if rows:
#                 print("\n📒 Kontaktlar ro'yxati:")
#                 for row in rows:
#                     print(f"name: {row[0]}, phone: {row[1]}")
#             else:
#                 print("❌ Hali kontakt yo‘q")
#
#         elif kod == "3":
#             name = input("Delete uchun name: ")
#             cur.execute("DELETE FROM contacts WHERE name = %s", (name,))
#             conn.commit()
#             print("🗑 Kontakt o‘chirildi (agar mavjud bo‘lsa)")
#
#         elif kod == "4":
#             print("👋 Dastur tugadi")
#             break
#
#         else:
#             print("❌ Noto‘g‘ri tanlov, qayta urinib ko‘ring")
#
#
# contact_manager()
#
# # dastur tugaganda ulanishni yopamiz
# cur.close()
# conn.close()
#
# cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
# print("📋 Bazadagi jadvallar:")
# for row in cur.fetchall():
#     print("-", row[0])

