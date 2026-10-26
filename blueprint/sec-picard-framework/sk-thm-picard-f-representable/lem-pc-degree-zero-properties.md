+++
id = "lem-pc-degree-zero-properties"
kind = "lemma"
title = "Cohomology of an object concentrated in one degree"
lean = ["DerivedCategory.isZero_homologyFunctor_obj_of_iso_singleFunctor", "DerivedCategory.homologyFunctorObjIsoOfIsoSingleFunctor"]
order = 793
uses = ["def-pc-derived-category", "def-sc-invertible-module", "def-weil-abstract-derived-category"]
+++
Let $\mathcal{A}$ be an abelian category with derived category
$D(\mathcal{A})$ ([def-weil-abstract-derived-category]), let $n\in\Z$, let
$E$ be an object of $\mathcal{A}$, write $E[-n]$ for the complex with $E$ in
degree $n$ and $0$ elsewhere, and let $M\in D(\mathcal{A})$ with
$M\cong E[-n]$. Then $H^i(M)=0$ for $i\neq n$ and $H^n(M)\cong E$.

In particular, for a scheme $X$, an object $M\in D(\mathcal{O}_X)$
([def-pc-derived-category]) and an invertible $\mathcal{O}_X$-module
$\mathcal{N}$ with $M\cong\mathcal{N}[0]$, one has $H^i(M)=0$ for $i\neq0$ and
$H^0(M)\cong\mathcal{N}$.
