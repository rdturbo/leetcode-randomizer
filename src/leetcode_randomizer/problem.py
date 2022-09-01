from dataclasses import dataclass
from datetime import datetime
from dateutil import parser


@dataclass
class Problem:
    prob_id: int
    name: str
    diffculty: str
    times: int
    patterns: list[str]
    last_date: datetime

    @staticmethod
    def decode_data(json_data: dict) -> "Problem":
        for page in json_data["results"]:
            prob_id = int(page["properties"]["No."]["number"])
            prob_name = page["properties"]["Problem"]["title"][0]["plain_text"]
            prob_attempts = int(page["properties"]["Times"]["number"])
            prob_diff = page["properties"]["Level"]["select"]["name"]
            prob_date = parser.parse(page["last_edited_time"]).date()
            prob_patterns = Problem.get_patterns(
                page["properties"]["Data Structures"]["multi_select"]
            )

        return Problem(
            prob_id=prob_id,
            name=prob_name,
            diffculty=prob_diff,
            times=prob_attempts,
            last_date=prob_date,
            patterns=prob_patterns,
        )

    @staticmethod
    def get_patterns(multi_select: list) -> list[str]:
        return [pattern["name"] for pattern in multi_select]
