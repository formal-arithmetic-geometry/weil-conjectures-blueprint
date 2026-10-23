+++
id = "lem-weil-pbc-ext-one-direct-sum"
kind = "lemma"
title = "Ext one of a direct sum is the product of Ext one"
lean = ["LinearMap.extOne_directSum_bijective"]
order = 1751
+++
Let $A$ be a commutative ring, let $N$ be an $A$-module, and let $(C_j)_{j\in J}$ be a family of $A$-modules. Put $P=\bigoplus_{j\in J}C_j$, with canonical inclusions $\iota_j:C_j\to P$. For an $A$-module $Q$, define $\operatorname{Ext}^{1,\mathrm{ext}}_A(Q,N)$ to be the set of equivalence classes of short exact sequences $0\to N\xrightarrow{u}E\xrightarrow{v}Q\to0$, where two sequences are equivalent when there is an $A$-module isomorphism $h:E\xrightarrow{\sim}E'$ with $h\circ u=u'$ and $v'\circ h=v$. For each $j$, pullback along $\iota_j$ sends the class of $(u,v)$ to the class of $0\to N\to E\mathbin{\times_P}C_j\to C_j\to0$, where $E\mathbin{\times_P}C_j=\{(e,c)\mid v(e)=\iota_j(c)\}$. The resulting map $\Phi_A: \operatorname{Ext}^{1,\mathrm{ext}}_A(P,N)\to\prod_{j\in J}\operatorname{Ext}^{1,\mathrm{ext}}_A(C_j,N)$, $[E]\mapsto([E\mathbin{\times_P}C_j])_{j\in J}$, is a bijection.
