+++
id = "lemma-nagata-affine-gluing-identities-eventually"
kind = "lemma"
title = "The selected finite-stage datum satisfies the gluing axioms"
order = 40
lean = ["AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.gluing_identities_of_glueStage_le"]
uses = ["def-nagata-affine-gluing-valid-stage", "lemma-nagata-affine-gluing-coefficients-descend"]
+++
For the valid stage $\lambda_{\mathrm{glue}}(S)$ and every valid stage
$\lambda\geq\lambda_{\mathrm{glue}}(S)$, the coefficient subrings satisfy
$A^{\mathrm{coeff}}_a\subseteq A_{\lambda,a}$, and the gluing identities
hold at $\lambda$: the $f_{aar}$ generate the unit ideal of
$A_{\lambda,a}$; $A_{\lambda,a}[1/f_{abr}]=A_{\lambda,b}[1/g_{abr}]$, so
the overlap maps are defined and mutually inverse; the restrictions of the
$f_{baq}$ generate the unit ideal of $A_{\lambda,b}[1/g_{abr}]$, so the
overlap maps preserve the overlaps; and the restrictions of the $f_{bcq}$
generate the unit ideal of $A_{\lambda,a}[1/(f_{abr}f_{acs})]$, so triple
overlaps are preserved, giving the cocycle condition.
