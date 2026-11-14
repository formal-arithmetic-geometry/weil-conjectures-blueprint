+++
id = "dag-det-pe-hypercover-single-affine"
kind = "dag-lemma"
title = "Every qcqs object of the pro-etale site admits a simplicial hypercover over it with each term a single spectrum of a w-contractible ring and with covering proper-face matching arrows."
name_showing = false
order = 103506
tags = ["sheaf-dag"]
split_from = "proposition-weakly-contractible-hypercovers--1"
dag_id = "det-pe-hypercover-single-affine"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["exists_single_affine_wContractible_hypercover"]
uses = ["dag-det-pe-wlocal-strict-contractible", "dag-sk-def-pe-wlocal"]
+++
Let X be any scheme and U a quasi-compact quasi-separated object of X_proet. There exists a simplicial object W in the slice over U such that every W_r has underlying site object literally a spectrum Spec D_r for a w-contractible ring D_r; the augmentation W_0 to U is a singleton pro-etale cover; and for each r there is a limiting cone c of the proper-face diagram in degree r+1 with an arrow mu from W_(r+1) to c.pt, whose underlying arrow is a singleton pro-etale cover and whose composite with each cone projection equals the corresponding simplicial proper-face map. Weak contractibility of representable sheaves is derived separately in the parent theorem.

(SHEAF DAG node `det-pe-hypercover-single-affine`; machine-alignment layer.) Split from [proposition-weakly-contractible-hypercovers--1]. DAG kind: statement. Placed through `det-pe-hypercover-existence` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sfb-proper-face-diagram`, `def-weil-affine-spectrum`, `def-weil-pbc-scheme-conventions`, `def-weil-pbc-simplicial-coskeleton`, `def-weil-pbc-simplicial-object`, `lem-weil-pbc-matching-object-proper-faces`, `sk-def-pe-site`.
