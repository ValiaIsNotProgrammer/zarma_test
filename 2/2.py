from db import SQLiteRepo


repo = SQLiteRepo("example.db")
repo.create_schema()
repo.generate_fake_users()
users = repo.get_user_by_age(30)
print(users)
