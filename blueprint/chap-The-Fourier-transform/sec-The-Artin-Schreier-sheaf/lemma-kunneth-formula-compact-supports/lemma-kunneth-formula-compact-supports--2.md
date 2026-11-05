+++
id = "lemma-kunneth-formula-compact-supports--2"
kind = "lemma"
title = "Base change for compactly supported direct image"
order = 1225002
aliases = ["bp-r377-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange_padicAlgCl"]
+++
Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be a prime,
and let $E$ be a field that is an admissible coefficient ring, for instance $\overline{\mathbf Q}_\ell$. Let $f:X\to S$ and $g:Y\to S$
be morphisms of separated schemes of finite type over $k$, and let
$p_1:X\times_SY\to X$ and $p_2:X\times_SY\to Y$ be the projections.
The compact-support base-change map

$$
f^*Rg_!\longrightarrow Rp_{1!}p_2^*
$$

is an isomorphism of functors on bounded constructible $E$-complexes.
For $K$ on $X$ and $L$ on $Y$, its inverse therefore induces

$$
Rf_!(K\otimes Rp_{1!}p_2^*L)\simeq Rf_!(K\otimes f^*Rg_!L).
$$
