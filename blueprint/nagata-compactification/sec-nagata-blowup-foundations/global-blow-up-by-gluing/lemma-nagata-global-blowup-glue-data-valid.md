+++
id = "lemma-nagata-global-blowup-glue-data-valid"
kind = "lemma"
title = "Validity of the global blow-up gluing datum"
order = 229
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupNatTrans_equifibered"]
uses = ["def-nagata-global-blowup-glue-data", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-global-blowup-overlap-cocycle", "lemma-nagata-global-blowup-overlap-id-symm"]
+++
The raw datum $\mathsf G(X,\mathcal I,(V_i))$ has isomorphism-valued
overlap maps satisfying the identity, symmetry, and triple-overlap cocycle
axioms; hence it is a scheme gluing datum.

## Proof

The overlap maps are isomorphisms by
[lemma-nagata-global-blowup-overlap-basic]; independence of refinements,
identity, symmetry, and the triple cocycle are given by the cited coherence
lemmas. Hence the hypotheses of
`AlgebraicGeometry.Scheme.GlueData.glued` are satisfied.
