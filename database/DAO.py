from database.DB_connect import DBConnect
from model.confine import Confine
from model.nazione import Nazione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNazioni(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select c.StateAbb, c.CCode, c.StateNme 
                    from contiguity co, country c 
                    where co.`year` <= %s and co.state1no = c.CCode 
                    group by co.state1no 
                    order by c.StateAbb """
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Nazione(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConfiniAnno(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from contiguity c 
                    where c.`year` <= %s and c.conttype = 1"""
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Confine(**row))
        cursor.close()
        conn.close()
        return result