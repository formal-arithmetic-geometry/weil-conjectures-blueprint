+++
kind = "proof"
of = "lemma-kunneth-field-coefficients--1"
order = 714002
uses = ["definition-constructible-sheaves", "lemma-finiteness-small-etale-topoi", "lemma-finiteness-small-etale-topoi--1"]
+++
Put $J=\operatorname{rad}(A)$. Since $J$ is nilpotent and both sides of
$\tau_{E,F}$ are triangulated functors of $F$, it suffices to treat
sheaves killed by $J$. Indeed, for a sheaf killed by $J^{m+1}$,
the quotient by its subsheaf killed by $J$ is killed by $J^m$.
This is the reduction in
`AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_singleFunctor_of_smul_eq_zero`.

Assume now that $JF=0$. Flatness of $E$ identifies the cohomology maps
of $\tau_{E,F}$ with the degreewise tensor base change maps. These
maps depend only on $E/JE$. On sheaves killed by $J$ their sources are
exact functors, since $A/J$ is semisimple, and their targets have the
long exact sequences of higher direct images.

A constructible sheaf killed by $J$ embeds into a finite sum of
sheaves $\pi_*\underline{V}$, with $\pi$ finite and $V$ a finite
$A/J$-module; its cokernel is again constructible and killed by $J$.
This uses the finite-type form of the embedding in
[lemma-finiteness-small-etale-topoi], namely
`AlgebraicGeometry.Etale.exists_mono_biproduct_lowerStar_of_smul_eq_zero`.
Each $V$ is a direct summand of a finite free $A/J$-module. The assumed
isomorphisms for $\pi_*A_{X_i}$ therefore give the degreewise
isomorphisms for these finite sums. Naturality first gives injectivity
for every constructible sheaf killed by $J$. Induction on the degree,
using the long exact sequence for the cokernel, gives surjectivity;
the negative degrees vanish. This is
`CategoryTheory.isIso_app_of_dimensionShift`.

Finally, $E/JE$ is a filtered colimit of constructible subsheaves
killed by $J$, as in [lemma-finiteness-small-etale-topoi--1]. Both
sides of the degreewise maps commute with these colimits, using that
$h$ is quasi-compact and quasi-separated for the higher direct images.
Thus every cohomology map is an isomorphism, and so is $\tau_{E,F}$.
