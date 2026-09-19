+++
id = "prop-openclosed-conservative"
kind = "theorem"
title = "$j^*$ and $i^*$ jointly reflect isomorphisms"
order = 985
lean = ["AlgebraicGeometry.Etale.jointlyReflectIsomorphisms_upperStar"]
tags = ["latex:proposition"]
uses = ["lemma-openclosed-point-factors", "lemma-openclosed-point-ulift", "lemma-openclosed-stalk-upperstar"]
+++
Let $(j,i)$ be a complementary pair on $X$ and let
$\varphi\colon\mathcal F\to\mathcal F'$ be a morphism in $\shv{\et X}$ such
that $j^*\varphi$ and $i^*\varphi$ are isomorphisms. Then $\varphi$ is an
isomorphism.

## Proof

By [lemma-openclosed-point-ulift] it suffices to prove that
$\varphi_{\bar x}$ is an isomorphism for every geometric point $\bar x$ of
$X$. By [lemma-openclosed-point-factors], $\bar x$ factors as
$j\circ\bar u$ for a geometric point $\bar u$ of $U$, or as $i\circ\bar z$
for a geometric point $\bar z$ of $Z$. In the first case
[lemma-openclosed-stalk-upperstar] identifies $\varphi_{\bar x}$ with
$(j^*\varphi)_{\bar u}$, an isomorphism by hypothesis; in the second case it
identifies $\varphi_{\bar x}$ with $(i^*\varphi)_{\bar z}$, again an
isomorphism.
