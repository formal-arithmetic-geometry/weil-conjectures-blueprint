+++
kind = "proof"
of = "lemma-reduced-fractions-integer-coefficients"
order = 1380
uses = ["lemma-hankel-rank-rationality"]
+++
We repeat the construction in the proof of Lemma [lemma-hankel-rank-rationality]
with an integral basis of the row span. This gives an integral
fraction, which we then reduce with Gauss' lemma.

Let $V$ be the rational row span of Lemma [lemma-hankel-rank-rationality], and put
$L=V\cap\mathbf Z^{\mathbf Z_{\geq0}}$. Then $L$ contains all rows,
spans $V$, and is preserved by the left shift. Since $V$ is
finite-dimensional, some $r$ of the coordinate functionals span its
dual, as in the proof of (2)$\Rightarrow$(3) in
Lemma [lemma-hankel-rank-rationality], and so they are jointly injective on $V$.
These coordinates embed $L$ into $\mathbf Z^r$. Since a subgroup
of $\mathbf Z^r$ is free of finite rank, $L$ is a shift-stable lattice
in $V$, free of rank $\dim V$.

In a basis of $L$, the shift matrix $M$, the row $e$ and the column
$v=R_0$ are integral. The matrix identity in the proof of
Lemma [lemma-hankel-rank-rationality] yields integral polynomials

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

For uniqueness, let $A/B=A'/B'$ be two such fractions, so that
$AB'=A'B$ in $\mathbf Q[T]$. Since $B$ is coprime to $A$, it divides
$B'$, and in the same way $B'$ divides $B$. So $B'=cB$ for a scalar
$c$. Comparing constant coefficients gives $c=1$, and then $AB=A'B$
forces $A=A'$.
