+++
id = "fin4-thm-reduction-to-projective-line"
kind = "theorem"
title = "Reduction to the projective line"
order = 3260
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "fin4-lem-composition-constructibility", "fin4-lem-domination-trick", "fin4-thm-finite-morphisms-constructible", "fin4-thm-reduction-to-projective", "sbc-def-coefficient-conventions", "thm-fin-proper-case"]
+++
Assume that $P$ (the assertion of
[fin4-lem-domination-trick]) holds for the structure morphism
$\mathbf P^1_S\to S$ for every $S$ of finite type over $k$. Then
$P(f)$ holds for every
projective morphism
$f:X\to S$ with the constructible $\Lambda$-sheaves of
[sbc-def-coefficient-conventions] and the direct image of
[def-weil-pbc-direct-image].

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
