+++
id = "lem-weil-pbc-dplus-injective-representative"
kind = "lemma"
title = "Every object of D^+ is represented by a bounded below K-injective complex of injectives"
uses = ["lem-weil-pbc-module-sheaves-enough-injectives", "def-weil-pbc-bounded-derived-subcategories", "def-weil-abstract-derived-category", "def-weil-pbc-kinjective-resolutions"]
lean = ["DerivedCategory.Plus.exists_injective_nonempty_iso"]
tags = ["sheaf-dag", "mathlib", "stacks-013K"]
+++
Let $\mathcal A$ be an abelian category with enough injectives (for example $\Ab(T_{\Et})$ or $\Mod(T_{\Et},R)$ for a scheme $T$ [lem-weil-pbc-module-sheaves-enough-injectives]), $D^+(\mathcal A)$ its bounded below derived category [def-weil-pbc-bounded-derived-subcategories] and $Q$ the localization functor from cochain complexes [def-weil-abstract-derived-category]. (1) If $K\in D^+(\mathcal A)$ and $n\in\mathbf Z$ are such that $\mathcal H^i(K)=0$ for all $i<n$, there are a complex $L$ of injective objects of $\mathcal A$ with $L^i=0$ for $i<n$ and an isomorphism $QL\cong K$ in $D^+(\mathcal A)$. (2) Every bounded below complex of injective objects of $\mathcal A$ is K-injective [def-weil-pbc-kinjective-resolutions]. In particular every object of $D^+(\mathcal A)$ is isomorphic to $QI$ for a bounded below K-injective complex $I$.
