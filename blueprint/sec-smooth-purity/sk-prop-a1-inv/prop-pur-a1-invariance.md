+++
id = "prop-pur-a1-invariance"
kind = "theorem"
title = "Invariance along the affine line"
order = 2301
tags = ["latex:proposition"]
uses = ["def-pur-conventions", "def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-a1-components", "lem-pur-lisse-uniqueness"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $Y$ be a separated finite-type $k$-scheme, let
$a:\mathbf A^1_Y\to Y$ be the projection, and let
$i_0,i_1:Y\to\mathbf A^1_Y$ be the sections $t=0$ and $t=1$, so that
$a\circ i_0=a\circ i_1=\operatorname{id}_Y$ and hence
$i_0^*a^*\cong\operatorname{id}\cong i_1^*a^*$. Let
$F\in D^b_{ctf}(\mathbf A^1_Y,\Lambda)$ and
$C\in D^b_{ctf}(Y,\Lambda)$, and let
$\theta:i_1^*F\xrightarrow{\sim}C$ be an isomorphism. Suppose given an
etale covering family $\{u_\alpha:Y_\alpha\to Y\}$ by separated
finite-type schemes such that:

- *local shape.* for every $\alpha$ the restriction
$F|_{\mathbf A^1_{Y_\alpha}}$ is a shift and twist
$\mathcal L_\alpha(m_\alpha)[n_\alpha]$ of a finite locally
constant $\Lambda$-sheaf $\mathcal L_\alpha$ of rank one on
$\mathbf A^1_{Y_\alpha}$;
- *normalized local comparisons.* for every $\alpha$ there is an
isomorphism
$\kappa_\alpha:F|_{\mathbf A^1_{Y_\alpha}}\xrightarrow{\sim}
a^*C|_{\mathbf A^1_{Y_\alpha}}$ whose restriction along the section
$t=1$ is $\theta|_{Y_\alpha}$, i.e.
$i_1^*\kappa_\alpha=\theta|_{Y_\alpha}$ under
$i_1^*a^*C\cong C$.

Then:

1. *gluing.* There is a unique isomorphism
$\kappa:F\xrightarrow{\sim}a^*C$ with
$\kappa|_{\mathbf A^1_{Y_\alpha}}=\kappa_\alpha$ for every
$\alpha$.
1. *uniqueness.* $\kappa$ is the unique isomorphism
$F\xrightarrow{\sim}a^*C$ with $i_1^*\kappa=\theta$; in
particular it does not depend on the cover or on the local
comparisons $\kappa_\alpha$.
1. *constancy.* Restriction along $i_0$ and $i_1$ gives a
canonical identification
$$
i_0^*F\xrightarrow{\ i_0^*\kappa\ }i_0^*a^*C\cong C
\cong i_1^*a^*C\xleftarrow{\ i_1^*\kappa\ }i_1^*F,
$$
the right-hand map being $\theta$: the object $F$ is constant
along the $\mathbf A^1$-direction, its values at $t=0$ and
$t=1$ agreeing.
