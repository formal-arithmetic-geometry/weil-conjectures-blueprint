+++
kind = "proof"
of = "dag-lem-pe-roos-coordinates-quasi-iso"
tags = ["sheaf-dag"]
+++
1. Include V shifted by minus one as the second coordinate and project L onto the first coordinate. The displayed differential makes these chain maps and gives a short exact sequence split in each degree. Do the same for the primed data. The coordinate formula on f supplies a morphism of these short exact sequences, with outer arrows a shifted by minus one and a. Shift preserves quasi-isomorphisms, so the two outer arrows are quasi-isomorphisms. Apply the five lemma to the long exact homology sequences, equivalently HomologicalComplex.HomologySequence.quasiIso_τ₂ from the source library, to conclude that f is a quasi-isomorphism.
