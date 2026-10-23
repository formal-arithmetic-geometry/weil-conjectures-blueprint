+++
kind  = "proof"
of    = "sk-thm-wrp-l2-dictionary"
+++
Suppose first that $\mathcal G$ is real ([sk-def-wrp-real-definition]), and
put $\mathcal T=\mathcal G\otimes\mathcal G$. For $x\in X_0(k_n)$ we have
$\iota t_{\mathcal T,n}(x)=|\iota t_{\mathcal G,n}(x)|^2$, because
$\iota t_{\mathcal G,n}(x)$ is real. By the Euler product and the trace
formula ([sk-thm-trace-transport]),

$$
 \varphi_{\mathcal G}(t)=\frac{L'(t)}{L(t)},\qquad
 L(t)=\frac{\iota\det(1-Ft\mid H_c^1(X,\mathcal T))}
            {\iota\det(1-Ft\mid H_c^2(X,\mathcal T))}.
$$

Indeed, if we group the local logarithms by degree, the coefficient of
$t^{n-1}$ becomes the sum of the traces over $X_0(k_n)$, which is
$S_n(\mathcal G)$ ([lem-wf-conjugate-tensor-traces]). Since $\mathcal T$ is
pure of weight $2w$, [sk-lem-wrp-hc2] shows that all roots of the denominator
have absolute value $R=q^{-w-1}$.

We claim that $L$ has a pole on the circle $|t|=R$. By
[sk-lem-wrp-positive-euler], each local Euler factor of
$\mathcal T$ has nonnegative Taylor coefficients, and so the
coefficients of the full product dominate those of any one factor.
Choose a closed point of the curve. Since $\mathcal G$ has positive
rank and Frobenius is invertible, its Euler factor is the reciprocal
of a nonconstant polynomial, and hence it has infinitely many nonzero
Taylor coefficients (a polynomial cannot be inverse to a nonconstant
polynomial). Therefore the full Euler product is not a polynomial. It
follows that the rational function $L$ has a pole, and by the bound on
the denominator every pole lies on $|t|=R$.

A pole of $L$ is also a pole of its logarithmic derivative: if
$L(t)=(t-t_0)^{-a}u(t)$ near $t_0$, with $a>0$ and $u(t_0)\ne0$, then
$L'/L=-a/(t-t_0)+u'/u$. Thus the radius of convergence of
$\varphi_{\mathcal G}$ is at most $R$. Since $\mathcal G$ is pure of
weight $w$, [sk-lem-wrp-l2-growth] gives the reverse inequality.
Hence the radius is $R$, and $\nu(\mathcal G)=w$
([thm-wf-l2-dictionary]).

For an arbitrary pure $\mathcal G$, consider its real envelope
([sk-prop-wrp-real-envelope]). The sheaf
$\mathcal G^0=\mathcal G\otimes\mathcal B_b$ is pure of weight zero,
and $\nu(\mathcal G^0)=\nu(\mathcal G)-w$. The real envelope
$\mathcal E=\mathcal G^0\oplus(\mathcal G^0)^\vee$ is nonzero, real
and pure of weight zero, so $\nu(\mathcal E)=0$ by the case already
treated. For every $n$ and $x\in X_0(k_n)$ we have
$\iota t_{\mathcal E,n}(x)=2\operatorname{Re}(\iota t_{\mathcal G^0,n}(x))$,
and hence $S_n(\mathcal E)\le4S_n(\mathcal G^0)$ and
$\nu(\mathcal G^0)\ge0$. The upper bound for pure sheaves gives the
opposite inequality. Thus $\nu(\mathcal G^0)=0$, which proves the
theorem ([lem-wf-l2-purity-rigidity]).

*Complement.* If $S_n(N)\le Cq^{nB}$, then $\nu(N)\le B-1$ by the definition
of $\nu$, and $\nu(N)=v$ by the theorem.
