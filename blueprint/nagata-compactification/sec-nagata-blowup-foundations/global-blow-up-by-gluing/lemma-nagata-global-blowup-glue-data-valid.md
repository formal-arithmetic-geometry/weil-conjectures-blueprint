+++
id = "lemma-nagata-global-blowup-glue-data-valid"
kind = "lemma"
title = "Validity of the global blow-up gluing datum"
order = 303
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupNatTrans_equifibered"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-global-blowup-overlap-cocycle", "lemma-nagata-global-blowup-overlap-id-symm", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
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
