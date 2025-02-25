from faker import Faker

class FakeCustomerGenerator:
    def __init__(self):
        self.fake = Faker()

    def fake_name(self) -> str:
        return self.fake.name()
