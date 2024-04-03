from pydantic import BaseModel, Field, field_validator
from pydantic_extra_types.payment import PaymentCardBrand, PaymentCardNumber
from datetime import date


class CardInfo(BaseModel):
    name_on_card: str = Field(
        title="Name on Card",
        description="Name on the card",
        examples=["Seyi Oyewunmi"],
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z\s]+$",
    )
    card_no: PaymentCardNumber = Field(
        title="Card Number",
        description="Card number",
        examples=["1234567890123456"],
        min_length=16,
        max_length=16,
    )
    cvv: str = Field(
        title="CVV", description="CVV", examples=["123"], min_length=3, max_length=4
    )
    expiry_date: str = Field(
        title="Expiry Date",
        description="Expiry date of the card",
        examples=["11/24"],
        pattern="^[0-9]{2}/[0-9]{2}$",
    )

    @field_validator("card_no")
    def validate_card_brand(cls, value):
        """
        A function to validate the card brand being Visa, MasterCard, Verve, or Amex.
        
        Parameters:
            cls: The class object.
            value: The value to be validated.
        
        Returns:
            The validated value.
        """
        if value.brand not in [PaymentCardBrand.visa, PaymentCardBrand.mastercard, PaymentCardBrand.amex]:
            raise ValueError("Only Visa, MasterCard or ame cards are accepted")
        return value

    @field_validator("expiry_date")
    def validate_expiry_date(cls, value):
        """
        A function to validate the expiry date of a card.

        Parameters:
            cls: The class reference.
            value: The expiry date value to be validated.

        Returns:
            The validated expiry date value.
        """
        mm, yy = value.split("/")
        expiration_date = date(int("20" + yy), int(mm), 1)
        current_date = date.today()
        if expiration_date < current_date:
            raise ValueError("Card has expired")
        return value

    @field_validator("cvv")
    def validate_cvv(cls, value):
        """
        A field validator for the 'cvv' field. Validates that the input value is numeric and raises a ValueError if it's not. 
        Parameters:
            cls: The class object
            value: The value to be validated
        Returns:
            The validated value
        """
        if not value.isnumeric():
            raise ValueError("CVV must be numeric")
        return value


class PaymentModel(BaseModel):
    amount: float = Field(
        title="Amount", description="Amount to be paid", examples=[1000.00], gt=0
    )
    card: CardInfo
