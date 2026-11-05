+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--8"
order = 865017
uses = ["theorem-trace-isomorphism-top-degree--4", "corollary-continuity-cohomology"]
+++
The underlying abelian sheaf of $\overline{\mathbf Q}_{\ell,S}$ is the filtered union of the sheaves $\mathcal C_\Lambda$, where $\Lambda\subset\overline{\mathbf Q}_\ell$ runs through compact additive subgroups with finite-dimensional $\Ql$-span. Indeed, on a quasi-compact open a section has compact image in such a finite-dimensional space, and that image is contained in a compact lattice. Lean records this as `AlgebraicGeometry.ProEtale.isColimitAdicConstantSheafCocone`.

For each $\Lambda$, decreasing open balls give open subgroups with trivial intersection, so [theorem-trace-isomorphism-top-degree--4] gives vanishing above $2d$. Continuity of pro-étale cohomology on the quasi-compact quasi-separated scheme $S$ passes the bound to the filtered union. Forgetting the module structure preserves the computed cohomology.

For the constant Weil sheaf, identify cohomology with the pro-étale cohomology of $X$. Smoothness bounds the dimension of this geometric fibre by $d$, so the preceding bound applies. Negative cohomology vanishes because the coefficient sheaf is in degree zero. These last steps are `AlgebraicGeometry.WeilSheaf.subsingleton_cohomology_adicConstant_of_two_mul_lt` and `AlgebraicGeometry.topologicalKrullDim_geometricFiber_le_of_smoothOfRelativeDimension`.
