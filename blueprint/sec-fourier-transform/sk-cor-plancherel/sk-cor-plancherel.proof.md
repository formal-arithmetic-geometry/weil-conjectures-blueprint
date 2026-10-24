+++
kind  = "proof"
of    = "sk-cor-plancherel"
+++
*The formula (17.3).* By the stalk formula of [sk-thm-inversion] and the
Grothendieck–Lefschetz formula ([sk-thm-tf-uniform-formula], in the
point-counting form of [sk-cor-tf-point-counting]) on the fibre
$\mathbf A^1$ of $p_2$ over $y$, whose $\mathbf F_{q^n}$-points are the
$x\in\mathbf F_{q^n}$, the trace of Frobenius at $y$ is the sum over these
points of the traces of $K\otimes\mathcal L_{\psi(xy)}$, times $-1$ for the
shift $[1]$; the trace of the character sheaf at $x$ is
$\psi(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}(xy))$ by [sk-lem-as-properties],
and traces are multiplicative for tensor products.

*Plancherel.* We expand the square of the sum in (17.3),
using that the complex conjugate of a character value is its inverse.
For $x,z\in\mathbf F_{q^n}$, the orthogonality of characters gives

$$
 \sum_{y\in\mathbf F_{q^n}}\iota\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}((x-z)y)\bigr)
  =\begin{cases}q^{n},&x=z,\\0,&x\ne z.\end{cases}
$$

Indeed, $\psi\circ\operatorname{Tr}_{\mathbf F_{q^n}/k_0}$ is nontrivial,
since $\psi$ is nontrivial and the trace is surjective; for $x\ne z$,
multiplication by $x-z$ is a bijection of $\mathbf F_{q^n}$, so a
translation in $y$ multiplies the sum by a scalar different from one, and
the sum is zero. Hence only the diagonal terms remain, and they give the
asserted identity. The factor $q^n$ raises the growth parameter by one
([sk-def-wrp-l2-definition]: $\nu$ is defined by
$\limsup_n n^{-1}\log_qS_n-1$, and $S_n(\operatorname{FT}_\psi K)=q^nS_n(K)$).

*Complement.* Applying (17.3) for $\psi^{-1}$ and then for $\psi$, the two
signs cancel and

$$
 t_{\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi K,n}(z)
  =\sum_{x\in\mathbf F_{q^n}}t_{K,n}(x)
     \sum_{y\in\mathbf F_{q^n}}\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}((x-z)y)\bigr)
  =q^n\,t_{K,n}(z)
$$

by the same orthogonality relation; this is the trace function of $K(-1)$,
whose Frobenius traces at points of degree $n$ are multiplied by $q^n$.
