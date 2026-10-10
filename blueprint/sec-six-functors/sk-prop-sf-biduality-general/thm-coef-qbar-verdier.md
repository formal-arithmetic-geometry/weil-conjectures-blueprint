+++
id = "thm-coef-qbar-verdier"
kind = "theorem"
title = "Verdier biduality at algebraically closed coefficients"
order = 2154
uses = ["def-weil-algebraically-closed-coefficients", "lem-coef-rational-operations", "lem-coef-rational-retract-evaluation", "prop-weil-pbc-common-stage-calculus", "prop-weil-pbc-descent-functors", "thm-coef-rational-verdier"]
+++
The finite-field dualities and their scalar-extension comparisons
induce an exact $\Qlb$-linear anti-equivalence

$$
D_{X,\Qlb}:D^b_c(X,\Qlb)^{\mathrm{op}}
\xrightarrow{\sim}D^b_c(X,\Qlb),
\qquad (E,K)\longmapsto(E,D_{X,E}K).
$$

It is the internal Hom into $\omega_{X,\Qlb}=Ra_X^!\Qlb$
in the common-stage category. Evaluation and biduality descend,
giving a natural isomorphism
$K\xrightarrow{\sim}D_{X,\Qlb}D_{X,\Qlb}K$.
For a separated finite-type $f:X\to Y$, the same passage
gives the constructible adjunction $Rf_!\dashv Rf^!$ and
$Rf^!=D_Xf^*D_Y$. All of these maps are compatible with
finite scalar extension and with retracts.
