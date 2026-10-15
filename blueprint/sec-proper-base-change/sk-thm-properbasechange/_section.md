+++
id = "sk-thm-properbasechange"
kind = "theorem"
title = "Proper base change on classical pro-étale complexes"
order = 1066
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-pbc", "sk-def-pbc-conventions", "sk-thm-p1", "sk-thm-reduction", "sk-cor-pe-classical-derived", "sk-thm-pe-direct-image-comparison"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring, let $f:X\to Y$ be a proper morphism of
schemes, and let $g:Y'\to Y$ be arbitrary. Set $X'=X\times_YY'$, with
projections $f':X'\to Y'$ and $g':X'\to X$. If
$K\in D^+_{\mathrm{class}}(X_{\mathrm{proét}},\Lambda)$ has torsion underlying
abelian cohomology sheaves, the canonical exchange, defined as in
[sk-def-exchange] from the pro-étale inverse and direct images $g^*,g'^*$ and
$Rf_*,Rf'_*$ on $D^+(\,\cdot_{\mathrm{proét}},\Lambda)$,

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is an isomorphism in $D^+_{\mathrm{class}}(Y'_{\mathrm{proét}},\Lambda)$.

The complex $K$ need not be constructible, and the torsion orders need not be
invertible on $Y$. Classicality of $K$ is required: it is what brings the
statement back to the étale site.
