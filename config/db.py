# mysql://uxda84jyihh60vb9:Q76TWKdshSHgFmt9CDUP@btu2b5sbpoat5f5nhoeg-mysql.services.clever-cloud.com:3306/btu2b5sbpoat5f5nhoeg

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
# engine = create_engine("mysql+pymysql://uxda84jyihh60vb9:Q76TWKdshSHgFmt9CDUP@btu2b5sbpoat5f5nhoeg-mysql.services.clever-cloud.com:3306/btu2b5sbpoat5f5nhoeg")
engine = create_engine("mysql+pymysql://root:Saurabh.10@accounterp.cb67gu1lvxk6.us-west-2.rds.amazonaws.com:3306/accountERP")
meta = MetaData()
conn = engine.connect()
Base = declarative_base()
