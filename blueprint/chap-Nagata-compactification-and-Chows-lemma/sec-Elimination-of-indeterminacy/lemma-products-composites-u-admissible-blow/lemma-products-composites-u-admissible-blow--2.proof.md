+++
kind = "proof"
of = "lemma-products-composites-u-admissible-blow--2"
order = 1430005
uses = ["lemma-products-composites-u-admissible-blow--1"]
+++
Finite-degree descent of the second center gives $d>0$ and a
quasi-coherent ideal $\mathcal L\subseteq\mathcal I^d$ of finite type
on $T$ such that

$$
\mathcal L\mathcal O_{T_1}
=(\mathcal I\mathcal O_{T_1})^d\mathcal J,
\qquad
V(\mathcal L)=V(\mathcal I)\cup\pi\bigl(V(\mathcal J)\bigr).
$$

This is `AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteDegree_center`.
Its construction chooses a finite affine cover and finitely many
generators of the second center on blow-up charts, clears denominators
in a common positive degree, and extends the resulting finite sets of
numerators to finite-type ideal subsheaves on $T$. Their sum gives
$\mathcal L$. The support formula is checked over $V(\mathcal I)$ and
over its complement, where $\pi$ is an isomorphism.

Put $\mathcal K=\mathcal I\mathcal L$. By
[lemma-products-composites-u-admissible-blow--1], its blow-up is the blow-up
of $(\mathcal I\mathcal O_{T_1})^d\mathcal J$ on $T_1$.
The exceptional ideal $\mathcal I\mathcal O_{T_1}$ is invertible, and
multiplication by an invertible ideal does not change a blow-up. Lean
proves this last comparison by the universal property in
`AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_isInvertible_iso`.
It therefore identifies the blow-up of $\mathcal K$ with $T_2$ over $T$.

The ideal $\mathcal K$ is of finite type and
$V(\mathcal K)=V(\mathcal I)\cup\pi(V(\mathcal J))$.
The first set misses $U$ by the first admissibility hypothesis, and the
second misses $U$ because $V(\mathcal J)$ misses $\pi^{-1}(U)$.
Lean packages the comparison and support formula in
`AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comp`, then applies
this disjointness argument in `AlgebraicGeometry.IsAdmissible.exists_comp`.
