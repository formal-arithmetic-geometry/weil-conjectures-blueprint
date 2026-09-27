+++
id = "sk-prop-sf-pf-coherence"
kind = "section"
title = "Coherence of the projection formula"
order = 2101
uses = ["sk-lem-sf-mate", "sk-prop-sf-pf-reduction", "sk-thm-sf-pf-field", "sk-thm-sf-pf-finite", "sk-thm-sf-pf-proetale"]
lean = ["AlgebraicGeometry.Etale.hasProjectionFormula_coherence"]
+++
*Proposition (sketch).*

The projection transformations are natural in $K$, $L$, $f$ and the
coefficient ring; the transformation for $f=\mathrm{id}$ is the identity; the
associativity pentagon for composable $f,g$ commutes and is compatible with
the composition law of def:compact-support-direct-image; the
transformation is independent of the chosen compactification; for proper $f$
it agrees with the direct-image projection formula through $Rf_!\cong Rf_*$;
and it is compatible with finite reduction, scalar extension and the
pro-étale realization. Every one of these assertions is an identity between
natural transformations of the functors typed in [sk-def-sf-operations] and
[sk-def-sf-exchanges], at the categories written there.

## Proof

Naturality is that of the mate construction, which uses only the natural units
and counits. For $f=\mathrm{id}$ the two adjunctions are the identity
adjunction and the mate of the identity is the identity. In the pentagon both
sides are mates of the same composite of the two component mate constructions,
because the units and counits of composite adjunctions are the pasted ones and
pasting of mates is associative; the associativity of the derived tensor
product identifies the two tensor reassociations. Independence of the
compactification is the compatibility of the refinement comparisons with the
counits and with $j_!$, together with naturality and
prop:compactification-coherence. The last clause is
[sk-prop-sf-pf-reduction], [sk-thm-sf-pf-field] and
[sk-thm-sf-pf-proetale].

Uses: `\Cref{lem:sf-mate}`, `\Cref{prop:sf-pf-reduction}`, `\Cref{thm:sf-pf-field}`, `\Cref{thm:sf-pf-finite}`, `\Cref{thm:sf-pf-proetale}`
