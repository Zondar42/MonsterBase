from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Monster import *

class baseSearch(object):
    def __init__(self, session, _table, _next = None):
        self._session = session
        self._table = _table
        self.next = _next

    def run(self):
        new_sql = "SELECT * FROM " + self._table.__tablename__ + " WHERE "
        return self.run_next(new_sql)

    def run_next(self, sql):
        new_sql = sql + self._sql
        if self.next == None:
            return self._run_final(new_sql)
        else:
            return self.next.run_next(new_sql + " AND ")

    def _run_final(self, new_sql):
        return self._session.query(self._table).from_statement(text(new_sql + ";")).all()

class intSearch(baseSearch):
    def __init__(self, session):
        pass

class stringSearch(baseSearch):
    def __init__(self, session, _table, value, field, next = None):
        self._sql = field + " == " + str(value)
        super().__init__(session, _table, next)

class floatSearch(baseSearch):
    def __init__(self, session, _table, value, field, next = None, epsilon = 0.0):
        if epsilon < 0.1:
            epsilon = 0.1
        level_lower = float(value) - float(epsilon)
        level_higher = float(value) + float(epsilon)
        self._sql = field + " > " + str(level_lower) + " AND " + field + " < " + str(level_higher)
        super().__init__(session, _table, next)

class uniqueSearch(object):
    def __init__(self, _session, _table, field):
        self._session = _session
        self._table = _table
        self._field = field

    def run(self):
        #new_sql = "SELECT DISTINCT " + self._field + " FROM " + self._table.__tablename__ + ";"
        s = select([Monster.c.CR]).where(Monster.c.CR > 20)
        return self._session.execute(s).fetchone()
        #sql_statement = "SELECT Name FROM " + self._table.__tablename__ + ";"
        #return self._session.query(self._table).from_statement(text(sql_statement)).one()
