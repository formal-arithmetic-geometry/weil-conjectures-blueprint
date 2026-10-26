+++
id = "sk-thm-tf-uniform-formula"
kind = "theorem"
title = "Grothendieck–Lefschetz trace formula"
order = 3529
uses = ["sk-def-sf-weil-complexes", "sk-prop-scalar-six", "sk-lem-tf-frobenius-convention", "sk-def-pe-derived-completion", "sk-thm-trace-formula", "sk-prop-tf-transport-integral", "sk-lem-tf-rational-model", "sk-p-trace", "sk-thm-sfb-qlbar-two-colimit", "sk-lem-finite"]
tags = ["sketch"]
+++
Let $X_0$ be separated and of finite type over $\mathbf F_q$, put
$X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, and suppose
$\ell\nmid q$. Let

$$
 \Lambda\in\{A,\Zl,\mathcal O_E,\Ql,E,\overline{\mathbf Q}_\ell\},
 \qquad K\in\Dctf(X,\Lambda),
$$

with a Weil structure as in [sk-def-sf-weil-complexes].
Here $A$ is any finite commutative $\ell$-primary ring, and for
integral and rational coefficients $\Dctf(X,\Lambda)=\Dbc(X,\Lambda)$.
Let $\operatorname{Frob}_{X,K}$
be the geometric Frobenius on $R\Gamma_c(X_{\mathrm{pro\acute et}},K)$ and
$\operatorname{Frob}_{y,m}$ its local operator on $K_{\bar y}$ at
$y\in X_0(\mathbf F_{q^m})$. For every $m\geq1$, in $\Lambda$,

$$
 \boxed{\quad
 \operatorname{tr}_{\Lambda}
   \bigl(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro\acute et}},K)\bigr)
 =\sum_{y\in X_0(\mathbf F_{q^m})}
   \operatorname{tr}_{\Lambda}
   \bigl(\operatorname{Frob}_{y,m}\mid K_{\bar y}\bigr).
 \quad}
 \tag{1}
$$

The complexes inside the traces are perfect over $\Lambda$, and the
formula is compatible with the coefficient comparisons of
[sk-prop-scalar-six]. For $\Lambda=\Ql,E,\overline{\mathbf Q}_\ell$, it reads

$$
 \sum_i(-1)^i\operatorname{Tr}
   \bigl(\operatorname{Frob}_{X,K}^m\mid H_c^i(X_{\mathrm{pro\acute et}},K)\bigr)
 =\sum_{y\in X_0(\mathbf F_{q^m})}\sum_j(-1)^j
   \operatorname{Tr}\bigl(\operatorname{Frob}_{y,m}\mid H^j(K_{\bar y})\bigr),
 \tag{2}
$$

where all sums over degrees are finite.
