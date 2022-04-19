import os
import sys
from pydantic import BaseSettings

class Settings(BaseSettings):
  database_hostname: str
  database_port: str
  database_password: str
  database_name: str
  database_username: str
  secret_key: str
  algorithm: str
  access_token_expire_minutes: int

  class Config:
    env_file = ".env"

settings = Settings()

parent_dir = os.path.abspath(os.path.join(os.getcwd(), "../alembic"))
sys.path.append(parent_dir)