+++
kind  = "proof"
of    = "lem-weil-coefficient-frobenius"
+++
The field cases are finite-dimensional vector-space duality. For
$A=A_{E,n}=\mathcal O_E/\varpi_E^n$, every ideal is
$\varpi^iA$. A homomorphism $u:\varpi^iA\to A$ satisfies
$\varpi^{n-i}u(\varpi^i)=0$, hence
$u(\varpi^i)\in\varpi^iA$. Write
$u(\varpi^i)=\varpi^ib$; multiplication by $b$ extends $u$ to
$A$. Baer's criterion, Stacks Project,
[Tag 0AVF](https://stacks.math.columbia.edu/tag/0AVF), now gives
self-injectivity. Since $A$ is Artinian, it is quasi-Frobenius.
A finite $A$-module is a finite direct sum of cyclic modules
$A/\varpi^i$, so it suffices to check evaluation on these. A functional
$A/\varpi^i\to A$ is determined by its value at $1$, which lies in
$\operatorname{Ann}_A(\varpi^i)=\varpi^{n-i}A/\varpi^n$, so that

$$
\operatorname{Hom}_A(A/\varpi^i,A)\cong\varpi^{n-i}A/\varpi^n
\cong A/\varpi^i ;
$$

the evaluation map at $1$ is a generator of the double dual, hence an
isomorphism. Exactness of $\operatorname{Hom}_A(-,A)$ and bounded
truncation give derived biduality for bounded finite cohomology.

Over $R=\mathcal O_E$, the finite module $T=R/\varpi_E R$ is
nonzero but $\operatorname{Hom}_R(T,R)=0$. In particular ordinary
duality is not exact: applying it to
$0\to R\xrightarrow{\varpi_E}R\to T\to0$ leaves the nonsurjective
map $R\xrightarrow{\varpi_E}R$. Thus $R$ is not self-injective.
It is a regular ring, so bounded complexes with finite cohomology are
perfect by Stacks Project,
[Tag 066Z](https://stacks.math.columbia.edu/tag/066Z).
For a perfect complex over any ring, a bounded finite projective model
computes its derived dual, and termwise evaluation computes the derived
double dual; this is Stacks Project,
[Tag 07VI](https://stacks.math.columbia.edu/tag/07VI).
It proves both the integral assertion and the last clause.
