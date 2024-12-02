Temporal Shift

    Definition: "A change in which the temporal location of a process is altered."
    Parent Class: Change
    Annotations:
        hasDefinition: "A change affecting the temporal occurrence of a process."
    Properties:
        affects some Process
        results_in some Process occurring at a different Temporal Region


Delay

    Definition: "A temporal shift where the scheduled start or end time of a process is postponed to a later time."
    Parent Class: Temporal Shift
    Annotations:
        hasDefinition: "A change causing a process to occur later than originally scheduled."
    Properties:
        affects some Scheduled Process
        results_in some Process occurring at a later Temporal Region
        has_cause some Event or Condition

Additional Considerations

    Other Subclasses of Temporal Shift:
        Advancement: A temporal shift where a process occurs earlier than scheduled.
        Rescheduling: A general reallocation of a process to a different temporal region, which could be earlier or later.

    Properties Specific to Temporal Shift:
        has_temporal_amount: The amount of time by which the process is shifted.
        has_new_temporal_location: The new temporal region where the process will occur.

    Examples of Temporal Shifts:
        Delay: A flight departure is delayed due to technical issues.
        Advancement: A meeting is moved up to an earlier time because all participants are available sooner.
        Rescheduling: A maintenance operation is rescheduled to a different day to accommodate resource availability.
