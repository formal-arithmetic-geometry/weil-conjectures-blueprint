+++
id = "lem-weil-pbc-etale-composition-cancellation"
kind = "lemma"
title = "Open immersions are etale; etale morphisms compose and cancel"
order = 1077
uses = ["def-pc-scheme", "def-weil-open-immersion", "def-weil-etale-morphism"]
lean = ["AlgebraicGeometry.Etale.of_comp, AlgebraicGeometry.Etale.etale_comp, instance [IsOpenImmersion f] : Etale f"]
tags = ["mathlib", "stacks-02GP"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be morphisms of schemes [def-pc-scheme]. (1) If $f$ is an open immersion [def-weil-open-immersion], then $f$ is etale [def-weil-etale-morphism]. (2) If $f$ and $g$ are etale, then $g\circ f$ is etale. (3) If $g\circ f$ and $g$ are etale, then $f$ is etale; in particular any morphism between two schemes etale over $Z$ which commutes with the structure morphisms is etale.
