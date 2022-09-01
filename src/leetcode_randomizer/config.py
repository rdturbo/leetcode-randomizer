from dataclasses import dataclass
from dotenv import load_dotenv
import os


@dataclass
class Settings:
    db_id: str
    api_key: str


load_dotenv()

settings = Settings(
    db_id=os.getenv("NOTION_DB_ID"), api_key=os.getenv("NOTION_API_KEY")
)
