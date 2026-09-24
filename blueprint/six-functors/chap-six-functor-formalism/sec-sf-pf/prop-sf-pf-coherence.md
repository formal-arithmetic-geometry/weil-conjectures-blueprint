+++
id = "prop-sf-pf-coherence"
kind = "theorem"
title = "Coherence of the projection formula"
order = 3396
tags = ["latex:proposition"]
uses = ["def-sf-datum", "def-sf-pf", "fix-prop-adjunctions", "prop-sf-pf-reduction", "thm-sf-pf-field", "thm-sf-pf-proetale"]
+++
In the setting of [def-sf-datum], the projection transformations
satisfy: naturality in $K$, $L$, $f$ and the coefficient ring; the identity
for $f=\operatorname{id}$; the associativity pentagon for composable
$f,g$, compatible with the composition law (A4); independence of the chosen
compactification; the identification with the direct-image projection
formula through $Rf_!\cong Rf_*$ for proper $f$; and compatibility with
finite reduction, scalar extension and the pro-étale realization.

## Proof

All projection transformations appearing below are those of
[def-sf-pf].
Naturality is the naturality of the mate construction, which uses only the
natural units and counits of the axioms; for $f=\operatorname{id}$ the two
adjunctions are the identity adjunction and the mate of the identity is the
identity. The pentagon: both sides are mates of the same composite of the
two component mate constructions, because the units and counits of composite
adjunctions are the pasted ones by [fix-prop-adjunctions], item (3),
and pasting of mates is associative; the associativity of the derived tensor
product identifies the two tensor reassociations. Independence of the
compactification is the compatibility of the refinement comparisons with
the counits and with $j_!$, together with naturality. The proper case is
(A4). The last clause is [prop-sf-pf-reduction],
[thm-sf-pf-field] and [thm-sf-pf-proetale].
