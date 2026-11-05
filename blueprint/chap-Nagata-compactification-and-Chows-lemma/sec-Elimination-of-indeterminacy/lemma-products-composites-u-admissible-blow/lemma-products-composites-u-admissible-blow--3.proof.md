+++
kind = "proof"
of = "lemma-products-composites-u-admissible-blow--3"
order = 1430006
uses = []
+++
First suppose $U\subseteq V$. Extend $\mathcal J$ to an ideal
$\mathcal I_1$ of finite type on $T$, using
`AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteType_comap_eq`.
Choose an ideal $\mathcal I_0$ of finite type whose vanishing set is
$T\setminus V$, using
`AlgebraicGeometry.Scheme.exists_finiteType_ideal_coe_support_eq_compl`.
Set $\mathcal K=\mathcal I_1\mathcal I_0$. Both factors are the unit ideal
on $U$, so the product center avoids $U$. Moreover
$\mathcal I_0|_V=\mathcal O_V$, whence $\mathcal K|_V=\mathcal J$.
Formation of the blow-up commutes with restriction to an open, giving the
required morphism and cartesian square. Lean uses
`AlgebraicGeometry.Scheme.IdealSheafData.exists_isPullback_blowup_comap`
for this last step; its proof constructs the two comparison morphisms by
the universal property and checks that they are inverse by uniqueness.

For the version without containment, extend $\mathcal J$ to the
quasi-coherent ideal $\mathcal G$ of sections of $\mathcal O_T$ whose
restrictions to $V$ lie in $\mathcal J$. Its vanishing set is the closure
of $V(\mathcal J)$ in $T$, which misses the open $U$ because
$V(\mathcal J)$ does. Hence $\mathcal G$ is the unit ideal on $U$ and
restricts to $\mathcal J$ on $V$, so it is of finite type on $U\cup V$.
This union is quasi-compact. The finite-type extension theorem produces
an ideal $\mathcal K\subseteq\mathcal G$ of finite type with the same
restriction to $U\cup V$.
This is `AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteType_comap_eq_of_disjoint`.
Again use open restriction of blow-ups to obtain the cartesian square.
