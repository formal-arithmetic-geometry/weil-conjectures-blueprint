+++
id = "lem-pc-projection-formula"
kind = "lemma"
title = "The projection formula"
order = 835
uses = ["def-pc-base-change", "def-pc-derived-category", "def-pc-derived-direct-image", "def-sc-invertible-module"]
+++
Let $f:X\to Y$ be a quasi-compact, quasi-separated morphism of schemes.
For $E\in D_{\text{QCoh}}(\mathcal{O}_X)$ and $K\in D_{\text{QCoh}}(\mathcal{O}_Y)$ the
canonical map

$$
Rf_*(E)\otimes_{\mathcal{O}_Y}^{\mathbb L}K\;\longrightarrow\;
Rf_*(E\otimes_{\mathcal{O}_X}^{\mathbb L}Lf^*K)
$$

is an isomorphism; in particular, for an invertible
$\mathcal{O}_Y$-module $\mathcal{N}$,
$Rf_*(E)\otimes\mathcal{N}\cong Rf_*(E\otimes f^*\mathcal{N})$.
