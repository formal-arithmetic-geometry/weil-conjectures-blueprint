+++
kind = "proof"
of = "proposition-twisting-weight-zero-adding-dual"
order = 1198
+++
A twist to weight zero puts all local eigenvalues on the unit circle,
where inversion is complex conjugation. Adding the dual therefore makes
each multiset of eigenvalues stable under conjugation.

To find the twist, choose a closed point $x$, of degree $d$, at which the stalk is
nonzero, and a Frobenius eigenvalue $\alpha$ at $x$.  Let $b\in\overline{\mathbf Q}_\ell$
be a $d$th root of $\alpha^{-1}$.  By purity,
$|\iota(b)|=|\iota(\alpha)|^{-1/d}=q^{-w/2}$, and
Proposition [proposition-weights-under-usual-operations] shows that $\mathcal F^0$
is pure of weight zero.

Its local eigenvalues $\beta_j$ therefore have absolute value one after applying
$\iota$. The local eigenvalues of its dual are the $\beta_j^{-1}$, and
$\iota(\beta_j^{-1})=\overline{\iota(\beta_j)}$. So the union of the
two multisets is stable under complex conjugation, and
$\mathcal E$ is real and pure. In the same way, at a point $x$ over $k_n$ the
eigenvalues of $\operatorname{Frob}_{x,n}$ on $(\mathcal F^0)^\vee$ become,
after $\iota$, the complex conjugates of those on $\mathcal F^0$. Hence
$\iota$ of the trace of $(\mathcal F^0)^\vee$ is the complex conjugate of
$\iota$ of the trace of $\mathcal F^0$, and the trace of $\mathcal E$ is twice
its real part.
