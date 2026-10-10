+++
id = "lemma-nagata-scheme-image-restrict-open"
kind = "lemma"
title = "Restriction of a scheme-theoretic image to an open target"
order = 85
lean = ["AlgebraicGeometry.Scheme.Hom.ker_morphismRestrict"]
uses = ["def-nagata-extended-ideal", "def-nagata-scheme-theoretic-image", "lemma-nagata-dense-flat-pullback"]
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

## Proof

The inclusion $W\hookrightarrow Y$ is an open immersion, hence flat, and
$g_W$ is the base change of the quasi-compact morphism $g$ along it. By
[lemma-nagata-dense-flat-pullback], $\ker(g_W)$ is the ideal sheaf of the
closed subscheme $\operatorname{SIm}(g)\times_YW\hookrightarrow W$. By
[def-nagata-extended-ideal] this is the extended ideal
$\ker(g)\mathcal O_W$, and along an open immersion the extended ideal of a
quasi-coherent ideal is its restriction: on an affine open
$\operatorname{Spec}(A)\subseteq W$ the extension of $\ker(g)(\operatorname{Spec}A)$
along the identity of $A$ is itself. Hence $\ker(g_W)=\ker(g)|_W$. Closed
subschemes of $W$ with the same ideal sheaf coincide, compatibly with their
inclusions into $W$, which gives the displayed isomorphism.
