+++
id = "prop-constructible-t-structure"
kind = "theorem"
title = "Constructible t-structure and pullback comparison"
order = 75
tags = ["latex:proposition"]
uses = ["def-constructible-truncation-functors", "def-derived-pullback", "def-weil-base-field", "def-weil-finite-coefficient-datum", "def-weil-frobenius", "prop-constructible-truncations", "prop-pullback-constructibility"]
+++
Fix a scheme $Y$, an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and
$\Lambda\in\{E,\Qlb\}$. The truncation functors of
Definition [def-constructible-truncation-functors] form a bounded
$t$-structure on $D^b_c(Y,\Lambda)$. For every scheme automorphism
$h:Y\to Y$, derived pullback $Lh^*$ preserves
$D^b_c(Y,\Lambda)$, is $t$-exact, and has a natural comparison

$$
c_{h,i}(K):Lh^*\mathcal H^i(K)
\xrightarrow{\sim}\mathcal H^i(Lh^*K)
$$

for every $i\in\mathbf Z$ and $K\in D^b_c(Y,\Lambda)$. In particular,
if $Y_0$ is of finite type over $k_0$,
$Y=Y_0\times_{k_0}k$, and $h=g_Y$ is geometric Frobenius, write this
comparison as $c_i(K)=c_{g_Y,i}(K)$.
