+++
kind = "proof"
of = "lemma-integral-changes-source-base--1"
order = 679002
uses = ["definition-small-pro-etale-site--1", "definition-underived-base-change-map--1", "lemma-identity-pasting--3", "theorem-comparison-over-henselian-pair-degree--1", "lemma-injectivity-base-change-map-degree--1", "lemma-injectivity-base-change-map-degree--2", "lemma-finite-direct-images--1"]
+++
Use the injectivity and cokernel comparison in Lemma [lemma-injectivity-base-change-map-degree], together with exactness and integral base change [Stacks, [04C2](https://stacks.math.columbia.edu/tag/04C2), [0EYP](https://stacks.math.columbia.edu/tag/0EYP), [0F04](https://stacks.math.columbia.edu/tag/0F04)].

For the first assertion, let $\pi$ be the integral surjective change of the
source. Since $\pi$ is surjective, the map $M\to\pi_*\pi^{-1}M$ is
injective. By Lemma [lemma-injectivity-base-change-map-degree] the
cokernel for $\pi_*\pi^{-1}M$ is therefore nonzero. Exactness of $\pi_*$
and the Leray spectral sequence identify the base change map for
$\pi_*\pi^{-1}M$ with the one for $\pi^{-1}M$ and the composite morphism.
Hence base change fails for the new source.

*Source:* the proof of Lemma [lemma-integral-changes-source-base].
