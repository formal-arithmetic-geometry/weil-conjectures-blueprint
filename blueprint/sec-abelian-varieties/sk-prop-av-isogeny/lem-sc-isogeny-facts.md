+++
id = "lem-sc-isogeny-facts"
kind = "lemma"
title = "Basic facts about isogenies"
lean = ["AlgebraicGeometry.isIsogeny_npow_id", "AlgebraicGeometry.isogenyDegree_npow_id", "AlgebraicGeometry.flat_torsionSubgroupScheme", "AlgebraicGeometry.finrankΓ_torsionSubgroupScheme"]
order = 561
uses = ["def-sc-abelian-variety", "def-sc-hilbert-degree", "def-sc-isogeny", "def-sc-mult-n", "lem-sc-abelian-variety-projective", "lem-sc-ample-tensor", "lem-sc-deg-pullback-finite", "lem-sc-finite-constant-length-flat", "lem-sc-hilbert-polynomial", "lem-sc-isogeny-degree", "lem-sc-mult-n-finite-flat", "lem-sc-mult-n-pullback", "thm-sc-theorem-of-cube"]
+++
Let $A$ be an abelian variety of
dimension $g$ over a field $k$ and $n\geq1$.

**(a)** The map $[n]$ of [def-sc-mult-n] is an
isogeny of degree $n^{2g}$, finite,
flat and surjective.

**(b)** In particular the kernel $A[n]$ is a finite flat group
scheme of order $n^{2g}$ over $k$, and $[n]:A\to A$ is an fppf
covering.
