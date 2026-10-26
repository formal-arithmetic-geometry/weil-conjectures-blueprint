+++
id = "lem-sc-canonical-sheaf"
kind = "lemma"
title = "The canonical sheaf of a smooth curve"
lean = ["AlgebraicGeometry.Scheme.Hom.isInvertible_relativeDifferentials"]
order = 638
uses = ["def-sc-curves", "def-sc-invertible-module", "def-sc-kahler-differentials"]
+++
Let $f:X\to S$ be a morphism of schemes which is smooth of relative
dimension one, and let $\Omega^1_{X/S}$ be its sheaf of relative Kähler
differentials (defined as in [def-sc-kahler-differentials], with the
rings of sections of $\mathcal O_S$ in place of $k$). Then
$\Omega^1_{X/S}$ is an invertible $\mathcal O_X$-module
([def-sc-invertible-module]). In particular, for a smooth connected
curve $C$ over $k$ of dimension one, $\omega_C=\Omega^1_{C/k}$ is a
line bundle.
