+++
id = "dag-lem-pe-affine-etale-large-limit-maps"
kind = "dag-lemma"
title = "Affine etale representables on larger affine limits"
name_showing = false
order = 115504
tags = ["sheaf-dag"]
split_from = "theorem-classical-sheaves-essential-image--1"
dag_id = "lem-pe-affine-etale-large-limit-maps"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.affineEtale_largeLimit_preservesColimit"]
+++
Let $X$ be a scheme in universe $u$. Let $I$ be a small cofiltered category whose objects and morphisms are in universe $u+1$, let $D:I\to X_{\mathrm{Proet}}$ have affine etale stages, and let $c$ be a cone whose image in schemes over $X$ is limiting. For an affine etale $X$-scheme $V$, the opposite Hom functor $\operatorname{Hom}_{X_{\mathrm{Proet}}^{\mathrm{op}}}(V^{\mathrm{op}},-)$ preserves the colimit of $D^{\mathrm{op}}$. Equivalently maps from the vertex to $V$ factor through stages, and equality of two stage maps is detected after refinement. The affine etale stages and the proetale site are as in [dag-det-pe-classical-definition-continuity-map].

(SHEAF DAG node `lem-pe-affine-etale-large-limit-maps`; machine-alignment layer.) Split from [theorem-classical-sheaves-essential-image--1]. DAG kind: lemma. Placed through `det-pe-classical-sheaves-image` (ancestor-1). DAG status: split.
