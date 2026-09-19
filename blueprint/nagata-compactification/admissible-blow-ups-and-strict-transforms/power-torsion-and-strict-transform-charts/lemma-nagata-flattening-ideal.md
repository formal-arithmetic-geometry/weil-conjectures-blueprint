+++
id = "lemma-nagata-flattening-ideal"
kind = "lemma"
title = "Properties of the selected flattening ideal"
order = 376
uses = ["def-nagata-flattening-ideal", "lemma-nagata-flattening-ideal-exists"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

The ideal $\mathcal F_U(q)$ is finite type and restricts to the unit ideal
on $U$; the strict-transform projection after blowing it up is an open
immersion and is the original isomorphism over $U$.

## Proof

The witness type is nonempty by
[lemma-nagata-flattening-ideal-exists]. Projecting its specification
fields along the choice made in
[def-nagata-flattening-ideal] gives finite type, unit restriction, the
open strict-transform projection, and the specified identification over $U$.
