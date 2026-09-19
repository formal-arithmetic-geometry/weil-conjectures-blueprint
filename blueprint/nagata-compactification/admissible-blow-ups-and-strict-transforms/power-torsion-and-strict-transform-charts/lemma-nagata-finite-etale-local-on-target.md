+++
id = "lemma-nagata-finite-etale-local-on-target"
kind = "lemma"
title = "Finiteness descends from an etale neighbourhood, [stacks-project]"
order = 371
uses = ["lemma-nagata-affine-fpqc-descent-package"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Finiteness of a morphism of schemes is local on the target for the etale
topology. In particular, if a morphism becomes finite after a surjective
etale base change over a neighbourhood of a point, it is finite after
shrinking that neighbourhood.

## Proof

After shrinking, take a quasi-compact surjective etale neighbourhood; it is
faithfully flat and quasi-compact. By
[lemma-nagata-affine-fpqc-descent-package], the original morphism is
affine. On an affine target write it as $\operatorname{Spec}(B)$ over
$A$. The base-change algebra is finite over $A'$, and faithful-flat descent
of finite generators gives that $B$ is finite over $A$. Hence the morphism
is finite on the chosen neighbourhood.
