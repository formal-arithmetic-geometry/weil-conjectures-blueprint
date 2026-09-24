+++
id = "lemma-nagata-affine-image-kernel-localization"
kind = "lemma"
title = "Localization of the affine image kernel"
order = 148
lean = ["AlgebraicGeometry.Scheme.Hom.ker_pullback_snd"]
uses = ["def-nagata-dense-compactification", "def-nagata-scheme-theoretic-image"]
+++
Let $A$ be a ring, let $T\to\operatorname{Spec}(A)$ be quasi-compact and
quasi-separated, and let $s\in A$. Put

$$
I=\ker\bigl(A\longrightarrow\Gamma(T,\mathcal O_T)\bigr).
$$

If $T_s=T\times_{\operatorname{Spec}(A)}\operatorname{Spec}(A_s)$, then

$$
\ker\bigl(A_s\longrightarrow\Gamma(T_s,\mathcal O_{T_s})\bigr)=IA_s.
$$

This equality is functorial under further localization.

## Proof

Choose a finite affine cover $(T_i)$ of $T$. Quasi-separatedness makes
each $T_i\cap T_j$ quasi-compact, so choose a finite affine refinement of
every such intersection. The sheaf equalizer for this finite covering
computes $\Gamma(T,\mathcal O_T)$ from finite products of the coordinate
rings of the selected affine opens and their finite affine refinements.
Localizing this equalizer at $s$ is exact, commutes with its finite
products, and replaces every selected affine by its inverse image in
$T_s$. It therefore computes $\Gamma(T_s,\mathcal O_{T_s})$. Taking the
kernel of the structural map gives $IA_s$. Repeating the same construction
after a second localization gives the stated functoriality.
