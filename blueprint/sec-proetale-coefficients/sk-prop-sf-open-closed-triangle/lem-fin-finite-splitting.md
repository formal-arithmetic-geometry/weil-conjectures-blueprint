+++
id = "lem-fin-finite-splitting"
kind = "lemma"
title = "Etale splitting of a finite morphism"
lean = ["AlgebraicGeometry.Scheme.Hom.SplitNbhd", "AlgebraicGeometry.Scheme.Hom.SplitNbhd.exists_hom"]
order = 1094
uses = ["def-weil-pbc-geometric-fibre", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit"]
+++
Let $f:X\to S$ be a finite morphism and let $\bar s:\operatorname{Spec}\Omega\to S$
be a geometric point with $\Omega$ algebraically closed. Call a pointed etale
neighbourhood $(V,\bar v)$ of $\bar s$ *split* if it comes with a decomposition
$$
X\times_SV=\bigsqcup_{\bar x}X_{\bar x}
$$
into pairwise disjoint open-and-closed subschemes indexed by the points $\bar x$
of the finite geometric fibre of $f$ over $\bar s$ [def-weil-pbc-geometric-fibre],
such that $X_{\bar x}$ contains the point $(\bar v,\bar x)$ of $X\times_SV$. Then
every pointed etale neighbourhood of $\bar s$ is refined by a split one: for
every $(U,\bar u)$ there are a split neighbourhood $(V,\bar v)$ and a morphism
$(V,\bar v)\to(U,\bar u)$ of pointed etale neighbourhoods. Each piece
$X_{\bar x}\to V$ is finite, being a closed subscheme of the finite $V$-scheme
$X\times_SV$.
