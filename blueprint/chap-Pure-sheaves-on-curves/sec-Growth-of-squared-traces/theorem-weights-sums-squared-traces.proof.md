+++
kind = "proof"
of = "theorem-weights-sums-squared-traces"
order = 1212
uses = ["proposition-sp-unique-adjoint", "definition-trace-function", "theorem-trace-formula-euler-product", "lemma-filtrations-spectra", "proposition-weights-under-usual-operations", "lemma-degree-zero-top-cohomology", "definition-real-sheaves", "lemma-positivity-convergence", "lemma-extreme-degrees-affine-curve", "lemma-cohomological-range-curve", "proposition-twisting-weight-zero-adding-dual", "lemma-radius-squared-traces", "lemma-bounds-squared-traces", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Lemma [lemma-bounds-squared-traces](1) gives $\nu(\mathcal G)\le w$, so,
by Lemma [lemma-radius-squared-traces], we must show that the radius of $\varphi_{\mathcal G}$ is not larger than
$q^{-w-1}$. For a real sheaf we find a pole of the logarithmic
derivative of an $L$-function on that circle, and
Proposition [proposition-twisting-weight-zero-adding-dual] reduces the
general case to this one by twisting to weight zero and adding the dual.

*The real case.* Suppose first that $\mathcal G$ is real, and put
$\mathcal T=\mathcal G\otimes\mathcal G$. The squared traces of
$\mathcal G$ are then the traces of $\mathcal T$, and we express their
generating series through the $L$-function of $\mathcal T$. Since
$\iota t_{\mathcal G,n}(x)$ is real, we have
$\iota t_{\mathcal T,n}(x)=|\iota t_{\mathcal G,n}(x)|^2$ for
$x\in X_0(k_n)$. The Euler product and the trace formula then give

$$
\varphi_{\mathcal G}(t)=\frac{L'(t)}{L(t)},\qquad
L(t)=\frac{\iota\det(1-Ft\mid H_c^1(X,\mathcal T))}
{\iota\det(1-Ft\mid H_c^2(X,\mathcal T))}.
$$

For the first equality, group the local logarithms by degree. Then
the coefficient of $t^{n-1}$ in $L'/L$ is the sum of the traces over
$X_0(k_n)$, which is $S_n(\mathcal G)$. As $\mathcal T$ is pure of weight $2w$,
Lemma [lemma-degree-zero-top-cohomology] shows that all roots of the denominator have
absolute value $R=q^{-w-1}$.

We show that the function $L$ has a pole on the circle $|t|=R$. This is
not automatic, since a priori all the eigenvalues on $H^2_c$ could
cancel against eigenvalues on $H^1_c$, but positivity rules this out.
Indeed, by Lemma [lemma-positivity-euler-factors], each local Euler
factor of $\mathcal T$ has nonnegative Taylor coefficients, so the
coefficients of the full product dominate those of any one factor.
Now choose a closed point of the curve. Since $\mathcal G$ has positive rank and
Frobenius is invertible, the Euler factor of $\mathcal T$ at this point is the
reciprocal of a nonconstant polynomial. It has infinitely many nonzero Taylor
coefficients, because a polynomial cannot be inverse to a nonconstant
polynomial. Hence the full Euler product is not a polynomial, and the rational
function $L$ has a pole, which by the bound on the denominator lies on
$|t|=R$.

A pole of $L$ is also a pole of its logarithmic derivative: if
$L(t)=(t-t_0)^{-m}u(t)$ near $t_0$, with $m>0$ and $u(t_0)\ne0$, then
$L'/L=-m/(t-t_0)+u'/u$. So the radius of convergence of
$\varphi_{\mathcal G}$ is exactly $R$, and
Lemma [lemma-radius-squared-traces] gives $\nu(\mathcal G)=w$.

*The general case.* Let $\mathcal G$ be an arbitrary pure sheaf, and
let $\mathcal G^0=\mathcal G\otimes\mathcal B_b$ and $\mathcal E$ be as in
Proposition [proposition-twisting-weight-zero-adding-dual]. The sheaf
$\mathcal G^0$ is pure of weight zero, and by
Lemma [lemma-bounds-squared-traces](3) we have
$\nu(\mathcal G^0)=\nu(\mathcal G)+\lambda_\iota(b)=\nu(\mathcal G)-w$, so it
suffices to show that $\nu(\mathcal G^0)=0$. The sheaf
$\mathcal E=\mathcal G^0\oplus(\mathcal G^0)^\vee$ is nonzero, real
and pure of weight zero, so by the case already treated $\nu(\mathcal E)=0$.

This lower bound passes to $\mathcal G^0$, because the trace of
$\mathcal E$ is twice the real part of that of $\mathcal G^0$. In other words,
for every $n$ and $x\in X_0(k_n)$ we have
$\iota t_{\mathcal E,n}(x)=2\operatorname{Re}(\iota t_{\mathcal G^0,n}(x))$.
Hence $S_n(\mathcal E)\le4S_n(\mathcal G^0)$, and so
$\nu(\mathcal G^0)\ge0$. Since the opposite inequality comes from
Lemma [lemma-bounds-squared-traces](1), we obtain $\nu(\mathcal G^0)=0$, that is,
$\nu(\mathcal G)=w$.
