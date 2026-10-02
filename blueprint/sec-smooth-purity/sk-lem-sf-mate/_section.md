+++
id = "sk-lem-sf-mate"
kind = "section"
title = "Mate calculus for a pasted adjunction"
order = 1869
uses = ["sk-def-sf-operations", "sk-thm-sf-comp-composition"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp"]
+++
*Lemma (sketch).*

Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be composable separated finite-type
morphisms. Then the mate of the composition isomorphism
$R(gf)_!\cong Rg_!Rf_!$ of [sk-thm-sf-comp-composition] is the isomorphism $(gf)^!\cong f^!g^!$, and the
units and counits of the composite adjunctions are the pasted ones.

## Proof

The pasting is recorded in fix-prop-adjunctions; the functoriality of the
mate construction gives an isomorphism of right adjoints from the isomorphism
of left adjoints, and the triangle identities of the composite are the
composites of the component ones.

Uses: `\Cref{sk-def-sf-operations}`, `\Cref{thm-sf-comp-composition}`, `fix-prop-adjunctions`
