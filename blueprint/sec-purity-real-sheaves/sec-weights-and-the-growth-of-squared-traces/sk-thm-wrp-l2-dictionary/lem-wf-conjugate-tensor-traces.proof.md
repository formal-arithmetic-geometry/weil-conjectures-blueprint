+++
kind  = "proof"
of    = "lem-wf-conjugate-tensor-traces"
+++
At a closed point $x$ the eigenvalue multiset of
$\mathcal F\otimes\bar{\mathcal F}$ on the finite-dimensional
$\Qlb$-vector space $(\mathcal F\otimes\bar{\mathcal F})_{\bar x}=\mathcal F_{\bar x}\otimes\bar{\mathcal F}_{\bar x}$ is the set of
products $\alpha_i\bar\alpha_j$ of the $\iota$-images of the
eigenvalues of $F_x$ on $\mathcal F_{\bar x}$, hence at a point
$y\in X_0(k_m)$ the trace of the tensor is
$\sum_i|\iota(\alpha_i^m)|^2=|\iota\operatorname{Tr}(F_y)|^2\ge0$.
The regrouping of the closed points over the $k_m$-points therefore
gives the logarithmic derivative of the Euler product: the coefficient
of $t^{m-1}$ in $L'/L$ is
$\sum_{y\in X_0(k_m)}\operatorname{Tr}(F_y\mid(\mathcal F\otimes\bar{\mathcal F})_{\bar y})$,
the same point-counting step as in the graded Euler-product identity
[cor-rp-euler-product], with the logarithm of the Frobenius determinant
[lem-zl-log-det-identity] carrying the logarithmic derivative of
the factors: for the Frobenius module
$(\mathcal F\otimes\bar{\mathcal F})_{\bar x}$ with $F=F_x$ it gives
$\log\det(1-TF)^{-1}=\sum_{n\ge1}\Tr(F^n)T^n/n$ in $\Qlb[[T]]$;
substituting $T\mapsto t^{d(x)}$ and applying $t\,\frac{d}{dt}$ gives
$t\,\frac{d}{dt}\log\det(1-F t^{d(x)})^{-1}
=\sum_{n\ge1}d(x)\Tr(F^n)t^{d(x)n}$, and applying the field
embedding $\iota$ coefficientwise transports this identity of formal
power series from $\Qlb[[t]]$ to $\mathbf C[[t]]$. The displayed identity follows, and the coefficients of
$\varphi_{\mathcal F}$ are nonnegative reals.
