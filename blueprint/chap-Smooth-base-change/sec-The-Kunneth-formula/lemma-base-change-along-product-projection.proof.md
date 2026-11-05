+++
kind = "proof"
of = "lemma-base-change-along-product-projection"
order = 707
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "theorem-smooth-base-change-classical-torsion", "lemma-degree-zero-calculation", "lemma-injectivity-base-change-map-degree", "lemma-reduction-field", "lemma-integral-changes-source-base", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
The idea is to compactify $f$, so that only an open immersion remains,
and for an open immersion base change along a product projection holds even
when $T$ is singular. We argue on the étale site, where $M$ is a bounded
complex with torsion coefficients, and transport the result to the
pro-étale site by Theorem [theorem-comparison-direct-images].

Choose a compactification $f=\bar f j$, with $j:X\hookrightarrow\bar X$
open and $\bar f:\bar X\to Y$ proper (Theorem [theorem-nagata-s-compactification-theorem]).
Since base change maps compose, it suffices to prove the lemma for $j$ and
for $\bar f$ separately.
For the open immersion $j$, the base change map
$p_{\bar X}^*Rj_*M\to R(j\times\operatorname{id}_T)_*p_X^*M$ is an
isomorphism by [Stacks, [0F1H](https://stacks.math.columbia.edu/tag/0F1H)], applied to the cohomology sheaves of $M$
and combined with the bounded-below spectral sequence. For $\bar f$, proper
base change, applied to $Rj_*M$, shows that

$$
p_Y^*R\bar f_*Rj_*M\longrightarrow
R(\bar f\times\operatorname{id}_T)_*p_{\bar X}^*Rj_*M
$$

is an isomorphism. By Lemma [lemma-identity-pasting] the composite of
the two base change maps is the base change map for $f$.

The step for $j$ does not depend on
Proposition [proposition-ordinary-external-kunneth] below, so there is no
circularity. Indeed, the proof of [Stacks, [0F1H](https://stacks.math.columbia.edu/tag/0F1H)] has two inputs. The first is
base change under extension of the ground field [Stacks, [0F1C](https://stacks.math.columbia.edu/tag/0F1C)], which by
[Stacks, [0F09](https://stacks.math.columbia.edu/tag/0F09)] follows from smooth base change
(Theorem [theorem-smooth-base-change-classical-torsion-2]), because
after passing to perfect closures the larger field is a filtered union of
smooth algebras over the smaller one. The second input, [Stacks, [0F1G](https://stacks.math.columbia.edu/tag/0F1G)], is a
Künneth formula with one proper factor, which comes from proper base
change and the projection formula.
