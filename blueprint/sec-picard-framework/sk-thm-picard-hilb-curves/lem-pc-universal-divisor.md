+++
id = "lem-pc-universal-divisor"
kind = "lemma"
title = "The universal divisor"
lean = ["AlgebraicGeometry.isRelativeEffectiveCartier_universal_hilbertPresheaf"]
order = 818
uses = ["def-pc-divisor-line-bundle", "def-pc-hilb-functor", "def-pc-relative-effective-cartier", "def-nagata-invertible-ideal", "lem-pc-cartier-criterion", "lem-pc-recd-pullback", "thm-pc-hilb-curves"]
+++
Let $X\to S$ be a smooth morphism of relative dimension $1$, let
$d\geq0$ and let $H$ be an $S$-scheme representing
$\operatorname{Hilb}^d_{X/S}$ ([def-pc-hilb-functor]), with universal closed
subscheme

$$
D_{\mathrm{univ}}\subset H\times_SX .
$$

Then $D_{\mathrm{univ}}$ is a relative effective Cartier divisor on
$H\times_SX$ over $H$ ([def-pc-relative-effective-cartier]), with associated
invertible module $\mathcal{O}(D_{\mathrm{univ}})$; and for every $S$-scheme $T$
and every $h:T\to H$, with $D_h\subset X_T$ the closed subscheme classified by
$h$, one has
$\mathcal{O}_{X_T}(D_h)\cong(h\times\mathrm{id}_X)^*\mathcal{O}(D_{\mathrm{univ}})$.
In particular, for $X$ as in [thm-pc-hilb-curves] over $S=\operatorname{Spec}(k)$
and a $k$-rational point $[D]\in\underline{\operatorname{Hilb}}^{d}_{X/k}$
corresponding to an effective Cartier divisor $D\subset X$ of degree $d$, the
restriction of $\mathcal{O}(D_{\mathrm{univ}})$ to the fibre $[D]\times X\cong X$
is $\mathcal{O}_X(D)$.
