import pyhs2
 
with pyhs2.connect(host='localhost',
    port=10000,
    authMechanism="PLAIN",
    user='root',
    password='test',
    database='default') as conn:
    with conn.cursor() as cur:
        #Show databases
        print cur.getDatabases()
        
        #Execute query
        #cur.execute("CREATE TABLE r(a STRING, b INT, c DOUBLE)")
        cur.execute("SELECT * FROM r") 
        #Return column info from query
        #print cur.getSchema()
        
        #Fetch table results
        for i in cur.fetch():
            print i
