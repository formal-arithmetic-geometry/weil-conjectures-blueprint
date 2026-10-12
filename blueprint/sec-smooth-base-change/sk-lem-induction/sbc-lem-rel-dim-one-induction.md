+++
id = "sbc-lem-rel-dim-one-induction"
kind = "lemma"
title = "The induction step in relative dimension one"
order = 1469
uses = ["def-sbc-smooth-morphisms", "sbc-def-base-change-property", "sbc-lem-bc-universal-test", "sbc-thm-universal-test-vanishing"]
+++
Let $f:X\to S$ be an affine smooth morphism of relative dimension one
with $X$ affine, let $n$ be an integer invertible on $S$, and assume, for some $q\geq1$, that
$\mathrm{BC}(f,n,q')$ holds universally for all $q'\leq q-1$ in the
sense of [sbc-def-base-change-property]. Then $\mathrm{BC}(f,n,q)$
holds universally, and hence $\mathrm{BC}(f,n,q')$ holds universally
for all $q'\leq q$.
