+++
kind  = "proof"
of    = "thm-wf-l2-dictionary"
+++
Put $\mathcal T=\mathcal G\otimes\mathcal G$.
At every point over every finite extension, the trace of $\mathcal G$
is real by [def-wf-iota-real]. Hence the trace of $\mathcal T$
is its square, equal to the squared absolute value of that trace.
The logarithm of the Frobenius determinant
[lem-zl-log-det-identity] (applied to each local factor, with
$T\mapsto t^{d(x)}$, and transported to $\mathbf C[[t]]$ by the field
embedding $\iota$, exactly as in the proof of
[lem-wf-conjugate-tensor-traces]) and the Euler product
[cor-rp-euler-product] therefore give

$$
\varphi_{\mathcal G}(t)=L'(t)/L(t),\qquad
L(t)=\frac{\iota\det(1-Ft,H_c^1(X,\mathcal T))}
{\iota\det(1-Ft,H_c^2(X,\mathcal T))}.
$$

Here $\varphi_{\mathcal G}$ is the series of
[def-wf-l2-series].

The tensor $\mathcal T$ is lisse and punctually pure of weight $2w$:
its local eigenvalues are products of two eigenvalues of weight $w$ ([p-linear-spectra]).
The description $H_c^2(X,\mathcal T)\simeq T_{\pi_1(X)}(-1)$ of
[lem-a1-affine-hc2], with the weight clause of [sk-lem-wrp-hc2], shows
that $H_c^2(X,\mathcal T)$ is $\iota$-pure of weight $2w+2$ in the
sense of [def-weil-frobenius-module-weights]: its Frobenius
eigenvalues $\alpha$ have $\iota$-modulus $q^{w+1}$. Hence every
denominator root $\alpha^{-1}$ of $L$, if there are any, has modulus

$$
R=q^{-w-1}.
$$

At least one of these roots remains a pole after cancellation.
Indeed [lem-rp-even-tensor-positivity], applied to
$\mathcal G$ with tensor exponent two, says that every local Euler
factor of $L$ has nonnegative real Taylor coefficients and constant
term one. Thus the coefficients of $L$ dominate those of any one
local factor. Choose a closed point $x$ of the nonempty curve.
Since $\mathcal G$ is nonzero lisse, its rank at $x$ is positive,
and the local factor for $\mathcal T$ is the reciprocal of a
nonconstant polynomial with nonzero leading coefficient.
Such a reciprocal has infinitely many nonzero Taylor coefficients:
if it were a polynomial, its product with the denominator would be
one, contradicting degrees. It follows that $L$ cannot be a
polynomial. As its denominator has all its roots on $|t|=R$,
its reduced rational expression has a pole on that circle.

The logarithmic derivative has a pole at every pole of $L$:
locally $L=(t-t_0)^{-a}u$, $a>0$, $u(t_0)\neq0$, gives
$L'/L=-a/(t-t_0)+u'/u$.
Consequently the Taylor radius of $\varphi_{\mathcal G}$ is at most
$R$. On the other hand [lem-wf-l2-upper], applied to the
punctually pure sheaf, bounds that radius below by $R$.
It is therefore exactly $q^{-w-1}$, and
[def-wf-l2-series], [def-wf-l2-norm], [lem-wf-l2-radius] gives
$\|\mathcal G\|=w$.
