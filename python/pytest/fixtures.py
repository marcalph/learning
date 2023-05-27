import pytest
from dataclasses import dataclass
import os
# using
from funcs import send_email, commit_order

@dataclass
class Customer:
    first_name: str
    last_name: str
    email: str | None = None



@dataclass
class Transaction:
    transaction_id: str
    customer: Customer | None = None
    sale: str | None = None





# normal fixture
@pytest.fixture
def customer():
    customer = Customer(first_name="Cosmo", last_name="Kramer")
    return customer


def test_customer_sale(customer):
    assert customer.first_name == "Cosmo"
    assert customer.last_name == "Kramer"
    assert isinstance(customer, Customer)


# fixture factory allows fixture w/ argument rather than paramnetrize
@pytest.fixture(params=["Cosmo", "Alice", "Bob"])
def make_customer(request):
    def make(
        first_name: str = request.param,
        last_name: str = "Kramer",
        email: str = "test@example.com",
        **rest
    ):
        customer = Customer(
            first_name=first_name, last_name=last_name, email=email, **rest
        )
        return customer

    return make


@pytest.fixture
def make_transaction(make_customer):
    def make(transaction_id, customer=None, sale=None):

        if customer is None:
            customer = make_customer()

        transaction = Transaction(
            transaction_id=transaction_id,
            customer=customer,
            sale=sale,
        )

        return transaction

    return make


def test_customer(make_customer):
    customer_1 = make_customer(first_name="Elaine", last_name="Benes")
    assert customer_1.first_name == "Elaine"
    customer_2 = make_customer()
    assert customer_2.first_name == "Cosmo"


# two way data binding (changes to model changes view and vice versa)
@pytest.fixture
def mock_send_email(monkeypatch):
    sent_emails = [1]

    def _send_email(recipient='test@example.com', subject='test subject', body='test body'):
        sent_emails.append((recipient, subject, body))
        print(sent_emails)
        return True
    sent_emails.pop()
    monkeypatch.setattr('funcs.send_email', _send_email)
    return sent_emails


def test_send_email(make_transaction, mock_send_email):

    assert mock_send_email == []
    transaction = make_transaction(transaction_id="1234")

    # Commit an order, which in turn sends a receipt via email with
    # `send_email` to the customer.
    commit_order(transaction=transaction)

    assert mock_send_email == [
        (
            "test@example.com",
            "Your order number 1234",
            "Thank you for buying...",
        )
    ]



# @pytest.fixture
# def make_db_connection(request):
#     def make(host: str = "localhost", port: int = 1234):
#         connection = create_database_connection(host=host, port=port)
#         connection.open()

#         def cleanup():
#             connection.close()

#         request.addfinalizer(cleanup)
#         return connection

#     return make

@pytest.fixture(autouse=True)
def make_db_connection():
    def cleanup():
        print("close connection")

    def make(host: str = "localhost", port: int = 1234):
        print("weird setup of factory fixture")
        print("open connection")
        # request.addfinalizer(cleanup)
        return f"connection to {host}:{port}"

    yield make
    cleanup()

def test_co(make_db_connection):
    con = make_db_connection(host="home")
    print(con)
    assert True

# @pytest.fixture
# def make_db_connection(request):
#     def make(host: str = "localhost", port: int = 1234):
#         connection = create_database_connection(host=host, port=port)
#         connection.open()

#         def cleanup():
#             connection.close()

#         request.addfinalizer(cleanup)
#         return connection

#     return make


