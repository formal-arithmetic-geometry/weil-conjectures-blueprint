+++
id = "sk-thm-sf-global-duality"
kind = "theorem"
title = "Global Verdier duality"
order = 3487
uses = ["sk-prop-sf-open-closed-triangle", "sk-thm-sf-verdier-exchange", "sk-def-ops"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_coefficientDual_rightDerivedLowerShriek"]
tags = ["sketch"]
+++
Here $\mathbb D_X$ and $\omega_X=a_X^!\Lambda_s$ are the Verdier dual and the dualizing
complex of [sk-def-ops], and $s=\operatorname{Spec}k$.

Over algebraically closed $k$, every
$K\in\Dctf(X,\Lambda)$ has natural isomorphisms in
$\Perf(\Lambda)$

$$
 R\Gamma(X,\mathbb D_XK)\simeq
 R\operatorname{Hom}_\Lambda(R\Gamma_c(X,K),\Lambda),
 \tag{1}
$$

$$
 R\Gamma_c(X,\mathbb D_XK)\simeq
 R\operatorname{Hom}_\Lambda(R\Gamma(X,K),\Lambda).
 \tag{2}
$$

The first is the adjoint of the pairing formed by mixed-support cup
product, evaluation, and the counit $\epsilon_{a_X}$ of
$Ra_{X!}\dashv a_X^!$:

$$
 R\Gamma_c(X,K)\otimes^{\mathbf L}R\Gamma(X,\mathbb D_XK)
 \longrightarrow R\Gamma_c(X,\omega_X)
 \xrightarrow{\epsilon_{a_X}}\Lambda.
$$

For a finite base field the same isomorphisms hold in
$D(s_{\mathrm{pro\acute et}},\Lambda)$, before passage to the geometric fibre.
