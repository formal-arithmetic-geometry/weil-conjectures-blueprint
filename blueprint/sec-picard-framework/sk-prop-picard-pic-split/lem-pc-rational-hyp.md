+++
id = "lem-pc-rational-hyp"
kind = "lemma"
title = "Curves with a rational point satisfy the hypotheses"
order = 822
uses = ["def-pc-rational-point", "def-pc-smooth-projective-curve", "lem-pc-flat-base-change-cohom", "lem-pc-flat-field", "lem-pc-h0-proper-variety", "lem-pc-structure-pushforward", "thm-pc-pic-split"]
+++
Let $k$ be a field and let $X$ be a
smooth projective curve over
$k$ which has a $k$-rational point $\sigma$. Then the hypotheses of
[thm-pc-pic-split] (with $S=\operatorname{Spec}(k)$, $f:X\to\operatorname{Spec}(k)$) are
satisfied: $f$ has the section $\sigma$, and
$\mathcal{O}_T\to f_{T,*}\mathcal{O}_{X_T}$ is an isomorphism for every
$T\in\operatorname{Ob}((\mathit{Sch}/k)_{fppf})$.
