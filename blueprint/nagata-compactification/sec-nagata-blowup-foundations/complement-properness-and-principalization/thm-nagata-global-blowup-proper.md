+++
id = "thm-nagata-global-blowup-proper"
kind = "theorem"
title = "Properness of the global blow-up"
order = 252
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isProper_blowupMap"]
uses = ["lemma-nagata-global-blowup-proper-local", "lemma-nagata-projective-target-local"]
+++
If $\mathcal I$ is of finite type, then
$b_{X,\mathcal I}$ is proper.

## Proof

Apply [lemma-nagata-global-blowup-proper-local] to the affine open cover
of $X$. Each restricted morphism is proper, and
[lemma-nagata-projective-target-local] is the verified target-local
properness lemma (despite its historical label). It follows that
$b_{X,\mathcal I}$ is proper. This argument does not use the unresolved
global projectivity theorem.
