+++
kind = "proof"
of = "lemma-integral-changes-source-base--2"
order = 679004
uses = ["definition-small-pro-etale-site--1", "definition-underived-base-change-map--1", "lemma-identity-pasting--3", "theorem-comparison-over-henselian-pair-degree--1", "lemma-finite-direct-images--1"]
+++
Use exactness of integral direct image and its compatibility with base change [Stacks, [04C2](https://stacks.math.columbia.edu/tag/04C2), [0EYP](https://stacks.math.columbia.edu/tag/0EYP), [0F05](https://stacks.math.columbia.edu/tag/0F05)].

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

*Source:* the proof of Lemma [lemma-integral-changes-source-base].
