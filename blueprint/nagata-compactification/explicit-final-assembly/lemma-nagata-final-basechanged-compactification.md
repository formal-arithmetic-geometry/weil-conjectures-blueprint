+++
id = "lemma-nagata-final-basechanged-compactification"
kind = "lemma"
title = "Property of the base-changed compactification"
order = 602
lean = ["AlgebraicGeometry.nagataCompactification_of_locallyOfFinitePresentation"]
uses = ["def-nagata-compactifiable", "def-nagata-final-basechanged-compactification", "def-nagata-noetherian-inverse-system", "lemma-nagata-compactification-base-change", "lemma-nagata-final-descended-model", "lemma-nagata-final-noetherian-compactification", "lemma-nagata-separated-eventually", "prop-nagata-noetherian-inverse-system", "thm-nagata-noetherian"]
+++
The constructed $C_f^{\mathrm{fp}}$ is a compactification of
$X_f^{\mathrm{fp}}\to S$.

## Proof

Base change preserves every compactification field by
[lemma-nagata-compactification-base-change]. Transporting the source
across the isomorphism $\epsilon_f$ preserves the open-immersion,
quasi-compactness, properness, and factorization equalities.
