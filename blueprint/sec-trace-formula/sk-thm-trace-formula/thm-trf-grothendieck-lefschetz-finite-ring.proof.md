+++
kind  = "proof"
of    = "thm-trf-grothendieck-lefschetz-finite-ring"
+++
This is the case $\psi=u_1$ of the coefficient-morphism trace formula
[thm-trf-coefficient-morphism-trace-formula], whose hypotheses are
among those assumed here; that theorem is proved by reduction to curves
(closed subschemes of the affine line, the Weil $!$-pushforward along
the relative Frobenius factorization, and localization), and it uses
no compactification of $X_0$.

The scheme-Frobenius map $u_1=\varphi\circ\kappa_K$ of
[def-trf-iterated-weil-map] is an invertible Frobenius coefficient
morphism of [def-trf-frobenius-coefficient-morphism] (the example there),
and its iterates are the scheme-Frobenius maps $u_m$: both are built by
the same recursion, using the cocycle identity
[lem-trf-iterated-weil-cocycle] for $\varphi^{[m]}$ and the
multiplicativity of $\kappa^{(m)}$ in
[prop-trf-scheme-galois-comparison]. By
[prop-trf-graph-frobenius-operator],
$F_{c,m}(u_1)=T_c(u_m)=F_{c,K}^{\,m}$. For
$y\in X_0(\mathbf F_{q^m})$ the geometric point $\bar y$ is fixed by
$\Phi^m$ ([thm-trf-frobenius-fixed-points]), and the stalk map
$u_{m,\bar y}=\varphi^{[m]}_{\bar y}\circ\kappa^{(m)}_{K,\bar y}$ is the
local geometric Frobenius $F_{y,m}=\varphi^{[m]}_{\bar y}\circ\tau_{y,m}$
of [def-trf-frobenius-operators], since at the fixed point $\kappa^{(m)}$
induces the stalk transport $\tau_{y,m}$
([prop-trf-scheme-galois-comparison]). Substituting into
[thm-trf-coefficient-morphism-trace-formula] gives the boxed formula.
Grouping the rational points above a closed point and applying
[lem-trf-frobenius-degree-formula] and
[lem-trf-local-frobenius-conjugacy] gives the second formula.
