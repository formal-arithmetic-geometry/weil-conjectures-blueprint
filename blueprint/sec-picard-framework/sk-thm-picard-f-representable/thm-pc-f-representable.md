+++
id = "thm-pc-f-representable"
kind = "theorem"
title = "$F$ is representable by an open subscheme of $\\underline{\\operatorname{Hilb}}^g_{X/k}$"
order = 838
uses = ["def-pc-derived-category", "def-pc-f-subfunctor", "def-pc-finite-locally-free", "def-pc-genus", "def-pc-hilb-functor", "def-pc-pic-sigma-functor", "def-pc-rational-point", "def-pc-relative-effective-cartier", "def-pc-representable-functor", "def-pc-smooth-projective-curve", "def-pc-subfunctor", "def-nagata-invertible-ideal", "def-sc-invertible-module", "lem-pc-cartier-criterion", "lem-pc-hilb-representable", "lem-pc-recd-pullback", "lem-pc-universal-adjoint-section", "lem-pc-universal-divisor", "thm-pc-hilb-curves"]
lean = ["AlgebraicGeometry.isRepresentable_picardFunctorInvertibleDirectImage"]
+++
Let $k$ be a field,
let $X$ be a scheme over $k$ which is smooth of relative dimension $1$,
proper and geometrically integral over $k$ (for instance a smooth
projective curve over $k$), of genus $g=\dim_kH^1(X,\mathcal{O}_X)$, with a
$k$-rational point $\sigma$, and let
$F$ be the subfunctor of
[lem-pc-f-open-subfunctor]. Let $H$ be a $k$-scheme representing
$\operatorname{Hilb}^g_{X/k}$. Then there are a scheme $W$ and an open
immersion $j:W\to H$ such that $W$, viewed as a $k$-scheme through $j$,
represents $F$; that is, $F$ is representable by an open
subscheme of $\underline{\operatorname{Hilb}}^g_{X/k}$.
