+++
id = "lem-sp-derived-cohomology-shift"
kind = "lemma"
title = "Cohomology of a shifted object of the derived category"
uses = ["def-weil-abstract-derived-category", "def-weil-pbc-bounded-derived-subcategories"]
refines = "proof/lem-sp-shift-identification"
lean = ["CategoryTheory.Functor.shiftIso"]
tags = ["sheaf-dag", "mathlib", "stacks-011G"]
+++
Let $\mathcal B$ be an abelian category with derived category $D(\mathcal B)$ and cohomology functors $H^n:D(\mathcal B)\to\mathcal B$ [def-weil-abstract-derived-category], and let $D^+(\mathcal B)\subset D(\mathcal B)$ be the bounded below derived category [def-weil-pbc-bounded-derived-subcategories]. For $k,a,a'\in\mathbf Z$ with $k+a=a'$ there is a canonical isomorphism

$$
 \tau^{k,a}_M:\ H^{a}(M[k ])\xrightarrow{\ \sim\ }H^{a'}(M),
$$

natural in $M\in D(\mathcal B)$ (and so in $M\in D^+(\mathcal B)$); on a complex $M$ it is the identity of $\ker d/\operatorname{im}d$ under the equality of terms $M[k ]^{a}=M^{a+k}$ (the sign $(-1)^k$ of the differential of $M[k ]$ changes neither kernel nor image). These isomorphisms are compatible with $[0 ]=\mathrm{id}$ and with $M[k ][l ]=M[k+l ]$.
