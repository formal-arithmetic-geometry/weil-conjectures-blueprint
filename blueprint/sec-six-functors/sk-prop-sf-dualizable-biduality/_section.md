+++
id = "sk-prop-sf-dualizable-biduality"
kind = "section"
title = "Biduality of a perfect complex"
order = 2172
uses = ["sk-def-sf-operations"]
lean = ["AlgebraicGeometry.Etale.DerivedCategory.isDualizable_coefficientDual", "AlgebraicGeometry.Etale.DerivedCategory.nonempty_iso_coefficientDual_coefficientDual", "AlgebraicGeometry.Etale.DerivedCategory.nonempty_iso_coefficientDual_tensor"]
+++
*Proposition (sketch).*

Let $K\in D(X,\Lambda)$ be perfect, that is, dualizable for
$\otimes^L_{\Lambda_X}$ (locally on the site of $X$ quasi-isomorphic to a bounded
complex of finite projective $\Lambda_X$-modules). Then
$K^\vee=\RHom_X(K,\Lambda_X)$ is again perfect, with evaluation
$K\otimes^L_{\Lambda_X}K^\vee\to\Lambda_X$ the counit of the
tensor–internal-Hom adjunction, and the biduality map $K\to K^{\vee\vee}$
is an isomorphism. For every $M\in D(X,\Lambda)$ the
canonical map $K^\vee\otimes^L_{\Lambda_X}M\to\RHom_X(K,M)$ is an isomorphism.

## Proof

Write $\otimes$ for $\otimes^L_{\Lambda_X}$ and $\mathbf 1=\Lambda_X$; recall
that $\RHom_X(K,-)$ is right adjoint to $-\otimes K$ in the closed symmetric
monoidal category $D(X,\Lambda)$.

*Perfect complexes are dualizable.* For $P$ finite projective the canonical
maps $P^\vee\otimes N\to\RHom_X(P,N)$ and $P\to P^{\vee\vee}$ are
isomorphisms: true for $P=\Lambda_X^r$ by inspection, and both constructions
are exact functors of $P$ preserving direct summands, so they hold for a
projective $P$, which is locally a direct summand of a finite free module.
Applying this termwise to a bounded complex of finite projectives
representing $K$ locally, one gets a dual pair $(K,K^\vee)$, with evaluation
the counit $K\otimes K^\vee\to\mathbf 1$ and coevaluation
$\mathbf 1\to K^\vee\otimes K$ corresponding to the identity of $K$, whose
two triangle composites are identities (this is checked locally). Only
dualizability is used below.

*Dualizable objects.* Let $K$ be dualizable, with dual $K'$, evaluation
$e:K\otimes K'\to\mathbf 1$ and coevaluation $c:\mathbf 1\to K'\otimes K$
satisfying the triangle identities. Then for all $N,M$ the maps
$\operatorname{Hom}(N\otimes K,M)\to\operatorname{Hom}(N,K'\otimes M)$,
$u\mapsto(1_{K'}\otimes u)\circ(c\otimes 1_N)$ (up to the symmetry), and
$\operatorname{Hom}(N,K'\otimes M)\to\operatorname{Hom}(N\otimes K,M)$,
$v\mapsto(e\otimes1_M)\circ(v\otimes1_K)$ (up to the symmetry), are mutually
inverse by the triangle identities and natural in $N$ and $M$. So
$K'\otimes-$ is right adjoint to $-\otimes K$, and by uniqueness of adjoints
there is a natural isomorphism $K'\otimes M\cong\RHom_X(K,M)$; under it the
counit of $-\otimes K\dashv\RHom_X(K,-)$ corresponds to $e\otimes1_M$, so this
isomorphism is the canonical map $K^\vee\otimes M\to\RHom_X(K,M)$ once $K'$
is identified with $K^\vee$ by the case $M=\mathbf 1$:
$K'\cong K'\otimes\mathbf 1\cong\RHom_X(K,\mathbf 1)=K^\vee$. This proves the
last assertion for every $M\in D(X,\Lambda)$, and shows that the evaluation
$K\otimes K^\vee\to\mathbf 1$ is the counit of the adjunction at $\mathbf 1$.

*The dual is dualizable, and biduality.* By the symmetry of $\otimes$, the
pair $(K^\vee,K)$, with the evaluation and coevaluation of $(K,K^\vee)$
composed with the symmetry, again satisfies the triangle identities, so
$K^\vee$ is dualizable with dual $K$. Applying the previous paragraph to
$K^\vee$ gives $K\cong K\otimes\mathbf 1\cong\RHom_X(K^\vee,\mathbf
1)=K^{\vee\vee}$, and unwinding the identifications this isomorphism is the
biduality map $K\to K^{\vee\vee}$, the adjoint of the evaluation
$K\otimes K^\vee\to\mathbf 1$ composed with the symmetry.
