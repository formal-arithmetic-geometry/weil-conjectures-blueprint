+++
id = "prop-weil-pbc-gabber-affine-comparison"
kind = "theorem"
title = "Gabber affine comparison"
order = 1189
tags = ["latex:proposition"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-etale-degree-zero", "lemma-weil-pbc-gabber-effacement"]
+++
Let $(A,I)$ be an affine henselian pair, $T=\operatorname{Spec}A$ and
$T_0=\operatorname{Spec}(A/I)$. For every torsion etale sheaf $F$ on $T$, with
restriction $F_0$ to $T_0$, restriction induces isomorphisms

$$
 H^q(T,F)\xrightarrow{\sim}H^q(T_0,F_0)
 \qquad(q\geq0).
$$

Consequently, if $X$ is an affine scheme over $T$ with closed fibre
$X_0=X\times_TT_0$ and $F$ is a torsion etale sheaf on $X$, then
restriction induces isomorphisms

$$
 \varinjlim_{(U,U_0)}H^q(U,F|_U)\xrightarrow{\sim}H^q(X_0,F|_{X_0})
 \qquad(q\geq0),
$$

the colimit running over the affine etale neighbourhoods $U\to X$ of $X_0$
(etale morphisms inducing an isomorphism $U\times_XX_0\cong X_0$). The map
$H^q(X,F)\to H^q(X_0,F|_{X_0})$ itself need not be an isomorphism when $X$
is not a henselian pair: for $A=k[[t]]$, $I=(t)$ and
$X=\operatorname{Spec}k((t))$ the closed fibre is empty while
$H^0(X,\mathbf Z/n)=\mathbf Z/n$.
