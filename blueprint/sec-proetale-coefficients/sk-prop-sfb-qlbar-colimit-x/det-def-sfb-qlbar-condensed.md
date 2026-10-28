+++
id = "det-def-sfb-qlbar-condensed"
kind = "definition"
title = "The condensed ring $\\underline{\\overline{\\mathbf Q}}_\\ell$"
order = 1240
uses = ["det-def-sfb-condensed-ring", "det-def-sfb-ring-object"]
lean = ["PadicAlgCl.FiniteIntermediateField", "PadicAlgCl.finiteIntermediateFieldValued", "Profinite.padicAlgClCondensedRing", "Profinite.padicAlgClRingObj", "Profinite.isCommMonObj_padicAlgClRingObj"]
+++
Let $\ell$ be a prime and $\Qlb$ an algebraic closure of $\mathbf Q_\ell$, with the
topology of the absolute value extending that of $\mathbf Q_\ell$. A *finite
subextension* is an intermediate field $\mathbf Q_\ell\subseteq E\subseteq\Qlb$ with
$[E:\mathbf Q_\ell]<\infty$. The finite subextensions, ordered by inclusion, form a
directed poset: the compositum of two of them is again one.

The condensed ring $\underline{\Qlb}$ on the pro-étale site of a point
$*_{\mathrm{proét}}$ ([det-def-sfb-condensed-ring]) is defined by its sections

$$
\underline{\Qlb}(S):=\{a\in C(S,\Qlb)\mid a(S)\subseteq E\ \text{for some finite
subextension }E\},
$$

with restriction by precomposition and pointwise ring operations. In other words, it is
the subpresheaf of $C(-,\Qlb)$ of continuous maps with values in a finite subextension.
This is a sheaf of commutative rings, and it needs no sheafification. Its underlying
abelian sheaf is a commutative ring object of $\Sh(*_{\mathrm{proét}},\Ab)$
([det-def-sfb-ring-object]).
