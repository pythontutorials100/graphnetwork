 Event Description

    Definition: A Descriptive Information Content Entity that provides information detailing the characteristics, context, or specifics of an event or occurrence.


b. Report

    Definition: A Descriptive Information Content Entity that presents organized information, findings, or analysis on a particular topic or event.


Fault: A state of an item characterized by inability to perform as required, due to an internal condition (IEC 60050-192:2015).
Failure: An event where an item loses the ability to perform as required (IEC 60050-192:2015).


a. Analysis Report

    Definition: A Report documenting the results, conclusions, and recommendations derived from an analysis.



Classification

    Definition: A Descriptive Information Content Entity that provides a systematic arrangement or grouping of entities based on shared characteristics, following the principles of genus-species definitions.



Failure Classification

    Definition: A Classification that categorizes failure events into predefined classes based on shared characteristics.
    Placement: Subclass of Classification

Fault Classification

    Definition: A Classification that categorizes faults based on their nature, causes, or effects.
    Placement: Subclass of Classification



2. Differentiating Between Fault and Failure

Based on the definitions provided:

    Fault: A state of an item characterized by inability to perform as required, due to an internal condition (IEC 60050-192:2015).
    Failure: An event where an item loses the ability to perform as required (IEC 60050-192:2015).

Given that faults and failures are distinct—faults being states and failures being events—it makes sense to represent their descriptions separately.
a. Fault Description

    Definition: An Event Description that provides detailed information about the characteristics or context of a fault (the state of inability to perform).
    Placement: Subclass of Event Description

b. Failure Description

    Definition: An Event Description that provides detailed information about the characteristics or context of a failure event (the loss of ability to perform).
    Placement: Subclass of Event Description


a. Maintenance Data

    Definition: Data characterizing the maintenance action planned or done (ISO 14224:2016).
    Placement: Subclass of Descriptive Information Content Entity

b. Reliability Data

    Definition: Data for reliability, maintainability, and maintenance support performance (ISO 14224:2016).
    Placement: Subclass of Descriptive Information Content Entity

c. Failure Data

    Definition: Data characterizing the occurrence of a failure event (ISO 14224:2016).
    Placement: Subclass of Descriptive Information Content Entity

Hierarchy Placement:

    Information Content Entity
        Descriptive Information Content Entity
            Maintenance Data
            Reliability Data
            Failure Data
