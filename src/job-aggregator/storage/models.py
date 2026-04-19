from dataclasses import dataclass

@dataclass
class Job:
    timestamp: str
    title: str
    company_name: str
    headquarters: str
    post_date: str
    categories: str
    offer_url: str

