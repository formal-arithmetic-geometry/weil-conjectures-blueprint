+++
id = "sk-i-real-sheaves"
kind = "proposition"
title = "The lisse sheaf–representation equivalence"
order = 2887
uses = ["sk-d-real-setup", "sk-d-real-weil", "sk-i-real-galois"]
lean = ["AlgebraicGeometry.WeilGroup.isLisseRep_shortExact_iff", "AlgebraicGeometry.WeilGroup.isLisseRep"]
tags = ["sketch"]
+++
Throughout, $C_0$ is the curve and $C$ its base
change to $k$; $P=\pi_1(C)$ is the geometric fundamental group, $W(C_0)$ the
Weil group with degree map and chosen degree-one lift $\gamma$, and
$E\subset\Qlb$ a finite coefficient field with valuation ring
$\mathcal O_E$ and maximal ideal $\mathfrak m_E$, all as in
[sk-d-real-weil]. A lisse Weil sheaf $\mathcal F$ on $C_0$ has geometric
generic stalk $\mathcal F_{\bar\eta}$.

The functor $\mathcal F\mapsto(V,\rho)=(\mathcal F_{\bar\eta}, \rho_{\mathcal F})$ is an exact tensor equivalence between lisse Weil sheaves
on $C_0$ and the lisse representations of [sk-d-real-weil], i.e. the
representations of $W(C_0)$ on finite-dimensional $\Qlb$-vector spaces whose
restriction to $P$ is continuous: a short exact
sequence $0\to\mathcal F'\to\mathcal F\to\mathcal F''\to0$ corresponds to
$0\to V'\to V\to V''\to0$. Subobjects, quotients and subquotients therefore
match on the two sides, in both directions.
