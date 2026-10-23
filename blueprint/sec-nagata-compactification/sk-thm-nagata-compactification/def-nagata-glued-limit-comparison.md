+++
id = "def-nagata-glued-limit-comparison"
kind = "definition"
title = "Comparison from the original scheme to the inverse limit"
order = 36
lean = ["AlgebraicGeometry.Scheme.FiniteAffineGluingPresentation.stageCone"]
uses = ["def-nagata-noetherian-inverse-system"]
+++
Let $I_S$ be the set of valid stages of $\mathsf G_S$. For each valid stage
$\lambda$, the inclusions $A_{\lambda,a}\subseteq\Gamma(S,U_a)$ induce
morphisms $U_a\to\operatorname{Spec}(A_{\lambda,a})$ which glue to a
morphism $S\to S_\lambda$, and these morphisms are compatible with the
transition morphisms $S_\mu\to S_\lambda$. Define the comparison cone
$\kappa_S$ to be the cone with vertex $S$ over the system
$(S_\lambda)_{\lambda\in I_S}$ formed by these morphisms. We say that
$\kappa_S$ identifies $S$ with the inverse limit if it is a limit cone,
i.e. if the induced morphism

$$
S\longrightarrow\varprojlim_{\lambda\in I_S}S_\lambda
$$

is an isomorphism.
