+++
id = "lemma-triviality-fibres--1"
kind = "lemma"
title = "Triviality on fibres (1)"
name_showing = false
order = 1478002
aliases = ["bp-r459-1"]
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_iso_unit_fiber_iff"]
+++
Let $f:X\to T$ be proper with geometrically integral fibres, and let
$\mathcal A$ and $\mathcal B$ be invertible sheaves on $X$ with an
isomorphism $\mathcal A\otimes\mathcal B\simeq\mathcal O_X$.
For every $t\in T$,

$$
\mathcal A_t\simeq\mathcal O_{X_t}
\quad\Longleftrightarrow\quad
h^0(X_t,\mathcal A_t)>0\ \text{and}\ h^0(X_t,\mathcal B_t)>0.
$$

Taking $X=P\times_k T$, $\mathcal A=\mathcal L$ and
$\mathcal B=\mathcal L^{-1}$, this says that $\mathcal L_t$ is trivial if and only if
$H^0(P_t,\mathcal L_t)\ne0$ and $H^0(P_t,\mathcal L_t^{-1})\ne0$.
