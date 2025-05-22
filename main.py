import logging

from utils.filewatching import FileWatcher
from utils.statements import Statement

from utils.budget import (
    do_planned_budget_check,
    do_budget_checks,
    do_budget_prognosis_check,
)


def statements_loaded(statements: list[Statement]):
    """
    Callback function to be called when statements are loaded.
    """
    logging.info(f"Loaded {len(statements)} statements.")

    # First off we need to categorize the statements per payout period (month from 24th to 24th) and spending category
    # TODO: Implement categorization logic

    # Then we need to check if the statements are in the planned budget
    do_budget_checks()

    # Then we need to check if the statements are in the budged prognosis
    do_budget_prognosis_check()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Do preprocessing here
    do_planned_budget_check()

    # Start the file watcher
    watcher = FileWatcher(path="./data", callback=statements_loaded)
    watcher.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        watcher.stop()

    logging.info("CHISATO says sayonara.")
