+++
kind = "proof"
of = "theorem-pure-lisse-sheaves-over-relative--1"
order = 1345002
uses = ["proposition-composition-base-change-rf-shriek", "theorem-weight-bound-affine-curve", "lemma-finite-quasi-finite-direct-images", "lemma-extreme-degrees-affine-curve", "lemma-cohomological-range-curve", "theorem-grothendieck-lefschetz-trace-formula", "proposition-twisting-weight-zero-adding-dual", "theorem-real-constructible-sheaves-are-mixed", "proposition-weights-under-usual-operations"]
+++
*The punctual bound.* Fix a closed point $y$ of degree $d$ over $k_0$,
and regard $X'_0=U_0\times_{Y_0}\operatorname{Spec}\kappa(y)$ as a
$k_0$-scheme. It is affine and smooth of relative dimension one over
$k_0$, since $\kappa(y)/k_0$ is finite étale. Write $g:X'_0\to U_0$ for the projection and
$X'=X'_0\times_{k_0}\overline{k}_0$. Compact-support base change
(Proposition [proposition-composition-base-change-rf-shriek]) and
degree-zero cohomology of $\operatorname{Spec}\kappa(y)$ give

$$
P_{i,y}(T^d)
=\det(1-T\Phi\mid H_c^i(X',g^*F)),
\qquad
P_{i,y}(T)=\det(1-T\operatorname{Frob}_y\mid(R^ih_!F)_{\bar y}),
$$

where $\Phi$ is the Frobenius relative to $k_0$. This is
`AlgebraicGeometry.exists_fiber_charpolyRev_higherLowerShriek`.

The affine-curve estimate
`AlgebraicGeometry.hasWeightsAtMostOver_compactlySupportedCohomology_of_isAffine`
bounds the weights of $H_c^i(X',g^*F)$ by $w+i$. Its proof takes a finite
map from $X'_0$ to $\mathbf A^1_{k_0}$, uses
Lemma [lemma-finite-quasi-finite-direct-images], and restricts the
direct image to a dense open where it is lisse. The curve estimate
of Theorem [theorem-weight-bound-affine-curve], together with the
extreme degrees, treats this open, in the form
`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.hasWeightsAtMostOver_compactlySupportedCohomology`.
The finite complement contributes only in degree zero. The open–closed exact sequence gives the bound
on the whole affine line. Thus no geometric connectedness hypothesis
on $X'_0$ is needed.

The displayed polynomial identity says that every eigenvalue $\alpha$
at $y$ is $\beta^d$ for an eigenvalue $\beta$ on this cohomology.
Since $q_y=q^d$, the bound $|\iota(\beta)|\le q^{(w+i)/2}$ gives (1).

*Reality.* Apply the same fibre construction to $E$, and write
$Q_j(T)=\det(1-T\Phi\mid H_c^j(X',g^*E))$. The affine-curve endpoint
lemmas give $H_c^0=0$ and purity of weight two in degree two; the
cohomology vanishes outside degrees $0,1,2$
(Lemmas [lemma-extreme-degrees-affine-curve] and
[lemma-cohomological-range-curve]). In Lean the endpoint statements
for this possibly disconnected fibre are
`AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_zero_of_isAffine`
and
`AlgebraicGeometry.isPureOfWeightOver_compactlySupportedCohomology_two_of_isAffine`;
they are obtained by a finite map to the affine line. The curve bound
puts the degree-one eigenvalues in modulus at most $q^{1/2}$.

The traces of all positive powers of local Frobenius on $g^*E$ are
real. Theorem [theorem-grothendieck-lefschetz-trace-formula] therefore
makes
$\iota\bigl(\operatorname{Tr}(\Phi^m\mid H_c^2)-\operatorname{Tr}(\Phi^m\mid H_c^1)\bigr)$
real for every $m\ge1$. The logarithmic-derivative identities for
the two characteristic polynomials give

$$
\iota Q_1\,\overline{\iota Q_2}
=\overline{\iota Q_1}\,\iota Q_2.
$$

Their reciprocal roots have disjoint moduli, since $q^{1/2}<q$.
Consequently the polynomials are coprime, and their constant
coefficients are one, so each is fixed by complex conjugation. This
is `LinearMap.map_charpolyRev_conj_eq_self_of_trace`. In the other
degrees the local polynomial is one. The identity with $T^d$ then
shows that $P_{i,y}$ has real coefficients, proving (2).

*Mixedness.* Choose a weight $w'$ for which $F$ is pure and a scalar
$b$ with $|\iota(b)|=q^{-w'/2}$, using
`AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.exists_units_norm_eq`.
If a stalk has an eigenvalue, one may take $w'=w$; if no stalk has
an eigenvalue, take $w'=0$ and $b=1$. Put
$F^0=F\otimes\mathcal B_b$ and $E=F^0\oplus(F^0)^\vee$ as in
Proposition [proposition-twisting-weight-zero-adding-dual].
Then $E$ is lisse, real and pure of weight zero. By (2) and
Theorem [theorem-real-constructible-sheaves-are-mixed], $R^ih_!E$ is
mixed of weights at most some $v_0$.

Additivity carries the split inclusion $F^0\to E$ to a split
inclusion $R^ih_!F^0\to R^ih_!E$. Hence $R^ih_!F^0$ has the same
upper bound by Proposition [proposition-weights-under-usual-operations].
The isomorphism

$$
R^ih_!(F\otimes\mathcal B_b)
\simeq R^ih_!F\otimes\mathcal B_b
$$

is `AlgebraicGeometry.WeilSheaf.nonempty_higherLowerShriek_constantTwist_iso`.
Twisting back by $b^{-1}$ preserves mixedness and shifts the upper
bound by $w'$, giving (3) with $v=v_0+w'$.
