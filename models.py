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
        activity = relationship("Activities", back_populates="marksheets")
    except Exception as e:
        logger.exception(e)

    def __repr__(self):
        return "<ReportCard(roll_id='{}', name='{}', history='{}, maths='{}', science='{}')>" \
            .format(self.roll_id, self.name, self.History, self.Maths, self.Science)


class Activities(Base):
    """
    Activities of students
    """
    try:
        __tablename__ = 'activities'
        activity_id = Column(Integer, primary_key=True)
        roll_id = Column(Integer, ForeignKey('marksheet.roll_id'))  # {, ondelete="CASCADE"} can be used to cascade inside ForeignKey
        sports = Column(String)
        marksheets = relationship("Marksheet", back_populates="activity",order_by=Marksheet.roll_id)
    except Exception as e:
        logger.exception(e)

    def __repr__(self):
        return "Activities(activity_id='{}', roll_id='{}', sports='{}')>"\
            .format((self.activity_id, self.roll_id, self.sports))
