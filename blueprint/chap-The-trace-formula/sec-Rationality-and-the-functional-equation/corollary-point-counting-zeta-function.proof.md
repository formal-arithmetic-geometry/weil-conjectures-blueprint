+++
kind = "proof"
of = "corollary-point-counting-zeta-function"
order = 1040
uses = ["theorem-grothendieck-lefschetz-trace-formula", "lemma-hankel-rank-rationality"]
+++
The identities over $\Lambda$ are the trace formula and the Euler
product for the constant sheaf. What needs an argument is that
$Z(X_0,T)$ has rational coefficients, which we deduce at the end from
the rationality over $\mathbf Q_\ell$ by linear algebra.

For $K=\Lambda_X$, every stalk is $\Lambda$, and every stalk Frobenius
$\operatorname{Frob}_{y,m}$ is its identity, with categorical trace $1_\Lambda$. Thus
(12.9) follows from Theorem [theorem-grothendieck-lefschetz-trace-formula],
and the formula over the fields follows from its cohomological form
(12.4). By the orbit count in the proof of
Theorem [theorem-trace-formula-euler-product], we have
$\#X_0(\mathbf F_{q^m})=\sum_{\deg(x)\mid m}\deg(x)$. Expanding each
$(1-T^{\deg(x)})^{-1}$ as a geometric series shows that the product over
closed points has integer coefficients. By the orbit count, its
logarithm is the series defining $Z(X_0,T)$. The last equality is
Theorem [theorem-trace-formula-euler-product] for $K=\Lambda_X$.

Rationality descends from $\mathbf Q_\ell$ to $\mathbf Q$ for the following reason. A power series is rational exactly when its coefficients eventually satisfy a
linear recurrence with constant coefficients. The existence of such
a recurrence is a system of linear equations, and a system with rational
coefficients has a rational solution as soon as it has any solution.
More precisely, write $Z(X_0,T)=\sum_{n\geq0}z_nT^n$, with $z_n\in\mathbf Z$.
Rationality over $\mathbf Q_\ell$ means that there are integers $d,N$ and
$b_1,\ldots,b_d\in\mathbf Q_\ell$ such that
$z_n+b_1z_{n-1}+\cdots+b_dz_{n-d}=0$ for all $n>N$.
These are linear equations with rational coefficients in the $d$
unknowns $b_i$. Their coefficient rows span a finite-dimensional
subspace of $\mathbf Q^{d+1}$, and hence finitely many of the equations imply
all the others. This finite rational linear system has a solution over
$\mathbf Q_\ell$, and hence one over $\mathbf Q$ by Gaussian elimination. With these
rational $b_i$, the product of $1+b_1T+\cdots+b_dT^d\in\mathbf Q[T]$
and $Z(X_0,T)$ is a polynomial. Therefore $Z(X_0,T)\in\mathbf Q(T)$.
