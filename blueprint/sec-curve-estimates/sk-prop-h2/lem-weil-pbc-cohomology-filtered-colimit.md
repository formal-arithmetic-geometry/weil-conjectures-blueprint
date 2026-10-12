+++
id = "lem-weil-pbc-cohomology-filtered-colimit"
kind = "lemma"
title = "Filtered colimits of etale cohomology"
order = 961
uses = ["def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-finite-split-hypercover", "def-weil-pbc-scheme-conventions", "thm-weil-pbc-hypercover-cohomology"]
+++
Let $Y$ be quasi-compact and quasi-separated
[def-weil-pbc-scheme-conventions], and let $(F_a)$ be a filtered system of
abelian etale sheaves [def-weil-pbc-etale-sheaves]. Then

$$
 \varinjlim_a H^q(Y_{\Et},F_a)\xrightarrow{\sim}
 H^q(Y_{\Et},\varinjlim_a F_a)\qquad(q\geq0).
$$

Here cohomology is the derived functor of
[def-weil-pbc-etale-cohomology]; no torsion assumption is needed. The
assertion also holds in sheaves of modules over a fixed constant ring.
