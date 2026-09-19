+++
id = "lemma-weil-pbc-direct-image-derived-completion"
kind = "lemma"
title = "Direct image commutes with derived completion"
order = 862
uses = ["lemma-weil-pbc-completed-projection-formula-composite", "lemma-weil-pbc-derived-complete-reconstruction"]
+++
There is a functorial isomorphism

$$
\widehat{Rf_*E}\xrightarrow{\sim}Rf_*\widehat E.
$$

If $E$ is intrinsically derived $I$-complete, then $Rf_*E$ is intrinsically
derived $I$-complete. Both statements commute with compatible endomorphisms
and base change.

## Proof

Apply the completed projection-formula composite with $B=\Lambda$; its
finite reductions are $P_n$, which are perfect by the coefficient datum.
This gives the displayed map and its explicit inverse. If $E$ is complete,
reconstruction identifies $\widehat E$ with $E$. Naturality of the composite
identifies the resulting inverse $Rf_*E\to\widehat{Rf_*E}$ with the
completion unit, so that unit is an isomorphism. The naturality assertion is
inherited from the completed composite.
