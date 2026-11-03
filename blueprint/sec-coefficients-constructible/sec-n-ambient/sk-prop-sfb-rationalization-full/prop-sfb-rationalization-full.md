+++
id = "prop-sfb-rationalization-full"
kind = "proposition"
title = "Inverting $\\ell$ on the full derived categories"
order = 2330
tags = ["not-formalized"]
uses = ["det-prop-sfb-qlbar-colimit-x-invert-ell"]
+++
Let $X$ be a scheme and $E/\mathbf Q_\ell$ finite, with coefficient rings $\cO_{E,X}$ and
$E_X$ on $X_{\mathrm{proét}}$. Extension of scalars

$$
E_X\otimes_{\cO_{E,X}}-\colon D(X_{\mathrm{proét}},\cO_E)\to D(X_{\mathrm{proét}},E)
$$

identifies $D(X_{\mathrm{proét}},E)$ with the Verdier quotient of
$D(X_{\mathrm{proét}},\cO_E)$ by the complexes $K$ with $H^q(K)[1/\ell]=0$ for all $q$.
This kernel is larger than one might first guess: $\bigoplus_{n\ge1}\cO_{E,X}/\ell^n$ lies
in it, although no single power of $\ell$ kills it.

*Not formalized in Lean.* This is the tex proposition "Inverting $\ell$ on the full derived
categories" (n:rationalization-full), which nothing cites; only the bounded constructible
statement [sk-thm-sfb-rationalization-comparison] is used. It is recorded here and will not
be formalized.
