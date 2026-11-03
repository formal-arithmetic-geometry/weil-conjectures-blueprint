+++
kind = "proof"
of = "sk-lem-sbc-integral-tests"
uses = ["sk-prop-injectivity"]
+++
These are [Stacks, Tag 0F04](https://stacks.math.columbia.edu/tag/0F04), [Stacks, Tag 0F05](https://stacks.math.columbia.edu/tag/0F05). For an integral morphism
$\pi$, direct image of étale sheaves along $\pi$ is exact and
conservative [Stacks, Tag 04C2](https://stacks.math.columbia.edu/tag/04C2), even if $\pi$ is not surjective, and
commutes with arbitrary base change [Stacks, Tag 0EYP](https://stacks.math.columbia.edu/tag/0EYP).

For the first assertion, note that $M\to\pi_*\pi^{-1}M$ is injective when $\pi$ is
surjective, so by Lemma [sk-prop-injectivity] the cokernel for
$\pi_*\pi^{-1}M$ is nonzero. Exactness of $\pi_*$ together with the Leray spectral
sequence identifies the base change map for $\pi_*\pi^{-1}M$ with the one for
$\pi^{-1}M$ and the composite morphism, and so base change fails for the
new source.

For the second, let $\pi:T'\to T$ be integral, put
$Y'_T=Y'\times_YT$, and let $\pi':Y'_T\times_TT'\to Y'_T$ be the
base change of $\pi$. We apply $\pi'_*$ to the new base change map. By
exactness of $\pi'_*$, integral base change in degree zero and the Leray
spectral sequence, the result is identified with the old base change map. Hence if the new map were an
isomorphism, so would be the old one.
