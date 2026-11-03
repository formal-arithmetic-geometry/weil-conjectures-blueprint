+++
kind  = "proof"
of    = "lem-zl-mixed-punctual-cutoff"
+++
Take a finite filtration by constructible Weil subsheaves supplied
by the mixedness hypothesis in [def-weil-punctual-weights].
Write $\mathcal Q_r$ for its punctually pure quotients and $u_r$
for their weights. Remove zero quotients.

A nonzero $\mathcal Q_r$ has a nonzero stalk on some lisse stratum
of a constructible stratification
([sk-lem-coefficient-heart] (3)). The locus where the
lisse rank is nonzero contains a nonempty locally closed piece.
It contains a closed geometric point of $Y=Y_0\times_{k_0}k$:
on a nonempty affine open of that piece, take a maximal ideal;
the weak Nullstellensatz gives residue field $k$.
Its coordinates lie in a finite extension of the finite field
$k_0$, so its image $y$ in $Y_0$ is a closed point.
Thus $(\mathcal Q_r)_{\bar y}\neq0$ for some such $y$.

Taking stalks of the filtration is exact and respects local
Frobenius. Choose a basis adapted to it. The Frobenius matrix is
block triangular, so its characteristic polynomial is the product ([p-linear-filtration])
of those on the successive quotients. Each eigenvalue on
$(\mathcal Q_r)_{\bar y}$ is therefore an eigenvalue on
$\mathcal G_{\bar y}$. Choose one; it is nonzero since Frobenius
acts invertibly. Purity and the assumed bound give

$$
q_y^{u_r/2}=|\iota(\alpha)|\leq q_y^{v/2}.
$$

Since $q_y>1$, this implies $u_r\leq v$.
The original finite filtration now has all nonzero quotient weights
at most $v$, which is precisely the required mixedness bound.
