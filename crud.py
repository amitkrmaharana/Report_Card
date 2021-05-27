from config import engine, session
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
            return session.query(Marksheet).count()
        except Exception as e:
            logger.exception(e)

    def insert_data(self):
        """

        :return:
        """


# if __name__ == '__main__':
#     MarksheetOperations().create_table()
