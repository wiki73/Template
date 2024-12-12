import sqlite3


class SQL:
    def __init__(self):
        self.conn = sqlite3.connect('SQL_file\\main_table.sqlite')
        self.cursor = self.conn.cursor()

    def get_all_templates(self):
        res = list(self.cursor.execute("""SELECT * FROM s_table""").fetchall())
        return res

    def get_all_folder(self):
        res = list(self.cursor.execute("""SELECT name_folder FROM Folder_table""").fetchall())
        return res

    def delete_by_name_folder(self, name):
        self.cursor.execute('DELETE FROM folder_table WHERE name_folder = ?', (name,))
        self.conn.commit()


    def get_some_templates(self, tag):
        return self.cursor.execute("""SELECT * FROM s_table
                WHERE tag LIKE ?""", (tag,)).fetchall()

    def delete_by_title(self, title):
        self.cursor.execute('DELETE FROM s_table WHERE title = ?', (title,))
        self.cursor.execute('DELETE FROM code_table WHERE title = ?', (title,))
        self.conn.commit()

    def update_template_by_title(self, title):
        return self.cursor.execute('''SELECT code FROM code_table
                                                            WHERE title = ?''', (title,))

    def delete_s_table(self):
        self.cursor.execute('''DELETE FROM s_table;''')

    def insert_s_table(self, tag_text, name_text):
        self.cursor.execute('''INSERT INTO s_table (tag, title)  VALUES (?, ?)''',
                            (tag_text, name_text))  # добавление в бд в s_table новый tag и новый title
        self.conn.commit()

    def insert_folder(self, name):
        print(11)
        self.cursor.execute('''INSERT INTO folder_table (name_folder) VALUES (?);''',
                            (name,))  # добавление в бд в folder_table новый folder
        print(22)
        self.conn.commit()

    def insert_code_table(self, name_text, code_text):
        self.cursor.execute('''INSERT INTO code_table  VALUES (?, ?)''',
                            (str(name_text), str(code_text)))  # добавление в бд в code_table новый код
        self.conn.commit()

    def code_by_title(self, name):
        return self.cursor.execute('''SELECT code FROM code_table
                                                        WHERE title = ?''', (name,))

    def get_tags(self):
        return list(self.cursor.execute('''SELECT DISTINCT tag FROM s_table'''))
