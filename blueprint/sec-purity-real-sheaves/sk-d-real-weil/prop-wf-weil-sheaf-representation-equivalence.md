+++
id = "prop-wf-weil-sheaf-representation-equivalence"
kind = "theorem"
title = "The lisse sheaf–representation equivalence"
lean = ["AlgebraicGeometry.WeilGroup.exists_equivalence_isLisse", "AlgebraicGeometry.WeilGroup.exists_equivalence_fundamentalRep", "AlgebraicGeometry.WeilGroup.isLisseRep_shortExact_iff", "AlgebraicGeometry.WeilGroup.isLisseRep"]
order = 3776
uses = ["d-real-setup", "def-galois-fibre-functor", "def-wf-fundamental-representation", "def-wf-weil-group", "lem-wf-weil-fundamental-representation", "sk-lem-coefficient-heart", "thm-lisse-qlbar-representations"]
tags = ["latex:proposition"]
+++
Throughout, $C_0$ is the curve and $C$ its base
change to $k$; $P=\pi_1(C)$ is the geometric fundamental group, $W(C_0)$ the
Weil group with degree map and chosen degree-one lift $\gamma$, and
$E\subset\Qlb$ a finite coefficient field with valuation ring
$\mathcal O_E$ and maximal ideal $\mathfrak m_E$, all as in
[def-wf-weil-group]. A lisse Weil sheaf $\mathcal F$ on $C_0$, a lisse $\overline{\mathbf Q}_{\ell,C}$-module on
$C_{\mathrm{proét}}$ ([sk-lem-coefficient-heart]) with a Weil structure, has geometric
generic stalk $\mathcal F_{\bar\eta}$.

The functor $\mathcal F\mapsto(V,\rho)=(\mathcal F_{\bar\eta}, \rho_{\mathcal F})$, the representation of [def-wf-fundamental-representation] (continuous by [lem-wf-weil-fundamental-representation]), is an exact tensor equivalence between lisse Weil sheaves
on $C_0$ and the representations of [def-wf-weil-group]: a short exact
sequence $0\to\mathcal F'\to\mathcal F\to\mathcal F''\to0$ corresponds to
$0\to V'\to V\to V''\to0$. Subobjects, quotients and subquotients therefore
match on the two sides, in both directions.
