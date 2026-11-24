+++
id = "proposition-integral-trace-formula"
kind = "proposition"
title = "Integral trace formula"
order = 1011
+++
Let $K\in\href{@definition-constructible-sheaves}{\Dbc(X,\mathcal O_E)}$ and let $\theta:\Phi_X^*K\to K$ be any
morphism, that is, a [Frobenius correspondence](@definition-frobenius-correspondences-their-operators) with integral coefficients. Define its iterates $\theta_m$, the
endomorphisms $T_{c_m}(\theta_m)$ and the stalk maps
$\theta_{m,\bar y}$ by the formulas of Definition [definition-frobenius-correspondences-their-operators]. Then for every $m\geq1$ we have

$$
\href{@definition-categorical-trace}{\operatorname{tr}_{\mathcal O_E}}
\bigl(\href{@definition-frobenius-correspondences-their-operators}{T_{c_m}(\theta_m)}\mid R\Gamma_c(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\href{@definition-categorical-trace}{\operatorname{tr}_{\mathcal O_E}
\bigl(\theta_{m,\bar y}\mid K_{\bar y}\bigr)},
\tag{12.1}
$$

where both sides are [categorical traces](@definition-categorical-trace) of perfect complexes over
$\mathcal O_E$. Their reductions modulo $\pi_E^n$ are the
corresponding traces of Theorem [theorem-trace-formula-frobenius-correspondence]
for $K_n$ and the reduction $\bar\theta_n:\href{@definition-frobenius-correspondences-their-operators}{\Phi_X^*}K_n\to K_n$ of
$\theta$.
