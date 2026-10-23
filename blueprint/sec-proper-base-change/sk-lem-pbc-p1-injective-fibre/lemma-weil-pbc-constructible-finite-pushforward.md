+++
id = "lemma-weil-pbc-constructible-finite-pushforward"
kind = "lemma"
title = "Constructible sheaves reduce to finite pushforwards"
lean = ["AlgebraicGeometry.Etale.exists_mono_biproduct_lowerStar"]
order = 1579
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions"]
+++
Let $\Lambda$ be a Noetherian commutative ring, let $U$ be a quasi-compact and
quasi-separated scheme, and let $C$ be a constructible sheaf of
$\Lambda$-modules on $U_{\Et}$ [def-weil-pbc-constructible-complexes]. Then there
is a monomorphism of sheaves of $\Lambda$-modules

$$
 C\hookrightarrow\bigoplus_{i=1}^m(h_i)_*\underline{M_i},
$$

where every $h_i:V_i\to U$ is finite and locally of finite presentation, every
$M_i$ is a finitely generated $\Lambda$-module, $\underline{M_i}$ is the constant
sheaf on $V_{i,\Et}$, and $(h_i)_*$ is the direct image
[def-weil-pbc-direct-image]. (For instance, for $\Lambda$ finite the $M_i$ are
finite.)
