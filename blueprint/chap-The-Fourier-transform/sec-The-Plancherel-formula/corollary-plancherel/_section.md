+++
id = "corollary-plancherel"
kind = "corollary"
title = "Plancherel"
order = 1241
lean = ["AlgebraicGeometry.WeilComplex.traceEnergy_fourierTransform"]
uses = ["lemma-stability", "proposition-six-operations-change-coefficients", "definition-trace-function", "lemma-artin-schreier-character-sheaf", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
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
