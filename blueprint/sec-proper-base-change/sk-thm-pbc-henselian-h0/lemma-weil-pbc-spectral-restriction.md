+++
id = "lemma-weil-pbc-spectral-restriction"
kind = "lemma"
title = "Zariski restriction on a spectral space"
lean = ["TopCat.Sheaf.bijective_unit_app_top", "SpectralSpace.exists_shrink_of_isConnected_inter"]
order = 1526
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $T$ be spectral [def-weil-pbc-scheme-conventions], let $T_0\subset T$ be
closed with inclusion $i:T_0\to T$, and suppose every irreducible closed subset
$C\subset T$ meets $T_0$ in a nonempty connected subset. Then for every sheaf of
abelian groups $F$ on the topological space $T$, restriction (the unit
$F\to i_*i^{-1}F$ on global sections) is a bijection

$$
  \Gamma(T,F)\xrightarrow{\sim}\Gamma(T_0,F|_{T_0}).
$$

The key step is the following shrinking property. Let $U_1,\dots,U_m$ be
quasi-compact opens of $T$ covering $T_0$, and let $A_{jk}\subseteq T$ be opens,
reflexive ($U_j\subseteq A_{jj}$), symmetric and transitive
($A_{jk}\cap A_{kl}\subseteq A_{jl}$), with $U_j\cap U_k\cap T_0\subseteq A_{jk}$.
Then there are opens $W_j\subseteq U_j$ covering $T$ with
$U_j\cap T_0\subseteq W_j$ and $W_j\cap W_k\subseteq A_{jk}$.
