+++
id = "prose-07-02"
kind = "hidden"
title = "Torsion coefficients: the strategy"
order = 322
+++
For torsion coefficients we prove the two geometric facts on which the
reduction above rests: the adjunction $Rp_*\dashv p^*(1)[2]$ for the
projective line $p:\mathbf P^1_S\to S$
(Proposition [sk-prop-geo-p1-adjunction]), and, over a field, the
statement that direct image along an open immersion preserves bounded
constructible complexes and commutes with base change
(Corollary [sk-cor-geo-open-finiteness]).

The second fact is the hard one, and its proof uses the first. The
adjunction for the projective line shows that for a smooth $f$ the
functor $f^!$ is $f^*$ tensored with an invertible complex. Combined
with the adjunction $Rf_!\dashv f^!$, this shows that for a locally
constant sheaf $L$, up to twist and shift, $Rf_*L$ is the dual
$\cHom(-,\Lambda)$ of $Rf_!$ applied to the dual of $L$.
Since the constructibility of $Rf_!$ is known, $Rf_*L$ is generically
constructible and commutes with base change. The general case follows by
induction on the dimension of the generic fibre: projecting to a coordinate
line lowers this dimension, and the locus missed by the projections is
finite over the base, where constructibility can be detected by a proper
direct image.

**Conventions for the torsion case.** These conventions hold until
Section [sec-ctf-finite-geometric-restriction].
Here $\Lambda$ is a finite commutative $\ell$-primary ring. The
statements below concern the pro-étale site, while the proofs calculate
on the étale site. The results of these calculations lie in the
following category. Let

$$
D_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)\subset D(X_{\mathrm{pro}\acute{e}t},\Lambda)
$$

be the essential image of $\nu_X^*:D(X_{\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$. Its bounded below part is the category
$D^+_{\mathrm{class}}$ of Corollary [sk-cor-pe-classical-derived]. For $X$
of finite type over $k$, Proposition [sk-prop-pe-unbounded-classical]
identifies it with $D(X_{\acute{e}t},\Lambda)$, and
Proposition [sk-prop-ctf-finite-comparison] identifies it with the
localizing category $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ on which $f^!$ was constructed. For finite
coefficients, the objects of $\Dbc(X,\Lambda)$ are
classical by Theorem [sk-thm-pe-constructible-comparison].

Except in Lemmas [sk-lem-geo-cartier], [sk-lem-geo-p1-cohomology]
and [sk-lem-geo-coordinates], which allow more general bases as stated
there, all schemes and base changes are of finite type over $k$.

In each proof below, we calculate on the étale site and transport the
result to the pro-étale site by $\nu^*$. This is possible because
$\nu^*$ identifies cohomology, direct images and their base change maps
(also for unbounded complexes), inverse images, tensor products, extension
by zero and the localization triangles with their étale counterparts,
compatibly with units and counits, and because finite Tor amplitude can
be checked on the étale site (Theorems [sk-prop-sf-comparison]
and [sk-thm-pe-direct-image-comparison],
Proposition [sk-prop-pe-unbounded-classical],
Section [sec-pe-functor-comparison] and
Corollary [sk-cor-pe-finite-tor-comparison]). Hence a calculation of a
canonical map on the étale site proves the corresponding assertion on
the pro-étale site.

For a separated morphism $f:X\to S$ of finite
type, the functor $Rf_!:D_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)$ and its right adjoint $f^!$
are those of Theorem [sk-prop-sf-existence] on
$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$, and their adjunction, transported through the
comparison with the étale site, is the étale one. Accordingly, in a
statement, $g^*$, $Rf_*$, $Rf_!$, $f^!$ and $\otimes^{\mathbf L}$ denote the
functors between the categories $D_{\mathrm{class}}(-_{\mathrm{pro}\acute{e}t},\Lambda)$
(or their bounded below parts). In a proof that calculates on the
étale site, they denote the corresponding functors between the categories
$D(-_{\acute{e}t},\Lambda)$.

The comparison also identifies the composition maps of
Proposition [sk-thm-sf-comp-composition] on the two sites, since the
refinement maps (6.6) and the open–proper
interchange (6.7) are characterized by
their restriction to the open. It also preserves the counits defining
base change and the inverse counits defining forgetting supports
(Proposition [sk-prop-b-prop-forget-supports-composition]), so taking right
adjoints identifies the composition maps for $f^!$. Hence the classical
composition and base change compatibilities cited below apply to the maps
constructed here.

We use three classical theorems about the étale site.
