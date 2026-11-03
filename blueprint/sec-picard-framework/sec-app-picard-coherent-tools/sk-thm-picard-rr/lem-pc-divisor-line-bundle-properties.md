+++
id = "lem-pc-divisor-line-bundle-properties"
kind = "lemma"
title = "Properties of $\\mathcal{O}_X(D)$"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.isInvertible_dual_toModules", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.comap_of_flat", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.nonempty_pullback_toModules_iso", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.nonempty_dual_toModules_comap_iso"]
order = 728
uses = ["def-pc-base-change", "def-nagata-invertible-ideal", "def-sc-invertible-module", "lem-pc-closed-imm-base-change", "lem-pc-tensor-dual-invertible"]
+++
Let $S$ be a scheme and $D\subset S$ an
effective Cartier divisor.

1. $\mathcal{O}_S(D)$ is an
invertible $\mathcal{O}_S$-module.
1. If $g:Y\to S$ is a flat morphism and $D_Y=D\times_SY$, then
$\mathcal{I}_{D_Y}=g^*\mathcal{I}_D$ and $\mathcal{O}_Y(D_Y)\cong g^*\mathcal{O}_S(D)$.
