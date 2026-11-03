+++
id = "sk-cor-plancherel"
kind = "corollary"
title = "Plancherel"
order = 726
lean = ["FiniteField.sum_norm_sq_fourierTransform", "AlgebraicGeometry.WeilComplex.traceFunction_fourierTransform", "AlgebraicGeometry.WeilComplex.traceEnergy_fourierTransform"]
uses = ["sk-lem-as-properties", "sk-thm-inversion", "sk-def-sf-weil-complexes", "sk-thm-tf-uniform-formula", "sk-cor-tf-point-counting", "sk-def-wrp-l2-definition"]
tags = ["sketch"]
+++
For every $n\ge1$,

$$
\sum_y|\iota t_{\operatorname{FT}_\psi K,n}(y)|^2
=q^{nr}\sum_x|\iota t_{K,n}(x)|^2.
$$

Consequently, for $r=1$, the number $\nu$ of
Definition [sk-def-wrp-l2-definition] satisfies
$\nu(\operatorname{FT}_\psi K)=\nu(K)+1$ whenever these numbers
are finite.

*Complement.* For $\psi$ nontrivial, applying (17.3) twice with $\psi$ and $\psi^{-1}$
gives the trace-level inversion
$t_{\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi K,n}=q^{nr}\,t_{K,n}$,
the trace function of $K(-r)$. (Applying $\operatorname{FT}_\psi$ twice instead
introduces $[-1]^*$.)
