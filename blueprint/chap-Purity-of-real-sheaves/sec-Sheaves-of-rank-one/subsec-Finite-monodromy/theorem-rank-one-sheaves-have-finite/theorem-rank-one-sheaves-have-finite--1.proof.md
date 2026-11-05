+++
kind = "proof"
of = "theorem-rank-one-sheaves-have-finite--1"
order = 1104002
uses = ["lemma-invariant-additive-characters"]
+++
Apply `PadicAlgCl.exists_finiteDimensional_forall_mem` to the
one-dimensional matrix representation given by $\chi|_G$. Since $G$ is
compact, its values lie in a finite extension
$E/\mathbf Q_\ell$ inside $\overline{\mathbf Q}_\ell$. Write
$\psi:G\to E^\times$ for the resulting character.

Put $U_E=1+\ell^2\mathcal O_E$ and $H=\psi^{-1}(U_E)$. The subgroup
$H$ is normal, and it is open: it is the inverse image of the ball
$\{z:\lVert z-1\rVert\le\lVert\ell\rVert^2\}$, which is open in the
nonarchimedean topology. Compactness of $G$ makes $G/H$ finite. Thus
$N=[G:H]>0$ and $\psi(g)^N\in U_E$ for every $g\in G$.

On $U_E$ the logarithm is an injective homomorphism to the additive
group of $E$, by `PadicAlgCl.smallLog_mul` and
`PadicAlgCl.injOn_smallLog`. Set $a(g)=\log(\psi(g)^N)$. This map is
additive, and it is invariant under conjugation by the degree-one lift
$s$, because $\chi$ takes values in an abelian group. The estimate

$$
\lVert a(g)\rVert\le\lVert\chi(g)^N-1\rVert
$$

from `PadicAlgCl.norm_smallLog_le` gives continuity at the identity.
Every $\mathbf Q_\ell$-linear coordinate of $a$ is therefore a continuous
additive character, invariant under conjugation by $s$.

Apply the $\mathbf Q_\ell$-valued form of
[lemma-invariant-additive-characters],
`AlgebraicGeometry.WeilGroup.eq_one_of_conj_invariant_of_continuous`,
to each coordinate. Its proof first multiplies a coordinate by a power
of $\ell$ to put its compact image in $\mathbf Z_\ell$, and then uses
the integral form of the lemma. All coordinates vanish, so $a=0$.
Injectivity of the logarithm on $U_E$ gives $\psi(g)^N=1$, hence
$\chi(g)^N=1$.

The geometric image is consequently contained in the finite group of
$N$-th roots of unity. For a rank-one lisse representation $\rho$, Lean
applies this to the continuous character $\det\rho$ and uses
$\rho(g)=\det(\rho(g))\,\id$ to obtain finiteness of the image of $\rho$.
