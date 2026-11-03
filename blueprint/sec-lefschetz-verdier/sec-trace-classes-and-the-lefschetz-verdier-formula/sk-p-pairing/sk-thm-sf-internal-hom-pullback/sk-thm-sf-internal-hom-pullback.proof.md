+++
kind  = "proof"
of    = "sk-thm-sf-internal-hom-pullback"
+++
Write $\otimes$ for $\otimes^L_\Lambda$ and $M^\vee=\RHom_\Lambda(M,\Lambda_X)$.
The canonical comparison is the adjoint of
$Lg^*\RHom_\Lambda(M,N)\otimes Lg^*M\cong Lg^*\bigl(\RHom_\Lambda(M,N)\otimes
M\bigr)\xrightarrow{Lg^*\mathrm{ev}}Lg^*N$.

*Step 1: dualizable objects.* Let $(M,M')$ be a dual pair, with evaluation
$e:M\otimes M'\to\Lambda_X$ and coevaluation $c:\Lambda_X\to M'\otimes M$
satisfying the triangle identities. Then $M'\otimes-$ is right adjoint to
$-\otimes M$ (the unit and counit are built from $c$ and $e$, and the
triangle identities are those of the dual pair), so by uniqueness of adjoints
$M'\otimes N\cong\RHom_\Lambda(M,N)$ naturally in $N$, the counit
corresponding to $e\otimes1_N$; for $N=\Lambda_X$ this identifies $M'$ with
$M^\vee$.

*Step 2: pullback of a dual pair.* The functor $Lg^*$ is symmetric monoidal:
$Lg^*\Lambda_X=\Lambda_{Y'}$ and $Lg^*(A\otimes B)\cong Lg^*A\otimes Lg^*B$
compatibly with the associativity, unit and symmetry constraints. Hence it
carries $(M,M^\vee,e,c)$ to a dual pair $(Lg^*M,Lg^*M^\vee,Lg^*e,Lg^*c)$: the
triangle identities are preserved. So $Lg^*M$ is dualizable with dual
$Lg^*(M^\vee)$.

*Step 3: the comparison.* By Steps 1 and 2,

$$
Lg^*\RHom_\Lambda(M,N)\cong Lg^*(M^\vee\otimes N)\cong Lg^*M^\vee\otimes
Lg^*N\cong\RHom_\Lambda(Lg^*M,Lg^*N).
$$

Under the first isomorphism the evaluation $\RHom_\Lambda(M,N)\otimes M\to N$
is $e\otimes1_N$ (Step 1), so $Lg^*\mathrm{ev}$ corresponds to
$Lg^*e\otimes1_{Lg^*N}$, which under the last isomorphism is the evaluation
of $\RHom_\Lambda(Lg^*M,Lg^*N)$ (Step 1 for the dual pair of Step 2). Taking
adjoints, the composite is the canonical comparison, which is therefore an
isomorphism. Naturality in both variables and compatibility with shifts and
distinguished triangles in $N$ hold because the comparison is a natural
transformation between exact functors of $N$.

When $M$ is locally a bounded complex $P$ of finite free modules this is
also seen directly: the termwise identity
$\operatorname{Hom}(P^i,N^j)=(P^i)^\vee\otimes N^j$ gives
$M^\vee\otimes N\cong\RHom_\Lambda(M,N)$ with finitely many summands in each
total degree, and both sides of the displayed map commute with $Lg^*$.
