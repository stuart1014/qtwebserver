from nsnqtlib.db.mongodb import MongoDB
import datetime as dt
from nsnqtlib.config import DB_SERVER,DB_PORT,USER,PWD,AUTHDBNAME

class dbdata():
    def __init__(self):
        self.m = MongoDB(DB_SERVER,DB_PORT,USER,PWD,AUTHDBNAME)
        self.formatlist = ["date","volume","close","high","low","open","pre_close"]
        return

    def dbserver(self):
        return DB_SERVER

    def _getdata(self,trade_date=dt.datetime.today(),collection="000923.SZ",
                 db="ml_security_table",\
                 out=[],isfilt=True,filt={}):
        if not out:out = self.formatlist
        if isfilt and not filt: filt =  \
            {"date":{"$gt": trade_date, "$lt": trade_date+dt.timedelta(days=1)}}
        query = self.m.read_data(db,collection,filt=filt)
        return self.formatquery(query,out)

    def formatquery(self,query,out):
        '''
        query:your source data ,should be a list with dict
        out:the fields you want to convert into dataframe 
        '''
        if not out:
            query = [i for i in query.sort("policy", 1)]
        else:
            query = [{k:i[k] for k in out} for i in query.sort("policy", 1)]
        return query

