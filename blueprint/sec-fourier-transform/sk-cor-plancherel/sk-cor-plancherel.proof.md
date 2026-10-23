+++
kind  = "proof"
of    = "sk-cor-plancherel"
+++
*The formula (17.3).* By the stalk formula of [sk-thm-inversion] and the
Grothendieck–Lefschetz formula ([sk-thm-tf-uniform-formula], in the
point-counting form of [sk-cor-tf-point-counting]) on the fibre of $p_2$ over
$y$, the trace of Frobenius at $y$ is the sum over the fibre of the traces of
$K\otimes\mathcal L_{\psi\langle x,y\rangle}$, times $(-1)^r$ for the shift
$[r]$; the trace of the character sheaf at $x$ is
$\psi(\operatorname{Tr}\langle x,y\rangle)$ by [sk-lem-as-properties], and
traces are multiplicative for tensor products.

*Plancherel.* We expand the square of the sum in (17.3),
using that the complex conjugate of a character value is its inverse.
For $x,z\in\mathbf F_{q^n}^r$, the orthogonality of characters gives

$$
 \sum_y\iota\psi\bigl(\operatorname{Tr}\langle x-z,y\rangle\bigr)
  =\begin{cases}q^{nr},&x=z,\\0,&x\ne z.\end{cases}
$$

Indeed, for $x\ne z$ the nondegeneracy of the trace pairing provides a
translation in $y$ that multiplies the sum by a scalar different from
one, so the sum is zero. Hence only the diagonal terms remain, and they
give the asserted identity. On a line, the factor $q^n$ raises the
growth parameter by one ([sk-def-wrp-l2-definition]: $\nu$ is defined by
$\limsup_n n^{-1}\log_qS_n-1$, and $S_n(\operatorname{FT}_\psi K)=q^nS_n(K)$).
