+++
id = "lem-weil-pbc-horseshoe-degreewise-map"
kind = "lemma"
title = "Degreewise middle maps between split horseshoe rows"
uses = ["def-sp-abelian", "def-sp-injective-resolutions"]
lean = ["CategoryTheory.InjectiveResolution.horseshoe_degreewise_map"]
+++
Let C be an abelian category [def-sp-abelian]. Let X, Y, Z and X', Y', Z' be
nonnegative cochain complexes. Let alpha: X to Y, beta: Y to Z, alpha': X' to Y',
and beta': Y' to Z' be chain maps, with both composites zero and both rows short
exact in every degree. Suppose every term of X and X' is injective
[def-sp-injective-resolutions]. Given chain maps phiA: X to X' and phiC: Z to Z',
there is a family t of degreewise maps Y to Y' such that alpha followed by t equals
phiA followed by alpha', and t followed by beta' equals beta followed by phiC,
in every degree. No differential compatibility is asserted for t.
