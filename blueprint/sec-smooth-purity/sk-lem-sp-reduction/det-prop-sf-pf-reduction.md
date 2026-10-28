+++
id = "det-prop-sf-pf-reduction"
kind = "proposition"
title = "Projection formula: compatibility with finite reduction"
order = 2919
uses = ["det-def-sf-exchanges", "sk-lem-sf-determination", "det-thm-sf-pf-finite"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_reductionModIdeal_rightDerivedLowerShriek", "AlgebraicGeometry.Etale.nonempty_iso_reductionModIdeal_leftDerivedUpperStar"]
+++
Let $m\le n$ and let $K\in\Dctf(X,A_{E,n})$, $L\in\Dctf(Y,A_{E,n})$ with
reductions $K_m,L_m$. Then the square comparing
$\operatorname{PF}_{f,K,L}$ and $\operatorname{PF}_{f,K_m,L_m}$ through the
finite-reduction compatibilities of $Rf_!$, $-\otimes^L$ and $Lf^*$ commutes;
hence $\operatorname{PF}_{f,K,L}$ is an isomorphism if and only if
$\operatorname{PF}_{f,K_m,L_m}$ is.
