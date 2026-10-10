+++
id = "sk-lem-nagata-sketch-image-transform"
kind = "section"
title = "Images under admissible blow-up"
order = 230
uses = ["sk-lem-nagata-sketch-blowups", "sk-lem-nagata-sketch-closure"]
lean = ["AlgebraicGeometry.Scheme.Hom.ker_lift_admissibleBlowup"]
+++
*Lemma (sketch).*

Let $h:T\to X\times_SY$ be quasi-compact with
first projection factoring through an open $U\subseteq X$.
Under a $U$-admissible blow-up $X'\to X$, the scheme-theoretic image of a
lift $T\to X'\times_SY$ of $h$ is the strict transform of $\SIm(h)$, provided
the inclusion of the open part of $\SIm(h)\times_{X\times_SY}(X'\times_SY)$
over the complement of the centre is quasi-compact.

## Proof

Away from the centre the base-changed blow-up is an isomorphism, so the
open part of $\SIm(h)\times_{X\times_SY}(X'\times_SY)$ over the complement
of the centre is the corresponding open of $\SIm(h)$, and $T$ is
scheme-theoretically dense in it (flat base change of the dense map
$T\to\SIm(h)$). Hence the lift of $h$ and the inclusion of this open part
have the same kernel in $X'\times_SY$; the strict transform is the
scheme-theoretic closure of the open part, so both are the same closed
subscheme. See 0F3Y.
