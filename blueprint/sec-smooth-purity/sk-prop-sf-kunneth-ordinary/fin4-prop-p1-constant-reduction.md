+++
id = "fin4-prop-p1-constant-reduction"
kind = "theorem"
title = "The projective line: reduction to constant coefficients on curve families"
order = 1817
tags = ["latex:proposition"]
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "fin4-lem-domination-trick", "fin4-lem-fibrewise-cohomological-dimension", "fin4-thm-finite-morphisms-constructible", "lemma-weil-pbc-constructible-finite-pushforward", "sbc-def-coefficient-conventions", "thm-constructible-serre", "thm-fin-proper-case"]
+++
Assume that $P$ (the assertion of
[fin4-lem-domination-trick]) holds for every
projective morphism
$X\to S$ all of whose fibres have dimension at most one, for the
constant torsion sheaves $\underline{\mathbf Z/(l)}$, $l$ a prime,
together with the matching bound $R^qg_*G=0$ for $q>2$ (fibre
dimension one). Then $P$ holds for the structure morphism
$\mathbf P^1_S\to S$ for every $S$ of finite type over $k$, with the
bound $R^q\pi_*F=0$ for $q>2$ (the fibres
$\mathbf P^1_{\bar s}$ have dimension one, and the fibrewise
cohomological-dimension bound of
[fin4-lem-fibrewise-cohomological-dimension] applied to the
fibres).

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
