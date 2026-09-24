+++
id = "lemma-nagata-extend-finite-type-ideal"
kind = "lemma"
title = "Finite-type ideal extension, [stacks-project]"
order = 436
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteType_comap_eq"]
uses = ["def-nagata-finite-type-ideal-extension", "lemma-nagata-affine-image-kernel-flat", "lemma-nagata-finite-type-ideal-extension-exists", "lemma-nagata-scheme-image-flat-base-change"]
+++
The sheaf $\operatorname{Ext}_{X,W}(\mathcal J)$ is a finite type
quasi-coherent ideal on $X$, and its restriction to $W$ is
$\mathcal J$.

## Proof

The selected ideal is required to have these two properties in
[def-nagata-finite-type-ideal-extension]; the witness type is nonempty
by [lemma-nagata-finite-type-ideal-extension-exists].
