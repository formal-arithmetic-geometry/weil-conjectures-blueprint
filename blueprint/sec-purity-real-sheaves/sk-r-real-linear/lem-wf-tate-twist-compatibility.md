+++
id = "lem-wf-tate-twist-compatibility"
kind = "lemma"
title = "Compatibility of the Tate twists"
lean = ["AlgebraicGeometry.WeilSheaf.tateTwistSheafIso"]
order = 3985
uses = ["def-weil-pbc-proetale-site", "sk-def-sp-tate-twist", "def-wf-tate-twist", "lem-wf-internal-hom-weil", "lem-wf-tensor-weil"]
+++
For every $m\in\mathbf Z$, the functorial pullback of roots of unity
gives a strict arrow
$\Phi_X^*\Lambda_X(1)\stackrel{\sim}{\to}\Lambda_X(1)$ (the structure $\tau_1$), and the Tate twist functor
$(-)(m)$ of [def-wf-tate-twist] commutes with finite scalar
extension.
