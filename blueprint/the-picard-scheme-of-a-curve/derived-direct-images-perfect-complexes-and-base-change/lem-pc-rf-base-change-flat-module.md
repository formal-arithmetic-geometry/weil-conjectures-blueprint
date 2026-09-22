+++
id = "lem-pc-rf-base-change-flat-module"
kind = "lemma"
title = "Derived base change for a relatively flat module"
order = 4352
lean = ["AlgebraicGeometry.derivedPushforward_baseChange_of_flat"]
uses = ["def-pc-morphism-conventions", "def-pc-base-change", "def-pc-derived-direct-image", "def-pc-derived-pullback", "lem-pc-cech-resolution", "lem-pc-flat-complex-derived-pullback"]
+++
Let $f:X\to S$ be a quasi-compact separated morphism of schemes, and let
$\mathcal G$ be a quasi-coherent $\mathcal O_X$-module flat over $S$. For
every $g:T\to S$, derived pullback [def-pc-derived-pullback] gives an
isomorphism
$$
Lg^*Rf_*\mathcal G\;\cong\;Rf_{T,*}\mathcal G_T.
$$

## Proof

The claim is local on $S$ and $T$, so write $S=\operatorname{Spec}(A)$ and
$T=\operatorname{Spec}(B)$. Choose a finite affine cover of $X$ with affine
intersections. By [lem-pc-cech-resolution], its bounded Čech complex
$K^\bullet$ computes $Rf_*\mathcal G$. Each term is a finite product of
modules $N_J=\Gamma(U_J,\mathcal G)$ flat over $A$: relative flatness can
be checked on affine charts and localization at primes. $K^\bullet$ is a
bounded complex of flat modules, so by
[lem-pc-flat-complex-derived-pullback] it computes the derived pullback,
and $K^\bullet\otimes_AB$ computes $Lg^*Rf_*\mathcal G$.

The pullback cover of $X_T$ is again affine with affine intersections, and
$\Gamma(U_J\times_ST,\mathcal G_T)=N_J\otimes_AB$. Its restriction maps are
the tensor products of the original maps, so this is precisely the same
Čech complex $K^\bullet\otimes_AB$. Another application of
[lem-pc-cech-resolution] proves the claimed isomorphism, induced by the
canonical base-change map.
