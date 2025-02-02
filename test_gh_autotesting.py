import pytest
from .sfconn import SnowflakeConnection
from .psqlconn import PostgresConnection
import os

# comment placeholder
@pytest.fixture(scope="module")
def pg_conn():
    ssh_host = os.getenv('PG_SSH_HOST')
    ssh_port = int(os.getenv('PG_SSH_PORT'))
    ssh_user = os.getenv('PG_SSH_USER')
    ssh_password = os.getenv('PG_SSH_PASSWORD')
    pg_host = os.getenv('PG_HOST')
    pg_port = int(os.getenv('PG_PORT'))
    pg_user = os.getenv('PG_USER')
    pg_password = os.getenv('PG_PASSWORD')
    pg_db = os.getenv('PG_DB')

    # Print environment variables to verify they are set correctly
    print(f"PG_SSH_HOST: {ssh_host}")
    print(f"PG_SSH_PORT: {ssh_port}")
    print(f"PG_SSH_USER: {ssh_user}")
    print(f"PG_SSH_PASSWORD: {ssh_password}")
    print(f"PG_HOST: {pg_host}")
    print(f"PG_PORT: {pg_port}")
    print(f"PG_USER: {pg_user}")
    print(f"PG_PASSWORD: {pg_password}")
    print(f"PG_DB: {pg_db}")

    with PostgresConnection(ssh_host, ssh_port, ssh_user, ssh_password, pg_host, pg_port, pg_user, pg_password, pg_db) as conn:
        yield conn

@pytest.fixture(scope="module")
def sf_conn():
    sf_user = os.getenv('SF_USER')
    sf_password = os.getenv('SF_PASSWORD')
    sf_account = os.getenv('SF_ACCOUNT')

    # Print environment variables to verify they are set correctly
    print(f"SF_USER: {sf_user}")
    print(f"SF_PASSWORD: {sf_password}")
    print(f"SF_ACCOUNT: {sf_account}")

    with SnowflakeConnection(sf_user, sf_password, sf_account) as conn:
        yield conn

def test_row_counts(pg_conn, sf_conn, capfd):
    pg_cursor = pg_conn.cursor()
    pg_cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public' AND table_type = 'BASE TABLE'")
    pg_rowcount = pg_cursor.fetchone()[0]

    sf_cursor = sf_conn.cursor()
    sf_cursor.execute("SELECT COUNT(*) AS rowcount FROM dvdrental.INFORMATION_SCHEMA.TABLES WHERE table_schema = 'PUBLIC' AND table_type = 'BASE TABLE'")
    sf_rowcount = sf_cursor.fetchone()[0]

    assert pg_rowcount == sf_rowcount, f"Row counts do not match: PostgreSQL ({pg_rowcount}) vs Snowflake ({sf_rowcount})"

@pytest.mark.parametrize("table_name", ["actor", "film", "customer", "payment", "rental"])
def test_table_row_count(pg_conn, sf_conn, table_name):
    pg_cursor = pg_conn.cursor()
    pg_cursor.execute(f"SELECT COUNT(*) FROM public.{table_name}")
    pg_rowcount = pg_cursor.fetchone()[0]

    sf_cursor = sf_conn.cursor()
    sf_cursor.execute(f'SELECT COUNT(*) AS rowcount FROM dvdrental.PUBLIC.{table_name}')
    sf_rowcount = sf_cursor.fetchone()[0]

    print(f"PostgreSQL {table_name} table row count: {pg_rowcount}")
    print(f"Snowflake {table_name} table row count: {sf_rowcount}")

    assert pg_rowcount == sf_rowcount, f"Row counts do not match for table {table_name}: PostgreSQL ({pg_rowcount}) vs Snowflake ({sf_rowcount})"
