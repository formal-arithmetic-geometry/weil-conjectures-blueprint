+++
kind = "proof"
of = "lemma-weil-sheaves-point-mixed--1"
order = 1059003
uses = ["proposition-pro-etale-coverings", "theorem-grothendieck-lefschetz-trace-formula", "lemma-finite-quasi-finite-direct-images", "proposition-weights-under-usual-operations"]
+++
Put $X=X_0\times_{k_0}\overline{k}_0$. There are finitely many closed
points of $X_0$. We use strong induction on

$$
n(\cF)=\sum_{x\in|X_0|}
\dim_{\overline{\mathbf Q}_\ell}\cF_{\bar x}.
$$

The zero sheaf is mixed of weights at most $0$. If $\cF\ne0$, some
closed stalk is nonzero. By the quasi-finite vanishing in
[lemma-finite-quasi-finite-direct-images] and the trace formula
[theorem-grothendieck-lefschetz-trace-formula],

$$
\det(1-TF\mid H_c^0(X,\cF))=
\prod_{x\in|X_0|}\det(1-T^{\deg(x)}F_x\mid\cF_{\bar x}).
$$

Choose an eigenvalue $\gamma$ at a nonzero stalk and a
$\deg(x)$-th root $\delta$ of $\gamma$. Frobenius is invertible,
so $\delta\ne0$, and $\delta^{-1}$ is a root of this polynomial.
Thus $H_c^0(X,\cF)\ne0$. The scheme $X_0$ is finite over $k_0$,
hence proper, so $H_c^0(X,\cF)=H^0(X,\cF)=\Gamma(X,\cF)$.
This is the step formalized by
`AlgebraicGeometry.WeilSheaf.nontrivial_globalSections_of_not_isZero`.

Choose a nonzero Frobenius eigenvector $a\in\Gamma(X,\cF)$ with
eigenvalue $\beta\ne0$. Sending $1$ to $a$ gives a nonzero morphism
$\mathcal B_\beta\to\cF$, where $\mathcal B_\beta$ is the constant
rank-one Weil twist of [proposition-weights-under-usual-operations].
Its image $I$ is nonzero and is pure of weight
$w_\beta=2\log_q|\iota(\beta)|$: the constant sheaf has weight $0$,
constant twisting adds $w_\beta$, and purity passes to quotients.

Let $Q=\cF/I$. Exactness of stalks gives

$$
\dim Q_{\bar x}+\dim I_{\bar x}=\dim\cF_{\bar x}.
$$

Since $I$ has a nonzero closed stalk, $n(Q)<n(\cF)$. By induction,
$Q$ is mixed of weights at most some $v$. The one-step filtration of
$I$ makes it mixed of weights at most $w_\beta$. Enlarge both bounds
to $\max(w_\beta,v)$ and splice the filtrations along
$0\to I\to\cF\to Q\to0$, using
[proposition-weights-under-usual-operations]. This proves that
$\cF$ is mixed.
