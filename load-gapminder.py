import pandas
import psycopg2
import sys

# connect to database and create a cursor by which to interact with it.
try:
    conn = psycopg2.connect("dbname='root' user='root'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

# set up our table
cur.execute("DROP TABLE IF EXISTS " + sys.argv[2])
cur.execute("create table " + sys.argv[2] + "(country text, continent text, year integer, lifeexp real, pop integer, gdppercap real);")

# fetch data
#df = pandas.DataFrame.from_csv(sys.argv[1], sep='\t', header=1)
df = pandas.read_table(sys.argv[1])

# populate table from df
for row in df.itertuples():
    cmnd = "INSERT INTO "+sys.argv[2]+" VALUES ( '"+str(row[1]).replace('\'', '')+"','"+str(row[2])+"',"+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+" )"
    cur.execute(cmnd)

conn.commit()
