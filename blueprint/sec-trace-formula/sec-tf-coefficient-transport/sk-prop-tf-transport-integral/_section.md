+++
id = "sk-prop-tf-transport-integral"
kind = "proposition"
title = "Integral trace formula"
order = 603
uses = ["sk-def-pe-derived-completion", "sk-d-weil", "sk-thm-tf-coefficient-morphism-formula", "sk-lem-finite", "sk-prop-scalar-six", "sk-p-trace"]
tags = ["sketch"]
+++
Let $K\in\Dbc(X,\mathcal O_E)$ and let $\theta:\Phi_X^*K\to K$ be any
morphism, that is, a Frobenius correspondence with integral coefficients. Define its iterates $\theta_m$, the
endomorphisms $T_{c_m}(\theta_m)$ and the stalk maps
$\theta_{m,\bar y}$ by the formulas of Definition [sk-d-weil]. Then for every $m\geq1$ we have

$$
\operatorname{tr}_{\mathcal O_E}
\bigl(T_{c_m}(\theta_m)\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\mathcal O_E}
\bigl(\theta_{m,\bar y}\mid K_{\bar y}\bigr),
\tag{13.1}
$$

where both sides are categorical traces of perfect complexes over
$\mathcal O_E$. Their reductions modulo $\pi_E^n$ are the
corresponding traces of Theorem [sk-thm-tf-coefficient-morphism-formula]
for $K_n$ and the reduction $\bar\theta_n:\Phi_X^*K_n\to K_n$ of
$\theta$.
