+++
kind = "proof"
of = "corollary-point-counting-zeta-function--7"
order = 1040014
+++
Clause [corollary-point-counting-zeta-function--5] gives rationality over $\mathbf Q_\ell$, while clause [corollary-point-counting-zeta-function--6] gives rational Taylor coefficients.

Rationality descends from $\mathbf Q_\ell$ to $\mathbf Q$ for the following reason. A power
series is rational exactly when its coefficients eventually satisfy a
linear recurrence with constant coefficients. The existence of such
a recurrence is a system of linear equations, and a system with rational
coefficients has a rational solution as soon as it has any solution.
Write $Z(X_0,T)=\sum_{n\geq0}z_nT^n$, with $z_n\in\mathbf Z$.
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

*Source:* the proof of Corollary [corollary-point-counting-zeta-function].
