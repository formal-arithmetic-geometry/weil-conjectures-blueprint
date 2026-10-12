+++
id = "lem-weil-pbc-etale-stratification-local-gluing-core"
kind = "lemma"
title = "Global constructible immersed refinement factoring through local strata"
uses = ["def-constructible-stratification", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.exists_global_stratification_factoring_local"]
source = "literature/stacks-project/etale-cohomology.tex, Etale Cohomology, Tag 03S0, locality reduction"
+++
Let X be a quasi-compact quasi-separated scheme (def-weil-pbc-scheme-conventions). Given a finite affine open cover W indexed by Fin n and, for each chart W_a, a finite constructible locally closed immersed stratification T_a (def-constructible-stratification), there exists a finite constructible locally closed immersed stratification S of X such that each stratum immersion of S factors by an actual scheme morphism through one local stratum immersion T_a,b -> W_a -> X. No morphism U -> X or finite-etale property is assumed.
