+++
kind  = "proof"
of    = "sk-p-linear-filtration"
+++
In a basis adapted to the filtration, the matrix of $u$ is block upper
triangular, so its characteristic polynomial is the product of those of
the diagonal blocks. Over $\overline{\mathbf Q}_\ell$ we may also choose
bases in which $u$ and $v$ are upper triangular ([sk-p-linear-triangular]).
In the induced tensor basis and in the ordered wedge basis, the resulting
matrices are upper triangular with the stated diagonal entries. The matrix
on the dual is the inverse transpose.

For the complement, the same block-triangular computation works over a
commutative ring once $S$ and $V/S$ are free. If $f$ acts on $S/U\ne0$ by
the scalar $c$, apply the factorization to $f-c$ along
$U\subseteq S\subseteq V$: the factor on $S/U$ is the determinant of the
zero map on a nonzero space, so $\det(f-c\mid V)=0$. Taking $v=u$
repeatedly gives $\alpha^n$ among the eigenvalues of $u^{\otimes n}$, and a
diagonal $u$ is diagonal in the wedge basis with the stated entries.
