from database import create_connection

class UserModel:
    @staticmethod
    def get_all_users():
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user")
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    
    @staticmethod
    def insert_users(name,email,password):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user (name, email, password) VALUES(%s, %s, %s)", (name, email, password))
        connection.commit()
        cursor.close()
        connection.close()
        
    @staticmethod
    def delete_user(user_id):
        connection = create_connection()
        cursor = connection.cursor()
        sql_query = "DELETE FROM user WHERE id = %s"
        cursor.execute(sql_query, (user_id,))
        cursor.close()
        connection.close()