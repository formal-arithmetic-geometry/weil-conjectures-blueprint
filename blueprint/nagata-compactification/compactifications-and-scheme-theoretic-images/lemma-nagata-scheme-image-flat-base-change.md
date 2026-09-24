+++
id = "lemma-nagata-scheme-image-flat-base-change"
kind = "lemma"
title = "Flat base change of a scheme-theoretic image, [stacks-project]"
order = 152
lean = ["AlgebraicGeometry.Scheme.Hom.ker_pullback_snd"]
uses = ["def-nagata-dense-compactification", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-affine-image-kernel-flat", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion"]
+++
Let $g\colon T\to Y$ be quasi-compact and quasi-separated and let
$q\colon Y'\to Y$ be flat. For the base change
$g'\colon T\times_YY'\to Y'$ one has a canonical isomorphism

$$
\operatorname{SIm}(g')
\cong\operatorname{SIm}(g)\times_YY'
$$

of closed subschemes of $Y'$.

## Proof

Work over an affine open $V=\operatorname{Spec}(A)\subseteq Y$ and an
affine open $V'=\operatorname{Spec}(B)\subseteq q^{-1}(V)$. The ring map
$A\to B$ is flat. Apply
[lemma-nagata-affine-image-kernel-flat] to
$T\times_YV\to\operatorname{Spec}(A)$. It identifies the ideal of the
image after base change to $V'$ with the extension to $B$ of the original
image ideal. The latter is exactly the ideal defining
$\operatorname{SIm}(g)\times_YV'$ under the closed-subscheme pullback
isomorphism. Naturality and localization compatibility in
[lemma-nagata-affine-image-kernel-flat] show that these affine
identifications agree on all overlaps. Gluing gives the displayed
canonical isomorphism of closed subschemes of $Y'$. This is the
finite-affine-cover proof of Stacks Project, Tag 081I
(Lemma 29.26.16), with $f=q$ and $g$ the morphism in the present statement.
