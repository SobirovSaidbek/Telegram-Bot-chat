import psycopg2 as db
from main import config
import random

class Database:
    def __init__(self):
        self.conn = db.connect(
            database=config.DB_NAME,
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        user_table = """
        CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        chat_id BIGINT NOT NULL,
        full_name VARCHAR(55),
        phone_number VARCHAR(13),
        location VARCHAR(55),
        status BOOLEAN DEFAULT FALSE
        );
        """

        self.cursor.execute(user_table)

        self.conn.commit()


    def get_user(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id} and status = true"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result


    def add_user(self, data: dict):
        chat_id = data["chat_id"]
        full_name = data["full_name"]
        phone_number = data["phone_number"]
        location = data["location"]
        query = f"""INSERT INTO users (chat_id, full_name, phone_number, location)
        VALUES ({chat_id}, '{full_name}','{phone_number}', '{location}')"""
        self.cursor.execute(query)
        self.conn.commit()
        return True


    def get_follow_users(self, username):
        query = f"SELECT * FROM users WHERE user_name = {username} and status = true"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def chat_bot_message(self, chat_id):
        query_follow = f"SELECT COUNT(*) FROM users WHERE chat_id = {chat_id} and status = true"
        query_nefollow = f"SELECT COUNT(*) FROM users WHERE chat_id = {chat_id} and status = false"
        self.cursor.execute(query_follow)
        follow = self.cursor.fetchone()
        self.cursor.execute(query_nefollow)
        nefollow = self.cursor.fetchone()
        return follow, nefollow


    def get_user_by_chat_id(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_user_photo_by_chat_id(self, chat_id):
        query = f"SELECT * FROM photos WHERE chat_id = {chat_id} AND status = true"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result


    def user_like(self, chat_id, photo_id, is_like):
        query = f"""INSERT INTO likes (chat_id, photo_id, is_like)
           VALUES ({chat_id}, '{photo_id}', {is_like})"""
        self.cursor.execute(query)
        self.conn.commit()
        return True