+++
id = "lemma-openclosed-etale-lifts-locally"
kind = "lemma"
title = "Étale morphisms lift locally along a closed immersion"
order = 3028
lean = ["AlgebraicGeometry.Etale.exists_isPullback_of_isClosedImmersion", "AlgebraicGeometry.Etale.exists_pullback_hom_of_isClosedImmersion"]
+++
Let $i\colon Z\to X$ be a closed immersion, let $q\colon W\to Z$ be étale
and let $w\in W$. Then there are an open subscheme $W_0\subseteq W$
containing $w$, a scheme $V$ étale over $X$, and an isomorphism of
$Z$-schemes

$$
W_0\cong V\times_XZ.
$$

In pointed form: if $\bar w\colon\Spec\Omega\to W$ is a point
of $W$ with values in a field, then there are a scheme $V$ étale over $X$
and a morphism $V\times_XZ\to W$ of $Z$-schemes through which $\bar w$
factors: apply the above at the image point of $\bar w$ and compose the
isomorphism with the open immersion $W_0\subseteq W$.
