from crud import MarksheetOperations


class TestMarksheetOperations:
    marksheet_operation = MarksheetOperations()

    def test_create_table(self):
        """

        :return: checks table name exist or not
        """
        table_name = "marksheet"
        table_dict = self.marksheet_operation.create_table()
        assert table_name in table_dict.keys(), "Table not created"

    def test_insert_marksheet(self):
        """

        :return: check if rows inserted or not
        """
        row_count = self.marksheet_operation.insert_marksheet()
        assert row_count == 5, "Data not inserted"

    def test_insert_activities(self):
        """

        :return: check if rows inserted or not
        """
        row_count = self.marksheet_operation.insert_activities()
        assert row_count == 4, "Data not inserted"

    def test_delete_row(self):
        """

        :return: check if row is deleted or not
        """
        value = 103
        row_count = self.marksheet_operation.delete_row(value)
        assert row_count == 4, "Row not deleted"

    def test_update_row(self):
        """

        :return: check if the row is updated or not
        """
        value = "Mr."
        row_count = self.marksheet_operation.update_row(value)
        assert row_count == 4, "Row not updated"

    def test_create_join_and_fetch_data(self):
        """

        :return: count of rows created by join
        """
        value = 90
        row_count = self.marksheet_operation.fetch_records(value)
        assert row_count == 3, "Join unsuccessful"

