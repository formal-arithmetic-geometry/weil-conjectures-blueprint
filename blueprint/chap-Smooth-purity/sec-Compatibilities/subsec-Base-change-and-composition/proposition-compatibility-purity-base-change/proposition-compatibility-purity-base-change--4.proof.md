+++
kind = "proof"
of = "proposition-compatibility-purity-base-change--4"
order = 797009
uses = ["theorem-smooth-purity-all-admissible-coefficients", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-six-operations-change-coefficients", "proposition-composition-base-change-rf-shriek", "proposition-projection-formula-rational-coefficients", "lemma-integral-models", "proposition-inverting-ell", "proposition-dctf-x-qbar-2-colimit"]
+++
For (1), the orientations are isomorphisms. Lean proves that $b_{\Lambda_Y}$
is an isomorphism by reducing exceptional base change to finite étale
coefficients. The reduction comparisons for proper morphisms commute with
compact-support base change; this is
`AlgebraicGeometry.ProEtale.CondensedRing.etaleReductionProperBaseChangeCompatibleAll`.
Choose a compactification $f=p\circ j$, with $j$ open and $p$ proper.
Then the exceptional base change map for $f$ is the open restriction of the
map for $p$. Reduction carries the latter, up to the comparison
isomorphisms, to the finite-coefficient exceptional adjoint. Its open
restriction is invertible by smooth base change from
[proposition-exceptional-inverse-image-smooth-morphism](3). Reduction
modulo $\ell$ detects isomorphisms, so the integral open restriction is
also invertible. Integral models and extension of scalars then give
invertibility over
$\overline{\mathbf Q}_\ell$. This is the argument of
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_upperShriekBaseChange_of_smooth_of_etaleReductionProperCompatibleAll`.
Since $c_g$ is also an isomorphism, define

$$
\tau=o_{f'}^{-1}\circ b_\omega\circ g'^*o_f.
$$

Cancellation proves the claimed equality. This is
`AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_baseChange_of_isIso`;
it proves existence of $\tau$ without identifying it with the prescribed
Tate-twist comparison.

For (2), transpose both sides under $Rf'_!\dashv f'^!$. The transpose of
$b_K\circ g'^*\mu_{f,K}$ is the inverse compact-support base change map
followed by $g^*$ of the transpose of $\mu_{f,K}$. Expand the latter using
the tensor symmetry, the inverse projection formula and the counit at the
unit. Expanding the other side gives the same composite: naturality moves
$b_\omega$ through the projection formula, and the definition of
exceptional base change identifies its composite with the counit.
Compatibility of the projection formula with base change and compatibility
of pullback with tensor symmetry identify the remaining factors. Lean
applies `CategoryTheory.ProjectionBaseChange.map_tensorMap_comp_baseChange`,
with
`AlgebraicGeometry.ProEtale.CondensedRing.pfBaseChange_boundedConstructibleExceptionalProjection`;
the latter is proved by factoring into an open immersion and a proper map
and pasting the two squares.
