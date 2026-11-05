+++
kind = "proof"
of = "lemma-affine-covers-dense-intersection--1"
order = 1462003
uses = []
+++
For each $x\in X$, choose an affine open neighbourhood $W$ avoiding
the irreducible components that do not contain $x$. It contains the
generic points of all components through $x$. For each remaining
generic point $\eta$, choose an affine open neighbourhood $V_\eta$
avoiding $\overline W$ and all components other than
$\overline{\{\eta\}}$. These opens and $W$ are pairwise disjoint,
and there are only finitely many of them. Their union is therefore
affine, contains $x$, and contains every generic point. This is
`AlgebraicGeometry.exists_isAffineOpen_mem_and_genericPoints_subset`.

Quasi-compactness gives a finite subcover of these affine
neighbourhoods. Every generic point lies in every member of the
subcover, hence in their total intersection. Since the generic
points are dense in a scheme, the total intersection is dense.
