+++
id = "lemma-cohomology-near-two-transverse-divisors"
kind = "lemma"
title = "Cohomology near two transverse divisors"
order = 973
lean = ["AlgebraicGeometry.Etale.transverseBoundary", "AlgebraicGeometry.Scheme.TransverseCorner.transverse_boundary"]
+++
Let $X$ be a smooth surface over an algebraically closed field
of characteristic $p$, or an étale limit with affine transition
maps of such surfaces. Let $D_1,D_2$ be regular divisors meeting
transversely at exactly one point $z$, and let

$$
j:X-D_2\hookrightarrow X,\qquad
j':X-(D_1\cup D_2)\hookrightarrow X-D_2.
$$

Let $\ell\ne p$, let $A$ be a finite commutative $\ell$-primary ring,
and let $N$ be a bounded complex of $A$-modules on $X-(D_1\cup D_2)$
with finite locally constant cohomology whose monodromy factors
through a finite $\ell$-group. Put $M=Rj_*j'_!N$. Then $M_z=0$, and
$M|_{D_2-z}$ has finite locally constant cohomology. If $D_2$ is
connected, then for every closed geometric point $w\in D_2-z$ the
restriction map

$$
R\Gamma(D_2,M|_{D_2})\longrightarrow M_w
$$

is zero in $D(A)$.
