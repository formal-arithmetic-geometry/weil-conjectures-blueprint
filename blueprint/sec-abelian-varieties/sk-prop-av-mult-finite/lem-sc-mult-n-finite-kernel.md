+++
id = "lem-sc-mult-n-finite-kernel"
kind = "lemma"
title = "Multiplication by $n$ is finite"
lean = ["AlgebraicGeometry.isFinite_npow_id", "AlgebraicGeometry.isFinite_torsionSubgroupScheme", "AlgebraicGeometry.isMonHom_npow_id"]
order = 552
uses = ["def-sc-abelian-variety", "def-sc-group-scheme", "def-sc-mult-n", "lem-sc-av-commutative", "lem-sc-mult-n-homomorphism", "thm-pqf-finite-iff-proper-finite-fibres"]
+++
Let $A$ be an abelian variety
over a field $k$, and let $n\geq1$. Then the map $[n]$ of
[def-sc-mult-n] is a finite homomorphism of
group schemes, and its kernel
$A[n]$ is a finite group scheme over $k$.
