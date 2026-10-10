+++
id = "lemma-nagata-dense-flat-pullback"
kind = "lemma"
title = "Flat base change of scheme-theoretic images and dense pullbacks"
order = 84
lean = ["AlgebraicGeometry.IsSchemeTheoreticallyDominant.of_isPullback", "AlgebraicGeometry.Scheme.Hom.ker_pullback_snd"]
uses = ["def-nagata-dense-compactification", "def-nagata-extended-ideal", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc"]
+++
Let $h\colon U\to X$ be quasi-compact with
scheme-theoretic image $X$, and let
$q\colon P\to X$ be flat. Then

$$
U\times_XP\longrightarrow P
$$

has scheme-theoretic image $P$.

More generally, let $g\colon T\to Y$ be quasi-compact, let
$q\colon Y'\to Y$ be flat, and let $g'\colon T\times_YY'\to Y'$ be the base
change. Then the ideal sheaf $\ker(g')$ of $\operatorname{SIm}(g')$ equals
the ideal sheaf of the closed subscheme
$\operatorname{SIm}(g)\times_YY'\hookrightarrow Y'$; that is,
$\operatorname{SIm}(g')\cong\operatorname{SIm}(g)\times_YY'$ as closed
subschemes of $Y'$.
