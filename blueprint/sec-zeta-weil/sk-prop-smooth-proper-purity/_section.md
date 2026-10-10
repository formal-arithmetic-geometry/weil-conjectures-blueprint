+++
id = "sk-prop-smooth-proper-purity"
kind = "proposition"
title = "Smooth-proper purity"
order = 2867
lean = ["TraceDatum.isPureOfWeight_map_P_of_pairing"]
uses = ["sk-d-dl-general-weights", "sk-d-real-weights", "sk-def-cohfamily", "sk-def-sf-operations", "sk-prop-sf-comp-proper", "sk-thm-dl-general-sheaf", "sk-thm-poincare-duality", "sk-thm-properbasechange", "sk-thm-purity-transport", "sk-thm-sf-dual-perfect", "sk-thm-sf-tensor-hom", "sk-thm-smooth-base-change", "sk-thm-smooth-purity"]
tags = ["sketch"]
+++
Let $f_0:X_0\to Y_0$ be a smooth proper morphism of separated finite-type
$k_0$-schemes of pure relative dimension $d$ (no admissibility hypothesis on
$f_0$ or the structure morphisms: the exceptional adjoints are the
unconditional ones of [sk-def-sf-operations](vi)), and let $\mathcal F_0$ be a lisse
Weil sheaf on $X_0$ which is punctually $\iota$-pure of weight $w$ in the
sense of [sk-d-real-weights]. Then for every $i$:

- **(a)** the canonical map
$R^{i}f_{0!}\mathcal F_0\to R^{i}f_{0*}\mathcal F_0$ is an isomorphism and
this sheaf is lisse;
- **(b)** it is punctually $\iota$-pure of weight $w+i$.

In the absolute case $Y_0=\Spec k_0$, $\mathcal F_0=(\Ql)_{X_0}$ — the
setting of [sk-def-cohfamily] — clause (b) says that every
eigenvalue $\alpha$ of geometric Frobenius on $H^{i}(X,\Ql)$ satisfies
$|\iota(\alpha)|=q^{i/2}$.
