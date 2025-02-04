from dataclasses import dataclass

@dataclass
class MissedCallAlert:
    caller_number: str
    call_time: str
    secondary_phone_number: str