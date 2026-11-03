+++
id = "lem-trf-open-tensor"
kind = "lemma"
title = "Tensoring an extension by zero"
order = 3491
uses = ["def-trf-coefficient-conventions", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-extension-by-zero", "def-weil-scheme-morphism-properties"]
+++
Let $j:U\hookrightarrow Y$ be an
open immersion, and use
the finite coefficient ring
$A$. For $K\in D(U,A)$ and $M\in D(Y,A)$, there is a natural
isomorphism

$$
(j_!K)\otimes_A^LM\simeq j_!(K\otimes_A^Lj^*M),
$$

where $j_!$ is extension by
zero, tensor is the derived
tensor product, and $j^*$ is the
derived pullback.
