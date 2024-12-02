1. Remaining Life Measurement

Definition: An estimation of the remaining useful life of a component or system, typically expressed in time or usage cycles.


Class Information:

    Name: Remaining Life Estimate Information Content Entity


2. Cancellation

Definition: A planned act where a scheduled process or service is terminated before completion.

Parent Class:

    Planned Act
    (Under: Process > Act > Planned Act)

Class Information:

    Name: Act of Cancellation
    Annotations:
        hasDefinition: "A planned act where an intended process or service is terminated before completion."
    Properties:
        has_agent some Person or Organization
        acts_on some Process or Service

------------------

3. Delay

Definition: A change in the scheduled timing of a process, causing it to start or finish later than planned.

Parent Class:

    Change
    (Under: Process > Change)

Class Information:

    Name: Process Delay
    Annotations:
        hasDefinition: "A change where the scheduled time of a process is postponed or extended."
    Properties:
        affects some Process
        has_duration some Time Interval

-------------------------

5. Recall

Definition: A planned act where a producer or authority requests the return of a product due to identified issues or defects.

Parent Class:

    Planned Act
    (Under: Process > Act > Planned Act)

Class Information:

    Name: Act of Product Recall
    Annotations:
        hasDefinition: "A planned act where a producer or authority requests the return of a product due to identified issues."
    Properties:
        has_agent some Organization
        acts_on some Product

-----------------------------

4. Diversion

Definition: An act of travel where the planned route or destination is changed to an alternative.

Parent Class:

    Act of Travel
    (Under: Process > Act > Unplanned Act > Act of Motion > Act of Travel)

Class Information:

    Name: Act of Diversion
    Annotations:
        hasDefinition: "An act of travel where the planned route or destination is changed to an alternative."
    Properties:
        has_agent some Vehicle or Person
        has_origin some Original Destination
        has_destination some Alternate Destination

----------------------------------------


6. MRO Inspection

Definition: An act of maintenance involving the inspection of equipment or components as part of maintenance, repair, and operations procedures.

Parent Class:

    Act of Maintenance
    (Under: Process > Act > Planned Act > Act of Artifact Processing > Act of Maintenance)

Class Information:

    Name: MRO Inspection
    Annotations:
        hasDefinition: "An act of maintenance involving the inspection of equipment or components as part of MRO procedures."
    Properties:
        has_agent some Technician or Engineer
        acts_on some Equipment or Component

------------------------------------------------------


7. Performance Issue

Definition: A state where an artifact's function is degraded below nominal levels.

Parent Class:

    Stasis of Function
    (Under: Process > Stasis > Stasis of Specifically Dependent Continuant > Stasis of Realizable Entity > Stasis of Function)

Class Information:

    Name: Degraded Performance Stasis
    Annotations:
        hasDefinition: "A stasis where the function of an artifact is degraded below nominal levels."
    Properties:
        inheres_in some Artifact
        has_quality some Reduced Function

-------------------------


8. Part Failure Identifier

Definition: An identifier assigned to a part that has failed, used to uniquely identify and track the failed component.

Parent Class:

    Artifact Identifier
    (Under: Information Content Entity > Designative Information Content Entity > Non-Name Identifier > Artifact Identifier)

Class Information:

    Name: Part Failure Identifier
    Annotations:
        hasDefinition: "An artifact identifier assigned to a part that has failed."
    Properties:
        identifies some Failed Part
        has_value some Identifier Code


-----------------------------


9. Weather Event

Definition: A natural process involving atmospheric conditions, resulting in phenomena such as rain, snow, storms, etc.

Parent Class:

    Natural Process
    (Under: Process > Natural Process)

Class Information:

    Name: Weather Event
    Annotations:
        hasDefinition: "A natural process involving atmospheric conditions resulting in weather phenomena."
    Properties:
        has_location some Geospatial Region
        has_time some Temporal Interval


----------------------------------------

10. Operationality

Definition: The state of being operational or capable of functioning.

Parent Class:

    Stasis of Artifact Operationality
    (Under: Process > Stasis > Stasis of Specifically Dependent Continuant > Stasis of Realizable Entity > Stasis of Artifact Operationality)

Class Information:

    Name: Operationality
    Annotations:
        hasDefinition: "The state of being operational or capable of functioning."
    Properties:
        inheres_in some Artifact
        has_value some Operational Status (Operational, Non-Operational, Partially Operational)


---------------------------------

11. Requirement

Definition: A directive information content entity that specifies a necessary condition or capability.

Parent Class:

    Directive Information Content Entity
    (Under: Information Content Entity > Directive Information Content Entity)

Class Information:

    Name: Requirement
    Annotations:
        hasDefinition: "A directive information content entity that specifies a necessary condition or capability."
    Properties:
        specifies some Necessary Condition or Capability
        is_about some Process or Artifact


-----------------------------------


12. Failure Rate

Definition: A ratio measurement representing the frequency with which a component or system fails over a specified period.

Parent Class:

    Ratio Measurement Information Content Entity
    (Under: Information Content Entity > Descriptive Information Content Entity > Measurement Information Content Entity > Ratio Measurement Information Content Entity)

Class Information:

    Name: Failure Rate Measurement Information Content Entity
    Annotations:
        hasDefinition: "A ratio measurement information content entity representing the rate at which failures occur over time."
    Properties:
        measures some Failure Rate
        has_unit some Failures per Time Unit or Failures per Cycle

Additional Concepts Based on Decision Support Questions:
13. Failure Incident

Definition: An event where a component or system fails to perform its intended function.

Parent Class:

    Failure Event
    (Under: Process > Effect > Failure Event)

Class Information:

    Name: Failure Event
    Annotations:
        hasDefinition: "An effect where a component or system fails to perform its intended function."
    Properties:
        occurs_in some Component or System
        results_in some Loss of Function

14. Failure Classification

Definition: An information content entity that assigns a failure incident to a category based on predefined criteria.

Parent Class:

    Classification Information Content Entity
    (Under: Information Content Entity > Descriptive Information Content Entity > Classification Information Content Entity)

Class Information:

    Name: Failure Classification Information Content Entity
    Annotations:
        hasDefinition: "An information content entity that categorizes a failure incident."
    Properties:
        classifies some Failure Event
        has_value some Failure Category

15. System Health Indicator

Definition: A measurement or metric providing information about the operational health of a system.

Parent Class:

    Measurement Information Content Entity
    (Under: Information Content Entity > Descriptive Information Content Entity > Measurement Information Content Entity)

Class Information:

    Name: System Health Measurement Information Content Entity
    Annotations:
        hasDefinition: "A measurement information content entity that provides metrics about the health status of a system."
    Properties:
        measures some System Health Indicator
        has_value some Health Metric

16. Mandatory Action

Definition: A directive information content entity that specifies an action that must be performed.

Parent Class:

    Action Requirement
    (Under: Information Content Entity > Directive Information Content Entity > Action Requirement)

Class Information:

    Name: Mandatory Action
    Annotations:
        hasDefinition: "A directive specifying an action that must be executed."
    Properties:
        requires some Action
        is_about some System or Component

