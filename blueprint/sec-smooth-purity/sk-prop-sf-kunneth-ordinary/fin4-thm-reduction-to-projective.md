+++
id = "fin4-thm-reduction-to-projective"
kind = "theorem"
title = "Reduction of the proper case to projective morphisms"
order = 1680
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "fin4-lem-domination-trick", "lemma-weil-pbc-chow-factorization", "sbc-def-coefficient-conventions", "thm-fin-proper-case"]
+++
Assume that $P$ (the assertion of
[fin4-lem-domination-trick]) holds for every
projective morphism with
source and target of finite type over $k$, for the constructible
$\Lambda$-sheaves of [sbc-def-coefficient-conventions] and the
direct image of [def-weil-pbc-direct-image]. Then $P(f)$ holds
for every proper morphism
$f:X\to S$ with $S$ and $X$ of finite type over $k$.

## Proof

The conclusion, including its bound for the actual geometric
fibre dimension, is the already proved proper theorem
[thm-fin-proper-case]. A projective morphism in the statement
is proper. Thus the asserted implication holds; its conclusion is
now available without its preliminary hypothesis.
The independent proof above obtains constructibility by the
projective-line and finite-cover reductions and then obtains the
bound from geometric fibres, so there is no circular use of this
older reduction node.
