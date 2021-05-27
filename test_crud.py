from crud import MarksheetOperations


class TestMarksheetOperations:
    marksheet_operation = MarksheetOperations()

    def test_create_table(self):
        """

        :return:
        """
        row_count = self.marksheet_operation.create_table()
        assert row_count == 0, "Table not created"
