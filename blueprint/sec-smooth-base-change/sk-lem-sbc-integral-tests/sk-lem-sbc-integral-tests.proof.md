+++
kind = "proof"
of = "sk-lem-sbc-integral-tests"
uses = ["sk-prop-injectivity"]
+++
These are [Stacks, Tag 0F04](https://stacks.math.columbia.edu/tag/0F04) and
[Stacks, Tag 0F05](https://stacks.math.columbia.edu/tag/0F05). For an integral morphism
$\pi$, direct image of étale sheaves along $\pi$ is exact and
conservative ([Stacks, Tag 04C2](https://stacks.math.columbia.edu/tag/04C2)), even if $\pi$
is not surjective, and commutes with arbitrary base change
([Stacks, Tag 0EYP](https://stacks.math.columbia.edu/tag/0EYP)).

For the first assertion, $M\to\pi_*\pi^{-1}M$ is injective when $\pi$ is
surjective. [sk-prop-injectivity] preserves its nonzero
cokernel, and exactness of $\pi_*$ together with the Leray spectral
sequence identifies the exchange map for $\pi_*\pi^{-1}M$ with the one for
the composite source morphism.

For the second, let $a\colon T'\to T$ be integral, put
$Y'_T=Y'\times_YT$, and let $a'\colon Y'_T\times_TT'\to Y'_T$ be the
base change of $a$. Pushing the new
exchange map forward by $a'_*$ and using exactness, degree-zero integral
base change and the Leray spectral sequence identifies it with the old
exchange map. Hence if the new map were an isomorphism, so would be the
old one. Conservativity of $a'_*$ gives the converse when needed.
