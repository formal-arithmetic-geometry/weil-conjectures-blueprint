+++
id = "sec-zla-weights"
kind = "section"
title = "Weights and recovery of individual factors"
order = 1018
+++
Fix an integer $q>1$ and let $\Omega$ be an algebraically closed field of
characteristic zero; the case of interest is an abstract algebraic closure of
$\Qell$. Where the sketch article measures the size of a scalar through a
*universal complex-realization field* and its complex realizations, that
field and its realizations are replaced here by $\Qbar\subseteq\mathbf C$ and
the conjugates of the scalar, because
`AlgebraicGeometry.WeilRiemannHypothesis` of
`Comparator/Weil/Definitions.lean` speaks about complex roots.

Purity under a single embedding would not suffice here: the reciprocal roots
of $R$ of one prescribed absolute value need not form a conjugation-stable
family, and the factor they cut out need not be rational, which is why
[def-zla-universal-purity] tests every conjugate.

For the rest of this section fix $r\geq0$ and polynomials
$P_i(T)\in\Omega[T]$, $0\leq i\leq r$, with $P_i(0)=1$, and put

$$
O(T)=\prod_{\substack{0\leq i\leq r\\ i\text{ odd}}}P_i(T),
\qquad
E(T)=\prod_{\substack{0\leq i\leq r\\ i\text{ even}}}P_i(T).
$$
