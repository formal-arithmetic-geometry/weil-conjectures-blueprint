+++
id = "sk-lem-sf-mate"
kind = "section"
title = "Mate calculus for a pasted adjunction"
order = 1909
uses = ["sk-def-sf-operations"]
+++
*Lemma (sketch).*

Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be composable separated finite-type
morphisms. Then the mate of the composition isomorphism
$R(gf)_!\cong Rg_!Rf_!$ is the isomorphism $(gf)^!\cong f^!g^!$, and the
units and counits of the composite adjunctions are the pasted ones.

## Proof

The pasting is recorded in fix-prop-adjunctions; the functoriality of the
mate construction gives an isomorphism of right adjoints from the isomorphism
of left adjoints, and the triangle identities of the composite are the
composites of the component ones.

Uses: `\Cref{def:sf-operations}`, `fix-prop-adjunctions`
