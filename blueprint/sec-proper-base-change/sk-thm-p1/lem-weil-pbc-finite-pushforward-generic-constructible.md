+++
id = "lem-weil-pbc-finite-pushforward-generic-constructible"
kind = "lemma"
title = "Generic finite pushforward is constructible"
lean = ["AlgebraicGeometry.Etale.exists_dense_isFiniteLocallyConstantSheaf_lowerStar"]
order = 1175
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-noetherian-finite-components", "lemma-weil-pbc-finite-exchange", "pqf-lem-finite-integral-lft", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $S$ be an integral Noetherian affine scheme, let $g:Z\to S$ be finite, and
let $E$ be a constructible abelian etale sheaf on $Z$. There is a dense open
$S^\circ\subset S$ on which the direct image $g_*E$ is lisse.
