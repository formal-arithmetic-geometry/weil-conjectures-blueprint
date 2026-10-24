+++
id = "lem-pc-hilb-addition"
kind = "lemma"
title = "The addition morphism on Hilbert schemes"
lean = ["AlgebraicGeometry.IsHilbertSubscheme.exists_eq_mul", "AlgebraicGeometry.exists_addition_hilbertPresheaf"]
order = 812
uses = ["def-pc-finite-locally-free", "def-pc-hilb-functor", "lem-pc-cartier-criterion"]
+++
Let $X\to S$ be
a separated smooth morphism of relative dimension $1$, let $d\geq0$ and
assume that the functors $\operatorname{Hilb}^d_{X/S}$ and
$\operatorname{Hilb}^{d+1}_{X/S}$ are representable. There is a morphism of
$S$-schemes

$$
\underline{\operatorname{Hilb}}^d_{X/S}\times_SX\;\longrightarrow\;\underline{\operatorname{Hilb}}^{d+1}_{X/S},
$$

finite locally free of degree $d+1$, sending a $T$-point
$(Z,x)$, with $Z\subset X_T$ a degree-$d$ closed subscheme and $x:T\to X$ a
morphism over $S$, to the closed subscheme of $X_T$ whose ideal is the
product $\mathcal{I}_Z\cdot\mathcal{I}_{\Gamma_x}$ of the ideal of $Z$ and the
ideal of the graph $\Gamma_x\subset X_T$ of $x$.
For a rational point $x$ this is the divisor $Z+x$.
