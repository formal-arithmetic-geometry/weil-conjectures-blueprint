+++
id = "lemma-constructible-immersion-independence"
kind = "lemma"
title = "Independence of the scheme structure"
order = 1169
lean = ["AlgebraicGeometry.Scheme.IsFiniteLocallyConstantSheaf.upperStar_of_range_subset", "AlgebraicGeometry.Scheme.isFiniteLocallyConstantSheaf_upperStar_iff_of_range_eq"]
uses = ["def-constructible-finite-locally-constant", "lemma-constructible-iso-invariance", "lemma-constructible-pullback-stratification", "lemma-constructible-universal-homeomorphism-invariance", "prop-constructible-pullback"]
+++
Let $\mathcal F\in\shv{\et X}$, let $b\colon Z'\to X$ be an immersion and
let $a\colon Z\to X$ be a morphism whose image is contained in the image
of $b$. If $b^*\mathcal F$ is finite locally constant, then so is
$a^*\mathcal F$. In particular, if $a$ and $b$ are immersions with the same
image, then $a^*\mathcal F$ is finite locally constant if and only if
$b^*\mathcal F$ is.

## Proof

Let $W=Z\times_XZ'$ with projections $p\colon W\to Z$ and $q\colon W\to Z'$.
The projection $p$ is an immersion, as a base change of $b$, and it is
surjective: its image is $a^{-1}(b(Z'))$, which is all of $Z$ because
$a(Z)\subseteq b(Z')$. A surjective immersion is a surjective closed
immersion (an immersion is a closed immersion into an open subscheme, and
surjectivity forces that open to be everything). Suppose $b^*\mathcal F$ is
finite locally constant. Then $q^*b^*\mathcal F$ is finite locally constant
by [prop-constructible-pullback]. Since $a\circ p=b\circ q$, we have
$p^*a^*\mathcal F\cong q^*b^*\mathcal F$, so $p^*a^*\mathcal F$ is finite
locally constant by [lemma-constructible-iso-invariance]. Finite local
constancy descends along the surjective closed immersion $p$
([lemma-constructible-universal-homeomorphism-invariance]), so
$a^*\mathcal F$ is finite locally constant.

If $a$ and $b$ are immersions with the same image, the first part applies
to $(a,b)$ and to $(b,a)$, which gives the equivalence.
