# Jay's Feedback on Luna

## References

* Overview: https://luna.journey.io/p/luna-overview-june

## Day 1: Install & follow the Luna Docs

### [Core Concepts](https://docs.stage-luna-protocol.com/category/core-concepts)

#### [Participants](https://docs.stage-luna-protocol.com/Core%20Concepts/Participants):

 * Typo: "oOrganization"

#### [Contract](https://docs.stage-luna-protocol.com/Core%20Concepts/Contract): 

 * Typo: "When converting from a Contract into a Template" - think you meant from a Template into a Contract? Also is 'converting' the right word?
 * "Why is the Concept of a Contract Needed?" - this could be reworded to be clearer that you are talking about why is it an object / smart contract / first class ... thingy :-) of course contracts are needed in finance!

#### [Parameters](https://docs.stage-luna-protocol.com/Core%20Concepts/Parameters):

* The examples aren't very useful :-)
* They are showing code in the 'concepts' section, this hasn't been done yet and for a user working through from the top it feels a bit jarring. It would be better to order the pages such that code snippets are introduced in an intuitive order.

#### [Variables](https://docs.stage-luna-protocol.com/Core%20Concepts/Variables)

* Why are Variables a first class Luna construct? What happens if a client tries to just use primitive types or other objects as class attributes - are they just not stored?
* "in any format you like" - does this mean they can be objects, nested dictionaries etc?

#### [Clauses](https://docs.stage-luna-protocol.com/Core%20Concepts/Clauses):

* Typo: "hte"
* ctx introduced in code here, what is this
* what is self.reverse_direction - too early to introduce this maybe?
* ditto self.currency_unit? More generally, if we are assuming the reader knows Python and OO concepts, then why don't we talk about OO in the Templates vs Contracts concepts pages?

#### [Accounting](https://docs.stage-luna-protocol.com/Core%20Concepts/Accounting):

#### Documents():

#### [Engine Ticking]():

#### [Functions]():

### [Running Locally]():

#### [Setup](https://docs.stage-luna-protocol.com/Running%20Locally/Setup):

* Created a new VSCode workspace & Conda env (no instructions needed for me, but may be worth providing this since users will not be super technical)
* Pip instructions worked fine

### [Example Run](https://docs.stage-luna-protocol.com/Running%20Locally/Example%20run):

* My first thought: Initial running locally example should work and be fully provided, I had to figure out the imports (simple_transfer, BalanceSheetUnit)
* I later saw the Boilerplace section, but it was at the bottom. I think it must be the norm for the example to be at the top and then be decomposed.
* People want to copy and paste an example and run it to check their local installation works
* BalanceSheetUnit - I found it confusing that this is in 'functions', which I had to hunt down. It's not a function? The doc says _"The luna.functions package contains a set of useful built in functions."_
* What is "ctx" in the first code? That acronym is not explained anywhere.
* Boilerplate code worked fine!
* Question: why isn't there a security issue? When does authentication kick in?
* KeyError: 'var_name' when calling get_variable - should this be more friendly? maybe not?

## From local to prod (https://docs.stage-luna-protocol.com/Running%20Locally/From%20local%20to%20prod)

* _"Paste the code for the template here, including the relevant imports"_ - what are plans to automate this / enable CI/CD?




## https://docs.stage-luna-protocol.com/Additional%20Resources/Technical%20Advantages : 

* Is 3 retries hard-coded? exponential means 1, 2, 4 if so
* Edge Cases: exceptions probably needs more detail on the workflow e.g. can they drop into an application for resolving them? audit logs feels like not enough
* 90 days feels like not enough for something that could be a business exception - 
* Need more doco on contract upgrades path
* Infrastructure maintenance: what are downtime / green zone options
* "Luna has been designed based on modern cloud first software principles allowing us to scale horizontally meaning you never have to worry about Luna being a bottleneck in your business success." - suggest a comma or two to split this long sentence up
* AWS Security - a corporate client would probably want more detail here
* Data Segregation: I just can't think what customer would consider anything but option 3 given the sensitive nature of the data, the target market being private credit? Is it not better to only offer option 3? Shared compute feels a bit scary given the object-based system design?
