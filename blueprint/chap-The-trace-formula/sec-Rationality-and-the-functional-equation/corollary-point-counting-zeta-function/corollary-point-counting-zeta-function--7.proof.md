+++
kind = "proof"
of = "corollary-point-counting-zeta-function--7"
order = 1040014
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "definition-weil-structure--1", "definition-weil-structure--3", "theorem-grothendieck-lefschetz-trace-formula--5", "theorem-grothendieck-lefschetz-trace-formula--6", "corollary-point-counting-zeta-function--2", "corollary-point-counting-zeta-function--5", "corollary-point-counting-zeta-function--6", "lemma-hankel-rank-rationality--2", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "definition-admissible-blow-up--1", "theorem-extension-partial-section--1", "theorem-elimination-indeterminacy--1", "lemma-extending-graph-from-compactification--1", "lemma-separation-closures--1", "lemma-extending-isomorphism-over-closure-closed--1", "lemma-gluing-after-admissible-blow-ups--1", "lemma-affine-covers-dense-intersection--1"]
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
