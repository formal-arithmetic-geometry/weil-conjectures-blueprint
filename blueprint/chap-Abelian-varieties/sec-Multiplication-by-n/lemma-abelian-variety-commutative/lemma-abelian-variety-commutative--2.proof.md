+++
kind = "proof"
of = "lemma-abelian-variety-commutative--2"
order = 1495004
uses = ["lemma-abelian-variety-commutative--1"]
+++
By [lemma-abelian-variety-commutative--1], $A$ is geometrically integral.
Lean now applies
`AlgebraicGeometry.isCommMonObj_of_isProper_of_geometricallyIntegral`,
which proves that every proper geometrically integral group scheme over
a field is commutative.

For this theorem, first pass to an algebraic closure of $k$. The product
$A\times A$ is then integral. Let $h(x,y)=xyx^{-1}y^{-1}$ and
$\gamma(x,y)=(x,h(x,y))$. The map $\gamma$ is proper and sends
$\{e\}\times A$ to $(e,e)$. The finite-image neighbourhood lemma
`AlgebraicGeometry.exists_finite_imageι_comp_morphismRestrict_of_finite_image_preimage`
gives an open neighbourhood $U$ of $e$ on which the scheme-theoretic
image of $\gamma$ is finite over $U$ under the first projection.
For a closed point $x\in U$, the image of $\{x\}\times A$ under
$\gamma$ is thus finite and irreducible, hence a single point. Since
$h(x,e)=e$, this point is $(x,e)$.

It follows that $h=e$ on the closed points of the dense open
$U\times A$. Since $A\times A$ is reduced and $A$ is separated,
`AlgebraicGeometry.ext_of_apply_eq` gives equality of the two morphisms
everywhere. Finally, pullback to the algebraic closure is faithful, so
the equality descends to $k$. The commutator is therefore the constant
map $e$, which is equivalent to $m\circ s=m$.
