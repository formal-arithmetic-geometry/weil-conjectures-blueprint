+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--10"
order = 425021
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "lemma-extremally-disconnected-covers--3", "theorem-existence-contractible-covers--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "lemma-integral-models--3", "lemma-integral-models--4", "proposition-proper-direct-image-constructible-complexes--9", "proposition-comparison-etale-derived-category--5", "definition-sp-scalar-extension--2", "definition-compactification-refinement--1"]
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
