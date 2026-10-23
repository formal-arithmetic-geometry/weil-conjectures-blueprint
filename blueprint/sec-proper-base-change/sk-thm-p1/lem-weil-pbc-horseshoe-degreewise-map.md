+++
id = "lem-weil-pbc-horseshoe-degreewise-map"
kind = "lemma"
title = "Degreewise middle maps between split horseshoe rows"
uses = ["def-sp-abelian", "def-sp-injective-resolutions"]
lean = ["CategoryTheory.InjectiveResolution.horseshoe_degreewise_map"]
order = 1831
+++
Let $\mathcal C$ be an abelian category [def-sp-abelian]. Let $X,Y,Z$ and $X',Y',Z'$ be cochain complexes of $\mathcal C$ concentrated in degrees $\ge0$. Let $\alpha:X\to Y$, $\beta:Y\to Z$, $\alpha':X'\to Y'$ and $\beta':Y'\to Z'$ be morphisms of complexes with $\alpha\beta=0$ and $\alpha'\beta'=0$ (composition written diagrammatically), such that the rows $0\to X^n\to Y^n\to Z^n\to0$ and $0\to X'^n\to Y'^n\to Z'^n\to0$ are short exact in every degree $n$. Suppose every term $X^n$ and $X'^n$ is injective [def-sp-injective-resolutions]. Given morphisms of complexes $\varphi_A:X\to X'$ and $\varphi_C:Z\to Z'$, there is a family $t=(t_n:Y^n\to Y'^n)_n$ of maps with $\alpha_nt_n=(\varphi_A)_n\alpha'_n$ and $t_n\beta'_n=\beta_n(\varphi_C)_n$ for every $n$. No compatibility of $t$ with the differentials is asserted.
