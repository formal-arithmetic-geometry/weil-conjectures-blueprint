+++
id = "def-nagata-affine-gluing-valid-stage"
kind = "definition"
title = "Cocycle-valid stage of an affine gluing presentation"
order = 39
lean = ["AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.Stage", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.glueStage", "AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.exists_stage_superset"]
uses = ["def-nagata-affine-gluing-coefficient-stage"]
+++
A *valid stage* (valid finite coefficient refinement) of $\mathsf G_S$ is
a family $\lambda=(A_{\lambda,a})_a$ of finitely generated subrings
$A_{\lambda,a}\subseteq\Gamma(S,U_a)$ containing all basic-open elements
of the chart $a$, such that the finitely many gluing equations hold:

1. the $f_{aar}$ generate the unit ideal of $A_{\lambda,a}$ (identity);
1. $A_{\lambda,a}[1/f_{abr}]=A_{\lambda,b}[1/g_{abr}]$ inside
$\Gamma(S,D(f_{abr}))$ (the overlap maps are defined and mutually inverse);
1. the restrictions of the $f_{baq}$ generate the unit ideal of
$A_{\lambda,b}[1/g_{abr}]$ (the overlap maps preserve the overlaps);
1. the restrictions of the $f_{bcq}$ generate the unit ideal of
$A_{\lambda,a}[1/(f_{abr}f_{acs})]$ (triple overlaps are preserved).

Valid stages are ordered by chartwise inclusion. They are cofinal: any
finitely many sections of the charts lie in the coefficient subrings of one
valid stage. Define $\lambda_{\mathrm{glue}}(S)$ to be a
selected valid stage with
$A^{\mathrm{coeff}}_a\subseteq A_{\lambda_{\mathrm{glue}},a}$ for all $a$.
