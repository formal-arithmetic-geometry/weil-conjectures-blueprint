+++
id = "lemma-weil-pbc-epsilon-direct-image-constructible-bounds"
kind = "lemma"
title = "Finite constructibility and lower bounds"
order = 1809
uses = ["lemma-weil-pbc-epsilon-inverse-image-exact", "lemma-weil-pbc-epsilon-scheme-naturality"]
+++
Let $A$ be finite and let $L\in D_c^+(X_{\mathrm{et}},A)$ vanish in degrees
$<a$. Then $\epsilon_X^{-1}L$ has constructible cohomology and also vanishes
in degrees $<a$. Both $Rf_{\mathrm{et},*}L$ and
$Rf_{\mathrm{proet},*}\epsilon_X^{-1}L$ vanish in degrees $<a$.

## Proof

Exactness gives

$$
\mathcal H^q(\epsilon_X^{-1}L)
=\epsilon_X^{-1}\mathcal H^q(L).
$$

For each $q$, choose a finite stratification on which $\mathcal H^q(L)$ is
locally constant with finite stalks. Scheme naturality identifies its inverse
image on each pro-etale stratum with the same finite locally constant sheaf,
so that stratification witnesses constructibility of the corresponding
cohomology sheaf. The equality also preserves the lower vanishing bound.
Right-derived direct image has no
negative derived degree; its hypercohomology terms have $p\geq0$ and
$q\geq a$, which gives the same lower bound for both direct images.
