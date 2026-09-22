+++
id = "lem-finrepair-modification-extension-zero"
kind = "lemma"
title = "Extension by zero under a proper modification"
order = 5199
lean = ["AlgebraicGeometry.Etale.pushforward_extensionByZero_of_properModification"]
+++
Let $\pi:Y\to X$ be proper and let $j:U\hookrightarrow X$ be open such that
$\pi^{-1}(U)\to U$ is an isomorphism. Write
$j':U'=\pi^{-1}(U)\hookrightarrow Y$. For an étale $\Lambda$-sheaf $G$ on
$U$, let $G'$ be its pullback to $U'$. Then
$$
\pi_*j'_!G'\simeq j_!G,\qquad R^q\pi_*j'_!G'=0\quad(q>0).
$$

## Proof

Extension by zero commutes with pullback here: the map
$\pi^*j_!G\to j'_!G'$ is obtained from its identity restriction on $U'$, and
is an isomorphism on every geometric stalk. Over a point of $U'$ both stalks
are the stalk of $G$; outside $U'$ both are zero. Adjunction supplies
$j_!G\to\pi_*j'_!G'$.

At a geometric point $\bar x$ of $U$, the fibre of $\pi$ is one geometric
point and the restricted sheaf is $G_{\bar x}$. At a geometric point of
$X\setminus U$, the entire fibre is disjoint from $U'$, and the restricted
sheaf is zero. The proper geometric-fibre formula therefore identifies the
displayed adjunction morphism with an isomorphism on all stalks, and makes
every positive-degree stalk $R^q\pi_*j'_!G'$ zero. Conservativity of
geometric stalks finishes the proof.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-extension-by-zero, def:weil-pbc-inverse-image, cor:weil-pbc-geometric-fiber-finite, lem:weil-pbc-geometric-stalk-conservative
