import os
import toml
from typing import Any, Dict


def get_config(file_name: str) -> Dict[str, Any]:
    """
    Loads a configuration file and returns its content as a dictionary.

    Parameters
    ----------
    file_name : str
        The name of the configuration file to load.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the loaded configuration data.
    """
    config_path = os.path.join(os.path.dirname(__file__), "../config", file_name)
    return toml.load(config_path)
