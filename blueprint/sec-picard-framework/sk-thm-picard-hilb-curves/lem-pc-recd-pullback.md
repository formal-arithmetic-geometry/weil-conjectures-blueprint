+++
id = "lem-pc-recd-pullback"
kind = "lemma"
title = "Pullback of relative effective Cartier divisors"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.nonempty_pullback_dual_toModules_iso", "AlgebraicGeometry.Scheme.IdealSheafData.IsRelativeEffectiveCartier.isRelativeEffectiveCartier_comap_of_isPullback", "AlgebraicGeometry.Scheme.IdealSheafData.IsRelativeEffectiveCartier.comap_of_isPullback"]
order = 800
uses = ["def-pc-base-change", "def-pc-divisor-line-bundle", "def-pc-morphism-conventions", "def-pc-relative-effective-cartier", "def-sc-effective-cartier-divisor", "lem-pc-closed-imm-base-change", "lem-pc-divisor-line-bundle-properties", "lem-pc-flat-compose"]
+++
Let $f:X\to S$ be a flat morphism of finite presentation, let
$D\subset X$ be a
relative effective Cartier
divisor on $X/S$, and let $g:T\to S$ be a morphism. Then
$D_T:=D\times_ST$ is a relative effective Cartier divisor on $X_T/T$
and, with $g_X:X_T\to X$,

$$
\mathcal{O}_{X_T}(D_T)\cong g_X^*\mathcal{O}_X(D).
$$
