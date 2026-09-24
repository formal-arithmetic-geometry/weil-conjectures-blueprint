+++
id = "lem-sc-mult-n-finite-flat"
kind = "lemma"
title = "Multiplication by $d$ is finite flat of degree $d^{2g}$"
order = 2420
uses = ["def-sc-abelian-variety", "def-sc-mult-n", "lem-sc-fg-order-prime-etale"]
+++
Let $A$ be an abelian variety of dimension $g$ over a field $k$
and let $d\geq1$. Then $[d]:A\to A$ of [def-sc-mult-n] is
finite, flat and locally free of rank $d^{2g}$, with finite kernel
$A[d]$ of order $d^{2g}$; if $\operatorname{char}k\nmid d$, the
kernel is etale (equivalently $[d]$ is etale), and $A[d]$ is
etale-covering of the constant group scheme $(\mathbf Z/d\mathbf Z)^{2g}$
([lem-sc-fg-order-prime-etale]).
(*Stacks Project, Groupoid Schemes, Lemma 39.9.8,
[Tag 0BFG](https://stacks.math.columbia.edu/tag/0BFG); Proposition
39.9.11, [Tag 03RP](https://stacks.math.columbia.edu/tag/03RP);
Lemma 39.9.9, [Tag 0BFH](https://stacks.math.columbia.edu/tag/0BFH)*.)

## Proof

The clauses are the recorded classical input of the statement.
Finiteness, flatness and local freeness of rank $d^{2g}$ with finite
kernel of order $d^{2g}$ are Stacks Project, Groupoid Schemes, Lemma
39.9.8 ([Tag 0BFG](https://stacks.math.columbia.edu/tag/0BFG)) and
Proposition 39.9.11 ([Tag
03RP](https://stacks.math.columbia.edu/tag/03RP)); the etaleness of the kernel when $\operatorname{char}k\nmid d$,
and its description as an etale covering of the constant group scheme
$(\mathbf Z/d\mathbf Z)^{2g}$, are Lemma 39.9.9
([Tag 0BFH](https://stacks.math.columbia.edu/tag/0BFH)) together
with [lem-sc-fg-order-prime-etale]. The blueprint records the
complete list because the proofs below use all three clauses; no separate
proof is given.
