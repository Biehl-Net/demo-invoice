# John Biehl
# 20 November 2023

# Import the datetime and uuid modules
import datetime # https://docs.python.org/3/library/datetime.html (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
import uuid # https://docs.python.org/3/library/uuid.html (https://docs.python.org/3/library/uuid.html#uuid.uuid4)

# Define the Customer class
class Customer:
    def __init__(self, name, address, phone, email):
        self._name = name
        self._address = address
        self._phone = phone
        self._email = email

    # Method to collect customer information from user input
    def collect_customer_info(self):
        self._name = input("Enter customer name: ")
        while not self._name:
            print("Name cannot be empty.")
            self._name = input("Enter customer name: ")

        self._address = input("Enter customer address: ")
        while not self._address:
            print("Address cannot be empty.")
            self._address = input("Enter customer address: ")

        self._phone = input("Enter customer phone number: ")
        while not self._phone:
            print("Phone number cannot be empty.")
            self._phone = input("Enter customer phone number: ")

        self._email = input("Enter customer email address: ")
        while not self._email:
            print("Email address cannot be empty.")
            self._email = input("Enter customer email address: ")

    # Method to display customer information
    def display_customer(self):
        print("Customer Name: ", self._name)
        print("Customer Address: ", self._address)
        print("Customer Phone: ", self._phone)
        print("Customer Email: ", self._email)

# Define the Pet class, which inherits from the Customer class
class Pet(Customer):
    def __init__(self, name, address, phone, email, pet_name, pet_type, pet_age):
        super().__init__(name, address, phone, email)
        self._pet_name = pet_name
        self._pet_type = pet_type
        self._pet_age = pet_age

    # Method to collect pet information from user input
    def collect_pet_info(self):
        self._pet_name = input("Enter pet name: ")
        while not self._pet_name:
            print("Name cannot be empty.")
            self._pet_name = input("Enter pet name: ")

        self._pet_type = input("Enter pet type: ")
        while not self._pet_type:
            print("Type cannot be empty.")
            self._pet_type = input("Enter pet type: ")

        self._pet_age = input("Enter pet age: ")
        while not self._pet_age:
            print("Age cannot be empty.")
            self._pet_age = input("Enter pet age: ")

    # Method to display pet information
    def display_pet(self):
        print("Pet Name: ", self._pet_name)
        print("Pet Type: ", self._pet_type)
        print("Pet Age: ", self._pet_age)

# Define the Invoice class, which inherits from the Pet class
class Invoice(Pet):
    SALES_TAX_RATE = 0.0975

    def __init__(self, name, address, phone, email, pet_name, pet_type, pet_age, services):
        super().__init__(name, address, phone, email, pet_name, pet_type, pet_age)
        self._invoice_number = str(uuid.uuid4().fields[-1])[:6]
        self._invoice_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self._services = services
        self._subtotal = sum(service["price"] for service in services)

    # Method to display the invoice
    def display_invoice(self):
        self.display_customer()
        self.display_pet()
        print("Invoice Number: ", self._invoice_number)
        print("Invoice Date: ", self._invoice_date)
        Service.display_services()  # Call the display_services() method from the Service class
        print("Subtotal: $", format(self._subtotal, ".2f"))
        sales_tax = self._subtotal * self.SALES_TAX_RATE
        print("Sales Tax (", self.SALES_TAX_RATE * 100, "%): $", format(sales_tax, ".2f"))
        total = self._subtotal + sales_tax
        print("Total: $", format(total, ".2f"))

# Define the Service class
class Service:
    services = [] # Class variable to store services and prices in order to calculate subtotal

    @staticmethod
    def service_menu():
        print("Merlin's Pet Grooming Service Menu")
        print("1. Bathing")
        print("2. Haircut")
        print("3. Nail trim")
        print("4: Exit")
        while True:
            try:
                service = int(input("Enter service number: "))
                if service == 4:
                    return None
                elif 1 <= service <= 3:
                    return service
                else:
                    print("Invalid service number. Please enter a valid service number.")
            except ValueError:
                print("Invalid input. Please enter a valid service number.")

    @staticmethod
    def get_service_name(service_number):
        if service_number == 1:
            return "Bathing"
        elif service_number == 2:
            return "Haircut"
        elif service_number == 3:
            return "Nail trim"

    @staticmethod
    def collect_services():
        service = Service.service_menu()
        while service is not None:
            if service == 4:
                break
            price = None
            while price is None or price <= 0:
                try:
                    price = float(input("Enter price for service: "))
                    if price <= 0:
                        print("Price must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid price.")
            Service.services.append({"name": Service.get_service_name(service), "price": price})
            service = Service.service_menu()

    @staticmethod
    def display_services():
        print("Services:")
        for service in Service.services:
            service_name = service["name"]
            price = service["price"]
            print("- ", service_name, "($", format(price, ".2f"), ")")

# Main function to run the program
def main():
    # Create a Customer object and collect customer information
    customer = Customer("", "", "", "")
    customer.collect_customer_info()

    # Create a Pet object and collect pet information
    pet = Pet(customer._name, customer._address, customer._phone, customer._email, "", "", "")
    pet.collect_pet_info()

    # Collect services from the user
    Service.collect_services()

    # Create an Invoice object and display the invoice
    invoice = Invoice(customer._name, customer._address, customer._phone, customer._email, pet._pet_name, pet._pet_type, pet._pet_age, Service.services)
    invoice.display_invoice()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
