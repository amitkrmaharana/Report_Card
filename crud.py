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

