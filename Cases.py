import sqlite3
from Investigator import Investigator
investigator=Investigator()
class Cases:

    # CLASS INITIALIZE
    def __init__(self, database='cases.db',statements=[]):
        self.database=database
        self.statements=''
        self.display = False
        self.conn = sqlite3.connect(self.database)
        self.c = self.conn.cursor()

    # TABLE CASE FUNCTIONS
    def viewCases(self):
        self.c.execute("SELECT * FROM `case`")
        data = self.c.fetchall()
        if data is not None:
            for info in data:
                print("CASE ID: " + str(info[0]))
                print("NAME: " + info[1])
                print("DATE: " + info[3])
                print("DESCRIPTION: " + info[2])
                print("**********INVESTIGATOR**********")
                investigator.viewInvestigatorByID(info[4])
                print("************EVIDENCE************")
                self.viewAllEvidenceByCaseID(info[0])
                print("--------------------------------")
        else:
            print("There is no data!")

    def viewCaseByID(self, case_id):
        self.c.execute("SELECT * FROM `case` WHERE `case_id` = "+str(case_id)+";")
        data = self.c.fetchone()
        if data is not None:
            print("CASE ID: " + str(data[0]))
            print("NAME: " + data[1])
            print("DATE: " + data[3])
            print("DESCRIPTION: " + data[2])
            print("*********INVESTIGATOR*********")
            investigator.viewInvestigatorByID(data[4])
            print("***********EVIDENCE***********")
            self.viewAllEvidenceByCaseID(data[0])
            print("--------------------------------")
            #return data
        else:
            print("Case not found!")
        self.conn.commit()

    def addCase(self, name, description, date, id_num):
        self.c.execute("INSERT INTO `case`(`name`,`description`,`date`,`id_num`)"
                       "VALUES('"+name+"','"+description+"','"+date+"','"+id_num+"')")
        self.conn.commit()

    def editCase(self, name, description, date, case_id):
        self.c.execute("UPDATE `case` SET `name`=?,`description`=?, `date`=? WHERE `case_id`=?;",
                       [name, description, date, case_id])
        self.conn.commit()

       

    # TABLE EVIDENCE FUNCTIONS
    def addEvidence(self, name, description, case_id):
        self.c.execute("INSERT INTO evidence (name,description,case_id) "
                       "VALUES('"+name+"','"+description+"','"+case_id+"')")
        self.commit()

    def viewAllEvidenceByCaseID(self,case_id):
        self.c.execute("SELECT * FROM `evidence` WHERE `case_id`=?", [case_id])
        data = self.c.fetchall()
        if data is not None:
            for info in data:
                print("\t\tNAME: " + info[1])
                print()
                print("\t\tDESCRIPTION: " + info[2])
                print("********************************")
        else:
            print("No evidence found!")

    def editEvidence(self,name, description, case_id):
        self.c.execute("UPDATE evidence SET name='"+name+"',description='"+description+"',case_id='"+case_id+"' WHERE evid_id='"+case_id+"'")
        self.conn.commit()

    # DATABASE COMMIT AND CLOSE
    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.commit()
        self.conn.close()
