+++
kind = "proof"
of = "theorem-generic-constructibility-base-change-rj--2"
order = 582002
uses = ["theorem-generic-constructibility-base-change-rj--1", "lemma-identity-pasting"]
+++
The induction in the proof of
[theorem-generic-constructibility-base-change-rj--1] proves the two
assertions simultaneously. In Lean they are the two conjuncts of
`AlgebraicGeometry.Etale.HasConstructibleDirectImageBaseChangeOn`, for
each cartesian base change with noetherian $T$ and image in $S_0$.
Taking the second conjunct gives the first displayed isomorphism.

For the formulation over $S_0$, factor $T\to S$ through $S_0$ and paste
the two base change squares [lemma-identity-pasting]. Base change along
the open immersion $Y_{S_0}\hookrightarrow Y$ is an isomorphism, since
derived direct image commutes with restriction to an open of the target.
The pasting identity therefore identifies the first map with the map
over $S_0$, composed with an isomorphism. This proves the equivalent
formulation.
