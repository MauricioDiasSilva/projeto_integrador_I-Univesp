import MySQLdb

try:
    db = MySQLdb.connect(
        host="127.0.0.1",
        user="admin",
        passwd="123456",
        db="db"
    )
    print("Conectado com sucesso")
except MySQLdb.Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
