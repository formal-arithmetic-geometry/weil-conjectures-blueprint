+++
kind  = "proof"
of    = "prop-nagata-affine-blowup-chart"
+++
Since $x$ is homogeneous of positive degree, the standard open
$D_+(x)\subseteq\operatorname{Proj}(\mathcal R_A(I))$ is canonically
isomorphic to $\operatorname{Spec}(\mathcal R_A(I)_{(x),0})$, and $\chi_x$
is the inverse of this isomorphism followed by the inclusion of $D_+(x)$;
so $\chi_x$ is an open immersion with image $D_+(x)$. The structure
morphism of $\operatorname{Proj}$ to $\operatorname{Spec}$ of the degree-zero
part restricts on $D_+(x)$ to $\operatorname{Spec}$ of the inclusion
$\mathcal R_A(I)_0\to\mathcal R_A(I)_{(x),0}$, $y\mapsto y/1$; composing
with the identification $A\cong\mathcal R_A(I)_0$ gives the second claim.
This is checked on the image of every $r\in A$.

For $x=at$ the ring homomorphism
$\theta_a\colon\mathcal R_A(I)_{(at),0}\to A[I/a]$ is bijective by
[lemma-nagata-homogeneous-away-to-chart-injective] and
[lemma-nagata-homogeneous-away-to-chart-surjective], hence a ring
isomorphism. It is $A$-linear, so moreover
$D_+(at)\cong\operatorname{Spec}(A[I/a])$ over $\operatorname{Spec}(A)$.
