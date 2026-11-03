+++
id = "lemma-nagata-scheme-image-restrict-open"
kind = "lemma"
title = "Restriction of a scheme-theoretic image to an open target"
order = 45
lean = ["AlgebraicGeometry.Scheme.Hom.ker_morphismRestrict"]
uses = ["def-nagata-extended-ideal", "def-nagata-scheme-theoretic-image"]
+++
Let $g\colon T\to Y$ be quasi-compact, let
$W\subseteq Y$ be open, let $T_W=T\times_YW$, and let
$g_W\colon T_W\to W$ be the base change of $g$. Then the ideal sheaf
$\ker(g_W)$ of $\operatorname{SIm}(g_W)$ is the restriction to $W$ of the
ideal sheaf $\ker(g)$ of $\operatorname{SIm}(g)$; equivalently,

$$
\operatorname{SIm}(g_W)
\cong\operatorname{SIm}(g)\times_YW
$$

as closed subschemes of $W$, compatibly with their inclusions into $W$.
