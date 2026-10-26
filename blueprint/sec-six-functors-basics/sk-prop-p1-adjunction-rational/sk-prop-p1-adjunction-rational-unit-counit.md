+++
id = "det-prop-p1-adjunction-rational-unit-counit"
kind = "definition"
title = "Unit and counit for the rational projective line"
order = 2420
uses = ["sk-prop-diagonal-tower", "sk-thm-sf-pf-field", "def-amb-p1-trace"]
+++
Let $\Lambda=E$ or $\Qlb$, $q:P=\mathbf P^1_Y\to Y$, $W=P\times_YP$ with
projections $p_1,p_2:W\to P$ and diagonal $\Delta:P\to W$, and let
$\delta_\Lambda:\Delta_*\Lambda_P\to\Lambda_W(1)[2]$ and
$\operatorname{Tr}_q:Rq_*\Lambda_P(1)[2]\to\Lambda_Y$ be the morphisms of
[sk-prop-diagonal-tower]. All functors below are the restrictions to the
categories $\Loc(\Dbc(-,\Lambda))$.

1. For $M\in\Loc(\Dbc(P,\Lambda))$ there is a natural isomorphism
   $\Delta_*M\simeq p_1^*M\otimes^{\mathbf L}\Delta_*\Lambda_P$.
2. The *unit* $\eta_M:M\to q^*Rq_*M(1)[2]$ is the composite
   $$
   M=Rp_{2*}\Delta_*M\simeq Rp_{2*}(p_1^*M\otimes^{\mathbf L}\Delta_*\Lambda_P)
   \xrightarrow{Rp_{2*}(1\otimes\delta_\Lambda)}Rp_{2*}\bigl(p_1^*M(1)[2]\bigr)
   \xrightarrow{\ \sim\ }q^*Rq_*M(1)[2],
   $$
   the last arrow being the inverse of the proper base change isomorphism
   $q^*Rq_*\to Rp_{2*}p_1^*$ for the cartesian square formed by $p_1,p_2,q,q$.
3. The *counit* $\varepsilon_K:Rq_*q^*K(1)[2]\to K$ for
   $K\in\Loc(\Dbc(Y,\Lambda))$ is the composite of the projection formula
   isomorphism $Rq_*q^*K(1)[2]\simeq K\otimes^{\mathbf L}Rq_*\Lambda_P(1)[2]$
   with $1\otimes\operatorname{Tr}_q$.

Both are natural transformations of exact functors on these localizing
categories.
