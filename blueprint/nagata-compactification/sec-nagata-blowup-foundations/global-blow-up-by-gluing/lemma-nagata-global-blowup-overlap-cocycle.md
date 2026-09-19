+++
id = "lemma-nagata-global-blowup-overlap-cocycle"
kind = "lemma"
title = "Triple-overlap cocycle"
order = 227
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupNatTrans_equifibered"]
uses = ["lemma-nagata-affine-blowup-restrict-cocycle", "lemma-nagata-global-blowup-overlap-independent"]
+++
On every triple overlap, the composite of the $(i,j)$ and $(j,k)$ overlap
isomorphisms equals the $(i,k)$ overlap isomorphism.

## Proof

Cover the triple overlap by basic affine opens. On each such open,
$\omega_{jk,s}\omega_{ij,s}=r_{k,s}r_{j,s}^{-1}r_{j,s}r_{i,s}^{-1} =r_{k,s}r_{i,s}^{-1}=\omega_{ik,s}$; this is precisely the affine
restriction cocycle. Equality on the cover proves the claim.
