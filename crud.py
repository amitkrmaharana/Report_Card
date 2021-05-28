import json

from sqlalchemy.orm import relationship

from config import engine, session, metadata
from logger import logger
from models import Base, Marksheet, Activities


class MarksheetOperations:

    def create_table(self):
        """
        Creating tables provided in models.py and handling relationships
        :return: dictionary of table names and its fields
        """
        try:
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
            return metadata.tables
        except Exception as e:
            logger.exception(e)

    def insert_marksheet(self):
        """

        :return: number of rows inserted
        """
        try:
            with open('marksheet.json') as f:
                table_list = []
                data = f.read()
                jsondata = json.loads(data)
                for values in jsondata:
                    rows = Marksheet(roll_id=values['roll_id'], name=values['name'], History=values['History'], Maths=values['Maths'], Science=values['Science'])
                    table_list.append(rows)
            session.add_all(table_list)
            session.commit()
            return session.query(Marksheet).count()
        except Exception as e:
            logger.exception(e)

    def insert_activities(self):
        """

                :return: number of rows inserted
                """
        try:
            with open('activity.json') as f:
                table_list = []
                data = f.read()
                jsondata = json.loads(data)
                for values in jsondata:
                    rows = Activities(activity_id=values['activity_id'], roll_id=values['roll_id'], sports=values['sports'])
                    table_list.append(rows)
            session.add_all(table_list)
            session.commit()
            return session.query(Activities).count()
        except Exception as e:
            logger.exception(e)

    def delete_row(self, value):
        """

        :param value: value of the attribute
        :return: count of rows after deletion
        """
        try:
            print(value)
            result = session.query(Marksheet).filter(Marksheet.roll_id == value).first()
            print(result)
            session.delete(result)
            # result.delete()
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

    def fetch_records(self, value):
        """
        joined two tables marksheet and activities filtering students whose maths marks are greater than value given
        :param value: value to be referenced
        :return: length of the new table formed
        """
        try:
            try_list = []
            activity = session.query(Marksheet).join(Activities).filter(Marksheet.Maths > value).all()
            for marksheet in activity:
                for activities in marksheet.activity:
                    try_list.append(marksheet.name + "," + activities.sports)
            return len(try_list)
        except Exception as e:
            logger.exception(e)


# if __name__ == '__main__':
#     MarksheetOperations().fetch_records(90)
