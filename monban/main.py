import sys
import logging

from utils.statements import StatementReader

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class StatementAddedEventHandler(LoggingEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        else:
            logging.info(f"File created: {event.src_path}")
            self.handle_new_file(event.src_path)

    def handle_new_file(self, file_path):
        with open(file_path, "r") as file:
            data = file.read()

            logging.info(f"Processing new statement: {data}")

            statementReader = StatementReader()
            statements = statementReader.process_statement(file_path)
            for statement in statements:
                logging.info(f"Processed statement: {statement}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.info("Starting Monban...")

    path = sys.argv[1] if len(sys.argv) > 1 else "./data"

    event_handler = StatementAddedEventHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()
        logging.info("Monban stopped.")
