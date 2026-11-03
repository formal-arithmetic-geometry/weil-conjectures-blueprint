+++
id = "sk-lem-induction"
kind = "lemma"
title = "The induction step in relative dimension one"
order = 2206
uses = ["sk-def-bc", "sk-lem-universal-datum", "sk-thm-vanishing"]
lean = ["AlgebraicGeometry.Etale.UniversalBaseChangeProperty.of_forall_lt"]
+++
Let $f:X\to S$ be affine smooth of relative dimension one with $X$
affine, let $\Lambda$ be a commutative ring, and let $n$ be an integer
invertible on $S$ with $n\Lambda=0$. Let $q\ge1$. If
$\mathrm{BC}(f,\Lambda,q')$ holds universally for every $q'<q$
([sk-def-bc]), then $\mathrm{BC}(f,\Lambda,q)$ holds universally.
