+++
id = "sk-lem-nagata-sketch-closure"
kind = "section"
title = "Scheme-theoretic closure and compactification"
order = 63
uses = ["sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.Scheme.Hom.image", "AlgebraicGeometry.Compactification.ofIsImmersion", "AlgebraicGeometry.Compactification.denseRefinement", "AlgebraicGeometry.Compactification.baseChange"]
+++
*Lemma (sketch).*

For a morphism $h:T\to Y$, its
scheme-theoretic image $\SIm(h)$ is the smallest closed subscheme of $Y$
through which $h$ factors. For quasi-compact $h$ it commutes with
restriction to an open of $Y$.
Consequently, a quasi-compact immersion into a proper $S$-scheme gives a
compactification by taking its scheme-theoretic image. In particular,
compactifications of quasi-compact morphisms admit dense refinements, and
closed subschemes of a compactifiable quasi-compact $S$-scheme are
compactifiable. Compactifications are
preserved by base change.

## Proof

The ideal is the largest quasi-coherent ideal inside
$\ker(\mathcal O_Y\to h_*\mathcal O_T)$, and minimality is immediate. For
quasi-compact $h$ the ideal is this kernel itself, computed on affine opens
from a finite affine cover of the source; flat base change, in particular
restriction to an open, then commutes with it. An immersion is closed in
some open of its target, so its image factor identifies $T$ with an open
of $\SIm(h)$. This image is closed in the proper ambient scheme, hence
proper over $S$. For a compactification of a quasi-compact morphism, the
open immersion $X\to\overline X$ is quasi-compact because
$\overline X\to S$ is separated. Apply this first to $X\to\overline X$, and then to
$Z\hookrightarrow X\hookrightarrow\overline X$. Properness and
quasi-compact open immersions are stable under base change.
