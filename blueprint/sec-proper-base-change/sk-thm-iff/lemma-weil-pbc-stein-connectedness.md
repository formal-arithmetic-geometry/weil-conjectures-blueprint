+++
id = "lemma-weil-pbc-stein-connectedness"
kind = "lemma"
title = "Stein connectedness for $\\mathbf P^1_A$"
order = 1109
uses = ["def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "def-weil-pbc-stein-factorization", "def-weil-pbc-strict-henselian-setup", "lem-weil-pbc-closed-immersion-products", "lemma-weil-pbc-spectral-restriction"]
+++
Let $(A,I)$ be henselian [def-weil-pbc-henselian-terminology] and let
$p:Y\to\operatorname{Spec}A$ be proper
[def-weil-pbc-scheme-conventions]. In the Stein factorization
[def-weil-pbc-stein-factorization]

$$
  Y\longrightarrow\operatorname{Spec}B\longrightarrow\operatorname{Spec}A,
$$

$A\to B$ is finite and $(B,IB)$ is henselian. Every irreducible closed subset
of $Y$ meets $Y_0$ in a nonempty connected subset. Therefore the Zariski
restriction criterion of [lemma-weil-pbc-spectral-restriction] applies to
$(Y,Y_0)$.
