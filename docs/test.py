Definition of 'Failure'

    Label: Failure
    Definition: An Event in which an item loses its ability to perform a required function.



Justification:

    Failure is an Event because it is a process or process boundary recognized by an agent where an item loses functionality.
    Placing Failure directly under Event aligns with the definition of Event in your ontology:
        Event: Phenomena (process or process boundary) that is recognized by an agent and typically recorded.

Formal Axiom

    Axiom: Failure(x) → Event(x) ∧ ∃y(MaterialEntity(y) ∧ losesFunction(x, y))

    This axiom states that if x is a Failure, then x is an Event, and there exists a MaterialEntity y such that y loses its function during x.



     Definition of 'Fault'

    Label: Fault
    Definition: A Quality representing the state where an item is unable to perform as required due to an internal condition.


Definitions

    Accident:
        Definition: An Event involving significant damage or injury associated with the operation of an aircraft.

    Incident:
        Definition: An Event, other than an accident, associated with the operation of an aircraft, which affects or could affect the safety of that operation.

    Serious Incident:
        Definition: An Incident in which an accident nearly occurred.

    Immediate Hazard to Aircraft Operations:
        Definition: An Event posing an immediate threat to the safety of aircraft operations, even if no incident or accident has occurred.





     Option to Model 'Fault' as a 'MaterialState'

Alternatively, we can consider Fault as a specific type of MaterialState where the item's function is impaired.
Definition of 'FaultState'

    Label: FaultState
    Definition: A MaterialState where a material entity is unable to perform its required function due to an internal condition.

Placement

    Entity (BFO:0000001)
        Occurrent (BFO:0000003)
            Process (BFO:0000015)
                MaterialState
                    FaultState

Justification:

    MaterialState is defined as a process in which a material entity has a condition that remains unchanged.
    FaultState is a specific MaterialState where the condition is the inability to perform the required function.
    This placement emphasizes the processual aspect of the faulty condition over time.

Formal Axiom

    Axiom: FaultState(x) → MaterialState(x) ∧ ∃y(MaterialEntity(y) ∧ participatesInAtSomeTime(y, x) ∧ unableToPerformFunction(y))

-------------------------------------


b. Fault

Definition:

    Fault is a Stasis of Specifically Dependent Continuant representing the state of an item being unable to perform as required due to an internal state.


c. Failure Description

Definition:

    Failure Description is an Event Description that is an Information Content Entity providing details about a Failure, including its characteristics, context, and impact.

Explanation:

    Failure Description documents the occurrence of a failure, capturing relevant information for analysis and reporting.
