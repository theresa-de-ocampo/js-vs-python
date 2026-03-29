# https://dev.to/izabelakowal/some-ideas-on-how-to-implement-dtos-in-python-be3

# Data Transfer Objects are simply data structures typically used to
# pass data between application layers and services.

# DTO = meant for operations and data transferring
# Database Models = meant for data persistence (e.g., Prisma Model)

from dataclasses import dataclass


@dataclass(frozen=True)
class RuleEngine:
    allowed_products: tuple[str, ...]
    min_height: float
    max_height: float


foo = RuleEngine(
    allowed_products=("Oil", "Water", "Gasoline"), min_height=30, max_height=100
)

print(foo)

bar = RuleEngine(
    allowed_products=("Oil", "Water", "Gasoline"), min_height=30, max_height=100
)

print(foo == bar)
