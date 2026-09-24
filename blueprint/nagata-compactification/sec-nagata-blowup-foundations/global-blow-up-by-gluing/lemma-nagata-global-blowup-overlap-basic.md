+++
id = "lemma-nagata-global-blowup-overlap-basic"
kind = "lemma"
title = "The basic-overlap comparison is an isomorphism"
order = 298
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isPullback_blowupNatTrans_of_basicOpen"]
uses = ["def-nagata-global-blowup-overlap-basic-map", "prop-nagata-affine-blowup-restrict"]
+++
The constructed map $\omega_{ij,s}$ is an isomorphism over $D(s)$.

## Proof

Quasi-coherence identifies both restricted ideals with the same localized
ideal. Thus $r_{i,s}$ and $r_{j,s}$ are isomorphisms by
[prop-nagata-affine-blowup-restrict]; their composite with the inverse
of $r_{i,s}$ is an isomorphism, with inverse $r_{i,s}\circ r_{j,s}^{-1}$.
