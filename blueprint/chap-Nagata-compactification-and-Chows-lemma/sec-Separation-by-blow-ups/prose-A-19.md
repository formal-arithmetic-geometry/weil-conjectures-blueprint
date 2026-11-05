+++
id = "prose-A-19"
kind = "hidden"
title = "Separation by blow-ups (1)"
order = 1452
+++
The inductive step of Nagata's theorem is
Proposition [proposition-compactifying-union-two-opens]. Suppose that $M=M_1\cup M_2$
with $M_1\cap M_2$ dense, and that each $M_i$ has a compactification $X_i$;
we want a compactification of $M$. The natural candidate glues $M$ to each
$X_i$ along $M_i$, after we remove from $X_i$ the closure of the part lying
over $M\setminus M_i$. For the result to be separated, however, and for every
valuation to extend into one of the two pieces, the closures in $X_i$ of
the two disjoint closed subsets over $M\setminus M_1$ and
$M\setminus M_2$ must be disjoint. They need not be, and this is where
Lemma [lemma-separation-closures] enters: it makes them disjoint by an
admissible blow-up, as with the coordinate axes in
Section [sec-Elimination-of-indeterminacy].

We need two other lemmas.
Lemma [lemma-extending-isomorphism-over-closure-closed] keeps an
isomorphism near such a closure, and
Lemma [lemma-gluing-after-admissible-blow-ups] glues two
modifications into one separated scheme. Both use elimination of
indeterminacy from the previous section. Recall that it turns a map
that is an isomorphism over a quasi-compact open $U$ into an open
immersion after a $U$-admissible blow-up.
