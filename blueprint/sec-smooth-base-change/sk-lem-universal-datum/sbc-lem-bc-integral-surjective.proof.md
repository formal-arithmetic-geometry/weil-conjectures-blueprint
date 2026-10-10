+++
kind  = "proof"
of    = "sbc-lem-bc-integral-surjective"
+++
The maps $\mathcal F\to\pi_*\pi^{-1}\mathcal F$ are injective as $\pi$
is surjective, so by [sbc-lem-bc-injectivity] (2), applied to the base
change $f'$ of $f$ along $S'\to S$ and the quasi-compact
quasi-separated $g:T\to S'$, the task reduces to
showing the base-change map for $\pi_*\mathcal F'$ is an isomorphism.
For an integral morphism $\pi$ the direct image is exact by
[sbc-lem-integral-etale-direct-image-exact] (the finite case being
the one noted in [lemma-weil-pbc-finite-direct-image-exact]),
$R^qg_*\pi_*\mathcal F'=R^qg'_*\mathcal F'$ by the Grothendieck
spectral sequence for the composite, the Cartesian identification gives
$e^{-1}\pi_*\mathcal F'=\pi'_*(e')^{-1}\mathcal F'$, and
$R^qh_*\pi'_*(e')^{-1}\mathcal F'=R^qh'_*(e')^{-1}\mathcal F'$ by that
spectral sequence; the assumption on $\mathcal F'$ then gives the
isomorphism for $\pi_*\mathcal F'$, hence for $\mathcal F$ by the
five-lemma transfer of [lemma-weil-pbc-five-lemma-transfer].
