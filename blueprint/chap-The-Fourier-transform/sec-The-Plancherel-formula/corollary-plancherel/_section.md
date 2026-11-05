+++
id = "corollary-plancherel"
kind = "corollary"
title = "Plancherel"
order = 1238
lean = ["AlgebraicGeometry.WeilComplex.traceEnergy_affineSpaceFourierTransform", "AlgebraicGeometry.WeilComplex.l2Weight_fourierTransform"]
uses = ["definition-weil-structure", "definition-trace-function", "definition-growth-squared-traces", "lemma-artin-schreier-character-sheaf", "prose-16-06"]
+++
For every $n\ge1$,

$$
\sum_y|\iota t_{\operatorname{FT}_\psi K,n}(y)|^2
=q^{nr}\sum_x|\iota t_{K,n}(x)|^2.
$$

Consequently, for $r=1$, the number $\nu$ of
Definition [definition-growth-squared-traces] satisfies
$\nu(\operatorname{FT}_\psi K)=\nu(K)+1$ whenever these numbers
are finite.
