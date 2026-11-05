+++
kind = "proof"
of = "theorem-gabber-affine-proper-base-change"
order = 355
uses = ["lemma-cohomology-modules-underlying-abelian", "theorem-comparison-over-henselian-pair-degree", "theorem-gabber-affine-proper-base-change--1"]
+++
Put $X=\operatorname{Spec}B$, $X_0=\operatorname{Spec}(B/J)$, and let
$i:X_0\hookrightarrow X$. We prove the assertion for torsion sheaves of
$\Lambda$-modules, computing cohomology on their underlying abelian
sheaves as in [lemma-cohomology-modules-underlying-abelian]. Taking
$\Lambda=\Z$ gives the stated result.

Degree zero is [theorem-comparison-over-henselian-pair-degree], applied
to the identity $X\to\operatorname{Spec}B$. Suppose comparison holds
in degree $q$ for every torsion sheaf of $\Lambda$-modules. A monomorphism
$F\hookrightarrow F'$ into a torsion sheaf gives a short exact sequence

$$
0\longrightarrow F\longrightarrow F'\longrightarrow Q\longrightarrow0
$$

with $Q$ torsion. Forgetting the module structure and applying $i^*$
are exact. Restriction therefore gives a commutative diagram of long
exact cohomology sequences, including the connecting maps.

For surjectivity in degree $q+1$, take
$\eta\in H^{q+1}(X_0,i^*F)$ and choose $F\hookrightarrow F'$ killing
$\eta$ by [theorem-gabber-affine-proper-base-change--1]. Exactness
writes $\eta$ as the boundary of a class in $H^q(X_0,i^*Q)$. By the
induction hypothesis this class lifts to $H^q(X,Q)$, and its boundary
restricts to $\eta$.

For injectivity, let $\xi\in H^{q+1}(X,F)$ have zero restriction.
Apply [theorem-gabber-affine-proper-base-change--1] to the henselian
pair $(B,0)$, identifying $\operatorname{Spec}(B/0)$ with $X$, to
choose $F\hookrightarrow F'$ killing $\xi$ on $X$. Write $\xi$ as
the boundary of $z\in H^q(X,Q)$. The restriction of $z$ has zero
boundary, so comes from $w\in H^q(X_0,i^*F')$. Lift $w$ to
$v\in H^q(X,F')$ by the induction hypothesis. The image of $v$ in
$H^q(X,Q)$ and $z$ have the same restriction, so they are equal by
injectivity in degree $q$ for $Q$. Their boundary is zero, hence
$\xi=0$.
