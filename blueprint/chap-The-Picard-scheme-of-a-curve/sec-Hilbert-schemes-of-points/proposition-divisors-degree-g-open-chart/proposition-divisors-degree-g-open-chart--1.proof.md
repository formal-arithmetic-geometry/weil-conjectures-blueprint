+++
kind = "proof"
of = "proposition-divisors-degree-g-open-chart--1"
order = 1537003
uses = ["lemma-rigidification-along-section", "lemma-coherent-base-change-invertible-sheaves", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve"]
+++
Let $D_H$ be the universal divisor on $C_H$ and normalize its invertible
sheaf along $P_H$:

$$
\mathcal L_H=\mathcal O(D_H)\otimes
f_H^*(P_H^*\mathcal O(D_H))^{-1}.
$$

The openness assertion of
Lemma [lemma-coherent-base-change-invertible-sheaves] gives an open
$W\subset H$ such that $a:T\to H$ factors through $W$ exactly when the
pullback of $\mathcal L_H$ lies in $F(T)$. This is the application of
`AlgebraicGeometry.isOpenImmersion_picardFunctorInvertibleDirectImage_ι`
in the Lean proof.

For $\mathcal L\in F(T)$, put $\mathcal N=f_{T,*}\mathcal L$ and let
$\varphi:f_T^*\mathcal N\to\mathcal L$ be the evaluation map.
Its zero scheme commutes with base change. On each fibre, the evaluation
map is nonzero: its adjoint is the identity of the one-dimensional space
of sections. The fibre is integral, so its zero scheme is an effective
Cartier divisor. The relative Cartier criterion then makes
$D=Z(\varphi)$ a relative effective Cartier divisor, finite locally free
over $T$. Its rank is $g$, since cohomology and base change give
$\chi(\mathcal L_t)=1$, while Riemann–Roch and invariance of the genus
under field extension give

$$
\deg D_t=\deg\mathcal L_t
=\chi(\mathcal L_t)-\chi(\mathcal O_{C_t})=1-(1-g)=g.
$$

These are `AlgebraicGeometry.comap_zeroLocus_directImageCounit` and
`AlgebraicGeometry.isInvertible_zeroLocus_directImageCounit`; they define
the natural map $\Phi:F\to\operatorname{Hilb}^{g}_{C/k}$.

To check the inverse constructions, suppose first that
$\mathcal L\simeq\mathcal O(D)\otimes f_T^*\mathcal N'$ lies in $F(T)$,
where $D\in\operatorname{Hilb}^{g}_{C/k}(T)$. The canonical section of
$\mathcal O(D)$, tensored with $f_T^*\mathcal N'$, factors through the
evaluation map by adjunction. Thus its zero scheme $D$ contains
$Z(\varphi)$. Both are finite locally free of rank $g$, so this inclusion
is equality. This is
`AlgebraicGeometry.zeroLocus_directImageCounit_eq_of_iso`.

Conversely, for $D=Z(\varphi)$ there is an isomorphism
$\mathcal L\simeq\mathcal O(D)\otimes f_T^*\mathcal N$.
The pullback of $\mathcal L_H$ along the classifying map of $D$ has the
same form, with another invertible sheaf from $T$. Both classes are
normalized along $P_T$, so they agree by
`AlgebraicGeometry.picardFunctorNormalized_eq_of_iso_tensorObj`, the
normalization argument of Lemma [lemma-rigidification-along-section].
The classifying map therefore factors through $W$. These two identities
give the representation $R$ and its compatibility with $\Phi$.
