+++
id = "lem-trf-simple-constructible"
kind = "lemma"
title = "Simple constructible sheaves"
order = 3878
+++
Let $X$ be a Noetherian scheme and $\Lambda$ a finite ring. Every
simple constructible $\Lambda$-sheaf on $X_{\Et}$ is of the form
$i_*M$, where $i:V\hookrightarrow X$ is a closed immersion of an
irreducible closed subset $V$ and $M$ is a simple $\Lambda$-module
viewed as a locally constant sheaf on the generic point of $V$.

## Proof

A constructible sheaf $F$ is nonzero on finitely many irreducible
closed subsets; choose one, $V$, maximal for the property that the
pullback of $F$ to $V$ is nonzero, so $F|_V$ is locally constant.
Its restriction to the generic point $\eta$ of $V$ is a finite
$\Lambda$-module $M_\eta$, and the natural map
$F\to i_*i^*F$ has kernel concentrated on proper closed subsets of
$V$, on which $F$ is zero by maximality. Hence $F\cong i_*M_\eta$
on the complement of those subsets; if $F$ is simple then either this
kernel is zero, in which case $F\cong i_*M_\eta$, or $F$ is the
pushforward of a sheaf on a smaller closed subset, contradicting
maximality. A simple $\Lambda$-module is simple as such, and the
lisse restriction of $F$ to the open dense smooth locus of $V$
is the locally constant sheaf attached to $M_\eta$. This is the
standard classification.
