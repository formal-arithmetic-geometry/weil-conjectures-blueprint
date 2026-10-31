+++
kind = "proof"
of = "sk-lem-wweil-integer-rationality"
+++
Let $V$ be the rational row span of Lemma [sk-prop-criterion], and put
$L=V\cap\mathbf Z^{\mathbf Z_{\geq0}}$. Then $L$ contains all rows,
spans $V$, and is preserved by the left shift. A finite set of
coordinates embeds $L$ into some $\mathbf Z^r$, and a subgroup of
$\mathbf Z^r$ is free of finite rank. Thus $L$ is a shift-stable lattice in $V$, free of
rank $\dim V$.

In a basis of $L$, the shift matrix $M$, the row $e$ and the column
$v=R_0$ are integral, and so the matrix identity in the proof of
Lemma [sk-prop-criterion] yields integral polynomials

$$
A_0=e\operatorname{adj}(I-TM)v,\qquad B_0=\det(I-TM),
\qquad C=A_0/B_0.
$$

Both constant coefficients are one. Let $G$ be a primitive integral
polynomial that is a greatest common divisor of $A_0$ and $B_0$ in
$\mathbf Q[T]$. By Gauss' lemma the quotients $A_0/G$ and $B_0/G$ are
integral. Since $G(0)$ divides $B_0(0)=1$, we may choose the sign of
$G$ so that $G(0)=1$. Dividing by $G$, we obtain polynomials $A$ and
$B$ that are coprime and have constant coefficients one.

For uniqueness, we cross-multiply two reduced fractions over
$\mathbf Q$. By coprimality, the denominators are scalar multiples of
each other, the constant coefficients force the scalar to be one, and
then the numerators coincide.
