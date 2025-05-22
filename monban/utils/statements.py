# A statement is a record of financial transactions. It is a tab separated file
# that contains the following columns:
# 1. Account Number
# 2. Currency MutationCode in ISO 4217 format (e.g. USD, EUR)
# 3. Transaction Date in YYYYMMDD
# 4. Start balance
# 5. End balance
# 6. Value date in YYYYMMDD
# 7. Amount
# 8. Description, string


class StatementReader:
    """
    StatementReader is a class for reading and parsing bank statement files.

    Methods
    -------
    process_statement(file_path):
        Reads a statement file at the given file_path, parses each non-empty line,
        and returns a list of statement dictionaries. Each line is expected to be
        tab-separated with 8 fields.

    parse_statement(line):
        Parses a single line from the statement file, splitting it into 8 fields:
        account_number, currency, transaction_date, start_balance, end_balance,
        value_date, amount, and description. Raises ValueError if the line does not
        contain exactly 8 tab-separated fields.
    """

    def __init__(self):
        self.statements = []

    def process_statement(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    statement = self.parse_statement(line)
                    self.statements.append(statement)
        return self.statements

    def parse_statement(self, line):
        parts = line.strip().split("\t")
        if len(parts) != 8:
            raise ValueError(f"Invalid statement format: {line}")

        start_balance_str = parts[3].replace(",", ".")
        end_balance_str = parts[4].replace(",", ".")
        amount_str = parts[6].replace(",", ".")

        return {
            "account_number": parts[0],
            "currency": parts[1],
            "transaction_date": parts[2],
            "start_balance": float(start_balance_str),
            "end_balance": float(end_balance_str),
            "value_date": parts[5],
            "amount": float(amount_str),
            "description": parts[7],
        }
