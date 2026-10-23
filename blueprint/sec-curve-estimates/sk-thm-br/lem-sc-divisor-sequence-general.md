+++
id = "lem-sc-divisor-sequence-general"
kind = "lemma"
title = "The divisor sequence of an integral regular scheme"
order = 1359
uses = ["lem-sc-regular-dim1-dvr"]
lean = ["AlgebraicGeometry.Scheme.exists_shortExact_divisorSequence"]
+++
Let $X$ be an integral regular locally noetherian scheme (for
example a connected smooth scheme over a field) with generic point
$j:\eta=\operatorname{Spec}k(X)\to X$, let $X^{(1)}$ be the set of
codimension-one points of $X$, and for $x\in X^{(1)}$ let
$i_x:\operatorname{Spec}k(x)\to X$ be the canonical morphism (not a
closed immersion unless $x$ is closed). There is a morphism
$\operatorname{div}$ of etale sheaves on $X$ such that the sequence

$$
0\longrightarrow\mathbf G_m\longrightarrow j_*\mathbf G_{m,\eta}
\xrightarrow{\ \operatorname{div}\ }\bigoplus_{x\in X^{(1)}}i_{x*}\mathbf Z\longrightarrow0
$$

is exact, where the first map is the unit
$\mathbf G_m\to j_*j^*\mathbf G_m$.
