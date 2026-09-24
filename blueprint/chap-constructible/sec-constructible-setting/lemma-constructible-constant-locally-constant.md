+++
id = "lemma-constructible-constant-locally-constant"
kind = "lemma"
title = "Constant sheaves are locally constant"
order = 1043
lean = ["CategoryTheory.Sheaf.IsConstant.isLocallyConstantSheaf"]
uses = ["def-constructible-constant", "def-constructible-locally-constant"]
+++
A constant sheaf is locally constant.

## Proof

The identity cover $(X\to X)$ is a trivialising datum: the restriction of
$M_X$ to $\et X$ localised at $X$ is $M_X$ again, which is constant.
