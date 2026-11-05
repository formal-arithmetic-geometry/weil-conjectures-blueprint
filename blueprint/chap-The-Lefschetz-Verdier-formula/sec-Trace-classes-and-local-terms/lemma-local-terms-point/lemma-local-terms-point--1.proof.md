+++
kind = "proof"
of = "lemma-local-terms-point--1"
order = 918002
uses = ["definition-verdier-dual-evaluation", "lemma-external-duality-trace-morphism", "definition-trace-morphism", "definition-trace-class-local-terms", "definition-categorical-trace"]
+++
Write the trace class of Definition [definition-trace-class-local-terms]
as the exceptional adjoint of the diagonal pullback of the supported
class, followed by evaluation
(`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_homEquiv`).
For the identity correspondence, the supported class is the class of
$1_K$ read through the inverse external-duality isomorphism of
[lemma-external-duality-trace-morphism], followed by $p_1^*u\otimes 1$
(`AlgebraicGeometry.ProEtale.CondensedRing.supportedClass_ofEnd`).
Naturality of $\Delta^*(K\boxtimes D)\simeq K\otimes^{\mathbf L}D$
moves this endomorphism to $u\otimes 1_D$. Integration on $s$ is
composition with $\omega_s\simeq\Lambda_s$
(`AlgebraicGeometry.ProEtale.CondensedRing.BorelMooreSection.integral_point`).
Expanding the exceptional adjunction therefore gives the first identity.

For the second identity, express $\sigma_u$ as the pullback of the class
of $1_K$ through inverse external duality, preceded by a map
$\tau:\Lambda_s\to\Delta^*R\Delta_!\Lambda_s$; the pairing $e_u$ is
evaluation followed by $\omega_s\simeq\Lambda_s$
(`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointCoev_eq` and
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointPairing_eq`).
The inverse external-duality map cancels against its uncurried pairing.
Transport this identity along the monoidal functor $\Delta^*$, which
preserves the Koszul symmetry. Under $\Delta^*p_i^*\simeq\mathrm{id}$,
the exceptional Künneth map becomes the unit identification, and the
class of $1_K$ becomes the counit
(`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointKunneth_transport`,
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointKunneth_baseChange`, and
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointClass_transport`).
Finally, $\tau$ followed by that counit is the identity
(`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.pointTau_comp_counit`).
The transport identity
`CategoryTheory.MonoidalCategory.zigzag_of_transport` now gives the
displayed zigzag.

If $K$ has a right dual, this zigzag suffices to identify
$e_u\circ(u\otimes 1_D)\circ\sigma_u$ with the categorical trace of
[definition-categorical-trace]. Indeed, transpose $e_u$ to a map
$D\to K^\vee$; symmetry identifies $e_u$ with evaluation through this
map, and the zigzag identifies the image of $\sigma_u$ with coevaluation.
This is `CategoryTheory.MonoidalCategory.trace_eq_of_zigzag`, the final
step of the point normalization in Lean.
