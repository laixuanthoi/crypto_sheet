import xlwings as xw



def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    # sheet["A1"].value


if __name__ == "__main__":
    xw.Book("token_analytics.xlsm").set_mock_caller()
    main()
