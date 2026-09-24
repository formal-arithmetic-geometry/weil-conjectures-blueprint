+++
id = "prop-nagata-global-blowup-affine-restrict"
kind = "theorem"
title = "Affine restriction of the global blow-up"
order = 309
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isPullback_blowupι"]
tags = ["latex:proposition"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup", "def-nagata-global-blowup-affine-restriction-map", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-diagonal-base-change", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-global-blowup-overlap-cocycle", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-affine-blowup-restrict", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
The constructed comparison $q_V$ is an isomorphism over $V$.

## Proof

Cover $V$ by basic opens contained in the chosen affine charts. On each,
the comparison is an isomorphism by
[prop-nagata-affine-blowup-restrict]; the overlap cocycle and local-map
compatibility show that these maps and their inverses agree. The gluing
theorem therefore produces mutually inverse global morphisms over $V$.
