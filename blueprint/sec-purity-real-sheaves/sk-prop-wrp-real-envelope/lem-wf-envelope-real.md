+++
id = "lem-wf-envelope-real"
kind = "lemma"
title = "The envelope is real"
order = 4125
uses = ["def-weil-punctual-weights", "def-wf-iota-real", "def-wf-normalized-real-envelope"]
lean = ["AlgebraicGeometry.WeilSheaf.isReal_realEnvelope", "AlgebraicGeometry.WeilSheaf.IsLisse.realEnvelope"]
+++
Let $\mathcal F$ be a Weil sheaf, punctually $\iota$-pure of weight $w$,
and let $b\in\Qlb^\times$ with $|\iota(b)|=q^{-w/2}$ (for instance
a $d$th root of $\alpha^{-1}$ for a Frobenius eigenvalue $\alpha$ at a
closed point of degree $d$, as in [def-wf-normalized-real-envelope]). Then the envelope
$\operatorname{Env}_\iota(\mathcal F;b)$ of
[def-wf-normalized-real-envelope] is $\iota$-real in the sense of
[def-wf-iota-real]. If $\mathcal F$ is lisse, so is
$\operatorname{Env}_\iota(\mathcal F;b)$.
