+++
id = "prop-pur-affine-line-orientation-uniqueness"
kind = "theorem"
title = "Uniqueness of the global orientation"
order = 2292
tags = ["latex:proposition"]
uses = ["def-pur-conventions", "def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-scheme-morphism-properties", "lem-pur-gysin-structure", "thm-pur-affine-line-orientation", "thm-pur-rank-one-local-calculation"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting), let $Y$ and $\kappa(t)$ be as in
[thm-pur-affine-line-orientation]. The restriction of the
homomorphism group to
geometric points is an
injective map

$$
\operatorname{Hom}_{D(Y,\Lambda)}
\bigl(\Lambda_Y,Rs^!\Lambda_{\mathbf A^1_Y}(1)[2]\bigr)
\longrightarrow
\prod_{\bar y\to Y}H^2_{s(\bar y)}(\mathbf A^1_{\bar y},\Lambda(1)),
$$

whose image contains the family with every component $1\in\Lambda$ (by
[thm-pur-rank-one-local-calculation] and the normalization of
[thm-pur-affine-line-orientation]). Consequently
$\operatorname{pur}_s$ is the unique global morphism whose pullback to
every geometric point is the normalized class $1$.
