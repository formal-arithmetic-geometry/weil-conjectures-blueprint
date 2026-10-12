+++
id = "lem-weil-pbc-sheaf-flat-separator"
kind = "lemma"
title = "Sheaves on an essentially small site have a flat separator (Lean split)"
uses = ["lem-weil-pbc-sheaf-tensor-closed"]
tags = ["stacks-03EV"]
+++
Let $\mathcal C$ be an essentially small category with a Grothendieck topology $J$, and let $\mathcal A$ be a Grothendieck abelian category with a symmetric monoidal closed structure whose tensor product is additive in each variable. Call an object $P$ of $\mathcal A$ (resp. of the category $\mathrm{Sh}(\mathcal C,J;\mathcal A)$ of $\mathcal A$-valued sheaves, with the monoidal structure obtained by sheafifying the objectwise tensor product) *flat* if tensoring with $P$ preserves finite limits, and a *separator* if for every two distinct parallel morphisms $u\neq v:M\to N$ there is a morphism $h:P\to M$ with $u h\neq v h$. If $\mathcal A$ has an object that is both flat and a separator, then so does $\mathrm{Sh}(\mathcal C,J;\mathcal A)$. (For $\mathcal A$ the category of $\Lambda$-modules and $\mathcal C$ the small étale site of a scheme, such an object is $\bigoplus_U j_{U!}\Lambda_U$, the sum over the objects $U$ of extension by zero of the constant sheaf.)
