+++
kind  = "proof"
of    = "thm-sf-pf-adic"
+++
*The general criterion.* Objects of $\Dbc(Y,\mathcal O_E)$ are derived
$\pi_E$-complete ([sk-prop-integral-criterion]), and derived complete
complexes form a triangulated subcategory, so the cone $C$ of a morphism
$u$ in $\Dbc(Y,\mathcal O_E)$ is derived complete. Reduction modulo $\pi_E$ is
the cone of multiplication by $\pi_E$, hence exact, so if $u/\pi_E$ is an
isomorphism then $C\otimes^{\mathbf L}_{\mathcal O_{E,Y}}(A_{E,1})_Y=0$ and
$C=0$ by derived Nakayama ([sk-lem-pe-derived-nakayama]).

*The projection formula.* Both sides of $\operatorname{PF}_{f,K,L}$ lie in
$\Dbc(Y,\mathcal O_E)$: $Rf_!$ ([sk-def-sfb-dc-lower-shriek]) and $Lf^*$ preserve the condensed integral
constructible categories, and so does $\otimes^{\mathbf L}$ ([sk-lem-int-tensor]).
Reduction $\mathcal O_E\to A_{E,n}$ commutes with $Rf_!$, $Lf^*$ and
$\otimes^{\mathbf L}$ through the coefficient comparisons of
[sk-prop-scalar-six], which respect the units, counits and associativity
maps from which $\operatorname{PF}$ is built in [def-sf-pf]; hence the
reduction of $\operatorname{PF}_{f,K,L}$ is $\operatorname{PF}_{f,K_n,L_n}$. The
objects $K_n,L_n$ are finite-Tor constructible over $A_{E,n}$
([sk-prop-scalar-six]), so $\operatorname{PF}_{f,K_n,L_n}$ is an isomorphism by
[thm-sf-pf-finite]. The case $n=1$ and the general criterion show that
$\operatorname{PF}_{f,K,L}$ is an isomorphism. This is the argument of
[det-thm-sf-pf-adic-projection] for a compactifiable $f$ instead of a proper
$p$.
