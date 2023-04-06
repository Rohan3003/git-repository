from dataclasses import dataclass
from datetime import datetime

@dataclass
class Customer:
    name : str
    phone : str
    cc_number : str
    cc_exp_month : int
    cc_exp_year : int
    cc_valid : bool = False

#def validate_card(customer: Customer) -> bool:


type(Customer)