+++
kind = "proof"
of = "lemma-filtrations-spectra--4"
order = 1067009
uses = []
+++
Choose a basis in which the matrix $A$ of $u$ is upper triangular.
In the induced wedge basis, indexed by $r$-element subsets $I$ of
the basis indices, the matrix entry at $(I,J)$ is the minor of $A$
with rows $I$ and columns $J$.

Order these subsets first by the sum of their indices and then by
colexicographic order. A nonzero term in the determinant of a minor
pairs each row index with a column index at least as large. Hence
the sum for $I$ is at most that for $J$, and equality forces $I=J$.
The exterior-power matrix is therefore upper triangular in this
order. Its diagonal entry at $I$ is the principal minor
$\prod_{i\in I}A_{ii}$. Reading off the roots with multiplicity gives
the products over all $r$-element submultisets of the roots for $u$,
which Lean writes using `Multiset.powersetCard`.
