+++
id = "prose-06-02"
kind = "hidden"
title = "Conventions (1)"
order = 531
+++
In this subsection and the next four, until Section [sec-Finite-coefficients-2],
$\Lambda$ is a finite commutative $\ell$-primary ring. The statements below
concern the pro-étale site, but the proofs calculate on the étale site.
The results of these calculations lie in the following category. Let

$$
D_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)\subset D(X_{\mathrm{pro}\acute{e}t},\Lambda)
$$

be the essential image of $\nu_X^*:D(X_{\acute{e}t},\Lambda)\to
D(X_{\mathrm{pro}\acute{e}t},\Lambda)$. Its bounded below part is the category
$D^+_{\mathrm{class}}$ of Corollary [corollary-bounded-below-classical-complexes]. For $X$
of finite type over $k$, this category is identified with
$D(X_{\acute{e}t},\Lambda)$ by
Proposition [proposition-unbounded-comparison-finite-coefficients]. By
Proposition [proposition-comparison-etale-derived-category], it is also
identified with the localizing category $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ on which
$f^!$ was constructed. For finite coefficients, the objects of
$\Dbc(X,\Lambda)$ are classical by
Theorem [theorem-comparison-constructible-sheaves].

Except in Lemmas [lemma-cycle-class-cartier-divisor], [lemma-cohomology-projective-line-trace]
and [lemma-coordinate-projections], which allow more general bases as stated
there, all schemes and base changes are of finite type over $k$.

Each proof below calculates a canonical map on the étale site and
transports the result to the pro-étale site by $\nu^*$. This works
because $\nu^*$ identifies all the operations we use with their étale
counterparts, compatibly with units and counits
(Lemma [lemma-comparison-direct-images-compatibilities]). These
operations are the cohomology
(Theorem [theorem-bounded-below-cohomology-comparison]); the direct
images and their base change maps, also for unbounded complexes
(Theorem [theorem-comparison-direct-images] and
Proposition [proposition-unbounded-comparison-finite-coefficients]); and
the inverse images, tensor products, extension by zero and the localization
triangles (Section [sec-Direct-images]). Moreover, by
Corollary [corollary-finite-tor-amplitude-under-comparison], finite Tor
amplitude can be checked on the étale site.

Let $f:X\to S$ be a separated morphism of finite type. The functor
$Rf_!:D_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)\to
D_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)$ and its right adjoint $f^!$ are
those of Theorem [theorem-existence-exceptional-inverse-image] on
$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$. Transported through the comparison with the
étale site, their adjunction is the étale one. Accordingly, in a
statement, $g^*$, $Rf_*$, $Rf_!$, $f^!$ and $\otimes^{\mathbf L}$ denote the
functors between the categories $D_{\mathrm{class}}(-_{\mathrm{pro}\acute{e}t},\Lambda)$
(or their bounded below parts). In a proof that calculates on the
étale site, they denote the corresponding functors between the categories
$D(-_{\acute{e}t},\Lambda)$.

The point of the following is that the classical composition and base
change compatibilities cited below apply to the maps constructed here. The
comparison identifies the composition maps of
Proposition [proposition-composition-base-change-rf-shriek] on the two
sites. Indeed, the refinement maps (5.7) and the
open–proper interchange (5.9) are
characterized by their restriction to the open. The comparison also
preserves the counits defining base change and the inverse counits defining
forgetting supports
(Proposition [proposition-forgetting-supports-composition]). Taking right
adjoints, we see that it identifies the composition maps for $f^!$ as well.

We use three classical theorems about the étale site.
