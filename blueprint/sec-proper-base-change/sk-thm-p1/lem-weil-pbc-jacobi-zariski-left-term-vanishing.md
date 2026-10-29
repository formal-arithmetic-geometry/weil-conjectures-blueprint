+++
id = "lem-weil-pbc-jacobi-zariski-left-term-vanishing"
kind = "lemma"
title = "Vanishing of the left base-change term of the Jacobi-Zariski sequence"
lean = ["Algebra.jacobiZariski_leftTerm_vanishing"]
order = 1970
+++
Let $A\to B$ be a homomorphism of commutative rings such that $H_1(L_{B/A})=0$ and the module of Kähler differentials $\Omega_{B/A}$ is a projective $B$-module, where $\mathrm{NL}_{B/A}=\bigl(N_1\xrightarrow{\ \delta\ }N_0\bigr)$, $N_1=I/I^2$, $N_0=\bigoplus_{b\in B}B\,\mathrm d[b]$, is the naive cotangent complex of the canonical presentation $A[B]\to B$ (with kernel $I$) and $H_1(L_{B/A})=\ker\delta$. Let $\mathfrak a\subseteq B$ be an ideal and $C=B/\mathfrak a$, and let $\mathrm{NL}_{B/A}\otimes_BC$ be the two-term complex $N_1\otimes_BC\xrightarrow{\ \delta\otimes\mathrm{id}_C\ }N_0\otimes_BC$. Then $$H_1(\mathrm{NL}_{B/A}\otimes_BC)=\ker(\delta\otimes\mathrm{id}_C)\cong H_1(L_{B/A})\otimes_BC=0.$$ More precisely, the map $H_1(L_{B/A})\otimes_BC\to N_1\otimes_BC$ induced by the inclusion $\ker\delta\subseteq N_1$ is injective with image $\ker(\delta\otimes\mathrm{id}_C)$.
