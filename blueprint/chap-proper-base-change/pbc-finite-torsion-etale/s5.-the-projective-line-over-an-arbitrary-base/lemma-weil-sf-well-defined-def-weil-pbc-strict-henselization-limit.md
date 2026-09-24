+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-strict-henselization-limit"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-strict-henselization-limit"
order = 1666
uses = ["def-weil-pbc-strict-henselization-limit", "lemma-weil-pbc-affine-neighbourhood-cofinal"]
+++
The coordinate-ring rule of Definition
[def-weil-pbc-strict-henselization-limit] is a functor
$D_{\bar s}:\mathcal I_{\bar s}\to\mathbf{CRing}$. Applying
$\operatorname{Spec}$ to its colimit cocone gives the displayed limit cone,
and affine cofinality gives the same strict-local object when nonaffine
pointed neighbourhoods are admitted.

## Proof

Coordinate rings carry an identity pointed map to an identity ring map and
reverse composition. Passage to
$(\mathcal N^{\mathrm{aff}}_{\bar s})^{\mathrm{op}}$ therefore makes
$D_{\bar s}$ covariant. The fixed universe of the coefficient convention
makes this a small diagram, so its colimit exists in $\mathbf{CRing}$.

The anti-equivalence between affine schemes and commutative rings sends this
colimit, together with its structure maps, to the inverse-limit cone on the
affine pointed neighbourhoods. The initiality statement in
Lemma [lemma-weil-pbc-affine-neighbourhood-cofinal] makes restriction to
the affine subcategory limit-cofinal and opposite-colimit-cofinal. Hence the
same ring and affine scheme compute the indicated strict-local object.
