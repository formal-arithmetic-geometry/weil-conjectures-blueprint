+++
id = "lem-weil-pbc-derived-stalk-conservative"
kind = "lemma"
title = "Conservativity of geometric stalks on the derived category"
lean = ["AlgebraicGeometry.Scheme.isIso_iff_isIso_sheafFiber_map_homologyFunctor_map_plus"]
order = 2074
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $T$ be a scheme and let $\mathcal A$ be a coefficient category as in
[lemma-weil-pbc-geometric-stalk-conservative] whose etale sheaves on $T$ form an
abelian category (for instance $R$-modules for a commutative ring $R$). Let
$K\to L$ be a morphism in the bounded-below derived category $\Dplus(T_{\Et})$
of $\mathcal A$-valued sheaves, formed as in [def-weil-pbc-derived-categories].
For every point $t$ of $T$ let $\bar t$ be the geometric point
[def-weil-pbc-geometric-stalks] at an algebraic closure of $\kappa(t)$. Then
$K\to L$ is an isomorphism of $\Dplus(T_{\Et})$ if and only if for every
point $t$ of $T$ and every integer $i$ the induced map

$$
 \mathcal H^i(K)_{\bar t}\longrightarrow\mathcal H^i(L)_{\bar t}
$$

of geometric stalks is an isomorphism.
