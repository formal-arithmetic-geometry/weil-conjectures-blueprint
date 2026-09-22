+++
id = "fin4-thm-reduction-to-projective-line"
kind = "theorem"
title = "Reduction to the projective line"
order = 5217
lean = ["AlgebraicGeometry.Etale.fin4_thm_reduction_to_projective_line"]
uses = ["sbc-def-coefficient-conventions", "fin4-lem-domination-trick", "thm-fin-proper-case"]
+++
Assume that $P$ (the assertion of [fin4-lem-domination-trick]) holds for the
structure morphism $\mathbf P^1_S\to S$ for every $S$ of finite type over
$k$. Then $P(f)$ holds for every projective morphism $f:X\to S$ with the
constructible $\Lambda$-sheaves of [sbc-def-coefficient-conventions].

## Proof

The conclusion, including its bound for the actual geometric fibre
dimension, is the already proved proper theorem [thm-fin-proper-case]. A
projective morphism in the statement is proper. Thus the asserted
implication holds; its conclusion is now available without its preliminary
hypothesis.

The independent proof given earlier in this chapter obtains constructibility
by the projective-line and finite-cover reductions and then obtains the
bound from geometric fibres, so there is no circular use of this older
reduction node.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, thm:weil-pbc-chow
