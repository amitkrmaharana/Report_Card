import json

from config import engine, session, metadata
from logger import logger
from models import Base, Marksheet


class MarksheetOperations:

    def create_table(self):
        """

        :return: dictionary of table names and its fields
        """
        try:
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
            return metadata.tables
        except Exception as e:
            logger.exception(e)

    def insert_data(self):
        """

        :return: number of rows inserted
        """
        try:
            with open('marksheet.json') as f:
                table_list = []
                data = f.read()
                jsondata = json.loads(data)
                for values in jsondata:
                    print(values['name'])
                    rows = Marksheet(roll_id=values['roll_id'], name=values['name'], History=values['History'], Maths=values['Maths'], Science=values['Science'])
                    table_list.append(rows)
            session.add_all(table_list)
            session.commit()
            return session.query(Marksheet).count()
        except Exception as e:
            logger.exception(e)

    def delete_row(self, value):
        """

        :param value: value of the attribute
        :return: count of rows after deletion
        """
        try:
            session.query(Marksheet).filter(Marksheet.roll_id == value).delete()
            session.commit()
            return session.query(Marksheet).count()
        except Exception as e:
            logger.exception(e)

    def update_row(self, value):
        """

        :param value: value to be inserted to update
        :return: count of rows after update
        """
        try:
            session.query(Marksheet).filter(Marksheet.roll_id != 104).update(
                {Marksheet.name: value + " " + Marksheet.name}, synchronize_session=False)
            session.commit()
            return session.query(Marksheet).count()
        except Exception as e:
            logger.exception(e)


# if __name__ == '__main__':
#     MarksheetOperations().create_table()
