from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from logger import logger

Base = declarative_base()


class Marksheet(Base):
    """
     Marksheet of students
    """
    try:
        __tablename__ = 'marksheet'  # Name of the table
        roll_id = Column(Integer, primary_key=True, unique=True)  # primary Key attribute
        name = Column(String)
        History = Column(Integer)
        Maths = Column(Integer)
        Science = Column(Integer)
    except Exception as e:
        logger.exception(e)

    def __repr__(self):
        return "<ReportCard(roll_id='{}', name='{}', history='{}, maths='{}', science='{}')>" \
            .format(self.roll_id, self.name, self.History, self.Maths, self.Science)




