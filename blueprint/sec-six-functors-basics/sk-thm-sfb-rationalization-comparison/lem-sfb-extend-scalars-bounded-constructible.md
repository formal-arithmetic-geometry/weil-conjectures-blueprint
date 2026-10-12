+++
id = "lem-sfb-extend-scalars-bounded-constructible"
kind = "lemma"
title = "Derived extension of scalars preserves bounded constructible complexes"
order = 1593
uses = ["def-sfb-integers-to-subfield", "sk-def-sfb-derived-extension-of-scalars", "sk-def-sfb-bounded-constructible"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalars_obj"]
+++
Let $X$ be a scheme and $\varphi\colon\cO_{E,X}\to E_X$ as in
[def-sfb-integers-to-subfield]. If $K\in D(\Mod_{\cO_{E,X}})$ is bounded constructible
[sk-def-sfb-bounded-constructible], then so is
$E\otimes^{\mathrm L}_{\cO_E}K=L(\operatorname{Ext}_\varphi)(K)\in D(\Mod_{E_X})$
[sk-def-sfb-derived-extension-of-scalars].
