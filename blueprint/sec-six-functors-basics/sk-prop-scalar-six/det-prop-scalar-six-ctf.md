+++
id = "det-prop-scalar-six-ctf"
kind = "lemma"
title = "Extension of scalars preserves $\\Dctf$"
uses = ["det-prop-scalar-six-pullback", "sk-lem-sf-flat-model", "det-lem-int-tensor-shriek", "sk-cor-coefficient-heart-ii", "sk-thm-sf-ctf-stability"]
+++
Let $\Lambda\to\Lambda'$ be one of the listed coefficient maps of
[sk-prop-scalar-six] (or a composite of them) and $X$ a standing scheme. Then:

1. Every object of $\Dctf(X,\Lambda)$ is obtained by finitely many shifts,
   extensions and direct summands from objects $a_!P$, where
   $a\colon S\hookrightarrow X$ is a locally closed immersion and $P$ is pro-étale locally on
   $S$ of the form $P_0\otimes_{\Lambda(*)}\Lambda_S$ for a bounded complex $P_0$ of
   finite projective $\Lambda(*)$-modules ("locally perfect").
2. If $P$ is locally perfect over $\Lambda$, then $P_{\Lambda'}$ is locally perfect over
   $\Lambda'$, and $a_!(P_{\Lambda'})\in\Dctf(X,\Lambda')$.
3. $K\mapsto K_{\Lambda'}$ maps $\Dctf(X,\Lambda)$ into $\Dctf(X,\Lambda')$.
