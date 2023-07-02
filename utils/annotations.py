from typing import Protocol

# Protocols
class Strable(Protocol):
    def __str__(self) -> str: ...
