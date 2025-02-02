import psycopg2
from sshtunnel import SSHTunnelForwarder

class PostgresConnection:
    def __init__(self, ssh_host, ssh_port, ssh_user, ssh_password, pg_host, pg_port, pg_user, pg_password, pg_db):
        self.ssh_host = ssh_host
        self.ssh_port = ssh_port
        self.ssh_user = ssh_user
        self.ssh_password = ssh_password
        self.pg_host = pg_host
        self.pg_port = pg_port
        self.pg_user = pg_user
        self.pg_password = pg_password
        self.pg_db = pg_db
        self.tunnel = None
        self.connection = None

    def __enter__(self):
        self.tunnel = SSHTunnelForwarder(
            (self.ssh_host, self.ssh_port),
            ssh_username=self.ssh_user,
            ssh_password=self.ssh_password,
            remote_bind_address=(self.pg_host, self.pg_port)
        )
        self.tunnel.start()
        self.connection = psycopg2.connect(
            database=self.pg_db,
            user=self.pg_user,
            password=self.pg_password,
            host=self.tunnel.local_bind_host,
            port=self.tunnel.local_bind_port
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
        if self.tunnel:
            self.tunnel.stop()
