import psycopg2
import psycopg2.extras

# Client class manesta3mlouha ken bech njibou mel base 
#add tsir b class okhra ok
class Client: #Client / ClientInDb / BaseClient
    def __init__(self, firstname, lastname, balance , id = None):
        assert firstname, "first name lezem ykoun mch none" # first name is required no matter the type
        assert isinstance(lastname, str), "first name lezem ykoun int" # last name is required a string type only
        self.firstname = firstname
        self.lastname = lastname
        self.__id = id
        self.__balance = balance
        print("Welcome")

    #getter 
    @property
    def id(self):
        return self.__id

    #also getter
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__balance = amount


    def add_user_in_db(self):
        conn = psycopg2.connect(dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost")

        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("INSERT INTO clients (firstName, lastName) VALUES(%s, %s)", (self.firstname, self.lastname))
                except Exception as e:
                    print("fama mochkla jareb ba3ed")
                    print(e)
    
    def get_full_name(self):
        return self.firstname + "/" + self.lastname

    def __repr__(self) -> str:
        return self.firstname + " - " + self.lastname + " - " + (str)(self.id)
