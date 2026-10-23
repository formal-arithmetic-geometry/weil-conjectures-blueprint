+++
kind  = "proof"
of    = "sk-p-real-semi"
+++
We first prove the weaker bound $a+2$ at the boundary, and then remove
the extra $2$ by taking tensor powers. The assertion is local at a
missing point, so we may replace $X_0$ by an affine neighbourhood of
that point. The complement of $U_0$ is an effective Cartier divisor,
which locally on $X_0$ has one equation, so the open immersion
$U_0\hookrightarrow X_0$ is affine. Thus both curves are affine. Write
$i:S_0=X_0-U_0\hookrightarrow X_0$.

Put $L_U(t)=L(U_0,\mathcal F,t)$. The logarithm of the Euler product
has coefficients

$$
 \log\iota L_U(t)=\sum_{n\ge1}\frac{c_n}{n}t^n,
 \qquad
 c_n=\sum_{d\mid n}d\sum_{d(x)=d}
       \iota\operatorname{Tr}(F_x^{n/d}\mid\mathcal F_{\bar x}).
$$

If $r=\operatorname{rank}\mathcal F$, then the punctual bound and
[sk-lem-wrp-point-count] give $|c_n|\le rDq^{n(a/2+1)}$. Hence the
logarithm converges on the disc $|t|<R=q^{-a/2-1}$, and its exponential
is a nonvanishing holomorphic function there. By the trace formula
([sk-thm-trace-transport]), its Taylor series is that of the rational function
$\iota L_U(t)$, so the two agree on the whole disc.

Let $L_X(t)=L(X_0,j_*\mathcal F,t)$. A compactly supported section of
$j_*\mathcal F$ vanishes on an open subset meeting $U_0$, hence on
$U_0$ because $\mathcal F$ is lisse, and so it is zero by the
definition of $j_*$. Therefore $H_c^0(X,j_*\mathcal F)=0$. The
quotient sheaf in

$$
 0\longrightarrow j_!\mathcal F\longrightarrow j_*\mathcal F
   \longrightarrow i_*i^*j_*\mathcal F\longrightarrow0
$$

is supported on the finite boundary, whose cohomology is concentrated
in degree zero. Hence $H_c^2(X,j_*\mathcal F)=H_c^2(U,\mathcal F)$
canonically, and by [sk-lem-wrp-hc2] its eigenvalues have absolute
value at most $q^{a/2+1}$. It follows from the trace formula that
$\iota L_X$ is holomorphic on $|t|<R$ ([lem-wf-euler-product-middle-extension]).

Comparing the Euler factors, we get

$$
 L_X(t)=L_U(t)\prod_{s\in S_0}
   \det(1-F_st^{d(s)}\mid(j_*\mathcal F)_{\bar s})^{-1}.
$$

Since $L_U$ has no zero on the disc, the finite product on the right
is holomorphic there. This product is the reciprocal of a product of
polynomials with constant term one, so each of these polynomials has
no zero on the disc. For an eigenvalue $\alpha$ at $s$, the roots of
$1-\iota(\alpha)t^{d(s)}$ have absolute value
$|\iota(\alpha)|^{-1/d(s)}$, which is therefore at least $R$. This
gives the preliminary bound

$$
 |\iota(\alpha)|^2\le q_s^{a+2}.
$$

To sharpen it, we apply the preliminary bound to $\mathcal F^{\otimes k}$
for every $k\ge1$; this sheaf has a punctual bound at most $ka$. By
[sk-i-real-boundary], we may choose an eigenvector
$v\in V^{I_s}$ for $\alpha$. Then $v^{\otimes k}$ is a nonzero
invariant eigenvector in $V^{\otimes k}$ with eigenvalue $\alpha^k$,
and hence $|\iota(\alpha)|^{2k}\le q_s^{ka+2}$. Taking $k$th roots and
letting $k$ tend to infinity, we obtain $|\iota(\alpha)|^2\le q_s^a$
([lem-wf-boundary-semicontinuity]).
