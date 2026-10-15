+++
id = "det-picard-f-representable-chart"
kind = "lemma"
title = "The chart $W$: its map to the Picard functor and its smoothness"
uses = ["thm-pc-f-representable", "thm-pc-hilb-curves", "lem-pc-universal-adjoint-section", "cor-pc-sigma-pic-iso"]
+++
Let $C/k$ be a smooth projective geometrically connected curve of genus
$g$ with a point $P\in C(k)$, let $H_g$ represent $\Hilb^g_{C/k}$ with
universal divisor $D_g\subset C\times H_g$, and let $W\subset H_g$ be the
open subscheme representing $F$ of [thm-pc-f-representable] (over a
separably closed field, or more generally whenever that theorem
applies). Then:

1. the composite $h_W\xrightarrow{\sim}F\subset\operatorname{Pic}_{C/k,P}\cong\operatorname{Pic}_{C/k}$
sends a $T$-point $D\subset C_T$ of $W$ (a relative effective Cartier
divisor, finite locally free of degree $g$ over $T$) to the class of the
normalized sheaf $\cO_{C_T}(D)\otimes f_T^*\bigl(P_T^*\cO_{C_T}(D)\bigr)^{-1}$,
i.e. to the rigidified invertible sheaf of $D$;
1. $W$, and hence the functor $F$, is smooth of pure dimension $g$ over
$k$ (if $W\ne\emptyset$).
