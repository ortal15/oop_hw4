class BankAccount:
    __bank_address = "1 Allenby St, Tel Aviv"

    def __init__(self, owner: str, balance: float):
        self.__owner = owner
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @classmethod
    def get_bank_address(cls) -> str:
        return cls.__bank_address

    @staticmethod
    def highest_balance(acc1: "BankAccount", acc2: "BankAccount", acc3: "BankAccount") -> float:
        return max(acc1.balance, acc2.balance, acc3.balance)

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        self.__balance -= amount

    def is_rich(self) -> bool:
        return self.__balance > 1_000_000

    def __add__(self, other):
        if isinstance(other, BankAccount):
            if self.owner == other.owner:
                return BankAccount(self.owner, self.balance + other.balance)
            else:
                return f"Joint: {self.owner} & {other.owner}"
        elif isinstance(other, (int, float)):
            return BankAccount(self.owner, self.balance + other)

    def __sub__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(self.owner, self.balance - other.balance)
        elif isinstance(other, (int, float)):
            return BankAccount(self.owner, self.balance - other)

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.owner == other.owner and self.balance == other.balance
        elif isinstance(other, (int, float)):
            return self.balance == other
        elif isinstance(other, tuple) and len(other) == 2:
            return (self.owner, self.balance) == other
        return False

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return round(self.balance)

    def __getitem__(self, key):
        if key == 'owner' or key == 0:
            return self.owner
        elif key == 'balance' or key == 1:
            return self.balance
        else:
            raise KeyError("Invalid key")

    def __iter__(self):
        yield self.owner
        yield self.balance

    def freeze(self) -> None:
        self.__owner = "FROZEN"
        self.__balance = 0.0


# --- Demo Code for BankAccount class ---

# Create accounts
acc1 = BankAccount("Alice", 800.0)
acc2 = BankAccount("Bob", 1200.0)
acc3 = BankAccount("Alice", 800.0)
acc4 = BankAccount("Charlie", 300.0)

# Test __repr__ / __str__
print("Accounts:")
print(acc1)
print(acc2)
print(acc3)

# Test __eq__ (same owner and balance)
print("\nEquality:")
print("acc1 == acc3:", acc1 == acc3)  # True
print("acc1 == acc2:", acc1 == acc2)  # False
print("acc1 == 800:", acc1 == 800)  # True
print("acc1 == ('Alice', 800):", acc1 == ("Alice", 800))  # True

# Test __ne__
print("\nInequality:")
print("acc1 != acc2:", acc1 != acc2)  # True

# Test __gt__ (based on balance)
print("\nGreater Than:")
print("acc2 > acc1:", acc2 > acc1)  # True
print("acc4 > acc1:", acc4 > acc1)  # False

# Test __lt__, __ge__, __le__
print("\nOther comparisons:")
print("acc1 < acc2:", acc1 < acc2)  # True
print("acc2 >= acc1:", acc2 >= acc1)  # True
print("acc4 <= acc1:", acc4 <= acc1)  # True

# Test __add__ (same owner)
print("\nAdd:")
acc5 = acc1 + acc3
print("acc5 (Alice + Alice):", acc5)

# Test __add__ (different owners)
acc6 = acc1 + acc2
print("acc6 (Alice + Bob):", acc6)

# Test __add__ with number
acc7 = acc1 + 200
print("acc1 + 200:", acc7)

# Test __sub__ with another account
acc8 = acc2 - acc1
print("acc2 - acc1:", acc8)

# Test __sub__ with number
acc9 = acc2 - 500
print("acc2 - 500:", acc9)

# Test __getitem__
print("\nGet item:")
print("acc1['owner']:", acc1['owner'])
print("acc1[1]:", acc1[1])  # balance

# Test __iter__
print("\nIterating acc1:")
for info in acc1:
    print(info)

# Test __len__
print("\nLength of acc1:", len(acc1))

# Test class method
print("\nBank address:", BankAccount.get_bank_address())

# Test static method
print("\nHighest balance:", BankAccount.highest_balance(acc1, acc2, acc4))
