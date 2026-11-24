+++
id = "prose-06-02"
kind = "hidden"
title = "Conventions (1)"
order = 536
+++
Until Section [sec-Finite-coefficients-2] the coefficient ring is a finite
commutative $\ell$-primary ring, which we denote by $A$. With such coefficients nothing is lost by computing on the étale site. For $X$ of
finite type over $k$, the [comparison functor](@proposition-comparison-morphism-inverse-image)

$$
\nu_X^*:D(X_{\acute{e}t},A)\longrightarrow D(X_{\mathrm{pro}\acute{e}t},A)
$$

is fully faithful
(Proposition [proposition-unbounded-comparison-finite-coefficients]),
and it identifies $D(X_{\acute{e}t},A)$ with the [localizing category](@definition-localizing-subcategory)
[$\Loc(D^b_{\mathrm{ctf}}(X,A))$](@definition-localizing-subcategory) on which [$f^!$](@theorem-existence-exceptional-inverse-image) was constructed
(Proposition [proposition-comparison-etale-derived-category]). It also
identifies the [constructible complexes](@definition-constructible-sheaves) on the two sites
(Theorem [theorem-comparison-constructible-sheaves]). In the following
sections we therefore work in $D(X_{\acute{e}t},A)$, and every result is
transported to the [pro-étale site](@definition-small-pro-etale-site) by [$\nu_X^*$](@proposition-comparison-morphism-inverse-image).

This transport is harmless because [$\nu^*$](@proposition-comparison-morphism-inverse-image) identifies all the operations we use with their étale
counterparts, compatibly with units and counits
(Lemma [lemma-comparison-direct-images-compatibilities]). These
operations are the cohomology
(Theorem [theorem-bounded-below-cohomology-comparison]); the direct
images and their [base change maps](@definition-derived-base-change-map), also for unbounded complexes
(Theorem [theorem-comparison-direct-images] and
Proposition [proposition-unbounded-comparison-finite-coefficients]); and
the inverse images, tensor products, extension by zero and the [localization
triangles](@proposition-comparison-immersions) (Section [sec-Direct-images]). Moreover, by
Corollary [corollary-finite-tor-amplitude-under-comparison], [finite Tor
amplitude](@definition-constructible-sheaves) can be checked on the étale site.

We write $\Dbc(X,A)$ also for the bounded [constructible](@definition-constructible-sheaves) objects of
$D(X_{\acute{e}t},A)$, which correspond to those of the pro-étale category.
For a separated morphism of finite type $f:X\to S$, the
functor [$Rf_!$](@proposition-construction-independence-rf-shriek) and its right adjoint $f^!$ of
Theorem [theorem-existence-exceptional-inverse-image] correspond to
the functors $Rf_!$ and $f^!$ between $D(X_{\acute{e}t},A)$ and $D(S_{\acute{e}t},A)$,
and the two adjunctions correspond. Accordingly, from now on $g^*$, $Rf_*$, $Rf_!$, $f^!$ and $\otimes^{\mathbf L}$ denote the functors on the étale derived
categories.

Below we apply
Proposition [proposition-composition-base-change-rf-shriek], stated on
[$\Loc(D^b_{\mathrm{ctf}}(-,A))$](@definition-localizing-subcategory), to the étale functors. This is legitimate because the
comparison identifies the composition maps of
Proposition [proposition-composition-base-change-rf-shriek] on the two
sites: the refinement maps (5.7) and the
open–proper interchange (5.9) are
characterized by their restriction to the open. The comparison also preserves the counits defining base change and the inverse counits defining
forgetting supports
(Proposition [proposition-forgetting-supports-composition]). Taking right adjoints, we see that it identifies the composition maps for [$f^!$](@theorem-existence-exceptional-inverse-image) as well.

Except in Lemmas [lemma-cycle-class-cartier-divisor], [lemma-cohomology-projective-line-trace]
and [lemma-coordinate-projections], which allow more general bases as stated
there, all schemes and base changes are of finite type over $k$.

We use three classical theorems about the étale site.
