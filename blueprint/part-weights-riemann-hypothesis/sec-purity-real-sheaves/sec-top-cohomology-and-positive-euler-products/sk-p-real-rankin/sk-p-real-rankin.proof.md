+++
kind = "proof"
of = "sk-p-real-rankin"
+++
On an affine curve the $L$-function of
$\mathcal G^{\otimes2m}$ has poles only from $H^2_c$, which is
controlled by determinant weights, and positivity forces every local
factor to be holomorphic where the $L$-function is.
Replacing $\mathcal G$ by its semisimplification does not change
its local characteristic polynomials or the determinant weights of its
constituents (Lemma [sk-p-linear-filtration]). We may therefore
assume that $\mathcal G$ is semisimple, and then its restriction to the
geometric fundamental group is semisimple by
Lemma [sk-i-restriction].

*The top cohomology.* Fix $m\ge1$ and put
$\mathcal T=\mathcal G^{\otimes2m}$. By
Proposition [sk-prop-walg-determinant-weights](1), every constituent of
$\mathcal T$ has determinant weight at most $2m\beta$.

By Lemma [sk-lem-wrp-hc2], $H_c^2(U,\mathcal T)=T_{\pi_1(U)}(-1)$, where
$T$ is the generic fibre of $\mathcal T$. The geometric fundamental
group acts trivially on $T_{\pi_1(U)}$, so its simple Weil factors are one-dimensional, as one sees
by triangularizing the operator induced by a degree-one lift. If
$b$ is the eigenvalue on such a factor, the factor is a constituent of
$\mathcal T$, because $T_{\pi_1(U)}$ is a Weil quotient of $T$, and its
determinant weight is $\lambda_\iota(b)$. Since
$\lambda_\iota(b)=2\log_q|\iota(b)|\le2m\beta$, we get
$|\iota(b)|\le q^{m\beta}$. Since the twist $(-1)$ multiplies
eigenvalues by $q$, every eigenvalue $\mu$ of $F$ on
$H_c^2(U,\mathcal T)$ satisfies $|\iota(\mu)|\le q^{m\beta+1}$.

*The local factors.* Next we compare the global Euler product
with its local factors. Since $H_c^0=0$ by Lemma [sk-lem-wrp-hc2],
Theorem [sk-thm-trace-transport] gives

$$
L(U_0,\mathcal T,t)
=\prod_{x\in|U_0|}\det(1-\operatorname{Frob}_x t^{\deg(x)}\mid\mathcal T_{\bar x})^{-1}
=\frac{\det(1-Ft\mid H_c^1(U,\mathcal T))}
{\det(1-Ft\mid H_c^2(U,\mathcal T))}.
$$

This is an identity of formal power series, and the product is
coefficientwise locally finite because there are only finitely many
closed points of bounded degree. After applying $\iota$, the bound on
$H_c^2$ shows that the denominator has no zero on the disc $|t|<R_m$,
where $R_m=q^{-m\beta-1}$. Hence the rational function, and with it
its Taylor series, is holomorphic on this disc.

By Lemma [sk-lem-wrp-positive-euler], each local factor
$\det(1-\operatorname{Frob}_x t^{\deg(x)}\mid\mathcal T_{\bar x})$ has no zero on the same
disc. If $\alpha$ is a local eigenvalue of $\mathcal G$, then
$\alpha^{2m}$ is an eigenvalue on $\mathcal T$ by
Lemma [sk-p-linear-filtration], so that
$1-\iota(\alpha)^{2m}t^{\deg(x)}$ divides the local factor. Its roots
have absolute value
$|\iota(\alpha)|^{-2m/\deg(x)}$, which must therefore be at least $R_m$.
Consequently

$$
|\iota(\alpha)|^2\le q_x^{\beta+1/m}.
$$

Letting $m$ tend to infinity proves the bound.
