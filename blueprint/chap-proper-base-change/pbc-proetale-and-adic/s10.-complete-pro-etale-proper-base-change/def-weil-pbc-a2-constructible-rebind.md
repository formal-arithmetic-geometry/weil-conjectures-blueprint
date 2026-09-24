+++
id = "def-weil-pbc-a2-constructible-rebind"
kind = "definition"
title = "A2 constructible rebinding certificate"
order = 2005
uses = ["def-weil-pbc-completed-reduction-square", "def-weil-pbc-level-map-corners"]
+++
Specialize A2 to $\Lambda=\mathbf Z_\ell$, $I=(\ell)$, and
$P_n=\Lambda/\ell^n$. For a scheme $Z$ write

$$
\mathsf C(Z):=D^b_c(Z_{\mathrm{proet}},\mathbf Z_\ell),
\qquad
\mathsf C_n(Z):=D^b_c(Z_{\mathrm{proet}},\mathbf Z/\ell^n)
$$

for the full subcategories defined, respectively, by
`def:weil-a2-dbc-zl` and `def:weil-a2-dbc-torsion`.

Fix a proper Cartesian square $\square$ as in S10. An A2 constructible
rebinding certificate for $K\in\mathsf C(X)$ consists of the following
displayed data.

1. An A2 proper complete-base-change datum, hence compatible etale-origin
objects
$$
L_n\in D^b_c(X_{\mathrm{et}},\mathbf Z/\ell^n),\qquad
\alpha_n:\epsilon_X^{-1}L_n\xrightarrow{\sim}K_n,
$$
including their transition equations. The superscript $b$ is part of
the certificate: one interval $[d_0,d_1]$ works for every $L_n$ and
every $K_n$.
1. On each of $X,X',Y,Y'$, one finite stratification, each stratum having
finitely many connected components, and A2 finite-torsion
constructibility witnesses, uniform in $n$, for every finite object
occurring in S7–S10. On $Y'$ these are, in particular, the four
objects $A_n,B_n,C_n,D_n$ of Definition
[def-weil-pbc-level-map-corners]; their witnesses use one common
interval and one common refinement.
1. The finite exceptional-direct-image values for the identity
compactifications of the proper maps,
$$
Rf_!^{(1,f)}K_n\in\mathsf C_n(Y),\qquad
Rf'_!{}^{(1,f')}E_n\in\mathsf C_n(Y'),
$$
with the A2 torsion witnesses retained by the typed A1 input and with
their transition squares. The certificate records their displayed
identifications with $Rf_*K_n$ and $Rf'_*E_n$.
1. A2 constructible-stratification witnesses for
$$
S(K):=Lg^*_{\mathrm{comp}}Rf_*K,
\qquad
T(K):=Rf'_*L(g')^*_{\mathrm{comp}}K
$$
in $\mathsf C(Y')$. Their finite reductions are required to be the
objects identified by the maps $\alpha_n$ and $\delta_n$ of Definition
[def-weil-pbc-completed-reduction-square].

Let $\mathsf C_\square(X)$ be the full subcategory of $\mathsf C(X)$ on
objects for which the type of such certificates is nonempty. Certificates
are membership witnesses only; morphisms in $\mathsf C_\square(X)$ are the
ambient A2 morphisms, so no selected witness enters their equality.

Unresolved dependencies: def:weil-a1-rfshriek-selected, def:weil-a1-torsion-derived-category, def:weil-a2-constructible-stratification-witness, def:weil-a2-dbc-torsion, def:weil-a2-dbc-zl, def:weil-a2-finite-level-etale-origin-realization, def:weil-a2-proper-complete-base-change-datum, def:weil-a2-torsion-constructibility-witness
