+++
kind = "proof"
of = "lemma-filtrations-spectra--1"
order = 1067006
uses = []
+++
For one invariant subspace $W$, choose a basis of $W$ and lift a basis
of $V/W$. In the resulting basis the matrix of $u$ has blocks
$\left(\begin{smallmatrix}A&B\\0&C\end{smallmatrix}\right)$, where
$A$ and $C$ represent the restriction and quotient endomorphisms.
Its characteristic polynomial is the product of theirs. This is
`LinearMap.charpoly_eq_charpoly_restrict_mul_charpoly_mapQ`; it holds
over a commutative ring when $V$, $W$, and $V/W$ are finite free.

Apply this identity inside $F_{m+1}$ to the subspace $F_m$, and induct
on $m$. The characteristic polynomial on $F_0=0$ is $1$.
The natural identifications of the subspace with $F_m$, and of $F_n$
with $V$, intertwine the endomorphisms, so
`LinearMap.charpoly_eq_of_comp_eq` identifies their characteristic
polynomials. This gives the asserted product at $m=n$.
