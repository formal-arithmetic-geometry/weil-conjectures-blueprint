+++
id = "lem-fin-finite-boundary-comparison"
kind = "lemma"
title = "A proper direct image detects a comparison off a finite boundary"
lean = ["AlgebraicGeometry.Etale.isIso_of_isIso_upperStar_map_of_isIso_rightDerivedLowerStar_map"]
order = 1976
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $b:Y\to S$ be proper, let $a:G\hookrightarrow Y$ be open
with closed complement $i:Z\hookrightarrow Y$, and suppose $bi$
is finite.
Let $c:K\to L$ be a morphism of ordinary
bounded-below derived
etale module complexes.
If $a^*c$ and the
direct image $Rb_*c$ are
isomorphisms, then $c$ is an isomorphism.
