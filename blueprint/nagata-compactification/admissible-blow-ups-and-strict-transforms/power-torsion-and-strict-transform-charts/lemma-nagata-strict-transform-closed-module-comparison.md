+++
id = "lemma-nagata-strict-transform-closed-module-comparison"
kind = "lemma"
title = "Module and scheme strict transforms agree for a closed immersion"
order = 364
uses = ["lemma-nagata-module-power-torsion-localization", "lemma-nagata-module-strict-transform-chart", "lemma-nagata-strict-transform-closure-characterization", "prop-nagata-strict-transform-closed-fiber-product"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $i\colon Z\hookrightarrow V$ be a finite-presentation closed immersion
and let $V'\to V$ be a blow-up with center ideal $\mathcal I$. On every
affine blow-up chart, the coordinate algebra of the scheme-theoretic strict
transform of $Z$ is the strict-transform quotient of the pulled-back
coordinate module of $Z$. These identifications are compatible with
localization and hence identify the resulting quasi-coherent module with
the structure sheaf of the strict transform.

## Proof

Work on an affine chart $V=\operatorname{Spec}(A)$, write
$Z=\operatorname{Spec}(B)$ with $B=A/J$, and let
$R=A[I/a]$ be a blow-up chart. The ordinary base-change chart has ring
$B\otimes_A R$, while the scheme strict-transform chart has ring
$(B\otimes_A R)/\Gamma_{(a)}(B\otimes_A R)$ by
[prop-nagata-strict-transform-closed-fiber-product] and
[lemma-nagata-strict-transform-closure-characterization]. The
module strict-transform chart for the $A$-module $B$ is the same quotient
by [lemma-nagata-module-strict-transform-chart]; the $B$-algebra
structure is the one induced from the ordinary base-change chart. On a
basic overlap, both descriptions localize to the corresponding quotient,
and the quotient-localization cocycle is
[lemma-nagata-module-power-torsion-localization]. Thus the affine
identifications glue and identify the module's associated sheaf with the
structure sheaf of the scheme strict transform.
