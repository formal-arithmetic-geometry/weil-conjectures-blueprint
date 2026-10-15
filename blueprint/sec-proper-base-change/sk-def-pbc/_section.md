+++
id = "sk-def-pbc"
kind = "definition"
title = "Torsion and the PBC property"
order = 1046
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-pbc-conventions"]
tags = ["sketch"]
+++
A sheaf $F$ of abelian groups, or of $\Lambda$-modules, is *torsion* if every
geometric stalk is a torsion abelian group. Equivalently,

$$
F=\varinjlim_{n\geq1}F[n],\qquad F[n]=\ker(n:F\to F),
$$

where the positive integers are ordered by divisibility. These are sheaf
colimits. The equivalence follows by taking geometric stalks, which commute
with colimits and finite limits and detect isomorphisms.

For a morphism $f:X\to Y$, write $\mathrm{PBC}_\Lambda(f)$ if the exchange
morphism $\Ex_{\square,K}:g^{-1}Rf_*K\to Rf'_*g'^{-1}K$ of [sk-def-exchange]
is an isomorphism in $D^+(Y'_{\Et},\Lambda)$ for every base change
$g:Y'\to Y$ and every $K\in D^+(X_{\Et},\Lambda)$ with torsion cohomology
sheaves. Put $\mathrm{PBC}(f)=\mathrm{PBC}_{\mathbf Z}(f)$. The definition
makes sense for any $f$; for proper $f$ the property is proved in
[sk-thm-p1] and [sk-thm-reduction].

Torsion is a local condition on sections: every section is killed by an
integer after an étale covering, with the integer allowed to vary between
members of the covering. On a non-quasi-compact object a section need not be
killed by a single integer. For example, the constant sheaf $\mathbf Q/\mathbf Z$
on a nonempty scheme is torsion, but on the disjoint union of countably many
copies of the scheme its sections include $(1/2^n)_{n\geq1}$, which has
infinite order.
