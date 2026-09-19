+++
id = "prop-nagata-global-blowup-affine-restrict"
kind = "theorem"
title = "Affine restriction of the global blow-up"
order = 234
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isPullback_blowupι"]
tags = ["latex:proposition"]
uses = ["def-nagata-global-blowup-affine-restriction-map", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-global-blowup-overlap-cocycle", "prop-nagata-affine-blowup-restrict"]
+++
The constructed comparison $q_V$ is an isomorphism over $V$.

## Proof

Cover $V$ by basic opens contained in the chosen affine charts. On each,
the comparison is an isomorphism by
[prop-nagata-affine-blowup-restrict]; the overlap cocycle and local-map
compatibility show that these maps and their inverses agree. The gluing
theorem therefore produces mutually inverse global morphisms over $V$.
