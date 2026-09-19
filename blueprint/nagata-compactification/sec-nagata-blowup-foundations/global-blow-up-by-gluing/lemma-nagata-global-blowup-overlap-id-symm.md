+++
id = "lemma-nagata-global-blowup-overlap-id-symm"
kind = "lemma"
title = "Identity and symmetry of overlap isomorphisms"
order = 226
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupNatTrans_equifibered"]
uses = ["lemma-nagata-global-blowup-overlap-independent"]
+++
The overlap isomorphism of a chart with itself is the identity, and the
overlap isomorphism from chart $i$ to chart $j$ is inverse to the one from
$j$ to $i$.

## Proof

On a basic refinement, $\omega_{ii,s}=r_{i,s}r_{i,s}^{-1}=1$ and
$\omega_{ji,s}\omega_{ij,s}=r_{j,s}r_{i,s}^{-1}r_{i,s}r_{j,s}^{-1}=1$.
The equalities descend from the basic cover.
