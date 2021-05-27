from crud import MarksheetOperations


class TestMarksheetOperations:
    marksheet_operation = MarksheetOperations()

    def test_create_table(self):
        """

        :return:
        """
        table_name = "marksheet"
        table_dict = self.marksheet_operation.create_table()
        assert table_name in table_dict.keys(), "Table not created"
