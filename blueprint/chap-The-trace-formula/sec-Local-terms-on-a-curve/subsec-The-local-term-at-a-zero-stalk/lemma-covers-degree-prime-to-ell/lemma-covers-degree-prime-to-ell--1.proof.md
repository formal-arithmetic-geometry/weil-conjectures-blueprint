+++
kind = "proof"
of = "lemma-covers-degree-prime-to-ell--1"
order = 982002
uses = []
+++
For (1), choose a connected finite étale Galois cover with group $Q$
which makes all the $\mathcal F_i$ constant, using
`AlgebraicGeometry.Scheme.IsFiniteLocallyConstantSheaf.exists_galoisCover_trivializing`.
Let $H\subseteq Q$ be an $\ell$-Sylow subgroup. The connected subgroup
quotient of this cover gives $v:V\to U$ with geometric fibres of
cardinality $[Q:H]$, and a connected $H$-Galois cover of $V$ with the
same total space as the original cover. The index $[Q:H]$ is prime to
$\ell$, and the pullbacks remain constant. This is
`AlgebraicGeometry.Scheme.GaloisCover.exists_connected_subgroup_quotient`
applied to $H$.

For (2), normalize $U$ in $V$. The normalization is finite over $U$
and contains $V$ as the inverse image of $U'$ by
`AlgebraicGeometry.Scheme.normalization_comp_of_finite_etale`.
Its local rings are normal, and it has dimension one, so it is a
smooth curve over the perfect field $k$. Put $A=\Gamma(U,\mathcal O_U)$
and $B=\Gamma(C,\mathcal O_C)$. Counting a geometric fibre over a
closed point of $U'$ identifies $d$ with the rank of $B$ over the
Dedekind domain $A$. The degree formula at $y$ then gives
$$
d=\sum_{c\mapsto y}e_c,
$$
since the residue fields are $k$. Thus some $e_c$ is not divisible by $\ell$.
The theorem `Ideal.exists_not_dvd_ramificationIdx` supplies such a
point. In the discrete valuation ring $\mathcal O_{C,c}$ the image of
any uniformizer at $y$ is a unit times the $e_c$th power of a
uniformizer, as recorded by
`AlgebraicGeometry.Scheme.Hom.exists_stalkMap_eq_unit_mul_pow_ramificationIdx`.

For (3), choose an irreducible affine open neighbourhood of $y$.
Only finitely many terms of $P_L$ and $P_K$ are nonzero. By
`AlgebraicGeometry.Scheme.exists_isFiniteLocallyConstantSheaf_punctured`,
after shrinking to a neighbourhood $W$ all these terms are finite
locally constant on $U'=W-\{y\}$. The punctured neighbourhood is
nonempty and irreducible. Apply (1) to the terms of both complexes
together, and then (2) to the resulting $v:V\to U'$. Transport the
Galois cover along $V\simeq p^{-1}(U')$.

On the connected total space of this Galois cover, the constant
sheaf functor on $\Lambda$-modules is fully faithful. It therefore
transports the differentials, as well as the terms, to complexes of
finite modules. The terms outside the original bounds are zero, so
the resulting complexes remain bounded. This is
`AlgebraicGeometry.Scheme.exists_constantComplex_iso`. Applying it
to both pullbacks supplies the required cover datum.
