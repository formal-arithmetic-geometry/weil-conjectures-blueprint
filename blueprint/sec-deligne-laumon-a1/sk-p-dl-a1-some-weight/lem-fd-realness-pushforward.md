+++
id = "lem-fd-realness-pushforward"
kind = "lemma"
title = "Reality survives the Fourier projection"
lean = ["AlgebraicGeometry.WeilSheaf.isReal_higherLowerShriek_one", "AlgebraicGeometry.WeilSheaf.isReal_higherLowerShriek_snd_one"]
order = 4001
uses = ["def-fd-transform", "sk-lem-coefficient-heart", "sk-def-sf-weil-complexes", "def-wf-iota-real", "sk-thm-sfb-shriek-base-change", "det-thm-tf-uniform-formula-weil"]
+++
Let $k_0=\mathbf F_q$, let
$X_0=\mathbf A^1_{k_0}\times_{k_0}\mathbf A^1_{k_0}$ with second
projection $p_2:X_0\to\mathbf A^1_{k_0}$ of
[def-fd-transform], and let $\mathcal K$ be a
constructible $\Qlb$-Weil sheaf on
$X_0$ (an object of $\Cons(X,\Qlb)$, [sk-lem-coefficient-heart], with a Weil
structure, [sk-def-sf-weil-complexes]) which is $\iota$-real in the sense of
[def-wf-iota-real]. Assume that

$$
R^\nu p_{2,!}\mathcal K=0\qquad(\nu\neq1).
$$

Then $R^{1}p_{2,!}\mathcal K$ is $\iota$-real.
