+++
id = "thm-nagata-global-blowup-projective"
kind = "theorem"
title = "Projectivity of the global blow-up"
order = 252
uses = ["def-nagata-global-finite-free-generation", "def-nagata-projective-morphism", "lemma-nagata-global-blowup-relative-projective-embedding"]
+++
**Status.** Bypassed by the formalized route: only properness of the global
blow-up is needed, and it is proved directly as
`AlgebraicGeometry.Scheme.IdealSheafData.isProper_blowupMap`; the
global blow-up is never exhibited as a projective morphism.

If $\mathcal I$ is of finite type, then
$b_{X,\mathcal I}\colon\operatorname{Bl}_{\mathcal I}(X)\to X$ is
projective provided that $\mathcal I$ admits a finite global free
presentation, i.e. there are $r\in\mathbb N$ and a surjection
$q\colon\mathcal O_X^{r+1}\twoheadrightarrow\mathcal I$.

## Proof

The preceding lemma supplies a closed immersion into the single finite
projective space $\mathbf P^r_X$ required by
[def-nagata-projective-morphism]; its structural composite is
$b_{X,\mathcal I}$, so the morphism is projective. Without the displayed
global-generation hypothesis, finite type alone yields the properness
statement below but does not imply projectivity for this finite-projective-
space definition.
