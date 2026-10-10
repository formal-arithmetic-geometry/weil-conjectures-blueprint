+++
id = "lemma-nagata-proj-chart-ring-cocycle"
kind = "lemma"
title = "Coherence of the standard Proj chart rings"
order = 9
uses = ["def-nagata-homogeneous-localization-degree-zero"]
+++
For positive-degree homogeneous $f,g,h$, localization induces canonical
equivalences between the restrictions of $(R_{(f)})_0$ and
$(R_{(g)})_0$ to the overlap indexed by $fg$. These equivalences are the
identity for $f=g$, are inverse under exchange of $f$ and $g$, and satisfy
the cocycle equality on the triple localization indexed by $fgh$.

## Proof

Use the canonical maps between the homogeneous localizations at $f$, $g$,
and $fg$. On a representative $x/f^m$ each map sends the fraction to its
image in the localization at $fg$; the localization relation proves
independence of representatives. The identity, inverse, and triple
cocycle equations follow because both sides are the same map into the
localization at $fgh$. These are the compatibilities used by the verified
declarations `Proj.basicOpenIsoSpec` and
`Proj.affineOpenCover`.
