+++
kind = "proof"
of = "lemma-filtrations-spectra--3"
order = 1067008
uses = []
+++
Dualization preserves the characteristic polynomial by
`LinearMap.charpoly_dualMap`, so it suffices to compute the roots for
$u^{-1}$. Choose a basis in which $u$ has an upper triangular matrix
$A$, using `Module.End.exists_basis_isUpperTriangular_toMatrix`.
The matrix $A'$ of $u^{-1}$ satisfies $A'A=1$ and is also upper
triangular. Comparing diagonal entries gives $A'_{ii}A_{ii}=1$.
The roots of the characteristic polynomial of an upper triangular
matrix are its diagonal entries, with multiplicity, so the roots
for $u^{-1}$ are the inverses of those for $u$.
