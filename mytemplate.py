from luna import (
    Template,
    Parameter,
    Variable,
    Role,
    clause,
    Event,
    Every
)
from decimal import Decimal
from luna.functions import simple_transfer, BalanceSheetUnit
#from luna.financial import BalanceSheetUnit

print("Testing luna...")


# print(Decimal(50))
# A new template must derive from the Template class and implement clauses.
class MyTemplate(Template):
    amount = Parameter(type_=Decimal)

    sender = Role()
    receiver = Role()

    @clause()
    def do_payment(self, ctx):
        simple_transfer(
            ctx=ctx,
            src_participant=self.sender,
            dst_participant=self.receiver,
            amount=self.amount,
            unit=BalanceSheetUnit.GBP,
        )


#     # Define other clauses here
