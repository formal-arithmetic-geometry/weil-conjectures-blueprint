+++
kind = "proof"
of = "lemma-inverse-image-tensor-product--2"
order = 494005
uses = ["lemma-inverse-image-tensor-product--1", "lemma-inverse-image-tensor-product--4", "lemma-inverse-image-tensor-product--6", "lemma-structure-integral-constructible-complexes", "definition-lisse-sheaves"]
+++
The unit is the free module of rank one in degree $0$. For tensor closure,
Lean applies `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_tensorObj`
with the integral coefficient hypotheses supplied by
`AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.lisseHypotheses`.

First consider bounded complexes with lisse cohomology. By truncation in
both variables, using [lemma-structure-integral-constructible-complexes](1),
it suffices to tensor two lisse sheaves in degree $0$. Pro-étale locally
these are finite sums of $\mathcal O_E$ and $\mathcal O_E/\pi_E^r$.
The two-term free resolutions of the torsion summands show that their
derived tensor product has lisse cohomology in degrees $[-1,0]$.
This proves the lisse case.

For general $K$ and $L$, argue by Noetherian induction on closed supports.
There is a nonempty open $V$ and a surjective closed immersion $c:T\to V$
on which both complexes have lisse cohomology. Pullback commutes with
tensor product, so the lisse case applies on $T$. By
[lemma-inverse-image-tensor-product--4] and the isomorphism
$M\simeq\mathbf Rc_*\mathbf Lc^*M$ for this surjective closed immersion,
the tensor product is bounded constructible on $V$. Its restriction to
the closed complement is bounded constructible by induction, using
[lemma-inverse-image-tensor-product--1]. Apply the locality statement
[lemma-inverse-image-tensor-product--6].
