+++
id = "sk-prop-smooth-proper-purity"
kind = "theorem"
title = "Relative smooth proper purity"
lean = ["AlgebraicGeometry.WeilSheaf.smooth_proper_relative_purity"]
order = 4329
uses = ["sk-d-real-weights", "sk-prop-sf-comp-proper", "sk-thm-dl-general-sheaf", "sk-thm-sfb-proper-base-change", "sk-thm-derived-duality", "sk-thm-frobenius", "sk-thm-smooth-base-change"]
tags = ["sketch"]
+++
Let $f_0:X_0\to Y_0$ be smooth proper of pure relative dimension $d$,
and let $F$ be a lisse Weil sheaf, punctually $\iota$-pure of weight
$w$ ([sk-d-real-weights]). For every $i$, the canonical identification

$$
 R^if_{0!}F=R^if_{0*}F
$$

is Weil-equivariant, and this constructible sheaf is punctually
$\iota$-pure of weight $w+i$. In particular, it is mixed of the
single weight $w+i$.

*Complement.* The sheaf $R^if_{0*}F$ is moreover lisse.
