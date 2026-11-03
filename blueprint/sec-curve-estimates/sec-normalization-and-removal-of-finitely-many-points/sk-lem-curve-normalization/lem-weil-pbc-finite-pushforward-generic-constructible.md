+++
id = "lem-weil-pbc-finite-pushforward-generic-constructible"
kind = "lemma"
title = "Generic finite pushforward is constructible"
lean = ["AlgebraicGeometry.Etale.exists_dense_isFiniteLocallyConstantSheaf_lowerStar"]
order = 1574
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-noetherian-finite-components", "lemma-weil-pbc-finite-exchange", "pqf-lem-finite-integral-lft", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $\Lambda$ be a finite commutative ring, let $S$ be an integral Noetherian
affine scheme, let $g:Z\to S$ be a finite morphism, and let $E$ be a
constructible etale sheaf of $\Lambda$-modules on $Z$. There is a dense open
$S^\circ\subset S$ such that the restriction of the direct image $g_*E$ to
$S^\circ$ is finite locally constant (lisse).
