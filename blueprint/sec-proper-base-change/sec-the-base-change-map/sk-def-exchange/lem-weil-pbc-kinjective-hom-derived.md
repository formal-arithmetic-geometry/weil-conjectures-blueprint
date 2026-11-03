+++
id = "lem-weil-pbc-kinjective-hom-derived"
kind = "lemma"
title = "Morphisms into a K-injective complex are computed in the homotopy category"
uses = ["def-weil-abstract-derived-category", "def-sp-kinjective-bridge", "def-weil-pbc-bounded-derived-subcategories"]
lean = ["CochainComplex.IsKInjective.Qh_map_bijective"]
order = 1412
tags = ["mathlib", "stacks-070I"]
+++
Let $\mathcal A$ be an abelian category, $K(\mathcal A)$ its homotopy category of cochain complexes and $Q:K(\mathcal A)\to D(\mathcal A)$ the localization at the quasi-isomorphisms [def-weil-abstract-derived-category]. Let $I$ be a K-injective complex (every morphism of complexes from an acyclic complex to $I$ is homotopic to zero; [def-sp-kinjective-bridge] for sheaves). Then for every complex $N$ the map $Q:\operatorname{Hom}_{K(\mathcal A)}(N,I)\to\operatorname{Hom}_{D(\mathcal A)}(QN,QI)$ is bijective. The same holds in the bounded below derived category $D^+(\mathcal A)$ [def-weil-pbc-bounded-derived-subcategories] when $N$ and $I$ are bounded below, $D^+(\mathcal A)$ being a full subcategory of $D(\mathcal A)$. In particular a quasi-isomorphism between K-injective complexes is a homotopy equivalence.
