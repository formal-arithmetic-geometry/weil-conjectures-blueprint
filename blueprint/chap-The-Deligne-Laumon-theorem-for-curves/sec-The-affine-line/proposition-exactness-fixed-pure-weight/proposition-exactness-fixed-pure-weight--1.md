+++
id = "proposition-exactness-fixed-pure-weight--1"
kind = "proposition"
title = "Exactness on a geometrically connected curve"
name_showing = false
order = 1295001
aliases = ["bp-r401-1"]
lean = ["AlgebraicGeometry.shortExact_map_directImage"]
uses = ["definition-weil-structure", "definition-lisse-sheaves", "proposition-topos-functoriality", "definition-weights"]
+++
Let $k_0=\Fq$, let $\ell$ be a prime different from the characteristic
of $k_0$, and fix $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$
and $w\in\mathbf R$. Let $C_0$ be a smooth, separated, geometrically
connected curve of finite type over $k_0$, and let
$j_0:U_0\hookrightarrow C_0$ be a quasi-compact dense open immersion.
Write $j:U\hookrightarrow C$ for its base change to
$k=\overline{\mathbf F}_q$. If $0\to F_1\to F\to F_2\to0$ is a
short exact sequence of lisse Weil $\overline{\mathbf Q}_\ell$-sheaves
on $U_0$, with $F_1$ and $F_2$ punctually $\iota$-pure of weight $w$,
then the sequence

$$
0\longrightarrow j_*F_1\longrightarrow j_*F
\longrightarrow j_*F_2\longrightarrow0
$$

is exact.

These are the hypotheses of the Lean declaration; purity is assumed
only for the two outer terms. The geometrically connected case includes
$C_0=\mathbf A^1_{k_0}$, where the declaration is used in the proof of
the affine-line weight bound.
