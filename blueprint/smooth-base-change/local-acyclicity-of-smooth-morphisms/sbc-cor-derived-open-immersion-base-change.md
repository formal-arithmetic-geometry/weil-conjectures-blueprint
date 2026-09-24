+++
id = "sbc-cor-derived-open-immersion-base-change"
kind = "theorem"
title = "Derived base change for open immersions"
order = 2818
tags = ["latex:corollary"]
uses = ["sbc-def-derived-categories-with-allowable-torsion", "sbc-def-universal-local-acyclicity", "sbc-lem-bounded-below-truncation-criterion", "sbc-thm-truncated-open-immersion-base-change"]
+++
In the situation of [sbc-thm-truncated-open-immersion-base-change],
let $\mathcal P$ be a set of primes invertible on $Z'$ and let
$K\in D^+_{\mathcal P\text{-tor}}(U_{\Et})$. Then

$$
La^{-1}Rj_*K\xrightarrow{\ \sim\ }Rj'_*La_U^{-1}K
$$

in $D^+_{\mathcal P\text{-tor}}(Z'_{\Et})$.

## Proof

The truncated theorem of
[sbc-thm-truncated-open-immersion-base-change] holds in every
degree for the cohomology sheaves $H^q(K)$ (each of which has torsion
stalks with orders invertible on $Z'$), and the truncation criterion
[sbc-lem-bounded-below-truncation-criterion] (for $j_*$,
$j'_*$) assembles the degreewise isomorphisms into the displayed
isomorphism of bounded-below complexes.
