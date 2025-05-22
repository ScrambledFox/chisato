import csv
from typing import Collection


class CSVWriter:
    from typing import List, Dict, Any

    def write(
        self,
        data: list[dict[str, Any]],
        new_file_path: str,
        headers: Collection[str] | None = None,
    ):
        """
        Write data to a CSV file.

        Parameters
        ----------
        data : list of dict
            The data to write to the CSV file.
        headers : list of str, optional
            The headers for the CSV file. If not provided, the keys of the first
            dictionary in data will be used.
        """
        fieldnames: list[str] = (
            list(headers) if headers is not None else list(map(str, data[0].keys()))
        )
        with open(new_file_path, "w", newline="") as csvfile:
            fieldnames = list(headers) if headers is not None else list(data[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
