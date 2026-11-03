+++
kind = "proof"
of = "sk-thm-wrp-l2-dictionary"
+++
By Lemma [sk-lem-wrp-l2-growth], we have $\nu(\mathcal G)\le w$, and we
must show that the radius of $\varphi_{\mathcal G}$ is not larger than
$q^{-w-1}$. For a real sheaf we find a pole of the logarithmic
derivative of an $L$-function on that circle. The general case then
follows by twisting to weight zero and adding the dual
(Proposition [sk-prop-wrp-real-envelope]).

*The real case.* Suppose first that $\mathcal G$ is real, and put
$\mathcal T=\mathcal G\otimes\mathcal G$. For $x\in X_0(k_n)$ we have
$\iota t_{\mathcal T,n}(x)=|\iota t_{\mathcal G,n}(x)|^2$, because
$\iota t_{\mathcal G,n}(x)$ is real. By the Euler product and the trace
formula,

$$
\varphi_{\mathcal G}(t)=\frac{L'(t)}{L(t)},\qquad
L(t)=\frac{\iota\det(1-Ft\mid H_c^1(X,\mathcal T))}
{\iota\det(1-Ft\mid H_c^2(X,\mathcal T))}.
$$

For the first equality, group the local logarithms by degree; then
the coefficient of $t^{n-1}$ in $L'/L$ becomes the sum of the traces over $X_0(k_n)$, which is
$S_n(\mathcal G)$. Since $\mathcal T$ is pure of weight $2w$,
Lemma [sk-lem-wrp-hc2] shows that all roots of the denominator have
absolute value $R=q^{-w-1}$.

We claim that $L$ has a pole on the circle $|t|=R$. By
Lemma [sk-lem-wrp-positive-euler], each local Euler factor of
$\mathcal T$ has nonnegative Taylor coefficients, and so the
coefficients of the full product dominate those of any one factor.
Choose a closed point of the curve. Since $\mathcal G$ has positive
rank and Frobenius is invertible, the Euler factor of $\mathcal T$ at
this point is the reciprocal of a nonconstant polynomial. It therefore
has infinitely many nonzero Taylor coefficients, because a polynomial
cannot be inverse to a nonconstant polynomial. Hence the full Euler
product is not a polynomial, and the rational function $L$ has a pole.
By the bound on the denominator, every pole lies on $|t|=R$.

A pole of $L$ is also a pole of its logarithmic derivative: if
$L(t)=(t-t_0)^{-m}u(t)$ near $t_0$, with $m>0$ and $u(t_0)\ne0$, then
$L'/L=-m/(t-t_0)+u'/u$. Thus the radius of convergence of
$\varphi_{\mathcal G}$ is at most $R$. Since $\mathcal G$ is pure of
weight $w$, the reverse inequality holds by Lemma [sk-lem-wrp-l2-growth].
Hence the radius is $R$, and $\nu(\mathcal G)=w$.

*The general case.* For an arbitrary pure $\mathcal G$, we use
Proposition [sk-prop-wrp-real-envelope]. The sheaf
$\mathcal G^0=\mathcal G\otimes\mathcal B_b$ is pure of weight zero,
and $\nu(\mathcal G^0)=\nu(\mathcal G)-w$. The sheaf
$\mathcal E=\mathcal G^0\oplus(\mathcal G^0)^\vee$ is nonzero, real
and pure of weight zero, so $\nu(\mathcal E)=0$ by the case already
treated. For every $n$ and $x\in X_0(k_n)$ we have
$\iota t_{\mathcal E,n}(x)=2\operatorname{Re}(\iota t_{\mathcal G^0,n}(x))$,
and hence $S_n(\mathcal E)\le4S_n(\mathcal G^0)$ and
$\nu(\mathcal G^0)\ge0$. The opposite inequality holds by
Lemma [sk-lem-wrp-l2-growth]. Thus $\nu(\mathcal G^0)=0$, and hence
$\nu(\mathcal G)=w$.
