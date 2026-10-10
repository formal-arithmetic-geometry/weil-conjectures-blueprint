+++
id = "lem-weil-pbc-etale-ring-base-change"
kind = "lemma"
title = "Base change of an etale ring map is etale"
uses = ["def-weil-etale-morphism"]
refines = "proof/lem-weil-pbc-map-into-henselian-colimit"
lean = ["Algebra.Etale.baseChange"]
tags = ["sheaf-dag", "mathlib", "stacks-00U2"]
+++
Let $R\to A$ and $R\to S$ be homomorphisms of commutative rings such that $\operatorname{Spec}A\to\operatorname{Spec}R$ is etale [def-weil-etale-morphism]. Then $\operatorname{Spec}(S\otimes_RA)\to\operatorname{Spec}S$, induced by $s\mapsto s\otimes1$, is etale.
