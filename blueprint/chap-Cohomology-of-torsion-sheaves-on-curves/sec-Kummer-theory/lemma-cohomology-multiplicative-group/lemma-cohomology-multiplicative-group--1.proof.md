+++
kind = "proof"
of = "lemma-cohomology-multiplicative-group--1"
uses = []
+++
An invertible sheaf $\mathcal L$ gives the $\mathbf G_m$-torsor
$\operatorname{Isom}(\mathcal O_X,\mathcal L)$. Conversely, trivialize a torsor
on an étale cover and use its transition functions to descend the structure
sheaf to an invertible sheaf. These constructions give
`AlgebraicGeometry.Scheme.picEquivQuotientTorsorGmSheaf`. Compose this
bijection with the classification of abelian torsors by $H^1$,
`CategoryTheory.Sheaf.Torsor.classH1`. Tensor products multiply transition
functions, so their classes add; this is
`AlgebraicGeometry.Scheme.Pic.toCohomologicalPicardGroup_mul`.
