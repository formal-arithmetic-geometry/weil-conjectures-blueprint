+++
id = "def-pc-f-subfunctor"
kind = "definition"
title = "The open subfunctor F"
order = 4240
lean = ["AlgebraicGeometry.picardOpenSubfunctor"]
uses = ["def-pc-pic-sigma-functor", "def-pc-derived-direct-image", "def-pc-invertible-in-degree-zero", "def-pc-subfunctor", "def-pc-base-change"]
+++
Let $k$ be a field, $X$ a scheme over $k$ and $\sigma\in X(k)$. For a
scheme $T$ over $k$, let
$F(T)\subseteq\operatorname{Pic}_{X/k,\sigma}(T)$ be the subset of those
$\mathcal{L}$ such that $Rf_{T,*}\mathcal{L}$ ($f_T:X_T\to T$,
$Rf_{T,*}$ as in [def-pc-derived-direct-image]) is an object of
$D(\mathcal{O}_T)$ isomorphic to an invertible $\mathcal{O}_T$-module
placed in degree $0$ [def-pc-invertible-in-degree-zero]; this is the
subfunctor $F$ of Stacks Project, Picard Schemes of Curves, Lemma 44.6.2
(the fact that it is a subfunctor, and the open-immersion property, are
[lem-pc-f-open-subfunctor]).
