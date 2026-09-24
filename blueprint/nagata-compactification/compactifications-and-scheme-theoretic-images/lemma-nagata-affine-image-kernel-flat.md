+++
id = "lemma-nagata-affine-image-kernel-flat"
kind = "lemma"
title = "Flat base change of the affine image kernel"
order = 151
lean = ["AlgebraicGeometry.Scheme.Hom.ker_pullback_snd"]
uses = ["def-nagata-dense-compactification", "def-nagata-scheme-image-factor", "lemma-nagata-affine-image-kernel-localization", "lemma-nagata-scheme-image-of-closed-immersion"]
+++
Let $A\to B$ be flat, let $T\to\operatorname{Spec}(A)$ be quasi-compact
and quasi-separated, and put

$$
I=\ker\bigl(A\longrightarrow\Gamma(T,\mathcal O_T)\bigr).
$$

For $T_B=T\times_{\operatorname{Spec}(A)}\operatorname{Spec}(B)$ one has

$$
\ker\bigl(B\longrightarrow\Gamma(T_B,\mathcal O_{T_B})\bigr)=IB.
$$

The equality is natural in the flat algebra $B$ and commutes with
localization on $B$.

## Proof

Use the finite affine cover and finite affine refinements from
[lemma-nagata-affine-image-kernel-localization]. Tensor its finite
sheaf equalizer with $B$. Flatness makes tensoring exact, and tensoring
commutes with the finite products in this diagram. The resulting affine
coordinate rings are precisely those of the base-changed cover of $T_B$,
so the resulting equalizer computes $\Gamma(T_B,\mathcal O_{T_B})$.
Exactness identifies the kernel of the base-changed structural map with
$I\otimes_A B$, whose image in $B$ is $IB$. Naturality follows from the
naturality of tensor product, and compatibility with localization is
[lemma-nagata-affine-image-kernel-localization] applied over $B$.
