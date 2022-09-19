# docs - https://docs.gspread.org/en/v5.4.0/user-guide.html
import gspread
import pandas as pd
import re


# Get data as list of dicts
# print(sheet.get_all_records())

# cell = sheet.find(query="15/07/1996")
# print(str(cell.row) + " | " + str(cell.col) + " | " + str(sheet.row_values(cell.row)))
# sheet.update_cell(row=cell.row, col=cell.col, value="Bingo!")
# print(str(cell.row) + " | " + str(cell.col) + " Updated")


class GSheet:
    def __init__(self) -> None:
        self._SPREADSHEET_ID: str = "1ZlGcpK2Xt-fEhLfAW5X7cfQqwcqhlBBrTvoV5oREMr0"
        self._gc = gspread.service_account(filename="credentials.json")

        self._workbook = self._gc.open_by_key(key=self._SPREADSHEET_ID)

        self._sheet = self._workbook.worksheet(title="Sheet1")

    def getWorkSheet(self):
        """Returns the Sheet1 of the workbook cofigured in init"""
        return self._sheet

    def getWorkBook(self):
        """Return the workbook of the configured spreadsheet ID in init

        Use this workbook to access different sheets of it

        """
        return self._workbook

    def getSheet(self) -> pd.DataFrame:
        sheetData = pd.DataFrame(self._sheet.get_all_records())
        return sheetData
