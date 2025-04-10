import pytest
from modtestpy.Connect import Connect
# test_Connect.py

@pytest.fixture
def basic_connection():
    """Fixture to create a basic connection instance"""
    return Connect("localhost", 8080)

def test_connection_initialization():
    """Test if the connection is properly initialized"""
    conn = Connect("test.com", 5000)
    assert conn.host == "test.com"
    assert conn.port == 5000

def test_connect_output(basic_connection, capsys):
    """Test if connect method prints the correct output"""
    basic_connection.connect()
    captured = capsys.readouterr()
    expected_output = "Connecting to localhost:8080...\nConnected!\n"
    assert captured.out == expected_output

def test_different_hosts():
    """Test initialization with different hosts"""
    hosts = ["127.0.0.1", "example.com", "test.local"]
    port = 8000
    for host in hosts:
        conn = Connect(host, port)
        assert conn.host == host
        assert conn.port == port

def test_different_ports():
    """Test initialization with different ports"""
    host = "localhost"
    ports = [80, 443, 8080, 5000]
    for port in ports:
        conn = Connect(host, port)
        assert conn.host == host
        assert conn.port == port