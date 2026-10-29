+++
id = "prose-07-01"
kind = "hidden"
title = "Strategy for constructibility of $f^!$ and torsion conventions"
order = 2600
+++
In this section we prove that for every separated morphism $f$ of finite
type and every admissible $\Lambda$, the right adjoint $f^!$ of
[sk-prop-sf-existence] maps $\Dctf(Y,\Lambda)$ into
$\Dctf(X,\Lambda)$, which is part (4) of [sk-thm-existence]. Without this, $f^!$ is only a functor between the
localizing categories $\Loc(\Dctf(-,\Lambda))$, and the six operations
would not act on constructible complexes. Brown representability gives no
information on the values of $f^!$, so we have to compute them. Since
$f^!$ is compatible with composition and is local on $X$ and on $Y$, we may
assume that $Y$ is affine and that $f$ is a closed immersion into some
$\mathbf A^n_Y$ followed by the projection to $Y$. Now $\mathbf A^n_Y$ is open
in $(\mathbf P^1_Y)^n$, we have $j^!=j^*$ for an open immersion $j$, and
$(\mathbf P^1_Y)^n\to Y$ is a composite of $n$ morphisms of the form
$\mathbf P^1_T\to T$. Hence it suffices to treat closed immersions and the
projection $p:\mathbf P^1_T\to T$. For
$p$, an explicit adjunction shows that $p^!=p^*(1)[2]$. For a closed
immersion, the localization triangle expresses $f^!$ through the direct
image along the complementary open immersion. The geometric difficulty is
therefore to show that this direct image preserves bounded constructibility
and finite Tor amplitude. We prove this for torsion coefficients, and pass
to integral and rational coefficients, where $\Dctf=\Dbc$, by reduction
modulo a uniformizer.

For torsion coefficients we prove the two geometric facts on which the
reduction above rests: the adjunction $Rp_*\dashv p^*(1)[2]$ for the
projective line $p:\mathbf P^1_S\to S$
([sk-prop-geo-p1-adjunction]), and, over a field, the
statement that direct image along an open immersion preserves bounded
constructible complexes and commutes with base change
([sk-cor-geo-open-finiteness]).

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
Section “Finite coefficients: finite Tor amplitude and the six operations”.
Here $\Lambda$ is a finite commutative $\ell$-primary ring. The
statements below concern the pro-étale site, while the proofs calculate
on the étale site. The results of these calculations lie in the
following category. Let

$$
D_{\mathrm{class}}(X_{\mathrm{pro\acute et}},\Lambda)\subset D(X_{\mathrm{pro\acute et}},\Lambda)
$$

be the essential image of $\nu_X^*:D(X_{\mathrm{\acute et}},\Lambda)\to
D(X_{\mathrm{pro\acute et}},\Lambda)$. Its bounded below part is the category
$D^+_{\mathrm{class}}$ of [sk-cor-pe-classical-derived]. For $X$
of finite type over $k$, [sk-prop-pe-unbounded-classical]
identifies it with $D(X_{\mathrm{\acute et}},\Lambda)$, and
[sk-prop-ctf-finite-comparison] identifies it with the
localizing category $\Loc(\Dctf(X,\Lambda))$ on which $f^!$ was constructed. For finite
coefficients, the objects of $\Dbc(X,\Lambda)$ are
classical by [sk-thm-pe-constructible-comparison].

Except in [sk-lem-geo-cartier], [sk-lem-geo-p1-cohomology]
and [sk-lem-geo-coordinates], which allow more general bases as stated
there, all schemes and base changes are of finite type over $k$.

In each proof below, we calculate on the étale site and transport the
result to the pro-étale site by $\nu^*$. This is possible because
$\nu^*$ identifies cohomology, direct images and their base change maps
(also for unbounded complexes), inverse images, tensor products, extension
by zero and the localization triangles with their étale counterparts,
compatibly with units and counits, and because finite Tor amplitude can
be checked on the étale site ([sk-prop-sf-comparison]
and [sk-thm-pe-direct-image-comparison],
[sk-prop-pe-unbounded-classical],
Section “Comparison of inverse and direct images” and
[sk-cor-pe-finite-tor-comparison]). Hence a calculation of a
canonical map on the étale site proves the corresponding assertion on
the pro-étale site.

For a separated morphism $f:X\to S$ of finite
type, the functor $Rf_!:D_{\mathrm{class}}(X_{\mathrm{pro\acute et}},\Lambda)\to
D_{\mathrm{class}}(S_{\mathrm{pro\acute et}},\Lambda)$ and its right adjoint $f^!$
are those of [sk-prop-sf-existence] on
$\Loc(\Dctf(-,\Lambda))$, and their adjunction, transported through the
comparison with the étale site, is the étale one. Accordingly, in a
statement, $g^*$, $Rf_*$, $Rf_!$, $f^!$ and $\otimes^{\mathbf L}$ denote the
functors between the categories $D_{\mathrm{class}}(-_{\mathrm{pro\acute et}},\Lambda)$
(or their bounded below parts). In a proof that calculates on the
étale site, they denote the corresponding functors between the categories
$D(-_{\mathrm{\acute et}},\Lambda)$.

We use three classical theorems about the étale site.
