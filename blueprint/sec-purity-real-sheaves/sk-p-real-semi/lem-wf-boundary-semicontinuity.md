+++
id = "lem-wf-boundary-semicontinuity"
kind = "lemma"
title = "Boundary semicontinuity of weights on a curve"
order = 2841
uses = ["d-real-cohom", "def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "def-wf-middle-extension", "lem-a1-affine-hc2", "lem-wf-boundary-stalk-invariants", "lem-wf-euler-product-middle-extension", "lem-wf-point-count-linear-growth", "p-linear-spectra"]
+++
Let $X_0$ be a smooth geometrically connected affine curve over
$k_0=\mathbf F_q$, let $j:U_0\hookrightarrow X_0$ be a dense open
immersion with finite complement $S_0$, and let $\mathcal F$ be a
lisse Weil sheaf of rank $r\ge1$ on $U_0$. Assume that for every
closed point $x\in|U_0|$ and every eigenvalue $\alpha$ of the local
Frobenius $F_x$ on $\mathcal F_{\bar x}$ the inequality

$$
|\iota(\alpha)|^2\le q_x^{\beta}
$$

holds for a real number $\beta$ (i.e. $\mathcal F$ is punctually
$\iota$-mixed of weights at most $\beta$ in the punctual weight
convention of [def-weil-punctual-weights]). Then the same
inequality holds at every boundary point: for every $s\in S_0$ and
every eigenvalue $\alpha$ of $F_s$ on the middle-extension stalk
$(j_*\mathcal F)_{\bar s}$ of
[def-wf-middle-extension],

$$
|\iota(\alpha)|^2\le q_s^{\beta}.
$$

## Proof

Step 1 (the pole-free region of the open part). Let
$L(U,t):=\prod_{x\in|U_0|}\det(1-F_xt^{d(x)},\mathcal F_{\bar x})^{-1}$
be the open-part $L$-series of [d-real-cohom]. In the punctual weight convention of
[def-weil-punctual-weights], its logarithmic derivative has the
coefficient series

$$
c_m:=\sum_{d\mid m}d\sum_{\substack{x\in|U_0|\\d(x)=d}}
\operatorname{Tr}\bigl(F_x^{m/d}\mid\mathcal F_{\bar x}\bigr),
$$

and by the hypothesis the summands have modulus at most
$r q^{m\beta/2}$ (an eigenvalue of $F_x^{m/d}$ has $\iota$-modulus
$q_x^{\beta/2}$ to the power $m/d$, i.e. $q^{m\beta/2}$). Since
the points over $k_m$ regroup as
$\#U_0(k_m)=\sum_{d\mid m}d\cdot\#\{x\in|U_0|:d(x)=d\}$, the estimate
of [lem-wf-point-count-linear-growth], applied over all base
extensions $k_n$, gives $|c_m|\le r\,d\,q^{m(\beta/2+1)}$ for a
constant $d$. Hence the series $\sum_m c_m t^{m-1}$ converges for
$|t|<R$ with $R:=q^{-\beta/2-1}$, the power series
$\log L(U,t)=\sum_m c_m t^m/m$ converges there, and
$L(U,t)=\exp(\log L(U,t))$ is holomorphic and nonzero on
$|t|<R$.

Step 2 (the poles of the graded form). By
[lem-wf-euler-product-middle-extension] the full $L$-series
$L(X,t):=\prod_{x\in|X_0|}\det(1-F_xt^{d(x)},(j_*\mathcal F)_{\bar x})^{-1}$
equals $\det(1-Ft,H_c^1)/\det(1-Ft,H_c^2)$ with $H_c^i$ the
compact-support cohomology of the middle extension
$j_*\mathcal F$ of [def-wf-middle-extension] in the convention of
[def-weil-ordinary-compact-cohomology] on $X_0$. The
$H_c^2$-factor: the boundary corrections at $S$ are concentrated in
degree zero (the recollement triangle
$j_!\mathcal F\to j_*\mathcal F\to i_*i^*j_*\mathcal F\to$, with
$H_c^i(X,i_*B)=0$ for $i\ge1$ on the zero-dimensional
$B$), so $H_c^2(X,j_*\mathcal F)\cong H_c^2(U,\mathcal F)$, and
[lem-a1-affine-hc2] describes
$H_c^2(U,\mathcal F)$ as the coinvariants $V_{\pi_1(U)}(-1)$ of the
local geometric generic stalk $V=\mathcal F_{\bar\eta}$ twisted by
$(-1)$. The quotient $Q=V_{\pi_1(U)}$ is a Weil subquotient on
which the geometric fundamental group acts trivially. Thus a closed
point Frobenius of degree $d(x)$ acts on $Q$ as the $d(x)$-th
power of its degree-one operator. For every eigenvalue $\lambda$
of that operator, $\lambda^{d(x)}$ is therefore a closed-point
eigenvalue of this quotient, and hence of the original sheaf.
The hypothesis gives $|\iota(\lambda)|\le q^{\beta/2}$.
This argument concerns only the geometrically constant quotient;
it makes no assertion about an arbitrary Frobenius lift on $V$.
Hence an eigenvalue $\alpha$ of the
global $F$ on $H_c^2(X,j_*\mathcal F)$ satisfies
$|\iota(\alpha)|\le q^{\beta/2+1}$, i.e. the roots of the
denominator polynomial, the inverses $\alpha^{-1}$, lie outside the
disc $|t|<R$. The numerator is a polynomial and the rational function
is therefore holomorphic on $|t|<R$.

Step 3 (each boundary factor is pole-free). The identity of
[lem-wf-euler-product-middle-extension] reads
$L(X,t)=L(U,t)\cdot\prod_{s\in S_0}B_s(t)$ with
$B_s(t):=\det(1-F_st^{d(s)},(j_*\mathcal F)_{\bar s})^{-1}$; by
Steps 1–2 the left-hand side is holomorphic and $L(U,t)$ is
holomorphic and nonzero on $|t|<R$, so the finite product
$\prod_s B_s(t)$ has a pole at no point of the disc. A pole of the
product at $t_0$ is a pole of one of the factors, so every
$B_s$ is holomorphic on the disc: no root of
$\det(1-F_st^{d(s)},(j_*\mathcal F)_{\bar s})$ lies in $|t|<R$.
For an eigenvalue $\alpha$ of $F_s$ on the boundary stalk, the
number $t_0$ with $t_0^{d(s)}=\alpha^{-1}$ is such a root, whence
$|\iota(\alpha)|^{-1}\ge q^{-d(s)(\beta/2+1)}$, i.e.

$$
|\iota(\alpha)|^2\le q^{d(s)(\beta+2)}=q_s^{\beta+2}.
$$

Step 4 (sharpening by tensor powers). Apply Steps 1–3 to the $k$-fold
tensor power $\mathcal F^{\otimes k}$, lisse of rank $r^k$ on
$U$, whose punctual bounds are $q_x^{k\beta}$. For an eigenvalue
$\alpha$ of $F_s$ on $(j_*\mathcal F)_{\bar s} =\mathcal F_{\bar\eta}^{I_s}$ (the boundary stalk description
[lem-wf-boundary-stalk-invariants]), choose an eigenvector
$v\in\mathcal F_{\bar\eta}^{I_s}$; then $v^{\otimes k}$ is an
$I_s$-invariant eigenvector of $F_s$ on
$\mathcal F_{\bar\eta}^{\otimes k}$ with eigenvalue $\alpha^k$ (an instance of [p-linear-spectra]), so
$\alpha^k$ is an eigenvalue of $F_s$ on the boundary stalk of
$\mathcal F^{\otimes k}$ and the $\beta+2$ bound of Step 3 for that
sheaf gives
$|\iota(\alpha)|^{2k}\le q_s^{k\beta+2}$, hence
$|\iota(\alpha)|^2\le q_s^{\beta+2/k}$. Letting $k\to\infty$
gives the asserted bound.
