import aiosqlite as sq

DB_PATH = "bot.db"

class Database:

    @staticmethod
    async def init():

        async with sq.connect(DB_PATH) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            await db.execute("""
                CREATE TABLE IF NOT EXISTS surveys (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    name TEXT,
                    age INTEGER,
                    city TEXT,
                    language TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            """)
            await db.commit()
            print("база данных успешно инициализирована!")

    
    @staticmethod
    async def add_user(user_id: int, username: str, first_name: str):
        async with sq.connect(DB_PATH) as db:
            await db.execute("""
                INSERT or IGNORE into users (user_id, username, first_name)
                VALUES (?, ?, ?)
            """, (user_id, username, first_name))
            await db.commit()

    @staticmethod
    async def save_survey(user_id: int, name: str, age: int, city: str, language: str):
        async with sq.connect(DB_PATH) as db:
            await db.execute("""
                INSERT or IGNORE into surveys (user_id, name, age, city, language)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, name, age, city, language))
            await db.commit()
    
    @staticmethod
    async def get_user_surveys(user_id: int):
        async with sq.connect(DB_PATH) as db:
            cursor = await db.execute("""
                SELECT
                    name, 
                    age,
                    city,
                    language,
                    created_at
                FROM 
                    surveys
                WHERE
                    user_id = ?
                ORDER BY
                    created_at DESC
            """, (user_id, ))

            rows  = await cursor.fetchall()

            return rows