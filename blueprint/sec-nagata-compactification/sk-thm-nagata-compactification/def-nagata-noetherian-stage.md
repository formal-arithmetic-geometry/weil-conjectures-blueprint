+++
id = "def-nagata-noetherian-stage"
kind = "definition"
title = "Finite-type Noetherian stage"
order = 349
lean = ["AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.Stage.scheme"]
uses = ["def-nagata-affine-gluing-valid-stage"]
+++
For a valid stage $\lambda$ of $\mathsf G_S$, with coefficient subrings
$A_{\lambda,a}\subseteq\Gamma(S,U_a)$, define $S_\lambda$ to be the scheme
obtained by gluing the charts $\operatorname{Spec}(A_{\lambda,a})$ along
the opens $\bigcup_rD(f_{abr})\subseteq\operatorname{Spec}(A_{\lambda,a})$,
the overlap maps being induced by the equalities
$A_{\lambda,a}[1/f_{abr}]=A_{\lambda,b}[1/g_{abr}]$ inside
$\Gamma(S,D(f_{abr}))$. In particular this defines
$S_{\lambda_{\mathrm{glue}}}$.
