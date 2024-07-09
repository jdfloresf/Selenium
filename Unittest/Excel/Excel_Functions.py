import openpyxl

class ExcelFunctios:

    def __init__(self, driver):
        self.driver = driver

    def getRowCount(self, path, sheet_name):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook[sheet_name]
        return sheet.max_row
    
    def getColumnCount(file, sheet_name):
        workbook = openpyxl.load_workbook(file)
        sheet = workbook[sheet_name]
        return sheet.max_column
    
    def readData(self, path, sheet_name, row, column):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook[sheet_name]
        return sheet.cell(row=row, column=column).value
    
    def writeData(self, path, sheet_name, row, column, data):
        workbook = openpyxl.load_workbook(path)
        sheet = workbook[sheet_name]
        sheet.cell(row=row, column=column).value = data
        workbook.save(path)
