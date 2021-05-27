from crud import MarksheetOperations


class TestMarksheetOperations:
    marksheet_operation = MarksheetOperations()

    def test_create_table(self):
        """

        :return: check table name exist or not
        """
        table_name = "marksheet"
        table_dict = self.marksheet_operation.create_table()
        assert table_name in table_dict.keys(), "Table not created"

    def test_insert_data(self):
        """

        :return: check if rows inserted or not
        """
        row_count = self.marksheet_operation.insert_data()
        assert row_count == 1, "Data not inserted"
