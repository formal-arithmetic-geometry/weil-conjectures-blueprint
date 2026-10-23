+++
kind  = "proof"
of    = "sk-lem-wweil-integer-rationality"
+++
Let $V$ be the rational row span of [sk-prop-criterion], and put
$L=V\cap\mathbf Z^{\mathbf Z_{\geq0}}$. Then $L$ contains all rows,
spans $V$, and is preserved by the left shift. A finite set of
coordinates embeds $L$ into some $\mathbf Z^r$. Every subgroup of
$\mathbf Z^r$ is free of finite rank. To see this, induct on $r$:
project to the last coordinate, and if the image $a\mathbf Z$ is
nonzero, split off a lift of $a$; the kernel is a subgroup of
$\mathbf Z^{r-1}$. Thus $L$ is a shift-stable lattice in $V$, free of
rank $\dim V$.

In a basis of $L$, the shift matrix $M$, the row $e$ and the column
$v=R_0$ are integral, and so the matrix identity in the proof of
[sk-prop-criterion] yields integral polynomials

$$
 A_0=e\operatorname{adj}(I-TM)v,\qquad B_0=\det(I-TM),
 \qquad C=A_0/B_0.
$$

Both constant coefficients are one. Let $G$ be a primitive integral
polynomial that is a greatest common divisor of $A_0,B_0$ in
$\mathbf Q[T]$. By Gauss' lemma the quotients $A_0/G$ and $B_0/G$ are
integral. Since $G(0)$ divides $B_0(0)=1$, we may choose the sign of
$G$ so that $G(0)=1$, and dividing by $G$ gives $A,B$ that are coprime
and have constant coefficients one.
For uniqueness, cross-multiply two reduced fractions over $\mathbf Q$.
By coprimality, the denominators are scalar multiples of each other,
the constant coefficients force the scalar to be one, and then the
numerators coincide.

For the complement, a quasi-compact $X_0$ is the disjoint union of finitely
many separated locally closed subschemes $V_j$ (the differences of a finite
affine open cover, with reduced structures). A morphism
$\operatorname{Spec}\mathbf F_{q^n}\to X_0$ factors uniquely through the
$V_j$ containing its image point, so the point counts add, $Z(X_0,T)$ is the
product of the $Z(V_j,T)$, and the first part applies. The closed points of
$X_0$ are the disjoint union of those of the $V_j$, with the same residue
fields, so the closed-point products of [sk-cor-tf-point-counting] for the
$V_j$ multiply to the closed-point product for $X_0$.
