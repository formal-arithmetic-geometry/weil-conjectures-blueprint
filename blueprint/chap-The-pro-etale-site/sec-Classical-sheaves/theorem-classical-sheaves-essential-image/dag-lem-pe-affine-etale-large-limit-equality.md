+++
id = "dag-lem-pe-affine-etale-large-limit-equality"
kind = "dag-lemma"
title = "Eventual equality of maps from larger affine etale limits"
name_showing = false
order = 115502
tags = ["sheaf-dag"]
split_from = "theorem-classical-sheaves-essential-image--1"
dag_id = "lem-pe-affine-etale-large-limit-equality"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.affineEtale_largeLimit_eventualEquality"]
+++
Let X be a scheme in universe u, I a small cofiltered category in universe u+1, D : I → X.ProEt a diagram with affine étale stages, and c a cone whose image under the forgetful functor to schemes over X is limiting. Let V be an affine étale object of X.ProEt. These objects and the forgetful functor are as in [dag-det-pe-classical-definition-continuity-map]. For i in I and a,b : D(i) → V with c.π_i ≫ a = c.π_i ≫ b, there are k in I and f : k → i such that D(f) ≫ a = D(f) ≫ b.

(SHEAF DAG node `lem-pe-affine-etale-large-limit-equality`; machine-alignment layer.) Split from [theorem-classical-sheaves-essential-image--1]. DAG kind: lemma. Placed through `det-pe-classical-sheaves-image` (ancestor-1). DAG status: split.
