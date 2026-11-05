+++
id = "corollary-degreewise-duality-over-fields--1"
kind = "corollary"
title = "Degreewise duality for lisse Weil sheaves"
name_showing = false
order = 859001
aliases = ["bp-r258-1"]
lean = ["AlgebraicGeometry.WeilSheaf.exists_isPerfPair_compactlySupportedCohomology_dual", "AlgebraicGeometry.WeilSheaf.exists_isPerfPair_compactlySupportedCohomology_dual_mul"]
uses = ["definition-weil-structure", "definition-lisse-sheaves", "definition-tate-twists", "definition-frobenius-operator", "definition-perfect-pairing", "theorem-poincare-duality--3"]
+++
Let $k_0=\Fq$, let $\ell\ne\operatorname{char}(k_0)$ be prime, and let
$X_0/k_0$ be smooth and separated of finite type and pure dimension $d$.
Put $X=X_0\otimes_{k_0}\overline{k}_0$, and let $\cF$ be a lisse Weil sheaf
on $X_0$ with coefficients in $\Qbarl$. Write $\cF^\vee$ for its coefficient dual,
and $\cF^\vee(d)$ for its Tate twist, whose geometric Frobenius is that of
$\cF^\vee$ multiplied by $q^{-d}$. For $i,j\in\Z$ with $i+j=2d$, there
exist perfect pairings of finite-dimensional vector spaces

$$
P:\ H_c^i(X,\cF)\times H^j(X,\cF^\vee(d))\longrightarrow\Qbarl,
\qquad
P_0:\ H_c^i(X,\cF)\times H^j(X,\cF^\vee)\longrightarrow\Qbarl(-d).
$$

Writing $\Frob$ for geometric Frobenius on each cohomology group, they satisfy

$$
P(\Frob x,\Frob y)=P(x,y),\qquad
P_0(\Frob x,\Frob y)=q^dP_0(x,y).
$$

Here $\Qbarl(-d)$ denotes the line on which geometric Frobenius acts by
$q^d$. These assertions concern the existence of pairings; their
identification with the pairings induced by $\beta_K$ is not part of the
Lean statements. If $X_0$ is proper, transport along $H_c^i\simeq H^i$
gives the same assertions with $H_c^i$ replaced by $H^i$.
