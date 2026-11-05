+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--10"
order = 425021
uses = ["proposition-proper-direct-image-constructible-complexes--9", "proposition-proper-direct-image-constructible-complexes--2"]
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
