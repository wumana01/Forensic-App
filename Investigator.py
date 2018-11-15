import sqlite3
class Investigator:

    # CLASS INITIALIZE
    def __init__(self, database='cases.db',statements=[]):
        self.database=database
        self.statements=''
        self.display = False
        self.conn = sqlite3.connect(self.database)
        self.c = self.conn.cursor()
         # TABLE INVESTIGATOR FUNCTIONS
    def viewInvestigators(self):
        self.c.execute("SELECT * FROM investigator")
        data = self.c.fetchall()
        for info in data:
            print("ID: " + str(info[1]))
            print("NAME: " + info[2])
            print("RANK: " + str(info[3]))
            print("AGENCY: " + str(info[4]))
            print("PRECINCT: " + str(info[5]))



    def viewInvestigatorByID(self, id_num):
        self.c.execute("SELECT * FROM investigator WHERE id_num=?", [id_num])
        data = self.c.fetchone()
        if data is not None:
            print("ID: " + str(data[1]))
            print("NAME: " + data[2])
            print("RANK: " + data[3])
            print("AGENCY: " + data[4])
            print("PRECINCT: " + data[5])
            #return data
        else:
            print("Investigator not found!")
            return None

    def addInvestigator(self, id_num, name, rank, agency, precinct):
        self.c.execute("INSERT INTO investigator (id_num,name,rank,agency,precinct) "
                       "VALUES('"+id_num+"','"+name+"','"+rank+"','"+agency+"','"+precinct+"')")
        self.conn.commit()

    def editInvestigator(self, id_num, name, rank, agency, precinct):
        self.c.execute("UPDATE investigator SET name='"+name+"',rank='"+rank+"',agency='"+agency+"',precinct='"+precinct+"' WHERE id_num='"+id_num+"'")
        self.conn.commit()
  
        #self.c.execute("ALTER TABLE investigator ADD COLUMN case_id interger")
    
