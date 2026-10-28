+++
id = "sk-prop-tf-transport-integral"
kind = "proposition"
title = "Integral trace formula"
order = 3831
uses = ["sk-def-pe-derived-completion", "sk-d-weil", "sk-thm-tf-coefficient-morphism-formula", "sk-lem-finite", "sk-prop-scalar-six", "sk-p-trace"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be separated and of finite type, $X=X_0\times_{\mathbf F_q}k$,
and $E/\Ql$ finite with uniformizer $\pi_E$.
For $K\in\Dbc(X,\mathcal O_E)$, write $(K_n)$ for its normalized reduction
tower modulo $\pi_E^n$ ([sk-def-pe-derived-completion]).

Let $K\in\Dbc(X,\mathcal O_E)$ and let $\theta:\Phi_X^*K\to K$ be any
morphism in $\Dbc(X,\mathcal O_E)$, a Frobenius correspondence with
integral coefficients. Define its iterates $\theta_m$, the global
operators $T_{c_m}(\theta_m)$ and the local operators
$\theta_{m,\bar y}$ by the formulas of [sk-d-weil]. For every $m\geq1$,

$$
 \operatorname{tr}_{\mathcal O_E}
   \bigl(T_{c_m}(\theta_m)\mid R\Gamma_c(X_{\mathrm{pro\acute et}},K)\bigr)
 =\sum_{y\in X_0(\mathbf F_{q^m})}
   \operatorname{tr}_{\mathcal O_E}
   \bigl(\theta_{m,\bar y}\mid K_{\bar y}\bigr),
 \tag{1}
$$

where both sides are categorical traces of perfect complexes over
$\mathcal O_E$. Their reductions modulo $\pi_E^n$ are the
corresponding traces of [sk-thm-tf-coefficient-morphism-formula]
for $K_n$ and the reduction $\bar\theta_n:\Phi_X^*K_n\to K_n$ of
$\theta$.
