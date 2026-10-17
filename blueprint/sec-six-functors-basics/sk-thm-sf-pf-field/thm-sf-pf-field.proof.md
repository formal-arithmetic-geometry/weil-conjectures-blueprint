+++
kind  = "proof"
of    = "thm-sf-pf-field"
+++
*Compatibility.* The projection transformation of [def-sf-pf] is built from
units, counits and the associativity of $\otimes^{\mathbf L}$. Localization
$\mathcal O_E\to E$ and extension of scalars $E\to F\to\Qlb$ are flat
($E_X=\mathcal O_{E,X}[1/\ell]$ by [sk-prop-sfb-qlbar-colimit-x], and
[sk-prop-sfb-finite-extension-compatibility]), and their coefficient
comparisons for $Rf_!$, $Lf^*$ and $\otimes^{\mathbf L}$ are isomorphisms
respecting these units, counits and associativity maps
([sk-prop-scalar-six]). Hence they carry $\operatorname{PF}$ to
$\operatorname{PF}$, which is the compatibility in the statement.

*$\Lambda=E$.* Fix $L$. Both sides of $\operatorname{PF}_{f,K,L}$ are exact
functors of $K$, so the $K$ for which it is an isomorphism form a
subcategory closed under cones and shifts. By [sk-lem-integral-models] (4)
it suffices to treat $K=K_0[1/\ell]$ with $K_0=a_!L'_0\in\Dbc(X,\mathcal O_E)$,
and in the same way, fixing such a $K$, to treat $L=L_0[1/\ell]$ with
$L_0\in\Dbc(Y,\mathcal O_E)$. Then $\operatorname{PF}_{f,K,L}$ is the
localization of $\operatorname{PF}_{f,K_0,L_0}$, an isomorphism by
[thm-sf-pf-adic].

*$\Lambda=\Qlb$.* By [sk-thm-sfb-qlbar-two-colimit] (3) there are finite
extensions over which $K$ and $L$ are defined; passing to their compositum
$E$ by extension of scalars, $K\cong(K_E)_{\Qlb}$ and $L\cong(L_E)_{\Qlb}$ with
$K_E\in\Dbc(X,E)$ and $L_E\in\Dbc(Y,E)$. By the compatibility,
$\operatorname{PF}_{f,K,L}$ is the extension of scalars of
$\operatorname{PF}_{f,K_E,L_E}$, an isomorphism by the case $\Lambda=E$.
