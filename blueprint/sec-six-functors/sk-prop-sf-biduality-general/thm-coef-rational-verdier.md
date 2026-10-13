+++
id = "thm-coef-rational-verdier"
kind = "theorem"
title = "Verdier biduality over a finite coefficient field"
order = 2495
uses = ["def-weil-rationalization-karoubi", "lem-coef-integral-finite-extension", "lem-coef-integral-residue-tor", "prop-weil-pbc-rational-transport", "thm-coef-integral-verdier"]
+++
For every finite extension $E/\Ql$, integral duality induces
an exact $E$-linear anti-equivalence

$$
D_{X,E}:D^b_c(X,E)^{\mathrm{op}}\xrightarrow{\sim}D^b_c(X,E).
$$

Its evaluation and natural isomorphism
$\delta_K:K\xrightarrow{\sim}D_{X,E}D_{X,E}K$ are obtained
by rationalizing integral evaluation and biduality. The dualizing
object is the image $\omega_{X,E}$ of $\omega_{X,\mathcal O_E}$.
For $E\subset L$, the canonical comparison

$$
(D_{X,E}K)\otimes_E L\xrightarrow{\sim}
D_{X,L}(K\otimes_E L)
$$

commutes with evaluation and $\delta$, and satisfies the unit
and associator equations for scalar extension.
