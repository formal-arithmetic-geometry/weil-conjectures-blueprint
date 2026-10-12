+++
id = "lem-weil-pbc-abelian-etale-sheaves-grothendieck"
kind = "lemma"
title = "Abelian sheaves on the small etale site form a Grothendieck abelian category"
uses = ["def-pc-scheme", "def-weil-pbc-abelian-etale-sheaves", "def-sp-grothendieck-abelian"]
refines = "proof/lem-weil-pbc-module-sheaves-grothendieck-abelian"
lean = ["AlgebraicGeometry.Scheme.isGrothendieckAbelian_sheaf_smallEtaleTopology"]
tags = ["sheaf-dag", "mathlib", "stacks-03CO"]
+++
Let $T$ be a scheme [def-pc-scheme] and $\Ab(T_{\Et})$ the category of sheaves of abelian groups on its small etale site [def-weil-pbc-abelian-etale-sheaves]. Then $\Ab(T_{\Et})$ is a Grothendieck abelian category [def-sp-grothendieck-abelian]: it is abelian, it has all small colimits, filtered colimits in it are exact (for a small filtered category $\mathcal I$ and a diagram of short exact sequences $0\to F_i\to G_i\to H_i\to0$, the sequence $0\to\colim F_i\to\colim G_i\to\colim H_i\to0$ is exact; in particular a filtered colimit of monomorphisms is a monomorphism), and it has a generator.
