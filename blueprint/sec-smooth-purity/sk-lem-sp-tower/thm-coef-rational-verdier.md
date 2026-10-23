+++
id = "thm-coef-rational-verdier"
kind = "theorem"
title = "Verdier biduality over a finite coefficient field"
order = 3002
uses = ["def-sf-setting", "sk-thm-existence", "sk-lem-integral-models", "sk-thm-sfb-rationalization-comparison", "sk-prop-scalar-six", "sk-prop-sfb-finite-extension-compatibility", "lem-coef-integral-finite-extension", "lem-coef-integral-residue-tor", "thm-coef-integral-verdier"]
+++
Let $E/\Ql$ be finite, $a:X\to\operatorname{Spec}k$ the structure map, and
$\omega_{X,E}=Ra^!_EE\in D^b_c(X,E)$ the dualizing object of the condensed
category $D^b_c(X,E)$ ([def-sf-setting], [sk-thm-existence]). Put

$$
D_{X,E}K=R\mathcal Hom_{E_X}(K,\omega_{X,E}).
$$

Then $D_{X,E}$ is an exact $E$-linear anti-equivalence

$$
D_{X,E}:D^b_c(X,E)^{\mathrm{op}}\xrightarrow{\sim}D^b_c(X,E),
$$

with natural isomorphism $\delta_K:K\xrightarrow{\sim}D_{X,E}D_{X,E}K$ given by
evaluation. On integral models it is integral duality with $\ell$ inverted:
$\omega_{X,E}\cong\omega_{X,\mathcal O_E}\otimes_{\mathcal O_E}E$, and for
$K_0\in D^b_c(X,\mathcal O_E)$ there is a natural isomorphism
$D_{X,E}(K_0\otimes E)\cong(D_{X,\mathcal O_E}K_0)\otimes E$ carrying
$\delta_{K_0\otimes E}$ to $\delta_{K_0}\otimes E$.
For $E\subset L$, the canonical comparison

$$
(D_{X,E}K)\otimes_E L\xrightarrow{\sim}
D_{X,L}(K\otimes_E L)
$$

commutes with evaluation and $\delta$, and satisfies the unit
and associator equations for scalar extension.
