+++
id = "lem-weil-pbc-horseshoe-defect-factorization"
kind = "lemma"
title = "Factorization and cocycle identities of horseshoe defects"
uses = ["def-sp-abelian", "def-sp-injective-resolutions"]
lean = ["CategoryTheory.InjectiveResolution.horseshoe_defect_factorization"]
order = 1809
+++
Let $\mathcal C$ be an abelian category [def-sp-abelian], $S=(S_1\xrightarrow{f}S_2\xrightarrow{g}S_3)$ and $T=(T_1\to T_2\to T_3)$ short exact sequences in $\mathcal C$, and $F=(F_1,F_2,F_3):S\to T$ a morphism of short complexes. Let $I_A,I_B,I_C$ and $J_A,J_B,J_C$ be injective resolutions [def-sp-injective-resolutions] of $S_1,S_2,S_3$ and of $T_1,T_2,T_3$ respectively, with augmentations $\iota$. Let $\alpha:I_A\to I_B$, $\beta:I_B\to I_C$, $\alpha':J_A\to J_B$, $\beta':J_B\to J_C$ be morphisms of complexes with $\alpha\beta=0$ and $\alpha'\beta'=0$ (composition written diagrammatically), whose rows $0\to I_A^n\to I_B^n\to I_C^n\to0$ and $0\to J_A^n\to J_B^n\to J_C^n\to0$ are short exact in every degree $n\ge0$, and such that all four augmentation squares commute ($\iota_A\alpha=f\iota_B$, $\iota_B\beta=g\iota_C$, and likewise for $T$). Let $\varphi_A:I_A\to J_A$ and $\varphi_C:I_C\to J_C$ be morphisms of complexes lifting $F_1$ and $F_3$ ($\iota_A\varphi_A=F_1\iota_A$, $\iota_C\varphi_C=F_3\iota_C$). Let $t=(t_n:I_B^n\to J_B^n)_{n\ge0}$ be a family of maps with $\alpha_nt_n=(\varphi_A)_n\alpha'_n$ and $t_n\beta'_n=\beta_n(\varphi_C)_n$ for every $n$. Then there exist maps $E_n:I_C^n\to J_A^{n+1}$ ($n\ge0$) and $e:S_3\to J_A^0$ such that

1. $\beta_nE_n\alpha'_{n+1}=t_nd_{J_B}^n-d_{I_B}^nt_{n+1}$ for every $n$;
2. $g\,e\,\alpha'_0=\iota_{B,0}\,t_0-F_2\,\iota'_{B,0}$, where $\iota_{B,0}:S_2\to I_B^0$ and $\iota'_{B,0}:T_2\to J_B^0$ are the augmentations;
3. $\iota_{C,0}E_0=e\,d_{J_A}^0$;
4. $d_{I_C}^nE_{n+1}=-E_n\,d_{J_A}^{n+1}$ for every $n$.
