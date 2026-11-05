+++
id = "lemma-external-duality-trace-morphism--1"
kind = "lemma"
title = "External duality (1)"
name_showing = false
order = 910001
aliases = ["bp-r275-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_kunnethVerdierMap"]
uses = ["definition-constructible-sheaves", "definition-verdier-dual-evaluation", "proposition-six-operations-dctf"]
+++
Let $\ell$ be a prime and let $k$ be a field of positive characteristic
different from $\ell$. Let $X,Y$ be separated $k$-schemes of finite type,
with projections $p_X,p_Y$ from $X\times_kY$. For
$M\in\Dbc(X,\Qbarl)$ and $N\in\Dbc(Y,\Qbarl)$, the canonical
Künneth–Verdier map is an isomorphism

$$
\kappa_{M,N}:M\boxtimes\mathbb D_YN
\xrightarrow{\sim}\cHom_{\Qbarl}(p_Y^*N,p_X^!M).
$$

The map is the tensor–Hom adjoint of the pairing obtained by evaluation
$N\otimes^{\mathbf L}\mathbb D_YN\to\omega_Y$ followed by the
exceptional Künneth map $M\boxtimes\omega_Y\to p_X^!M$.
Taking $Y=X$ and $M=N=K$ gives
$P_X=K\boxtimes\mathbb D_XK\xrightarrow{\sim}
\cHom_{\Qbarl}(p_2^*K,p_1^!K)$.
