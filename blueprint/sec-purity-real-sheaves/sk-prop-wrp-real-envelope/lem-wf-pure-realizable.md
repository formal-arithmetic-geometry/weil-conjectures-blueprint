+++
id = "lem-wf-pure-realizable"
kind = "lemma"
title = "A pure sheaf is realizable"
order = 3906
uses = ["def-weil-punctual-weights", "def-wf-constant-weil-twist", "def-wf-iota-real"]
lean = ["AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.isReal_biprod_constantTwist_dual", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.isRealizable"]
+++
Let $\mathcal F$ be a lisse Weil sheaf which is punctually
$\iota$-pure of weight $w$. Relative to the fixed isomorphism
$\iota$, put $c=\iota^{-1}(q^{w})$ and

$$
\mathcal R(\mathcal F)=\mathcal F\oplus
\bigl(\mathcal F^\vee\otimes\mathcal B_c\bigr),
$$

the second summand being the constant
Weil twist of the linear dual.
Then $\mathcal R(\mathcal F)$ is $\iota$-real in the sense of
[def-wf-iota-real]; consequently $\mathcal F$ is
$\iota$-realizable.
