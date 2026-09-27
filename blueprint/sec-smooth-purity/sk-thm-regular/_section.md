+++
id = "sk-thm-regular"
kind = "section"
title = "Purity for regular closed immersions"
order = 2033
uses = ["sk-def-purity-conv", "sk-lem-coprojection", "sk-lem-regular-smooth", "sk-thm-smooth-purity"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_dualizingComplex_of_isRegularImmersion"]
+++
*Theorem (sketch).*

Let $i:Z\hookrightarrow X$ be a regular closed immersion of pure codimension
$c$, with $X$ smooth over the perfect field $k$ and $Z$ regular. There is a
canonical isomorphism

$$
Ri^{!}\Lambda_X\ \xrightarrow{\ \sim\ }\ \Lambda_Z(-c)[-2c],
$$

carrying $1$ to the fundamental class $[Z\subset X]$, compatible with
étale base change and with exterior products.

## Proof

*Step 1: the $\omega$-identification.* Work on a connected component of
$X$; the resulting isomorphisms assemble over the disjoint union. By
[sk-lem-regular-smooth], $a_X$ and $a_Z$ are smooth of dimensions $n$ and
$m=n-c$ with $a_Z=a_X\circ i$, so the composition law for the exceptional
inverse image gives

$$
\omega_{Z/k}=Ra_Z^{!}\Lambda_k\ \cong\ Ri^{!}Ra_X^{!}\Lambda_k=Ri^{!}\omega_{X/k},
$$

while [sk-thm-smooth-purity] applied to $a_X$ and to $a_Z$ gives
$\omega_{X/k}\cong\Lambda_X(n)[2n]$ and $\omega_{Z/k}\cong\Lambda_Z(m)[2m]$.

*Step 2: the co-projection removes the twist.* By
[sk-lem-coprojection] with $K=\Lambda_X$ and the invertible
$L=\Lambda_X(n)[2n]$,

$$
Ri^{!}\bigl(\Lambda_X(n)[2n]\bigr)\ \cong\
Ri^{!}\Lambda_X\otimes^{\mathbb L}_{\Lambda_Z}\Lambda_Z(n)[2n].
$$

Combining with Step 1 and cancelling the invertible $\Lambda_Z(n)[2n]$,

$$
Ri^{!}\Lambda_X\ \cong\ \Lambda_Z(m-n)[2m-2n]=\Lambda_Z(-c)[-2c].
$$

The normalization carries $1$ to the fundamental class; base change and
exterior products are those of [sk-thm-smooth-purity] and of the
co-projection.

Uses: [sk-def-purity-conv], [sk-lem-coprojection], [sk-lem-regular-smooth], [sk-thm-smooth-purity]
