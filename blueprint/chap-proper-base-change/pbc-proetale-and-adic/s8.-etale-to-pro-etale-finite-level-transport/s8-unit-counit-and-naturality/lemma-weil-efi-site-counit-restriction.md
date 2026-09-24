+++
id = "lemma-weil-efi-site-counit-restriction"
kind = "lemma"
title = "Restriction equation for the comparison counit"
order = 1896
uses = ["def-weil-pbc-epsilon-unit-counit", "lemma-weil-pbc-epsilon-counit-representative-descent-v1"]
+++
For a pro-etale arrow $b:W'\to W$, restriction carries the counit value of
$(W\xrightarrow a\iota_XU,s)$ to the counit value of
$(W'\xrightarrow{ab}\iota_XU,s)$.

## Proof

The first route gives $G(b)G(a)(s)$ and the second gives $G(ab)(s)$; these
are equal by functoriality of $G$ and descend through sheafification.
