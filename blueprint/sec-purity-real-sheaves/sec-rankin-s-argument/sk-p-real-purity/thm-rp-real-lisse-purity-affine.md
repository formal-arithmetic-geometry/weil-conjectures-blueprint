+++
id = "thm-rp-real-lisse-purity-affine"
kind = "theorem"
title = "Purity of real lisse sheaves on curves"
lean = ["AlgebraicGeometry.WeilSheaf.IsReal.exists_isPunctuallyPureOfWeight_cokernel_detWeight", "AlgebraicGeometry.WeilSheaf.IsReal.exists_isPunctuallyPureOfWeight_cokernel", "AlgebraicGeometry.WeilGroup.isPunctuallyPure_of_isConstituent_of_isReal_of_isAffine"]
order = 4100
uses = ["cor-mg-det-weight-exterior", "d-real-setup", "def-real-weil-representation-operations", "def-rp-weight-blocks", "def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "def-wf-determinantal-weight", "def-wf-iota-real", "lem-mg-exterior-direct-sum", "lem-rp-exterior-reality", "lem-rp-upper-bound", "lem-wf-dense-open-pi1-surjective", "lem-wf-determinantal-weight-exists", "lem-wf-real-semisimplification", "p-linear-spectra", "sk-lem-coefficient-heart"]
+++
Let $C_0/\mathbf F_q$ be a smooth geometrically connected curve in the
sense of [d-real-setup] (not necessarily affine; e.g. proper) and let
$\mathcal G_0$ be a lisse
Weil sheaf on $C_0$ which is
$\iota$-real. Then every irreducible
constituent $\mathcal W$ of $\mathcal G_0$ (in the sense of
[def-real-weil-representation-operations]) is
punctually $\iota$-pure of
weight $\dw_\iota(\mathcal W)$, its
determinant weight with
respect to $\iota$.
