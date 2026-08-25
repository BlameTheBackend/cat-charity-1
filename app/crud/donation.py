from app.crud.investable import CRUDInvestable
from app.models import Donation


class DonationCRUD(CRUDInvestable):
    pass


donation_crud = DonationCRUD(Donation)
