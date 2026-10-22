+++
id = "lem-pc-flat-rf-open"
kind = "lemma"
title = "The open locus of invertible $Rf_*$"
order = 688
uses = ["def-pc-base-change", "def-pc-derived-category", "def-pc-derived-direct-image", "lem-pc-perfect-locus", "lem-pc-rf-perfect-base-change"]
lean = ["AlgebraicGeometry.Scheme.Modules.exists_opens_range_subset_iff_isFiniteLocallyFreeInDegree"]
+++
Let
$f:X\to S$ be a proper morphism of finite presentation and let $\mathcal{F}$ be an
$\mathcal{O}_X$-module of finite presentation, flat over $S$. Fix integers $i,r\ge0$.
Then there exists an open subscheme $U\subset S$, namely the set $U_{i,r}$ of points
$s\in S$ with $H^q(X_s,\mathcal F_s)=0$ for $q\neq i$ and
$\dim_{\kappa(s)}H^i(X_s,\mathcal F_s)=r$, such that a morphism
$T\to S$ factors through $U$ if and only if $Rf_{T,*}\mathcal{F}_T$ is isomorphic
to a finite locally free $\mathcal{O}_T$-module of rank $r$ placed in degree $i$,
that is, $R^qf_{T,*}\mathcal F_T=0$ for $q\neq i$ and $R^if_{T,*}\mathcal F_T$ is
finite locally free of rank $r$. Here $f_T:X_T\to T$ is the base change of $f$ and
$\mathcal F_T$ the pullback of $\mathcal F$ to $X_T$.
