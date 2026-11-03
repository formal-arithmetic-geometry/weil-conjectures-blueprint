+++
id = "sk-thm-sf-global-duality"
kind = "theorem"
title = "Global Verdier duality"
order = 516
lean = ["AlgebraicGeometry.Etale.nonempty_iso_coefficientDual_rightDerivedLowerShriek"]
uses = ["sk-prop-sf-open-closed-triangle", "sk-thm-sf-verdier-exchange", "sk-def-ops"]
tags = ["sketch"]
+++
Suppose $k$ is algebraically closed. For every
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ there are natural isomorphisms

$$
\begin{aligned}
R\Gamma(X,\mathbb D_XK)&\simeq
R\!\operatorname{Hom}_\Lambda(R\Gamma_c(X,K),\Lambda),
\\
R\Gamma_c(X,\mathbb D_XK)&\simeq
R\!\operatorname{Hom}_\Lambda(R\Gamma(X,K),\Lambda).
\end{aligned}
\tag{11.4, 11.5}
$$

The first is the adjoint of the pairing formed by the cup product
with mixed supports, evaluation, and the counit $\varepsilon_{a_X}$ of
$Ra_{X!}\dashv a_X^!$:

$$
R\Gamma_c(X,K)\otimes^{\mathbf L}R\Gamma(X,\mathbb D_XK)
\longrightarrow R\Gamma_c(X,\omega_X)
\xrightarrow{\varepsilon_{a_X}}\Lambda.
$$

For a finite base field, the same isomorphisms hold in
$D(s_{\mathrm{pro}\acute{e}t},\Lambda)$, before passage to the geometric fibre.
