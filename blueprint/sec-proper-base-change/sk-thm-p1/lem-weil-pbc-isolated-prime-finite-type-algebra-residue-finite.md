+++
id = "lem-weil-pbc-isolated-prime-finite-type-algebra-residue-finite"
kind = "lemma"
title = "An isolated prime of a finite type algebra over a field has finite residue field"
lean = ["isJacobsonRing_of_finiteType", "Algebra.FiniteType.isNoetherianRing", "PrimeSpectrum.isOpen_singleton_tfae_of_isNoetherian_of_isJacobsonRing", "PrimeSpectrum.isClosed_singleton_iff_isMaximal", "finite_of_finite_type_of_isJacobsonRing"]
order = 1969
+++
Let $k$ be a field and let $B$ be a finite type (finitely generated) $k$-algebra. If $\mathfrak p\in\operatorname{Spec}B$ has singleton $\{\mathfrak p\}$ open in $\operatorname{Spec}B$, then $\mathfrak p$ is a maximal ideal of $B$, and the residue field $\kappa(\mathfrak p)=B_{\mathfrak p}/\mathfrak pB_{\mathfrak p}$, with its field extension structure from $k\to B\to\kappa(\mathfrak p)$, is finite over $k$, i.e. $\dim_k\kappa(\mathfrak p)<\infty$.
