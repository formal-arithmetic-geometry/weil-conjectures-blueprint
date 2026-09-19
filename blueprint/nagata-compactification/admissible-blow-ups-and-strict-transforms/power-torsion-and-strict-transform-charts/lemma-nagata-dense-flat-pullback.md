+++
id = "lemma-nagata-dense-flat-pullback"
kind = "lemma"
title = "Scheme-theoretic density survives flat pullback"
order = 359
lean = ["AlgebraicGeometry.IsSchemeTheoreticallyDominant.of_isPullback"]
uses = ["def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-flat-base-change"]
+++
Let $h\colon U\to X$ be quasi-compact and quasi-separated with
scheme-theoretic image $X$, and let
$q\colon P\to X$ be flat. Then

$$
U\times_XP\longrightarrow P
$$

has scheme-theoretic image $P$.

## Proof

By [lemma-nagata-scheme-image-flat-base-change], the scheme-theoretic
image after pullback is canonically the pullback of the scheme-theoretic
image of $h$. By hypothesis that image is $X$, and its pullback along
$P\to X$ is the identity closed subscheme of $P$. Thus the base-changed
morphism is scheme-theoretically dense in $P$.
