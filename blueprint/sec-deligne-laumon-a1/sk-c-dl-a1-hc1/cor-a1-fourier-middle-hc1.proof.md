+++
kind  = "proof"
of    = "cor-a1-fourier-middle-hc1"
+++
*Step 1: the transform of the middle extension.* Since $\psi$ is
nontrivial and $\mathcal M$ is an irreducible (in particular nonzero)
lisse Weil sheaf which is nonexceptional in the above sense,
[prop-a1-fourier-middle-extension] supplies a dense open
$j':U'_0\hookrightarrow\mathbf A^1_{k_0}$ of the dual line and a nonzero
irreducible lisse Weil sheaf $\mathcal M'$ on $U'_0$ with

$$
\operatorname{FT}_\psi\bigl((j_*\mathcal M)[1]\bigr)\cong(j'_*\mathcal M')[1].
$$

*Step 2: the weight of $\mathcal M'$.* Since $\mathcal M$ is moreover
punctually $\iota$-pure of weight $w$, the last assertion of
[cor-fd-l2-plancherel-middle-extension] shows that $\mathcal M'$ is
punctually $\iota$-pure of weight exactly $w+1$ on all of $U'_0$.

*Step 3: weights of the middle extension on the dual line.* The dual
line is a smooth geometrically connected affine curve, and
$\mathcal M'$ is a nonzero lisse Weil sheaf on the dense open $U'_0$
all of whose closed-point Frobenius eigenvalues satisfy
$|\iota(\alpha)|^2=q_x^{w+1}\le q_x^{w+1}$. Boundary semicontinuity
[lem-wf-boundary-semicontinuity], with $\beta=w+1$, shows that the
middle extension $j'_*\mathcal M'$ of [def-wf-middle-extension] has
punctual weights at most $w+1$ at every closed point of the dual line,
including the finitely many points outside $U'_0$, where it may be
singular.

*Step 4: the origin fibre.* By the stationary-phase identification
[cor-fd-origin-stationary-phase], applied to the pair $(j',\mathcal M')$
of Step 1, whose middle extension is the transform of that of
$\mathcal M$, there is a Frobenius-equivariant isomorphism

$$
H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)\cong(j'_*\mathcal M')_{0'},
$$

the geometric Frobenius of $k_0$ on the left corresponding to the local
Frobenius $F_{0'}$ at the $k_0$-rational point $0'$ on the right. Hence
the eigenvalues of Frobenius on $H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)$
are those of $F_{0'}$ on the stalk, and by Step 3 (with $q_{0'}=q$)
each of them satisfies $|\iota(\alpha)|^2\le q^{w+1}$. In the
convention of [def-weil-punctual-weights], this says that
$H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)$ has weights at most $w+1$.
