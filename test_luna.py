from luna.engine.engine import Engine
from luna.clock import NowClock
from mytemplate import MyTemplate
from decimal import Decimal
from datetime import datetime
from pprint import pprint

# import luna.financial as financial
# import luna.functions as functions

from luna.clock import VirtualClock

clock = VirtualClock(datetime(2000, 1, 1))
# clock = NowClock()
engine = Engine(clock=clock)

contract = engine.add_contract(
    template=MyTemplate(),
    parameters={"amount": Decimal("50")},
    roles={
        "sender": ["sender_id"],
        "receiver": ["receiver_id"],
    },
)

engine.put_event(
    contract_id=contract.id,
    event_name="the name of the event",
    payload={"value1": 31, "value2": "some value"},
)

contract.tick()

clock.set_datetime(datetime(2000, 1, 2))
contract.tick()  # Tick on 02-01-2000

#print(contract.state.get_clause_eval_count("do_payment"))
#print(contract.state.get_clause_output("do_payment"))
#print(contract.state.contract_id)
#contract.state.get_variable("var_name")  # Access a variable
#contract.state.get_parameter("var_name")  # Access a parameter

