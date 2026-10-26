+++
id = "sk-thm-tf-sp-zero-section"
kind = "theorem"
title = "Verdier's zero-section specialization theorem"
order = 3566
uses = ["sk-lem-tf-sp-dnc-functorial", "sk-lem-tf-sp-constant-family", "sk-thm-pe-constructible-comparison", "sk-cor-pe-finite-tor-comparison", "sk-lem-tf-sp-defect-exchanges", "sk-lem-tf-sp-generic-divisor"]
tags = ["sketch"]
+++
For a separated finite-type $k$-scheme $X$ and a closed subscheme $i\colon Z\hookrightarrow X$, let
$\mathcal D_ZX$ be the deformation to the normal cone of [sk-lem-tf-sp-dnc-functorial], with
special fibre $N_ZX$ and zero section $e\colon Z\hookrightarrow N_ZX$, the special fibre of the
closed immersion $\widetilde e\colon Z\times S\hookrightarrow\mathcal D_ZX$. The specialization
functor is $\operatorname{Sp}_{X,Z}(L)=R\Psi_{\mathcal D_ZX}(L_\eta)$, with the nearby cycles of
[sk-lem-tf-sp-constant-family], and pullback exchange along $\widetilde e$ followed by the inverse
of [sk-lem-tf-sp-constant-family] gives the natural map

$$
\epsilon_{X,Z}(L):e^*\operatorname{Sp}_{X,Z}(L)
\longrightarrow R\Psi_{Z\times S}((i^*L)_\eta)\xrightarrow{\sim}i^*L.
\tag{1}
$$

On $\Dctf(X,A)$, the functor $\operatorname{Sp}_{X,Z}$ and the map (1) are the transports of these
étale constructions along the finite-coefficient constructible comparison
([sk-thm-pe-constructible-comparison], [sk-cor-pe-finite-tor-comparison]).

For every separated finite-type $k$-scheme $X$, every closed subscheme $Z\subset X$, and
$K\in\Dctf(X,A)$, the map (1)

$$
e^*\operatorname{Sp}_{X,Z}(K)\xrightarrow{\sim}i^*K
$$

is an isomorphism in $\Dctf(Z,A)$. In particular, $i^*K=0$ implies
$e^*\operatorname{Sp}_{X,Z}(K)=0$.
