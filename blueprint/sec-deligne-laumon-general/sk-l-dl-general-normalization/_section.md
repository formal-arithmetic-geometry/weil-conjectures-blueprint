+++
id = "sk-l-dl-general-normalization"
kind = "lemma"
title = "Relative Noether normalization on finite strata"
order = 4078
lean = ["AlgebraicGeometry.exists_dense_isFinite_toIteratedAffineLine"]
tags = ["sketch"]
+++
Let $f:X_0\to Y_0$ be a morphism of finite type. There are finite
partitions of $X_0$ and of $Y_0$ into locally closed pieces such that
each piece of $X_0$ lies over a piece $V$ of $Y_0$, and its map to $V$
factors through a finite morphism to $\mathbf A^d_V$ for some $d$.

*Complement (generic step).* If $f_0:X_0\to Y_0$ is a dominant affine
morphism of finite type between integral schemes whose generic fibre
has dimension $r$, there are a dense open $V_0\subseteq Y_0$ and a
finite surjective morphism $\nu_0$ factoring the restriction of $f_0$
over $V_0$ as

$$
f_0^{-1}(V_0)\xrightarrow{\nu_0}\mathbf A^r_{V_0}
\xrightarrow{\pi_0}V_0,
$$

where $\pi_0$ is the projection of the $r$-fold relative affine line,
a composition of $r$ affine-line projections.
