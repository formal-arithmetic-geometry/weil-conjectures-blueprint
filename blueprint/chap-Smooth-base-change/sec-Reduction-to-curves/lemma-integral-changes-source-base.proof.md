+++
kind = "proof"
of = "lemma-integral-changes-source-base"
order = 673
+++
Both assertions are [Stacks, [0F04](https://stacks.math.columbia.edu/tag/0F04), [0F05](https://stacks.math.columbia.edu/tag/0F05)]. They use three properties of
direct image along an integral morphism $\pi$. It is exact and
conservative [Stacks, [04C2](https://stacks.math.columbia.edu/tag/04C2)], even if $\pi$ is not surjective. And it
commutes with arbitrary base change [Stacks, [0EYP](https://stacks.math.columbia.edu/tag/0EYP)]. By exactness, the
Leray spectral sequence for a composite with $\pi$ degenerates. This means
that direct images along the composite are computed by applying $\pi_*$
first.

For the first assertion, let $\pi$ be the integral surjective change of the
source. Since $\pi$ is surjective, the map $M\to\pi_*\pi^{-1}M$ is
injective. By Lemma [lemma-injectivity-base-change-map-degree] the
cokernel for $\pi_*\pi^{-1}M$ is therefore nonzero. Exactness of $\pi_*$
and the Leray spectral sequence identify the base change map for
$\pi_*\pi^{-1}M$ with the one for $\pi^{-1}M$ and the composite morphism.
Hence base change fails for the new source.

For the second, let $\pi:T'\to T$ be integral, put
$Y'_T=Y'\times_YT$, and let $\pi':Y'_T\times_TT'\to Y'_T$ be the
base change of $\pi$, again an integral morphism. The new base change map
lives on $Y'_T\times_TT'$, and we compare it with the old one by applying
$\pi'_*$. As $\pi'_*$ is exact, it commutes with taking $R^q$. As it
commutes with base change, the pushed-down terms are the inverse images of
the corresponding terms on $T$. Using the Leray spectral sequence, which
degenerates by exactness, we see that $\pi'_*$ of the new map is the old
base change map. Because $\pi'_*$ is exact and conservative, the old map
would be an isomorphism if the new one were.
