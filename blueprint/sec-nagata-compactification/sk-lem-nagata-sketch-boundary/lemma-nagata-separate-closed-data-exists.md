+++
id = "lemma-nagata-separate-closed-data-exists"
kind = "lemma"
title = "Preparation data for separating two closed boundaries, [stacks-project]"
lean = ["AlgebraicGeometry.disjoint_range_inclusion_inter_preimage_and_subset", "AlgebraicGeometry.exists_separationPreparation", "AlgebraicGeometry.Scheme.IdealSheafData.separationPreparationCenter", "AlgebraicGeometry.Scheme.IdealSheafData.separationPreparationCenter_spec", "AlgebraicGeometry.Scheme.IdealSheafData.separationPreparationBlowupSubscheme"]
order = 253
uses = ["def-nagata-admissible-blowup", "def-nagata-qc-open-complement-ideal", "def-nagata-strict-transform", "lemma-nagata-chart-generator-regular", "lemma-nagata-finite-type-nil-ideal-nilpotent"]
+++
Let $X$ be qcqs, let $U\subseteq X$ be quasi-compact open, and let
$Z_i=V(\mathcal I_i)\hookrightarrow X$ be finite-presentation closed
immersions with $Z_1\cap Z_2\cap U=\varnothing$. Put
$Z=V(\mathcal I_1\mathcal I_2)$, $U_Z=Z\times_XU$, and
$P_i=Z_i\times_XU$. The two closed subschemes $P_i$ are the disjoint
open-and-closed components of $U_Z=P_1\amalg P_2$. There is a finite
presentation closed center $C\hookrightarrow Z$, disjoint from $U_Z$, such
that the blow-up $Z' = \operatorname{Bl}_C(Z)\to Z$ is $U_Z$-admissible
and the strict transforms of $Z_1$ and $Z_2$ in $Z'$ are disjoint.
