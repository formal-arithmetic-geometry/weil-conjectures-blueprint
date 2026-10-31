+++
kind = "proof"
of = "sk-p-real-semi"
+++
We first prove the weaker bound $a+2$ at the boundary by comparing
the $L$-functions of $\mathcal F$ and of $j_*\mathcal F$, and then
remove the extra $2$ by taking tensor powers. The assertion is local at
a point of $X_0-U_0$, so we may replace $X_0$ by an affine neighbourhood of
that point. The complement of $U_0$ is an effective Cartier divisor,
so after shrinking this neighbourhood it is cut out by one equation
$f$, and then $U_0=D(f)$ is affine as well. Write
$i:Z_0=X_0-U_0\hookrightarrow X_0$.

The hypotheses survive this replacement, since forming $j_*$ commutes
with restriction to open subschemes, the restriction of $\mathcal F$
is still punctually of weights $\le a$, and a nonempty open of $X_0$ is still
geometrically connected.

*The $L$-function on $U_0$.* Put $L_U(t)=L(U_0,\mathcal F,t)$.
The logarithm of the Euler product has coefficients

$$
\log\iota L_U(t)=\sum_{n\ge1}\frac{c_n}{n}t^n,
\qquad
c_n=\sum_{d\mid n}d\sum_{\deg(x)=d}
\iota\operatorname{Tr}(\operatorname{Frob}_x^{n/d}\mid\mathcal F_{\bar x}).
$$

Let $r=\operatorname{rank}\mathcal F$. For a closed point $x$ of
degree $d\mid n$, the bound on the weights gives
$|\iota\operatorname{Tr}(\operatorname{Frob}_x^{n/d}\mid\mathcal F_{\bar x})| \le rq_x^{(n/d)a/2}=rq^{na/2}$. Since
$\sum_{d\mid n}d\cdot\#\{x\in|U_0|:\deg(x)=d\}=\#U_0(k_n)$,
Lemma [sk-lem-wrp-point-count] gives $|c_n|\le rDq^{n(a/2+1)}$. Hence the
logarithm converges on the disc $|t|<R=q^{-a/2-1}$, and its exponential
is a nonvanishing holomorphic function there. By the trace formula,
its Taylor series is that of the rational function $\iota L_U(t)$, so
the two agree on the whole disc.

*The $L$-function on $X_0$.* Let $L_X(t)=L(X_0,j_*\mathcal F,t)$.
We show that $\iota L_X$ is holomorphic on the same disc. The support
of a compactly supported section of $j_*\mathcal F$ on $X$ is closed
and proper over $k$, hence finite since $X$ is an affine curve. So the
section vanishes on a dense open subset of $U$, hence on $U$ because
$\mathcal F$ is lisse and $U$ is connected, and it is zero because a
section of $j_*\mathcal F$ is determined by its restriction to $U$.
Therefore $H_c^0(X,j_*\mathcal F)=0$. The
quotient sheaf in

$$
0\longrightarrow j_!\mathcal F\longrightarrow j_*\mathcal F
\longrightarrow i_*i^*j_*\mathcal F\longrightarrow0
$$

is supported on the finite boundary, whose cohomology is concentrated
in degree zero. From the long exact sequence we obtain
$H_c^2(X,j_*\mathcal F)=H_c^2(U,\mathcal F)$, and by
Lemma [sk-lem-wrp-hc2] its eigenvalues have absolute value at most
$q^{a/2+1}$. By the trace formula, every pole of $\iota L_X$ is the
inverse of a Frobenius eigenvalue on $H^0_c$ or $H^2_c$. Since
$H^0_c=0$, the poles have absolute value at least $q^{-a/2-1}=R$, and so
$\iota L_X$ is holomorphic on $|t|<R$.

*The boundary factors.* Comparing the Euler factors, we get

$$
L_X(t)=L_U(t)\prod_{z\in Z_0}
\det(1-\operatorname{Frob}_z t^{\deg(z)}\mid(j_*\mathcal F)_{\bar z})^{-1}.
$$

Since $L_U$ has no zero on the disc, the finite product on the right
is holomorphic there. This product is the reciprocal of a product of
polynomials with constant term one, so each of these polynomials has
no zero on the disc. For an eigenvalue $\alpha$ at $z$, the roots of
$1-\iota(\alpha)t^{\deg(z)}$ have absolute value
$|\iota(\alpha)|^{-1/\deg(z)}$, which is therefore at least $R$. This
gives the preliminary bound

$$
|\iota(\alpha)|^2\le q_z^{a+2}.
$$

*Tensor powers.* To sharpen the bound, we apply it to
$\mathcal F^{\otimes m}$ for every $m\ge1$, which is punctually of
weights $\le ma$. Let $V$ be the local generic fibre of $\mathcal F$ at
$z$. By Lemma [sk-i-real-boundary], the eigenvalue $\alpha$ of
$\operatorname{Frob}_z$ on $(j_*\mathcal F)_{\bar z}$ has an
eigenvector $v\in V^{I_z}$. Then $v^{\otimes m}$ is a nonzero
invariant eigenvector in $V^{\otimes m}$ with eigenvalue $\alpha^m$,
so by the same lemma $\alpha^m$ is an eigenvalue on the stalk of
$j_*(\mathcal F^{\otimes m})$ at $\bar z$. Hence the preliminary bound for $\mathcal F^{\otimes m}$ gives
$|\iota(\alpha)|^{2m}\le q_z^{ma+2}$. Taking $m$th roots and
letting $m$ tend to infinity, we obtain $|\iota(\alpha)|^2\le q_z^a$.
