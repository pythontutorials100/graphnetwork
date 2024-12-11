Airfoil

    Placement:
        owl:Thing
            entity (BFO:0000001)
                continuant (BFO:0000002)
                    independent continuant (BFO:0000004)
                        material entity (BFO:0000040)
                            Material Artifact
                                Airfoil

Airfoil Parts (Fiat Object Parts)

    Placement:
        owl:Thing
            entity
                continuant
                    independent continuant
                        material entity
                            fiat object part (BFO:0000024)
                                Airfoil Part (new class)
                                    Leading Edge
                                    Trailing Edge
                                    Tip
                                    Surface

Airfoil Defect (Damage Quality)

    Placement:
        owl:Thing
            entity
                continuant
                    specifically dependent continuant (BFO:0000020)
                        quality (BFO:0000019)
                            Damage Quality (new class)
                                Airfoil Defect (new class)

Measurement Information Content Entities for Defect Distances and Dimensions

    Placement:
        owl:Thing
            entity
                continuant
                    generically dependent continuant (BFO:0000031)
                        Information Content Entity
                            Descriptive Information Content Entity
                                Measurement Information Content Entity
                                    Ratio Measurement Information Content Entity
                                        Distance Measurement Information Content Entity
                                            (Instances representing shortest/longest distances for the defect)
                                        (Instances representing Damage Depth, Damage Length as measurements)

Airfoil Number (Identifier)

    Placement:
        owl:Thing
            entity
                continuant
                    generically dependent continuant
                        Information Content Entity
                            Designative Information Content Entity
                                Non-Name Identifier
                                    Airfoil Number Identifier (instances here)

Datum (Tip/Platform Reference)

    If represented as a physical reference region:
        Under Airfoil Part (e.g., Tip as already listed)
    If represented as an identifier or coordinate reference:
        owl:Thing
            entity
                continuant
                    generically dependent continuant
                        Information Content Entity
                            Designative Information Content Entity
                                Spatial Region Identifier
                                    (Instance representing the datum reference)

Inspection Method (Scanbox)

    Placement:
        owl:Thing
            entity
                occurrent (BFO:0000003)
                    process (BFO:0000015)
                        Act
                            Act of Measuring
                                Scanbox Inspection (an instance of Act of Measuring)
