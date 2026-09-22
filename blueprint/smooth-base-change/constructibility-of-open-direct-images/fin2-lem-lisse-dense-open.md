+++
id = "fin2-lem-lisse-dense-open"
kind = "lemma"
title = "A lisse locus for a constructible sheaf"
order = 5175
lean = ["AlgebraicGeometry.Etale.IsConstructible.exists_isLisse_dense_open"]
uses = ["sbc-def-coefficient-conventions"]
+++
Let $X$ be of finite type over $k$ and let $F$ be a constructible
$\Lambda$-sheaf on $X_{\Et}$. Then there is an open subscheme
$U\hookrightarrow X$ with $\dim(X\setminus U)<\dim X$ on which the
restriction $F|_U$ is lisse.

## Proof

If $X$ is empty, take $U=X$. Otherwise let $C_1,\dots,C_t$ be all its
irreducible components. For each component of maximal dimension, first
remove all other components. This gives an irreducible open $O_i$ of $X$
containing its generic point $\eta_i$. By the finite partition in the
definition of constructibility, the stratum containing $\eta_i$ contains a
nonempty open $V_i\subset O_i$. The restriction to $V_i$ is finite locally
constant.

The $V_i$ are disjoint opens of $X$, so their finite union $U$ is open and
$F|_U$ is finite locally constant. The closed complement meets every
maximal-dimensional component in a proper closed subset. For finite-type
schemes over a field such a subset has strictly smaller dimension, by the
dimension formula for finitely generated algebras. The other components
already have smaller dimension. Hence $\dim(X\setminus U)<\dim X$.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, lem:weil-pbc-noetherian-finite-components
