import mysql.connector
import pandas as pd

con = mysql.connector.connect(
    user="root", password="!Zinn14113", host="localhost", port="3306", database="egc"
)

cur = con.cursor()
cur.execute("SELECT * FROM ve_status WHERE UTILITY='PECO' LIMIT 100")


columns = [x[0] for x in cur.description]

df = pd.DataFrame(cur)

cur.close()
con.close()


df.columns = columns

print(df.head())

