from __future__ import annotations

class CinemaBar:

    @staticmethod
    def sell_product(customer, product) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
