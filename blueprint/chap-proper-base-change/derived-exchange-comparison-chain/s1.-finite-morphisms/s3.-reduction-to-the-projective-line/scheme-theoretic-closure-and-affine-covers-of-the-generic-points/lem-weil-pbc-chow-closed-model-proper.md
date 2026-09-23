+++
id = "lem-weil-pbc-chow-closed-model-proper"
kind = "lemma"
title = "Closed model of an immersion into projective space"
order = 1478
uses = ["def-weil-pbc-chow-scheme-theoretic-closure", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-closed-immersion-proper", "lem-weil-pbc-proper-composition"]
+++
Let $Y$ be affine and let $j:U\hookrightarrow\mathbf P^n_Y$ be an immersion of
a quasi-compact scheme $U$. Let $Z\subseteq\mathbf P^n_Y$ be the
scheme-theoretic closure of the image of $j$, in the sense of
[def-weil-pbc-chow-scheme-theoretic-closure]. Then $j$ factors as

$$
 U\hookrightarrow Z\hookrightarrow\mathbf P^n_Y,
$$

where $U\hookrightarrow Z$ is a scheme-theoretically dense open immersion and
$Z\hookrightarrow\mathbf P^n_Y$ is the closed immersion; in particular $Z\to
Y$ is proper, as the composite of the closed immersion
$Z\hookrightarrow\mathbf P^n_Y$ with the proper $\mathbf P^n_Y\to Y$.

## Proof

By [def-weil-pbc-chow-scheme-theoretic-closure], $Z$ is the largest closed
subscheme of $\mathbf P^n_Y$ through which $j$ factors, so the factorization
into the closed immersion $Z\hookrightarrow\mathbf P^n_Y$ and the induced
morphism $U\to Z$ exists. The latter is an open immersion with $U$
scheme-theoretically dense in $Z$: this is exactly Stacks Project, Morphisms,
Lemma 29.7.7 (Tag [01RG](https://stacks.math.columbia.edu/tag/01RG)), applied
to the immersion $j$ (which is quasi-compact because $U$ is quasi-compact),
whose conclusion is that the scheme-theoretic image $Z$ of an immersion
contains $U$ as a scheme-theoretically dense open subscheme (and
topologically dense). Finally: a closed immersion is proper; the
projective-space morphism is proper (Stacks Project, Morphisms, Lemma 29.44.5,
Tag [01WC](https://stacks.math.columbia.edu/tag/01WC), applied to $\mathbf
P^n_Y\to Y$); composites of proper morphisms are proper. Hence $Z\to Y$ is the
composite of two proper morphisms, hence proper.
