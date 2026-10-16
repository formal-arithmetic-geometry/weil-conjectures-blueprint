+++
id = "lem-sc-flat-base-change-coherent"
kind = "lemma"
title = "Flat base change for coherent cohomology"
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_H_pullback_linearEquiv"]
order = 721
uses = ["lem-sc-cech-spectral"]
+++
Let $X$ be a proper scheme over a field $k$, $k\to k'$ a flat
$k$-algebra (e.g. a field extension) and $\mathcal F$ a
quasi-coherent sheaf on $X$. Then for all $i\geq0$

$$
H^i(X_{k'},\mathcal F_{k'})\cong H^i(X,\mathcal F)\otimes_kk'.
$$

In particular, if $k'\supseteq k$ is an extension of algebraically
closed fields and $\mathcal F=\mathcal O_X$, then

$$
\dim_{k'}H^i(X_{k'},\mathcal O_{X_{k'}})=\dim_kH^i(X,\mathcal O_X).
$$
