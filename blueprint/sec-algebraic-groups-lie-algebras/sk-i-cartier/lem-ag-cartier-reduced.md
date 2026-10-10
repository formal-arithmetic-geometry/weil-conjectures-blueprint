+++
id = "lem-ag-cartier-reduced"
kind = "lemma"
title = "Cartier: group schemes in characteristic zero are smooth and reduced"
order = 2492
uses = ["def-wf-lie-algebra-derivation", "lem-wf-affine-nullstellensatz-vanishing", "lem-wf-affine-product-reduced", "lem-wf-same-lie-closed-subgroup"]
lean = ["AlgebraicGeometry.isReduced_of_grpObj", "AlgebraicGeometry.smooth_of_grpObj_of_charZero", "AlgebraicGeometry.GrpObj.finrank_lie_eq_topologicalKrullDim", "AlgebraicGeometry.GeneralLinearGroup.finrank_lie_eq_ringKrullDim", "AlgebraicGeometry.GrpObj.lieEquivIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.lieAlgebraEquivIdentityComponent", "AlgebraicGeometry.GrpObj.lieEquiv_mul"]
+++
Let $K$ be a field of characteristic zero. Every group scheme locally of
finite type over $K$ is reduced and smooth over $K$. Moreover:

1. If $G$ is a group scheme of finite type over $K$, then
   $\dim_K\operatorname{Lie}(G)=\dim G$. In particular, for a closed
   subgroup scheme $G=V(I)\subseteq\operatorname{GL}_n$ cut out by a Hopf
   ideal $I$, $\dim_K\operatorname{Lie}(G)$ is the Krull dimension of
   $K[x_{ij},\det^{-1}]/I$.
2. If $G$ is a group scheme of finite type over any field $K$, the
   inclusion of the open identity component $G^\circ\subseteq G$ induces
   an isomorphism of Lie algebras
   $\operatorname{Lie}(G^\circ)\cong\operatorname{Lie}(G)$. If $K$ is
   algebraically closed of characteristic zero and $G=V(I)$ is a closed
   subgroup scheme of $\operatorname{GL}_n$, the same holds for the
   *reduced* identity component of [def-wf-lie-algebra-derivation]: the
   inclusion induces $\operatorname{Lie}(G^\circ)\cong\operatorname{Lie}(G)$.
3. For any group scheme $G$, the group law on tangent vectors at the
   identity (the points over the dual numbers reducing to $1$) is the
   addition of $\operatorname{Lie}(G)$; equivalently, the differential at
   $(1,1)$ of the multiplication is $(X,Y)\mapsto X+Y$.

In particular, let $\mathcal G\subseteq\operatorname{GL}(V)$ over
$k=\overline{\mathbf Q}_\ell$ be a closed subscheme of finite type, cut
out by a finitely generated, possibly nonradical, ideal, such that the
multiplication and inversion of $\operatorname{GL}(V)$ restrict to it.
Then $\mathcal G$ is smooth and reduced, so
$\mathcal G=\mathcal G_{\mathrm{red}}$ is a (smooth) closed matrix group. In particular, if a closed subgroup (a
stabilizer, a centralizer, or the kernel of a regular homomorphism) is
given by explicit equations, its Lie algebra in the sense of
[def-wf-lie-algebra-derivation] is the space of $X$ such that
$1+\varepsilon X$ satisfies those equations over
$k[\varepsilon]/\varepsilon^2$; no passage to the reduced structure
changes the tangent space.
