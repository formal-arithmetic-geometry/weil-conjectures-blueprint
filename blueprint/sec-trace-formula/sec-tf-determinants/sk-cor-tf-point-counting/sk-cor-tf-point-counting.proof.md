+++
kind = "proof"
of = "sk-cor-tf-point-counting"
uses = ["sk-thm-tf-uniform-formula", "sk-thm-trace-transport"]
+++
For $K=\Lambda_X$, every stalk is $\Lambda$, and every stalk Frobenius
$\operatorname{Frob}_{y,m}$ is its identity, with categorical trace $1_\Lambda$. Thus
(13.9) follows from Theorem [sk-thm-tf-uniform-formula],
and the formula over the fields follows from its cohomological form
(13.4). By the orbit count in the proof of
Theorem [sk-thm-trace-transport], we have
$\#X_0(\mathbf F_{q^m})=\sum_{\deg(x)\mid m}\deg(x)$. Expanding each
$(1-T^{\deg(x)})^{-1}$ as a geometric series, we see that the product over
closed points has integer coefficients, and the orbit count identifies its
logarithm with the series defining $Z(X_0,T)$. The last equality is
Theorem [sk-thm-trace-transport] for $K=\Lambda_X$.

It remains to descend rationality from $\Ql$ to $\mathbf Q$.
Write $Z(X_0,T)=\sum_{n\geq0}z_nT^n$, with $z_n\in\mathbf Z$.
Rationality over $\Ql$ means that there are integers $d,N$ and
$b_1,\ldots,b_d\in\Ql$ such that
$z_n+b_1z_{n-1}+\cdots+b_dz_{n-d}=0$ for all $n>N$.
These are linear equations with rational coefficients in the $d$
unknowns $b_i$. Their coefficient rows span a finite-dimensional
subspace of $\mathbf Q^{d+1}$, and hence finitely many of the equations imply
all the others. This finite rational linear system has a solution over
$\Ql$, and hence one over $\mathbf Q$ by Gaussian elimination. With these
rational $b_i$, the product of $1+b_1T+\cdots+b_dT^d\in\mathbf Q[T]$
and $Z(X_0,T)$ is a polynomial. Therefore $Z(X_0,T)\in\mathbf Q(T)$.
