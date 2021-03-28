import argparse
parser = argparse.ArgumentParser()
parser.add_argument("users", help="specify users ammount", type=int)
parser.add_argument("db", help="specify db path", type=str)
args = parser.parse_args()

f = open(args.db, 'r')
sql_script_data = f.read()
f.close()
file = open('./db_and_users.sql', 'w')
for i in range(1, args.users + 1):
    file.write(f"CREATE USER 'user_{i}'@'%' IDENTIFIED BY 'user{i}password';\n")
    file.write(sql_script_data.replace('classicmodels', f'db_user_{i}'))
    file.write(f"GRANT ALL PRIVILEGES ON db_user_{i}.* TO \'user_{i}\'@\'%\';\n")
    file.write('FLUSH PRIVILEGES;\n')
file.close()
