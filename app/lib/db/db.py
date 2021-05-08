import psycopg2

class DB:
    def __init__(self, host: str, db_name: str, username: str, password: str):
        self.host = host
        self.db_name = db_name
        self.username = username
        self.password = password

    def create_connection(self):
        conn = psycopg2.connect(
                host=self.host, 
                database=self.db_name, 
                user=self.username, 
                password=self.password)
        return conn

    def execute_query(self, query:str, flag: int, many=None):
        """
        Params
        ------
        query    :str
        flag     :int
                  1 - SELECT
                  2 - INSERT
        many     :bool
                 Use `True` if SELECT more than 1 columns. Default is None.
        """

        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(query)
        if flag == 1:
            if many: result = cur.fetchall()
            else: result = cur.fetchall()[0][0]
            cur.close()
            conn.close()
            return result
        else:
            conn.commit()
            cur.close()
            conn.close()