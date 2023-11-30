from luna import Template, Parameter, Variable, Role, clause, Event, Every
from luna.engine.engine import Engine
from luna.clock import NowClock

class MyTemplate(Template):
    var = Variable(type_=int, value=0)

    @clause()
    def some_clause(self):
        self.var = 42

engine = Engine(clock=NowClock())

contract = engine.add_contract(
    template=MyTemplate(),
    parameters={},
    roles={},
    linked_contracts={},
)

contract.tick()

print(contract.state.get_variable("var")) # Prints 42
