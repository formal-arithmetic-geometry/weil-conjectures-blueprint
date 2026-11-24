+++
id = "lemma-simple-objects"
kind = "lemma"
title = "The simple objects"
order = 1258
lean = ["AlgebraicGeometry.WeilComplex.simple_punctualObj_iff", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.simple_middleExtension"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-perfect-complexes-geometric-point", "definition-middle-extension", "definition-perverse-sheaves-curve", "lemma-perverse-sheaves-curve", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
In the category of [perverse sheaves](@definition-perverse-sheaves-curve) on $C$, and in that of [perverse
Weil sheaves](@definition-perverse-sheaves-curve) on $C_0$,
the simple objects are the irreducible [punctual](@definition-punctual-sheaf) objects and the objects
$(j_*M)[1]$ with $M$ nonzero irreducible [lisse](@definition-lisse-sheaves) on a dense open, where
irreducibility is taken in the geometric or in the Weil category,
respectively. These [middle extensions](@definition-middle-extension) have no nonzero [punctual](@definition-punctual-sheaf)
subobject or quotient in the [perverse heart](@definition-perverse-sheaves-curve).
