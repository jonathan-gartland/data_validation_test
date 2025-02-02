import snowflake.connector

class SnowflakeConnection:
    def __init__(self, user, password, account):
        self.user = user
        self.password = password
        self.account = account
        self.connection = None

    def __enter__(self):
        self.connection = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
