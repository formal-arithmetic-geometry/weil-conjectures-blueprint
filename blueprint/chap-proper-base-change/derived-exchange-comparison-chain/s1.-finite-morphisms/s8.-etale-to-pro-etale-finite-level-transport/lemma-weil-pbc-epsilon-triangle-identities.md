+++
id = "lemma-weil-pbc-epsilon-triangle-identities"
kind = "lemma"
title = "Triangle identities for the comparison adjunction"
order = 810
uses = ["def-weil-pbc-epsilon-unit-counit", "lemma-weil-pbc-epsilon-unit-counit-naturality"]
+++
The unit and counit satisfy

$$
\begin{aligned}
\varepsilon^X_{\epsilon_X^{-1}F}\,
\epsilon_X^{-1}(\eta^X_F)&=1_{\epsilon_X^{-1}F},\\
\epsilon_{X,*}(\varepsilon^X_G)\,
\eta^X_{\epsilon_{X,*}G}&=1_{\epsilon_{X,*}G}.
\end{aligned}
$$

## Proof

A section of $\epsilon_X^{-1}F$ is locally represented by
$(W\xrightarrow{a}\iota_XU,s)$. The first composite replaces $s$ by its
identity representative at $\iota_XU$ and then restricts it along $a$, which
returns the original class. For $s\in(\epsilon_{X,*}G)(U)=G(\iota_XU)$,
the second composite forms $(1_{\iota_XU},s)$ and evaluates it along the
identity, returning $s$. Local representatives determine maps of sheaves,
so both displayed composites are identities.
