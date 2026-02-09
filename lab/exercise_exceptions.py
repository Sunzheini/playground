"""
Custom Exception Showcase: Creating and Using Custom Exceptions in Python
"""
# ============= STEP 1: Define Base Custom Exception =============
class PaymentProcessingError(Exception):
    """Base custom exception for payment-related errors."""

    def __init__(self, message, payment_id=None, amount=None):
        self.message = message
        self.payment_id = payment_id
        self.amount = amount
        super().__init__(self.message)

    def __str__(self):
        details = [f"payment_id={self.payment_id}"] if self.payment_id else []
        if self.amount:
            details.append(f"amount=${self.amount}")
        return f"{self.message} [{', '.join(details)}]" if details else self.message


# ============= STEP 2: Define Specific Exception Types =============
class InsufficientFundsError(PaymentProcessingError):
    """Raised when user doesn't have sufficient balance."""
    pass


class InvalidPaymentMethodError(PaymentProcessingError):
    """Raised when payment method is invalid."""
    pass


# ============= STEP 3: Simulate Payment Processing =============
def process_payment(user_balance: float, amount: float, payment_id: str, card_valid: bool = True):
    """Simulates payment processing and raises custom exceptions."""

    if not card_valid:
        raise InvalidPaymentMethodError(
            "Card has expired",
            payment_id=payment_id,
            amount=amount
        )

    if user_balance < amount:
        raise InsufficientFundsError(
            f"Balance ${user_balance} is less than required ${amount}",
            payment_id=payment_id,
            amount=amount
        )

    return {"success": True, "new_balance": user_balance - amount}


# ============= STEP 4: Use Custom Exceptions with Proper Handling =============
def handle_payment(user_balance: float, amount: float, payment_id: str, card_valid: bool = True):
    """Demonstrates exception handling with custom exceptions."""

    try:
        result = process_payment(user_balance, amount, payment_id, card_valid)
        print(f"✓ Payment successful! New balance: ${result['new_balance']:.2f}")
        return result

    except InsufficientFundsError as e:
        print(f"✗ Insufficient Funds: {e}")
        return {"success": False, "error": "INSUFFICIENT_FUNDS"}

    except InvalidPaymentMethodError as e:
        print(f"✗ Invalid Payment: {e}")
        return {"success": False, "error": "INVALID_PAYMENT_METHOD"}

    except PaymentProcessingError as e:
        print(f"✗ Payment Error: {e}")
        return {"success": False, "error": "PROCESSING_ERROR"}


# ============= DEMONSTRATION =============
if __name__ == "__main__":
    print("=" * 60)
    print("Custom Exception Demonstration")
    print("=" * 60)

    # Scenario 1: Successful payment
    print("\n[Scenario 1] Successful Payment:")
    handle_payment(user_balance=100.0, amount=25.0, payment_id="PAY001")

    # Scenario 2: Insufficient funds
    print("\n[Scenario 2] Insufficient Funds:")
    handle_payment(user_balance=10.0, amount=50.0, payment_id="PAY002")

    # Scenario 3: Invalid payment method
    print("\n[Scenario 3] Invalid Payment Method:")
    handle_payment(user_balance=100.0, amount=25.0, payment_id="PAY003", card_valid=False)

    print("\n" + "=" * 60)
