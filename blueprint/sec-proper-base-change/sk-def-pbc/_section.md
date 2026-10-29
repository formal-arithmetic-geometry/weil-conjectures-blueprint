+++
id = "sk-def-pbc"
kind = "definition"
title = "Torsion and the PBC property"
order = 1632
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange", "AlgebraicGeometry.Scheme.IsTorsionSheaf", "AlgebraicGeometry.Scheme.IsTorsionModuleSheaf", "AlgebraicGeometry.Scheme.isTorsionAbelianSheaf_characterizations", "AlgebraicGeometry.Scheme.constant_ratModIntSheaf_sections_not_torsion"]
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
sheaves. If the ring $\Lambda$ is torsion as an abelian group, then $1$ has
finite additive order, so $\Lambda$ is annihilated by a positive integer and
every sheaf of $\Lambda$-modules is torsion.

For proper $f$ and a coefficient ring $\Lambda$ which is torsion as an abelian
group, $\mathrm{PBC}_\Lambda(f)$ is proved in [sk-thm-p1] and
[sk-thm-reduction]. Arbitrary coefficient rings are treated in
[sk-thm-properbasechange].

Torsion is a local condition on sections: every section is killed by an
integer after an étale covering, with the integer allowed to vary between
members of the covering. On a non-quasi-compact object a section need not be
killed by a single integer. For example, the constant sheaf $\mathbf Q/\mathbf Z$
on a nonempty scheme is torsion, but on the disjoint union of countably many
copies of the scheme its sections include $(1/2^n)_{n\geq1}$, which has
infinite order.
