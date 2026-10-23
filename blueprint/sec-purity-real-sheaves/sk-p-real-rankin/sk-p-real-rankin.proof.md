+++
kind  = "proof"
of    = "sk-p-real-rankin"
+++
We first bound the top cohomology of the even tensor powers.
Replacing $\mathcal G$ by its Weil semisimplification does not change
its local characteristic polynomials or the determinant weights of its
constituents ([sk-p-linear-filtration]). We may therefore
assume that $\mathcal G$ is semisimple; then its restriction to the
geometric fundamental group is semisimple by [sk-i-restriction].

Fix $k\ge1$ and put $\mathcal T=\mathcal G^{\otimes2k}$. Iterating the
tensor formula of [sk-p-tensor] $2k$ times, we see that every constituent of
$\mathcal T$ has determinant weight at most $2k\beta$; the hypotheses on
finite geometric determinants hold for all constituents involved by
[sk-d-real-detweights] (this is [sk-cor-walg-curve-calculus]).

By [sk-lem-wrp-hc2], $H_c^2(U,\mathcal T)=T_P(-1)$, where $T$ is
the generic fibre of $\mathcal T$. The geometric group acts trivially
on $T_P$, so its simple Weil factors are one-dimensional, as one sees
by triangularizing the operator induced by a degree-one lift. If
$b$ is the eigenvalue on such a factor, the factor is a constituent of
$\mathcal T$ with determinant weight $\lambda_\iota(b)$, and hence
$|\iota(b)|\le q^{k\beta}$ ([lem-rp-hc2-eigenvalue-determinant-weight]).
Therefore every eigenvalue $\lambda$ on $H_c^2$ satisfies
$|\iota(\lambda)|\le q^{k\beta+1}$.

Next we compare the global Euler product with its local factors.
By [sk-thm-trace-transport] and since $H_c^0=0$, we have

$$
 L(U_0,\mathcal T,t)
 =\prod_{x\in|U_0|}\det(1-F_xt^{d(x)}\mid\mathcal T_{\bar x})^{-1}
 =\frac{\det(1-Ft\mid H_c^1(U,\mathcal T))}
        {\det(1-Ft\mid H_c^2(U,\mathcal T))}
$$

([cor-rp-euler-product]). This is an identity of formal power series, and
the product is coefficientwise locally finite because there are only finitely
many closed points of bounded degree. After applying $\iota$, the bound on
$H_c^2$ shows that the denominator has no zero on the disc $|t|<R_k$,
where $R_k=q^{-k\beta-1}$. Hence the rational function, and with it
its Taylor series, is holomorphic on this disc.

By [sk-lem-wrp-positive-euler], each local factor
$\det(1-F_xt^{d(x)}\mid\mathcal T_{\bar x})$ has no zero on the same
disc. If $\alpha$ is a local eigenvalue of $\mathcal G$, then
$\alpha^{2k}$ is an eigenvalue on $\mathcal T$ by [sk-p-linear-filtration].
The roots of $1-\iota(\alpha)^{2k}t^{d(x)}$ have absolute value
$|\iota(\alpha)|^{-2k/d(x)}$, which must therefore be at least $R_k$.
Consequently

$$
 |\iota(\alpha)|^2\le q_x^{\beta+1/k}.
$$

Letting $k$ tend to infinity proves the bound ([lem-rp-upper-bound]).
