"""
General  configuration settings
"""

from abc import ABC
from pydantic import BaseSettings

class BaseConfig(BaseSettings,ABC,env_file=".env"):
    """
    """

class DBSettings(BaseConfig):
    db_url: str = ''

