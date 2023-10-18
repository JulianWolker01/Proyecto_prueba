import os.path as path

if path.exists("backend\\node_back\\.env"):
    print("Ya existe")
else:
    file = open("backend\\node_back\\.env", "w")
    file.write('DATABASE_URL = "sqlserver://10.120.0.176:1433;initialCatalog=proyecto_academico;trustServerCertificate=true;user=123;Password=456"')
    file.close()
