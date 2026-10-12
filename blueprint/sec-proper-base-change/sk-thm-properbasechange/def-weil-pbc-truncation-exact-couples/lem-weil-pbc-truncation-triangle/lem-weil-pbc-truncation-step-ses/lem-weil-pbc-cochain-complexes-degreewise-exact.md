+++
id = "lem-weil-pbc-cochain-complexes-degreewise-exact"
kind = "lemma"
title = "Complexes of an abelian category form an abelian category; short exactness is degreewise; the second map of a short exact sequence is a cokernel of the first"
uses = ["def-sp-abelian", "def-weil-abstract-derived-category"]
refines = "proof/lem-weil-pbc-truncation-step-ses"
lean = ["HomologicalComplex.shortExact_iff_degreewise_shortExact"]
tags = ["sheaf-dag", "mathlib", "stacks-0114"]
+++
Let $\mathcal A$ be an abelian category [def-sp-abelian] and let $\mathrm{CoCh}(\mathcal A)$ be the category of cochain complexes of $\mathcal A$ indexed by $\mathbf Z$ [def-weil-abstract-derived-category]. Then: (1) $\mathrm{CoCh}(\mathcal A)$ is an abelian category; (2) a sequence $0\to A\xrightarrow{f}B\xrightarrow{g}C\to0$ of morphisms of complexes with $g\circ f=0$ is short exact in $\mathrm{CoCh}(\mathcal A)$ ($f$ a monomorphism, $g$ an epimorphism, exact at $B$) if and only if for every $r\in\mathbf Z$ the sequence $0\to A^r\xrightarrow{f^r}B^r\xrightarrow{g^r}C^r\to0$ is short exact in $\mathcal A$; (3) in a short exact sequence $0\to A\xrightarrow{f}B\xrightarrow{g}C\to0$ of an abelian category (in particular of $\mathrm{CoCh}(\mathcal A)$), $g$ is an epimorphism and a cokernel of $f$.
