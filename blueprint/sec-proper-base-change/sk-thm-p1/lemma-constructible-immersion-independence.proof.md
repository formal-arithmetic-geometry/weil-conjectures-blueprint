+++
kind  = "proof"
of    = "lemma-constructible-immersion-independence"
+++
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
