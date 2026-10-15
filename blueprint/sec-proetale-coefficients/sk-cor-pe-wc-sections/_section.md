+++
id = "sk-cor-pe-wc-sections"
kind = "corollary"
title = "Exact sections on contractible affines"
order = 712
uses = ["sk-thm-pe-weakly-contractible-basis"]
tags = ["sketch"]
+++
For an affine $U$ as in [sk-thm-pe-weakly-contractible-basis], the functor
$F\mapsto F(U)$ on abelian sheaves is exact. In particular

$$
H^q(U,F)=0\quad(q>0),\qquad R\Gamma(U,K)\simeq K(U)
$$

for a complex $K$, with the last expression computed term by term.

The affine objects in [sk-thm-pe-weakly-contractible-basis] form a basis in the
cover-dense sense. Their fibre products need not be w-contractible, but they admit such
covers again. Sheaf-theoretic assertions can therefore be checked on these affines, while
global cohomology still records the gluing between them. This local exactness is the input
for the derived inverse-limit arguments below.
