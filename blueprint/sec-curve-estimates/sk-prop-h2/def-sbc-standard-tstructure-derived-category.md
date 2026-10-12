+++
id = "def-sbc-standard-tstructure-derived-category"
kind = "definition"
title = "The standard t-structure on the derived category of an abelian category"
order = 938
uses = ["def-weil-abstract-derived-category", "def-weil-t-structure"]
lean = ["DerivedCategory.TStructure.t"]
tags = ["mathlib", "stacks-08J5"]
+++
Let $\mathcal A$ be an abelian category and $D(\mathcal A)$ its derived category, with cohomology functors $H^i:D(\mathcal A)\to\mathcal A$ [def-weil-abstract-derived-category]. For $n\in\mathbf Z$ let $D(\mathcal A)^{\le n}$ (resp. $D(\mathcal A)^{\ge n}$) be the strictly full subcategory of objects $K$ with $H^i(K)=0$ for all $i>n$ (resp. for all $i<n$); equivalently, of objects isomorphic in $D(\mathcal A)$ to (the image of) a complex $K^\bullet$ with $K^i=0$ for $i>n$ (resp. $i<n$). The pair $(D(\mathcal A)^{\le0},D(\mathcal A)^{\ge0})$ is a t-structure on the triangulated category $D(\mathcal A)$ [def-weil-t-structure], the *standard* (or *natural*) t-structure, with $D(\mathcal A)^{\le n}=D(\mathcal A)^{\le0}[-n ]$ and $D(\mathcal A)^{\ge n}=D(\mathcal A)^{\ge0}[-n ]$. For a complex $K$ the truncation triangle of axiom (iii) is the image of the short exact sequence $0\to\tau_{\le0}K\to K\to K/\tau_{\le0}K\to0$, where $\tau_{\le0}K$ is the subcomplex $\cdots\to K^{-1}\to\ker(d^0)\to0\to\cdots$ of $K$, and $K/\tau_{\le0}K$ lies in $D(\mathcal A)^{\ge1}$.
