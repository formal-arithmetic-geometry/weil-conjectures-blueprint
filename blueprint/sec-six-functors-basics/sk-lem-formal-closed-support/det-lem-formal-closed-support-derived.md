+++
id = "det-lem-formal-closed-support-derived"
kind = "lemma"
title = "Sections with support: derived adjunction and fiber formula"
order = 2155
uses = ["det-lem-formal-closed-support-sheaves", "sk-prop-sf-open-closed-triangle"]
+++
In the situation of [det-lem-formal-closed-support-sheaves], let
$R\underline\Gamma_Z\colon\D(X_{\mathrm{proét}},\Lambda)\to\D(Z_{\mathrm{proét}},\Lambda)$ be the
right derived functor of $\underline\Gamma_Z$, computed on K-injective
complexes.

1. $R\underline\Gamma_Z$ is right adjoint to
   $i_*\colon\D(Z_{\mathrm{proét}},\Lambda)\to\D(X_{\mathrm{proét}},\Lambda)$, and for
   $A\in\D(Z_{\mathrm{proét}},\Lambda)$, $K\in\D(X_{\mathrm{proét}},\Lambda)$
   $$
   R\operatorname{Hom}_X(i_*A,K)\simeq R\operatorname{Hom}_Z(A,R\underline\Gamma_ZK).
   $$
2. For an injective $\Lambda_X$-module $I$, the unit $I\to j_*j^*I$ is surjective.
3. There is a distinguished triangle, natural in $K$,
   $$
   i_*R\underline\Gamma_ZK\longrightarrow K\longrightarrow Rj_*j^*K\longrightarrow i_*R\underline\Gamma_ZK[1]
   $$
   in $\D(X_{\mathrm{proét}},\Lambda)$, whose second arrow is the unit of $j^*\dashv Rj_*$.
   Consequently
   $$
   R\underline\Gamma_ZK\simeq i^*\fib\bigl(K\longrightarrow Rj_*j^*K\bigr)\quad\text{in }\D(Z_{\mathrm{proét}},\Lambda).
   $$
