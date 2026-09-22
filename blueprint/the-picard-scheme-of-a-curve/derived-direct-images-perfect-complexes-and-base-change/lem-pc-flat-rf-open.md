+++
id = "lem-pc-flat-rf-open"
kind = "lemma"
title = "The open locus of invertible $Rf_*$"
order = 4358
lean = ["AlgebraicGeometry.isOpen_locus_derivedPushforward_isInvertible"]
uses = ["def-pc-derived-category", "lem-pc-rf-perfect-base-change", "lem-pc-perfect-locus"]
+++
(Derived Categories of Schemes, Lemma 36.32.3, [Tag
0B9S](https://stacks.math.columbia.edu/tag/0B9S).) Let $f:X\to S$ be a
proper morphism of finite presentation and let $\mathcal{F}$ be an
$\mathcal{O}_X$-module of finite presentation, flat over $S$. Fix
$i,r\in\mathbb{Z}$. Then there exists an open subscheme $U\subset S$ such
that a morphism $T\to S$ factors through $U$ if and only if
$Rf_{T,*}\mathcal{F}_T$ is isomorphic to a finite locally free
$\mathcal{O}_T$-module of rank $r$ placed in degree $i$.

## Proof

By [lem-pc-rf-perfect-base-change] the object $Rf_*\mathcal{F}$ is perfect
and its formation commutes with arbitrary base change; the result is then
exactly [lem-pc-perfect-locus] with $E=Rf_*\mathcal{F}$ and the given $i$,
$r$.
