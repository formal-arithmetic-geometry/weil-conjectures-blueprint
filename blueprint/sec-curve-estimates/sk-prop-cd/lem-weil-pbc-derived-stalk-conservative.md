+++
id = "lem-weil-pbc-derived-stalk-conservative"
kind = "lemma"
title = "Conservativity of geometric stalks on the derived category"
order = 992
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $T$ be a scheme and let $K\to L$ be a morphism of complexes in
$\Dplus(T_{\Et})$ of [def-weil-pbc-derived-categories]. Then $K\to L$ is an
isomorphism of $\Dplus(T_{\Et})$ if and only if for every geometric point
[def-weil-pbc-geometric-stalks] $\bar t$ of $T$ and every integer $i$ the
induced map

$$
 \mathcal H^i(K)_{\bar t}\longrightarrow\mathcal H^i(L)_{\bar t}
$$

of geometric stalks is an isomorphism.
