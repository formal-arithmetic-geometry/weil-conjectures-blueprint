+++
kind  = "proof"
of    = "lem-wf-weil-fundamental-representation"
+++
*The abstract extension.* By [d-monodromy] every $w\in W$ has the form
$us^n$ with $n=\deg(w)$ and $u=ws^{-n}\in P$, and this expression is
unique because $n$ is determined by $w$. Hence $\tilde f$ is a
well-defined map; it restricts to $f$ (case $n=0$) and takes $s$ to $T$
(case $u=1$, $n=1$). Induction on $m$, in both directions, turns the
hypothesis on $T$ into $T^mf(u)T^{-m}=f(s^mus^{-m})$ for all
$m\in\mathbf Z$. Since
$(us^n)(u's^{n'})=u(s^nu's^{-n})s^{n+n'}$ with
$s^nu's^{-n}\in P$ ($P$ is normal), we get

$$
\tilde f\bigl((us^n)(u's^{n'})\bigr)
=f(u)\,T^nf(u')T^{-n}\,T^{n+n'}
=\tilde f(us^n)\,\tilde f(u's^{n'}),
$$

so $\tilde f$ is a homomorphism. If $P$ is open and $f$ is continuous,
then $\tilde f$ agrees with the continuous map $f$ on the open
neighbourhood $P$ of $1$, so it is continuous at $1$; a homomorphism of
topological groups that is continuous at $1$ is continuous.

*The Weil fundamental representation.* By
[lem-wf-weil-group-exact-sequence], $\deg:W(X_0,\bar x)\to\mathbf Z$ is
surjective with kernel $\pi_1(X,\bar x)$, so $(W(X_0,\bar x),\deg,s)$ is a
degree datum with $P=\pi_1(X,\bar x)$. Take $M=\operatorname{GL}(V)$,
$f=\rho_{\mathrm{geom}}$, which is a continuous homomorphism by the lisse
sheaf–representation equivalence of [thm-lisse-qlbar-representations],
and $T=T_s$; the commutation relation displayed in
[def-wf-fundamental-representation] is the hypothesis on $T$. The
subgroup $\pi_1(X,\bar x)$ is open in $W(X_0,\bar x)$: it is the fibre
over $0$ of the projection of the fibre product of
[def-wf-fundamental-representation] to the discrete group
$\langle\Phi_X\rangle\cong\mathbf Z$ of [def-tw-frobenius-action]. The
first part therefore applies, and $\tilde f$ is the displayed $\rho$.
