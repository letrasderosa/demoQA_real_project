import faker

fake = faker.Faker()

class PersonData:
    def __init__(self):
        self.fname = fake.name() # 'richard smith'   #
        self.femail =  fake.email()   #'richardsmith@example.com'   #
        self.fphone_number = fake.phone_number()
        self.faddress = fake.address()   #'Unit 0987 Box 5884DPO AA 93248'   #
        self.faddress2 =   fake.address()   # 'Unit 0987 Box 5884DPO AA 93248'
        self.fcity = fake.city()
        self.fstate = fake.state()
        self.fzipcode = fake.zipcode()
        self.fcountry = fake.country()
        self.fcompany = fake.company()
        self.fjob = fake.job()
        self.fssn = fake.ssn()
        self.fcredit_card = fake.credit_card_number()

# personData = PersonData()
# print(person.address)