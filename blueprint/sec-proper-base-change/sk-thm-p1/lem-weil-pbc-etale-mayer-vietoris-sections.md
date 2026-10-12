+++
id = "lem-weil-pbc-etale-mayer-vietoris-sections"
kind = "lemma"
title = "Sections of a two-open etale cover form an equalizer"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Etale.etale_mayerVietoris_sections"]
source = "literature/stacks-project/etale-cohomology.tex, Tag 0A50, proof: first and middle spots, via the sheaf condition"
+++
Let X be a scheme [def-pc-scheme], U,V opens with U ∨ V = top, and F an abelian sheaf on X.smallEtaleTopology [def-weil-pbc-etale-site], `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)). Put a(s)=(s|U,s|V), and b(s,t)=s|U∩V-t|U∩V, using the open-immersion restrictions. Then a is injective and Function.Exact a b. No injectivity assumption on F is needed.
