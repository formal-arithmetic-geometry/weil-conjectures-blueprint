+++
kind  = "proof"
of    = "prop-finite-compact-support-constructibility"
+++
*Step 1 (the compactification form).* By
[def-weil-compact-support-candidate] a compactification of $f$
is a factorisation $f=\bar f\circ j$ with $j:X\hookrightarrow\bar X$
an open immersion ([def-weil-scheme-morphism-properties]) and
$\bar f:\bar X\to Y$ proper ([def-weil-scheme-morphism-properties]),
and the candidate
attached to it is $R\bar f_*\circ j_!$, formed with the
derived direct image ([def-weil-derived-direct-image]); the functor
$Rf_{!,n}$ of
[def-compact-support-direct-image-detailed] is the coherent choice of a
candidate in the compactification category
[def-weil-compactifications-refinements], and by the hypothesis
recalled in the statement its comparison maps are identities satisfying
the cocycle condition. It therefore suffices to bound the candidate of
a single compactification, and the bound produced below involves only
the amplitude interval of $K$ and the fibre bound $e$, so that it is
independent of the choice.

*Step 2 (transport to the étale site).* The functor is defined on
the pro-étale categories. Under the comparison morphism of sites
$\nu$ of [def-weil-pbc-site-comparison-morphism] the direct images
correspond, $\nu^*Ru_{{\mathrm{et}},*}\cong Ru_{{\mathrm{proet}},*}\nu^*$
([prop-weil-pbc-comparison-direct-image]), and constructibility on
the pro-étale site is by definition the inverse image of
constructibility on the étale site
([def-weil-pbc-constructible-direct-image-finiteness]). It is
accordingly enough to prove the assertion for the étale direct image,
which is what the two classical finiteness theorems below provide.

*Step 3 (extension by zero and the proper case).* For
$K\in D^b_c(X,A)$ the object $j_!K$ lies in $D^b_c(\bar X,A)$ with
constructible cohomology
sheaves ([def-weil-derived-cohomology-sheaves]) in the same degrees: extension by zero
is exact and preserves
[def-weil-finite-torsion-constructibility]
([def-weil-extension-by-zero], [lem-fin-extension-by-zero]).
The geometric fibres of $\bar f$ have dimension at most $e$, so
[obl-fin-comparison] applies to $\bar f$: for every constructible
$A$-sheaf $F$ on $\bar X_{{\mathrm{et}}}$ the sheaves
$R^q\bar f_*F$ are constructible and vanish for $q>2e$. For a
complex whose cohomology sheaves lie in degrees $[a,b]$ the conclusion
holds degreewise, the constructible sheaves forming a weak Serre
subcategory ([thm-constructible-serre]), so that
$Rf_{!,n}K\in D_c^{[a,b+2e]}(Y,A)$ for the
constructible cohomological
interval ([def-weil-constructible-intervals]) $D_c^{[a,b+2e]}(Y,A)$.

*Step 4 (the finite-type form).* The same bound is available
without compactifying. By [sbc-thm-finiteness-finite-type],
applied to the finite-type morphism $f$ over the field $K_0$ whose
geometric fibres have dimension at most $e$, the sheaves $R^qf_!F$
are constructible for every $q$ and vanish for $q>2e$, for every
constructible $A$-sheaf $F$; the case of a complex follows as in
Step 3.

*Step 5 (exactness and reduction).* The restriction is a
triangulated functor, $j_!$ and $R\bar f_*$ being exact and
triangulated on the bounded constructible categories, and it commutes
with finite coefficient reduction because the finite-level direct image
does, the reduction being compatible with the comparison morphisms that
enter the definition ([def-compact-support-direct-image-detailed]).

*Step 6 (general finite coefficients).* For the clause on an arbitrary finite
ring $A$ annihilated by $\ell^N$, first pass to an étale model. Pro-étale
objects are handled through the comparison: by
[lem-sf-proetale-constructible-origin] they are of étale origin, and Step 2
applies. Then forget the $A$-module structure to $\mathbf Z/\ell^N$. Forgetting
is exact and commutes with $j_!$ and with the derived direct image. A sheaf of
$A$-modules is constructible with finite stalks exactly when the underlying
$\mathbf Z/\ell^N$-sheaf is, since $A$ is finite. The classical proper
finiteness theorem with $\mathbf Z/\ell^N$-coefficients (Step 3,
[obl-fin-comparison]) therefore gives constructibility and the bound
$[a,b+2e]$ for the underlying complex, hence for $R\bar f_*j_!K$. Over a
separably closed point a constructible sheaf has finite sections, which are
finite $A$-modules. Only bounded constructibility enters.
