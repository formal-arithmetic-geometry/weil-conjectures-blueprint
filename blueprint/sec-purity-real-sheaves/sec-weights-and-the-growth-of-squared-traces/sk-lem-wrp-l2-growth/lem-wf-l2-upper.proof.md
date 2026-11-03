+++
kind  = "proof"
of    = "lem-wf-l2-upper"
+++
At $y\in X_0(k_m)$ the eigenvalues of the Frobenius $F_y^{(m)}$
are the $m/d(y)$-th powers of the local eigenvalues at the closed
point below, hence have modulus at most $q^{mw/2}$ by the punctual
bounds of [def-weil-punctual-weights]; therefore

$$
\|f_{\mathcal F}\|_m^2\le r^2\cdot\#X_0(k_m)\cdot q^{mw}
\le C\,q^{m(w+1)}
$$

for a constant $C$ (the point-count bound of the affine curve,
[lem-wf-point-count-linear-growth] of the basic-weight chapter). The
$\limsup$ in [def-wf-l2-norm] is therefore $0$ for
$\beta>w$, hence $\|\mathcal F\|\le w$.
