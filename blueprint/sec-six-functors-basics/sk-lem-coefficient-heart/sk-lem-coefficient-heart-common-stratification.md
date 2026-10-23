+++
id = "det-lem-coefficient-heart-common-stratification"
kind = "lemma"
title = "Common refinement of stratifications and restriction to strata"
order = 2145
uses = ["sk-def-sfb-constructible", "def-constructible-stratification", "sk-prop-sfb-cartesian-coefficients"]
+++
Let $X$ be a Noetherian scheme and $\Lambda=E$ or $\Qlb$.

1. Finitely many finite stratifications of $X$ by locally closed subschemes have a common
   refinement which is again a finite stratification by locally closed subschemes; it may
   be chosen so that every stratum is connected and the strata can be ordered
   $S_1,\dots,S_m$ with $S_1\cup\dots\cup S_k$ open in $X$ for every $k$.
2. If $M$ is lisse on a locally closed $S$ and $T\subseteq S$ is locally closed, then $M|_T$
   is lisse. Hence a constructible sheaf is lisse on every stratum of any refinement of a
   stratification adapted to it.
3. For a stratum $g\colon S\to X$, restriction $g^*=g^{-1}$ is exact, and a morphism
   (resp. sequence) of $\Lambda_X$-modules is injective, surjective (resp. exact) iff its
   restriction to every stratum is.
