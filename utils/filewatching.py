import os
import os.path as path
from datetime import datetime
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent

from typing import Callable

from utils.statements import Statement, StatementReader
from utils.csv import CSVWriter


class StatementAddedEventHandler(FileSystemEventHandler):
    def __init__(self, callback: Callable[[list[Statement]], None]):
        super().__init__()
        self.callback = callback

    def on_created(self, event: FileSystemEvent):
        if event.is_directory:
            return None
        else:
            self.handle_new_file(str(event.src_path))

    def handle_new_file(self, file_path: str):
        statementReader = StatementReader()
        statements = statementReader.process_statement(file_path)

        if not path.exists(path.join(os.getcwd(), "processed")):
            os.makedirs(path.join(os.getcwd(), "processed"))

        processed_file_path = path.join(
            os.getcwd(), "processed", str(datetime.now()) + ".csv"
        )

        logging.info(
            f"Writing {len(statements)} statements to CSV file: {processed_file_path}"
        )
        CSVWriter().write(
            [
                {
                    "account_number": statement.account_number,
                    "currency": statement.currency,
                    "transaction_date": statement.transaction_date,
                    "start_balance": statement.start_balance,
                    "end_balance": statement.end_balance,
                    "value_date": statement.value_date,
                    "amount": statement.amount,
                    "description": statement.description,
                }
                for statement in statements
            ],
            processed_file_path,
        )

        if self.callback is not None:
            self.callback(statements)


class FileWatcher:
    def __init__(self, path: str, callback: Callable[[list[Statement]], None]):
        self.path = path
        self.event_handler = StatementAddedEventHandler(callback)
        self.observer = Observer()

    def start(self):
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()
