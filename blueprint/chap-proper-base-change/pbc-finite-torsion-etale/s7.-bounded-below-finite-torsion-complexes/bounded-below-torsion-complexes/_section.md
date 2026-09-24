+++
id = "bounded-below-torsion-complexes"
kind = "section"
title = "Bounded-below torsion complexes"
order = 1834
uses = ["def-sp-convergence", "def-sp-etale-dictionary", "def-sp-exact-couple", "def-sp-truncation-couple", "def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-sp-couple-morphism", "lem-sp-finite-filtration-induction", "lem-sp-shift-identification", "lemma-weil-pbc-derived-exchange-coherence", "lemma-weil-pbc-torsion-assembly", "thm-sp-half-plane-convergence", "thm-sp-truncation-e2"]
+++
The upgrade from sheaves to bounded-below complexes with torsion cohomology.
Canonical truncation gives hypercohomology spectral sequences on both sides of
the square [def-weil-pbc-hypercohomology-filtrations], convergent in
a half plane [lemma-weil-pbc-hypercohomology-convergence]; the exchange morphism
is a morphism of the underlying exact couples
[def-weil-pbc-truncation-exact-couples],
[lem-weil-pbc-exact-couple-differential] whose abutment map is the exchange
morphism itself [lemma-weil-pbc-exact-couple-abutment]. Since the $E_2$-map is
an isomorphism by [lemma-weil-pbc-torsion-assembly], so is the abutment
[thm-weil-pbc-bounded-below], which is the chapter's terminal statement
[prop-weil-proet-finite-proper-base-change], with its coherence
`prop-weil-pbc-finite-torsion-coherence` and the geometric-fibre formula
[cor-weil-pbc-geometric-fiber-finite].
