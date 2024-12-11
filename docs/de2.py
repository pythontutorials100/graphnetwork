Introductory Slide (Context & DSQs)

Title: Ontology-Based Defect Localization in Airfoils

Context:
Modern maintenance and inspection workflows rely on precise localization and characterization of defects on critical airfoil components (e.g., turbine blades, aircraft wings). Integrating data into a semantic ontology enables consistent querying, reasoning, and decision support.

Key Decision Support Questions (DSQs):

    DSQ1: Where is the defect located on the airfoil geometry?
    DSQ2: What are the dimensions of the defects (depth, length, distances from references)?
    DSQ3: How can these measurements inform maintenance priorities and actions?

Classes and Their Genus-Species Definitions

    Airfoil
        Genus: Material Artifact (a man-made physical object)
        Differentia: An aerodynamic component designed to interact with airflow and produce lift or control airflow.
        Definition: An Airfoil is a Material Artifact that is shaped and positioned to generate aerodynamic forces when moved through a fluid medium (air).

    Airfoil Part (Fiat Object Part)

        Genus: Fiat Object Part (a part of an object defined by some reference, not a natural discontinuity)

        Differentia: A non-physically discrete region of an airfoil defined to identify functional geometry.

        Definition: An Airfoil Part is a Fiat Object Part that represents a geometrically defined region of an airfoil, such as edges or surfaces.

        Leading Edge
            Genus: Airfoil Part
            Differentia: The forward-most boundary region of the airfoil.
            Definition: The Leading Edge is an Airfoil Part that denotes the foremost boundary of the airfoil geometry.

        Trailing Edge
            Genus: Airfoil Part
            Differentia: The rearmost boundary region of the airfoil.
            Definition: The Trailing Edge is an Airfoil Part that denotes the rear-most boundary of the airfoil geometry.

        Tip
            Genus: Airfoil Part
            Differentia: The outermost end of the airfoil spanwise.
            Definition: The Tip is an Airfoil Part representing the outermost extremity of the airfoil.

        Surface
            Genus: Airfoil Part
            Differentia: The exposed outer boundary region of the airfoil’s material structure.
            Definition: The Surface is an Airfoil Part that represents the exterior bounding region of the airfoil.

    Airfoil Defect
        Genus: Damage Quality (a quality that indicates damage)
        Differentia: A localized, undesired change in the intended geometry or integrity of the airfoil.
        Definition: An Airfoil Defect is a Damage Quality inhering in an Airfoil, signifying a flaw or damage area on its surface or edge.

    Measurement Information Content Entity (MICE) for Defect Dimensions
        Genus: Measurement Information Content Entity (information about a measurable quality)
        Differentia: Represents measured distances (e.g., depth, length, distances from datum references) of the defect.
        Definition: A Distance/Depth/Length MICE is a type of Measurement Information Content Entity capturing quantifiable values (e.g., defect depth in mm, distance from tip).

    Airfoil Number Identifier (Non-Name Identifier)
        Genus: Non-Name Identifier (a designative information content entity assigning an ID)
        Differentia: An identifier assigning a unique numerical ID to a specific airfoil instance.
        Definition: An Airfoil Number Identifier is a Non-Name Identifier that designates a specific airfoil instance.

    Datum Reference (e.g., Tip Datum)
        Genus: Spatial Region Identifier (if modeling as a reference line) or simply use the existing Tip as an Airfoil Part
        Differentia: A reference line/point serving as a datum for measurement.
        Definition: A Datum Reference is a Spatial Region Identifier used to define a baseline for measuring defect distances.

    Scanbox Inspection (Act of Measuring)
        Genus: Act of Measuring (a planned act of observation for measurement)
        Differentia: A specific measurement technique/method applied to detect and quantify defects.
        Definition: Scanbox Inspection is an Act of Measuring that uses a scanning device to detect and record defect dimensions on the airfoil.

Relations Between Individuals

    AirfoilDefect inheres_in Airfoil
    Meaning: Each defect is a quality of a particular airfoil.
    Purpose: Helps answer DSQ1 (Identify which airfoil the defect belongs to).

    AirfoilDefect located_in LeadingEdge (or TrailingEdge, Tip, Surface)
    Meaning: The defect is found on a specific region of the airfoil.
    Purpose: Directly addresses DSQ1 by providing location context: “Where on the geometry is the defect?”

    AirfoilDefect is_measured_by DistanceMeasurementInformationContentEntity
    Meaning: The defect’s dimensions (depth, length, distances from datum) are captured as measurement data.
    Purpose: Answers DSQ2 by providing a structured way to query exact numeric dimensions.

    DistanceMeasurementInformationContentEntity generically_depends_on InformationBearingEntity
    Meaning: The measurement value (a literal number) is stored in an information-bearing artifact.
    Purpose: Enables integration of raw numeric data into the semantic model.

    InformationBearingEntity has_decimal_value "0.16"^^xsd:float
    Triplet Example: :IBE_1 :has_decimal_value "0.16"^^xsd:float.
    Meaning: The actual numeric value of the measurement.
    Purpose: Precise numeric values enable quantitative decision-making (e.g., determining whether the defect size exceeds a maintenance threshold).

    Airfoil designated_by AirfoilNumberIdentifier
    Meaning: Each airfoil can be uniquely referenced, facilitating indexing and retrieval of defect data.
    Purpose: Supports the identification of which airfoil has the defect (part of DSQ1).

    AirfoilDefect detected_by ScanboxInspection
    Meaning: The inspection method used to find and measure the defect.
    Purpose: Adds provenance and process information, showing how the data was obtained and supporting auditing and quality control processes.

Example Triplets:

    :Defect_1 :inheres_in :Airfoil_1 .
    :Defect_1 :located_in :LeadingEdge .
    :Defect_1 :is_measured_by :DmgDepthMICE_1 .
    :DmgDepthMICE_1 :generically_depends_on :IBE_2 .
    :IBE_2 :has_decimal_value "0.092"^^xsd:float .
    :Airfoil_1 :designated_by :AirfoilNumber_1 .
    :AirfoilNumber_1 :has_text_value "1" .
    :Defect_1 :detected_by :ScanboxInspectionProcess_1 .

How These Relations Answer DSQs:

    DSQ1: “Where is the defect on the geometry?”
    By using :Defect :located_in :LeadingEdge (or another part), one can query the ontology and get the exact airfoil region, thus answering the location question.

    DSQ2: “What are the dimensions of the defect?”
    The relation :Defect :is_measured_by :DmgLengthMICE and :DmgLengthMICE :generically_depends_on :IBE_X with :IBE_X :has_decimal_value "0.249" provides the exact length. Similarly, depth and distances from datum lines are retrieved in the same manner. This allows a direct answer to the size/dimension queries.

Slide Summaries:

Intro Slide:

    Title, Context, DSQs

Classes Slide(s):

    Show hierarchical placement of each class
    Provide genus-species definitions

Relations Slide:

    List key object properties (inheres_in, located_in, is_measured_by, detected_by) and their significance

Query/DSQ Slide:

    Explain how querying located_in answers “Where is the defect?”
    Show how querying is_measured_by leads to measurement values, answering “What are the dimensions?”

Conclusion Slide:

    Semantic structure supports maintenance decisions and inspection prioritization.
    Ontology enables consistent data integration and retrieval for defect analysis.
