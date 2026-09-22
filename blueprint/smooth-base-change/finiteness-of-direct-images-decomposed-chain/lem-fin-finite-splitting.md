+++
id = "lem-fin-finite-splitting"
kind = "lemma"
title = "Étale splitting of a finite morphism"
order = 5160
lean = ["AlgebraicGeometry.IsFinite.exists_etale_neighborhood_decomposition"]
uses = ["def-weil-pbc-strict-henselization-limit"]
+++
Let $f:X\to S$ be a finite morphism with $S$ of finite type over $k$, and
let $\bar s$ be a geometric point of $S$. There are a pointed étale
neighborhood $V\to S$ of $\bar s$ and a decomposition
$$
X\times_SV=X_1\sqcup\cdots\sqcup X_m
$$
into open-and-closed $V$-subschemes, with $m$ the number of geometric points
of the finite fibre $X_{\bar s}$, such that every $X_i\to V$ is finite and
the geometric fibre $(X_i)_{\bar v}$ over the lifted point $\bar v$ of $V$
is connected.

## Proof

Let $A=\mathcal O^{\mathrm{sh}}_{S,\bar s}$ be the strict henselization [def-weil-pbc-strict-henselization-limit]. The
scheme $X\times_S\operatorname{Spec}A$ is the spectrum of a finite
$A$-algebra $B$, and, by the finite stalk formula, $B$ is a finite product
$B=B_1\times\cdots\times B_m$ of strictly henselian local algebras, one for
each geometric point of the finite fibre $X_{\bar s}$.

The algebra $B$ and the $m$ factor idempotents are generated over $A$ by
finitely many elements; the strict henselization $A$ is the filtered union of
the $\mathcal O_{V,\bar v}$ over pointed étale neighborhoods $V\to S$ of
$\bar s$ ([def-weil-pbc-strict-henselization-limit]), so one such $V$ carries the whole presentation of $B$ together
with the $m$ idempotents. Over that $V$ the decomposition
$X\times_SV=X_1\sqcup\cdots\sqcup X_m$ holds, each $X_i\to V$ is finite, and
$(X_i)_{\bar v}$ is the strictly henselian local piece, hence connected; the
number of pieces is the number of geometric points.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-geometric-stalks, lem:weil-pbc-finite-stalk-formula
