from site_builder.formatter.pvme_settings import github_json_request


class CCSpreadsheetData(dict):
    """CC Spreadsheet LUT:
    {
        'HallOfFame': {
            'A': ['10', '20', '30'],
            'B': ['30', '-1', '20,3']
        },
        'TTLeaderboard': {...}
    }
    """
    def __init__(self, url="https://raw.githubusercontent.com/Clue-Chasers/cc-settings/settings/cc-spreadsheet/cc_spreadsheet.json"):
        super().__init__(github_json_request(url))

    def cell_data(self, worksheet: str, col: str, row: int) -> str:
        rows = self.get(worksheet, {}).get(col, [])
        return rows[row] if row < len(rows) else 'N/A'


if __name__ == '__main__':
    CCSpreadsheetData()