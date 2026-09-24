+++
id = "lem-fin-finite-splitting"
kind = "lemma"
title = "Etale splitting of a finite morphism"
order = 3199
uses = ["def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit", "lemma-weil-pbc-finite-stalk-formula"]
+++
Let $f:X\to S$ be a finite
morphism with $S$ of finite type over $k$, and let $\bar s$ be a
geometric point of $S$.
There are a pointed etale neighborhood $V\to S$ of $\bar s$ and a
decomposition

$$
X\times_SV=X_1\sqcup\cdots\sqcup X_m
$$

into open-and-closed $V$-subschemes, with $m$ the number of geometric
points of the finite fibre $X_{\bar s}$, such that every $X_i\to V$ is
finite and the geometric fibre $(X_i)_{\bar v}$ over the lifted point
$\bar v$ of $V$ is connected.

## Proof

The morphism $f$ is finite in the sense of
[def-weil-pbc-scheme-conventions]. Let
$A=\mathcal O^{{\mathrm{sh}}}_{S,\bar s}$ be the strict
henselization of [def-weil-pbc-strict-henselization-limit]. The
scheme $X\times_S\operatorname{Spec}A$ is the spectrum of a finite
$A$-algebra $B$, and, following the argument of
[lemma-weil-pbc-finite-stalk-formula], the finite $A$-algebra $B$
is a finite product $B=B_1\times\cdots\times B_m$ of strictly
henselian local algebras, one for each geometric point of the finite
fibre $X_{\bar s}$ in the sense of [def-weil-pbc-geometric-stalks].
The algebra $B$ and the $m$ factor idempotents are generated over $A$
by finitely many elements; the strict henselization $A$ is the
filtered union of the $\mathcal O_{V,\bar v}$ over pointed etale
neighborhoods $V\to S$ of $\bar s$
([def-weil-pbc-strict-henselization-limit]), so one such $V$
carries the whole presentation of $B$ together with the $m$
idempotents. Over that $V$ the decomposition
$X\times_SV=X_1\sqcup\cdots\sqcup X_m$ holds, each $X_i\to V$ is
finite, and $(X_i)_{\bar v}$ is the strictly henselian local piece,
hence connected; the number of pieces is the number of geometric
points by the description of [def-weil-pbc-geometric-stalks].
