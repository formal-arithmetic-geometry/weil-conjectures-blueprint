+++
id = "def-weil-pbc-bounded-derived-subcategories"
kind = "definition"
title = "Bounded below, bounded above and bounded derived categories"
uses = ["def-weil-abstract-derived-category", "def-sbc-standard-tstructure-derived-category"]
refines = "def-weil-pbc-derived-categories"
lean = ["DerivedCategory.Plus"]
tags = ["sheaf-dag", "mathlib", "stacks-05RU"]
+++
Let $\mathcal A$ be an abelian category, $D(\mathcal A)$ its derived category with cohomology functors $H^n:D(\mathcal A)\to\mathcal A$ [def-weil-abstract-derived-category], and $(D(\mathcal A)^{\le n},D(\mathcal A)^{\ge n})$ the standard t-structure [def-sbc-standard-tstructure-derived-category]. The *bounded below*, *bounded above* and *bounded* derived categories are the strictly full subcategories $D^+(\mathcal A)$, $D^-(\mathcal A)$, $D^b(\mathcal A)$ of $D(\mathcal A)$ whose objects are the $X$ such that, respectively, $H^n(X)=0$ for all $n\ll0$; $H^n(X)=0$ for all $n\gg0$; $H^n(X)=0$ for all $|n|\gg0$. Equivalently $D^+(\mathcal A)=\bigcup_{n}D(\mathcal A)^{\ge n}$, $D^-(\mathcal A)=\bigcup_nD(\mathcal A)^{\le n}$ and $D^b(\mathcal A)=D^+(\mathcal A)\cap D^-(\mathcal A)$, i.e. $X\in D^b(\mathcal A)$ iff only finitely many $H^n(X)$ are nonzero. Each is closed under isomorphisms and under the shifts $[k ]$, contains $0$, and with two vertices of a distinguished triangle of $D(\mathcal A)$ contains the third (by the long exact cohomology sequence), so each is a full triangulated subcategory of $D(\mathcal A)$; $D^b(\mathcal A)$ is called the bounded derived category.
