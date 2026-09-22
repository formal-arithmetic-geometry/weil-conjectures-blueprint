+++
id = "lem-kun-projective-implies-proper"
kind = "lemma"
title = "Projective morphisms are proper"
order = 6070
lean = ["AlgebraicGeometry.IsProjectiveHom.isProper"]
uses = ["def-kun-projective"]
+++
Every projective morphism [def-kun-projective] is proper (the structural
morphism $\mathbf P^N_Y\to Y$ is proper, and closed immersions are proper;
the class of proper morphisms is closed under composition).

## Proof

By [def-kun-projective] the morphism $f$ is the composite of a closed
immersion $i:X\hookrightarrow\mathbf P^N_Y$ with the structural projection
$q:\mathbf P^N_Y\to Y$. Closed immersions are proper, and
$q:\mathbf P^N_Y\to Y$ is proper as the base change of
$\mathbf P^N_{\mathbf Z}\to\Spec\mathbf Z$, which is proper (Stacks Project,
[Tag 01WC](https://stacks.math.columbia.edu/tag/01WC)). Hence $f=q\circ i$
is proper.

Unresolved dependencies: def:weil-pbc-scheme-conventions, lem:weil-pbc-chow-closed-model-proper, lem:weil-pbc-closed-immersion-proper, lem:weil-pbc-proper-composition
