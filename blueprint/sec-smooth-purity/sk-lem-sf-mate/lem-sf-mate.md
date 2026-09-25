+++
id = "lem-sf-mate"
kind = "lemma"
title = "Mate calculus for a pasted adjunction"
order = 1914
uses = ["def-sf-datum", "fix-prop-adjunctions"]
+++
In the setting of [def-sf-datum], let
$X\xrightarrow{f}Y\xrightarrow{g}Z$ be composable separated finite-type
morphisms. Then the mate of the composition isomorphism
$R(gf)_!\cong Rg_!Rf_!$ is the isomorphism $(gf)^!\cong f^!g^!$, and the
units and counits of the composite adjunctions are the pasted ones.
([fix-prop-adjunctions], item (3).)

## Proof

The pasting of the units and counits is recorded in
[fix-prop-adjunctions]: the functoriality of the mate construction
gives the isomorphism of right adjoints from the isomorphism of left
adjoints $R(gf)_!\cong Rg_!Rf_!$, and the triangle identities of the
composite are the composites of the component ones.
