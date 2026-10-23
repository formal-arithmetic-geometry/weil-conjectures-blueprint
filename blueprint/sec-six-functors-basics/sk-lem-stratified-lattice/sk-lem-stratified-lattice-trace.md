+++
id = "det-lem-stratified-lattice-trace"
kind = "lemma"
title = "Pushing a lattice down a finite étale cover by the trace"
order = 2187
uses = ["det-lem-stratified-lattice-scheme", "det-lem-coefficient-heart-common-stratification"]
+++
Let $S$ be a Noetherian scheme, $L$ a lisse $E_S$-module of rank $r$, $p\colon V\to S$ finite
étale surjective, and $M_0\subseteq p^*L$ a lisse $\cO_{E,V}$-lattice. Let
$\Tr\colon p_*p^*L\to L$ be the trace of $p$ and $L_0=\Tr(p_*M_0)\subseteq L$. Then $L_0$ is a
lisse $\cO_{E,S}$-module with $L_0[1/\ell]=L$.

Consequently, for $X$ a standing scheme and $p\colon V\to X$ quasi-compact, separated, étale and
surjective with a lattice $M_0\subseteq p^*L$, there is a finite stratification of $X$ by
locally closed subschemes $S$ over which $p$ is finite étale surjective, and on each $S$ the
lattice $L_0$ above exists; this proves [sk-lem-stratified-lattice].
