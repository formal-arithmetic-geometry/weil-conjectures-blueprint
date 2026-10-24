+++
id = "det-lem-picard-zero-dictionary"
kind = "lemma"
title = "The zero-scheme dictionary"
order = 823
uses = ["det-cor-picard-degree-g"]
lean = ["AlgebraicGeometry.exists_isEffectiveCartierCenter_hilbertPresheaf", "AlgebraicGeometry.exists_isEffectiveCartierCenter_hilbertPresheaf_zeroLocus_adjointSection"]
+++
Let $k$ be a field and $X$ a $k$-scheme which is proper, smooth
of relative dimension $1$ and geometrically integral over $k$, of genus
$g=\dim_kH^1(X,\cO_X)$, with a $k$-rational point $\sigma$; let
$F\subseteq\Pic_{X/k,\sigma}$ be the subfunctor of classes $\cL$ with
$Rf_{T,*}\cL$ an invertible module placed in degree $0$, and $T$ a
$k$-scheme. Let $\cL\in F(T)$, $\cN$ invertible with
$Rf_{T,*}\cL\cong\cN[0]$, and let $s\in H^0(X_T,\cL\otimes f_T^*\cN^{-1})$ be the adjoint section. Then
$D:=Z(s)\subseteq X_T$ is a relative effective Cartier divisor on
$X_T/T$, finite locally free of *degree $g$* over $T$.
