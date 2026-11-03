+++
id = "prose-A-12"
kind = "hidden"
title = "Separating closed subsets by admissible blow-ups"
order = 837
+++
We now have the two operations that the gluing argument needs:
admissible blow-ups, which modify a scheme only outside a given open, and
elimination of indeterminacy, which turns a map that is an isomorphism
over that open into an open immersion after such a blow-up. This
subsection uses them to prove the inductive step of Nagata's theorem,
Proposition [sk-thm-nagata-sketch-two-open]: if $M=M_1\cup M_2$ with
$M_1\cap M_2$ dense, and each $M_i$ has a compactification $X_i$, then so
does $M$. The natural candidate glues $M$ to each $X_i$ along $M_i$,
after we remove from $X_i$ the closure of the part lying over
$M\setminus M_i$. For the result to be separated, and for every
valuation to extend into one of the two pieces, the closures in $X_i$ of
the two disjoint closed subsets over $M\setminus M_1$ and
$M\setminus M_2$ must be disjoint, and they need not be. We therefore
need a blow-up that makes the closures of two disjoint closed subsets of
an open disjoint (Lemma [sk-lem-nagata-sketch-boundary]), by the mechanism of
the coordinate axes in Section [sec-app-nagata-blowups], and a way to keep an
isomorphism near such a closure (Lemma [sk-lem-nagata-sketch-near-closure]).
A last lemma glues two modifications into one separated scheme
(Lemma [sk-lem-nagata-sketch-common]).
