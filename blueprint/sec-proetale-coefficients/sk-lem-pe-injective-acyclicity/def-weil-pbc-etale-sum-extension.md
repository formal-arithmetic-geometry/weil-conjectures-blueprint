+++
id = "def-weil-pbc-etale-sum-extension"
kind = "definition"
title = "Extension by zero along an etale map"
order = 966
lean = ["AlgebraicGeometry.Etale.etaleLowerShriek"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site"]
+++
Let $v:W\to X$ be etale [def-weil-pbc-etale-site], let $\Lambda$ be a
commutative ring, and let $M$ be a sheaf of $\Lambda$-modules on $W_{\Et}$, as in
[def-weil-pbc-etale-sheaves]. Define $v_!M$ by sheafifying the presheaf

$$
 V\longmapsto\bigoplus_{s\in\operatorname{Hom}_X(V,W)}M(V,s)
$$

on $X_{\Et}$. Here $(V,s)$ denotes $V$ as an etale $W$-scheme, and restriction
sends the summand indexed by $s$ to the summand indexed by its restriction.
Equivalently, $v_!$ is the left Kan extension along the functor
$W_{\Et}\to X_{\Et}$, $(V\to W)\mapsto(V\to W\to X)$, followed by
sheafification. When $v$ is an open immersion this is the usual extension by
zero: there is at most one such lift.
