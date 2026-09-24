+++
id = "lemma-weil-pbc-epsilon-direct-image"
kind = "lemma"
title = "Comparison direct-image transport"
order = 1922
uses = ["def-weil-pbc-epsilon-direct-image-comparison", "lemma-weil-pbc-epsilon-direct-image-constructible-bounds", "lemma-weil-pbc-epsilon-direct-image-higher-sheaves", "lemma-weil-pbc-epsilon-direct-image-naturality", "lemma-weil-pbc-hypercohomology-convergence"]
+++
Let $A$ be finite, let $f:X\to Y$ be quasi-compact and quasi-separated, and
let $L\in D_c^+(X_{\mathrm{et}},A)$. The canonical map

$$
D_f(L):\epsilon_Y^{-1}Rf_{\mathrm{et},*}L
\longrightarrow Rf_{\mathrm{proet},*}\epsilon_X^{-1}L
$$

is an isomorphism, natural in $L$, in $f$, and in Cartesian base change.

## Proof

Choose $a$ below the cohomology of $L$. The truncation towers on both sides
give morphisms of hypercohomology spectral sequences whose second pages are

$$
\epsilon_Y^{-1}R^pf_{\mathrm{et},*}\mathcal H^q(L)
\longrightarrow
R^pf_{\mathrm{proet},*}\epsilon_X^{-1}\mathcal H^q(L).
$$

Every component is an isomorphism by Lemma
[lemma-weil-pbc-epsilon-direct-image-higher-sheaves]. The bounds lemma
puts both spectral sequences in $p\geq0$, $q\geq a$. Thus each total degree
has a finite exhaustive separated filtration, by the numerical argument of
Lemma [lemma-weil-pbc-hypercohomology-convergence]. Page induction and
finite-filtration induction make the abutment map an isomorphism in every
degree. Hence $D_f(L)$ is an isomorphism in the derived category. Its
naturality statements are Lemma
[lemma-weil-pbc-epsilon-direct-image-naturality].
