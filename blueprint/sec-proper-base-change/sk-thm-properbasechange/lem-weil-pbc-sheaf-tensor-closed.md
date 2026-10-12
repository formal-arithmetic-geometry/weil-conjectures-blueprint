+++
id = "lem-weil-pbc-sheaf-tensor-closed"
kind = "lemma"
title = "A-valued sheaves on an essentially small site: Grothendieck abelian, symmetric monoidal closed under the sheafified tensor product"
lean = ["branch", "declarations", "note"]
tags = ["sheaf-dag", "stacks-0GMW"]
+++
Let $\mathcal C$ be an essentially small category with a Grothendieck topology $J$, and let $\mathcal A$ be a Grothendieck abelian category with a symmetric monoidal closed structure $(\otimes,\mathbf 1)$ whose tensor product is additive in each variable. Let $a:\mathrm{PSh}(\mathcal C;\mathcal A)\to\mathrm{Sh}(\mathcal C,J;\mathcal A)$ be sheafification, left adjoint to the inclusion $\iota$, and equip presheaves with the objectwise tensor product $(F\otimes_pG)(V)=F(V)\otimes G(V)$. Then: (1) $\mathrm{Sh}(\mathcal C,J;\mathcal A)$ is a Grothendieck abelian category, and $a$ is exact; (2) the morphisms inverted by $a$ are stable under $\otimes_p$ with any presheaf, so $F\otimes G:=a(\iota F\otimes_p\iota G)$ with unit $a(\mathbf 1)$ is a symmetric monoidal structure on $\mathrm{Sh}(\mathcal C,J;\mathcal A)$, additive in each variable, for which $a$ is strong symmetric monoidal: $a(P\otimes_pQ)\cong aP\otimes aQ$ naturally in presheaves $P,Q$; (3) this monoidal structure is closed, so for every sheaf $Q$ the functors $Q\otimes-$ and $-\otimes Q$ are left adjoints and preserve all colimits.
