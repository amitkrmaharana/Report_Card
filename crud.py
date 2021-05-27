import json

from config import engine, session, metadata
from logger import logger
from models import Base, Marksheet


class MarksheetOperations:

    def create_table(self):
        """

        :return: True if table created
        """
        try:
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
            return metadata.tables
        except Exception as e:
            logger.exception(e)

    def insert_data(self):
        """

        :return:
        """
        try:
            marksheet1 = Marksheet(roll_id=104, name="kajal", History=65, Maths=65, Science=82)
            session.add(marksheet1)
            session.commit()
            return session.query(Marksheet).count()
        except Exception as e:
            logger.exception(e)

    def delete_row(self, value):
        """

        :param value: value of the attribute
        :return: count of rows affected
        """
        try:
            session.query(Marksheet).filter(Marksheet.roll_id == value).delete()
            return session.query(Marksheet).count()
        except Exception as e:
            logger.exception(e)
