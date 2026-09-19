+++
id = "lemma-nagata-flat-dense-open-relative-dimension"
kind = "lemma"
title = "Relative dimension extends from a retrocompact dense open, [stacks-project]"
order = 367
uses = ["lemma-nagata-dense-open-dimension-package"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $q\colon Z\to X$ be flat and locally of finite type, and let
$U\subseteq X$ be a retrocompact dense open. If $q^{-1}(U)\to U$ has
relative dimension at most $e$, then every fibre of $q$ has dimension at
most $e$.

## Proof

Apply [lemma-nagata-dense-open-dimension-package] on affine charts of
$X$. Its finite-presentation upgrade and generic-point dimension argument
give the asserted bound, and the conclusions glue since they are local on
source and target.
