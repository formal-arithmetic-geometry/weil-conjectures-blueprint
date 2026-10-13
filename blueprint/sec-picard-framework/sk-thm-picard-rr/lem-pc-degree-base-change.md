+++
id = "lem-pc-degree-base-change"
kind = "lemma"
title = "Degree: base change and tensor products"
order = 747
uses = ["def-pc-base-change", "def-pc-degree-line-bundle", "def-pc-dimension", "def-pc-divisor-line-bundle", "def-pc-euler-characteristic", "def-sc-divisor", "def-sc-effective-cartier-divisor", "def-sc-invertible-module", "lem-pc-affine-vanishing", "lem-pc-euler-additive", "lem-pc-euler-characteristic-well-defined", "lem-pc-finite-support-hi", "lem-pc-flat-base-change-cohom", "lem-pc-divisor-line-bundle-agrees-sc", "lem-pc-proper-base-change", "lem-sc-point-cartier", "lem-sc-smooth-regular", "lem-sc-regular-dim1-dvr"]
+++
Let $k$ be a field, $X$ a proper scheme over $k$ of dimension $\le1$
(a proper curve), and let $\mathcal{L},\mathcal{M}$ be invertible
$\mathcal{O}_X$-modules.

1. (Base change) For a field extension $K/k$:
$\deg_{X_K}(\mathcal{L}\otimes_kK)=\deg_X(\mathcal{L})$.
1. (Tensor with an effective divisor) If $D\subset X$ is an
effective Cartier divisor and $\mathcal{M}=\mathcal{O}_X(D)$, then
$$
\chi(X,\mathcal{L}\otimes\mathcal{M})=\deg(\mathcal{L})+\chi(X,\mathcal{M}),\qquad
\deg(\mathcal{L}\otimes\mathcal{M})=\deg(\mathcal{L})+\deg(\mathcal{M}),
$$
and for a finite sum $D=\sum_in_i[P_i]$ of $k$-rational points
$\deg(\mathcal{O}_X(D))=\sum_in_i$.
1. (Additivity) For a short exact sequence of coherent modules
$0\to\mathcal{F}_1\to\mathcal{F}_2\to\mathcal{F}_3\to0$:
$\chi(X,\mathcal{F}_2)=\chi(X,\mathcal{F}_1)+\chi(X,\mathcal{F}_3)$
([lem-pc-euler-additive]).
