+++
kind = "proof"
of = "det-proper-heart-bound-indcons"
+++
Write $M=\varinjlim_\alpha C_\alpha$, a filtered colimit of constructible sheaves. By
[sk-lem-proper-heart-continuity], $R^qp_*M=\varinjlim_\alpha R^qp_*C_\alpha$.

*Ind-constructibility.* By [sk-thm-sfb-proper-base-change], $Rp_*C_\alpha\in\Dbc(Y,\Lambda)$, so
$R^qp_*C_\alpha\in\Cons(Y,\Lambda)$; hence $R^qp_*M$ is a filtered colimit of constructible sheaves, i.e. lies
in $\IndCons(Y,\Lambda)$.

*Vanishing.* For $q>2d+1$ each $R^qp_*C_\alpha=0$ by [det-proper-heart-bound-rational], so the colimit
vanishes.

*Direct sums.* $R^qp_*$ commutes with direct sums by [sk-lem-proper-heart-continuity], and the sum lies
in $\IndCons$ by part (2) of [sk-prop-ind-heart].
