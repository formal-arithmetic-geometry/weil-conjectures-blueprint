+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--10"
order = 425021
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "definition-w-local-w-strictly-local--4", "proposition-w-local-components--1", "theorem-existence-contractible-covers--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-comparison-morphism-inverse-image--2", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "theorem-comparison-direct-images--1", "proposition-comparison-immersions--1", "proposition-locally-constant-sheaves-finite-presentation--3", "lemma-constructible-sheaves--8", "proposition-proper-direct-image-constructible-complexes--2", "proposition-proper-direct-image-constructible-complexes--9", "proposition-comparison-etale-derived-category--5", "proposition-comparison-etale-derived-category--6", "lemma-inverse-image-tensor-product--1", "lemma-inverse-image-tensor-product--2", "proposition-six-operations-change-coefficients--1", "proposition-six-operations-change-coefficients--2", "proposition-six-operations-change-coefficients--3", "proposition-six-operations-change-coefficients--6", "definition-sp-scalar-extension--2", "definition-compactification-refinement--1"]
+++
The projection formula is tested modulo $\pi_E$ in the same way. Let $C$ be
the cone of the projection formula map for $K\in\Dbc(X,\mathcal O_E)$ and
$M\in\Dbc(Y,\mathcal O_E)$. Its source $Rp_*K\otimes^{\mathbf L}M$ and
target $Rp_*(K\otimes^{\mathbf L}p^*M)$ are integrally constructible, by
Lemma [lemma-integral-models](3) and the fact just proved that $Rp_*$
maps $\Dbc(X,\mathcal O_E)$ into $\Dbc(Y,\mathcal O_E)$. As objects of
$\Dbc$ they are derived complete, and so is $C$. Derived
Nakayama (Lemma [lemma-reduction-derived-nakayama]) therefore reduces us
to showing $C/\pi_E=0$. In other words, we must show that the reduction
of the projection formula map is an isomorphism.

This reduction is the torsion projection formula map, which is an
isomorphism by [Stacks, [0F0G](https://stacks.math.columbia.edu/tag/0F0G)]. To identify the two maps, note that the
sources and targets correspond by (4.15) and
associativity of extension of scalars. The maps agree because both are
adjoint to the counit $p^*Rp_*K\to K$, as is
(4.15).

*Source:* the proof of Proposition [proposition-proper-direct-image-constructible-complexes].
