+++
id = "prop-weil-efi-site-derived-comparison-isomorphism"
kind = "theorem"
title = "Finite-level etale/pro-etale cohomology comparison"
order = 1707
tags = ["latex:proposition"]
uses = ["def-weil-efi-site-derived-cohomology-comparison", "lemma-weil-efi-site-inverse-image-exact", "lemma-weil-pbc-epsilon-derived-unit"]
+++
Let $\ell$ be prime, let $r\geq1$, and let $\mathcal A$ be a constructible
$\mathbf Z/\ell^r$-module sheaf on $X_{\mathrm{et}}$. For $n\geq0$, the map

$$
c^n_{X,\mathcal A}:H^n(X_{\mathrm{et}},\mathcal A)
\longrightarrow
H^n(X_{\mathrm{proet}},\epsilon_X^{-1}\mathcal A)
$$

is an isomorphism.

## Proof

Exactness identifies
$\mathbf L\epsilon_X^{-1}(\mathcal A[0])$ with
$\epsilon_X^{-1}\mathcal A[0]$. The derived-unit lemma makes

$$
\mathcal A[0]\longrightarrow
R\epsilon_{X,*}\epsilon_X^{-1}\mathcal A[0]
$$

an isomorphism. Derived global sections preserve this isomorphism, and the
canonical identity
$R\Gamma(X_{\mathrm{et}},R\epsilon_{X,*}(-)) =R\Gamma(X_{\mathrm{proet}},-)$ identifies the resulting arrow with
$c_{X,\mathcal A[0]}$. Applying $H^n$ gives the displayed isomorphism.
