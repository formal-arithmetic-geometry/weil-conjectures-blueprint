+++
id = "sk-thm-intfactors"
kind = "section"
title = "Integral Frobenius factors"
order = 2901
uses = ["sk-def-cohfamily", "sk-def-roots", "sk-prop-rootpurity", "sk-prop-separation", "sk-thm-rationality"]
+++
*Theorem (sketch).*

For every $0\le i\le2d$ there is a unique polynomial $P_i(T)\in\Z[T]$ with
$P_i(0)=1$ such that for *every* prime $\ell\ne p$

$$
P_i^{(\ell)}(T)=\det\bigl(1-TF_{i,\ell}\mid H^{i}(X,\Ql)\bigr),
$$

and then

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}},
$$

a factorization that is independent of $\ell$.

## Proof

By [sk-thm-rationality], $Z=A/B$ with $A,B\in\Z[T]$, $A(0)=B(0)=1$,
$\gcd(A,B)=1$ in $\Q[T]$: a normalized integral presentation. By
[sk-prop-rootpurity] the reciprocal roots of the $\ell$-adic factors carry
the weights $q^{i/2}$, which are pairwise distinct for distinct $i$, so
[sk-prop-separation] separates the factors: the multiplicity of each root in
$A$ or $B$ determines its weight, hence its index $i$: a root of $A$ or $B$ is
an ordinary root $\beta=\alpha^{-1}$ with $\alpha$ an eigenvalue of $F$ on some
$V_{j,\ell}$, and $j$ is determined by $|\iota(\alpha)|=q^{j/2}$, which is
[sk-prop-rootpurity]. Two points have to be supplied to conclude
$P_i\in\Z[T]$. *(i) Rationality.* $\Gal(\overline\Q/\Q)$ permutes the
roots of the rational polynomials $A$ and $B$, and it preserves each weight
stratum, because the weight of $\alpha$ is intrinsic:
$|\tau(\alpha)|=q^{j/2}$ for *every* embedding $\tau$ of $\Q(\alpha)$.
Hence the submultiset of roots of weight $j$ is Galois-stable, so the product
of the corresponding factors $(1-\alpha T)$ lies in $\Q[T]$; with $P_i(0)=1$
this is the sought $P_i$, whose $\ell$-adic extension is $P_{i,\ell}$.
*(ii) Integrality.* Write $P_i(T)=\prod_\alpha(1-\alpha T)$, the product
over the eigenvalues $\alpha$ of $F$ on $V_{i,\ell}$; its coefficients are the
elementary symmetric functions of the $\alpha$, so it suffices that every
$\alpha$ is an algebraic integer and that $P_i\in\Q[T]$ (which is (i)). Each
$\alpha$ is an algebraic integer because $F$ preserves the image
$H^{i}(X,\Z_\ell)$ of compact-support integral cohomology, a finitely generated
$\Z_\ell$-module, so that the characteristic polynomial of $F$ has
$\Z_\ell$-coefficients and its roots are integral over $\Z_\ell$. A
coefficient of $P_i$ is therefore a rational algebraic integer, hence an
integer, and $P_i\in\Z[T]$. Uniqueness is clear from the determinant
formula, and independence of $\ell$ follows because the presentation
$A/B$ and the weight grouping do not mention $\ell$.
*Provenance.* The realization-independence step — that the
factorization is common to all $\ell$ — is the deepest *algebraic*
step of this layer, and the two points above compress eight statements of the
expanded blueprint: `thm:weil-realization-independence` with
`prop:weil-intrinsic-weights` and
`lem:embedding-extension` for the intrinsic weight and the
embedding transport, `prop:galois-weight-strata`,
`prop:galois-weight-strata-integrality` and
`prop:galois-weight-strata-identification` for the Galois stability,
integrality and identification of the strata, and
`prop:integral-recovery` with
`lem:weil-finite-coordinate-detection` for the recovery of the
integral factors. These are pure algebra: no geometric input enters beyond
[sk-prop-rootpurity].

Uses: [sk-def-cohfamily], [sk-def-roots], [sk-prop-rootpurity], [sk-prop-separation], [sk-thm-rationality]
