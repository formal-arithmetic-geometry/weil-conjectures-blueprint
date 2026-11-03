+++
kind = "proof"
of = "sk-lem-tf-independent-base-change"
uses = ["sk-thm-nagata-compactification", "sk-cor-geo-open-finiteness", "sk-thm-properbasechange", "sk-thm-pe-direct-image-comparison", "sk-lem-pbc-exchange-pasting", "sk-thm-sbc-derived"]
+++
The idea is to compactify $f$, so that only an open immersion remains,
for which base change along a product projection holds even when $T$
is singular. We argue on the étale site, where $M$ is a bounded
complex with torsion coefficients, and transport the result to the
pro-étale site by Theorem [sk-thm-pe-direct-image-comparison].

Choose a compactification $f=\bar f j$, with $j:X\hookrightarrow\bar X$
open and $\bar f:\bar X\to Y$ proper (Theorem [sk-thm-nagata-compactification]).
For the open immersion $j$, the base change map
$p_{\bar X}^*Rj_*M\to R(j\times\operatorname{id}_T)_*p_X^*M$ is an
isomorphism by [Stacks, Tag 0F1H](https://stacks.math.columbia.edu/tag/0F1H), applied to the cohomology sheaves of $M$
and combined with the bounded-below spectral sequence. Proper base
change for $\bar f$, applied to $Rj_*M$, shows that

$$
p_Y^*R\bar f_*Rj_*M\longrightarrow
R(\bar f\times\operatorname{id}_T)_*p_{\bar X}^*Rj_*M
$$

is an isomorphism. By Lemma [sk-lem-pbc-exchange-pasting] the composite of
the two base change maps is the base change map for $f$.

This is where smooth base change enters. The proof of [Stacks, Tag 0F1H](https://stacks.math.columbia.edu/tag/0F1H)
rests on base change under extension of the ground field [Stacks, Tag 0F1C](https://stacks.math.columbia.edu/tag/0F1C),
which follows from smooth base change (Theorem [sk-thm-sbc-derived],
[Stacks, Tag 0F09](https://stacks.math.columbia.edu/tag/0F09)), because after passing to perfect closures the larger
field is a filtered union of smooth algebras over the smaller one. The
other input of [Stacks, Tag 0F1H](https://stacks.math.columbia.edu/tag/0F1H) is [Stacks, Tag 0F1G](https://stacks.math.columbia.edu/tag/0F1G), a Künneth formula with
one proper factor, which comes from proper base change and the
projection formula. There is therefore no circularity with
Proposition [sk-lem-sf-kunneth-star] below.
