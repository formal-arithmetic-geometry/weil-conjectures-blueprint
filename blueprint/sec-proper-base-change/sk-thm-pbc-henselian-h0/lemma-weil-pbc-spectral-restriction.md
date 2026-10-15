+++
id = "lemma-weil-pbc-spectral-restriction"
kind = "lemma"
title = "Zariski restriction on a spectral space"
order = 1107
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions"]
+++
Let $T$ be spectral [def-weil-pbc-scheme-conventions] and $T_0\subset T$
closed. Suppose every irreducible closed subset $C\subset T$ meets $T_0$ in a
nonempty connected subset. Then restriction is a bijection

$$
  \Gamma(T,F)\xrightarrow{\sim}\Gamma(T_0,F|_{T_0})
$$

for every sheaf of abelian groups $F$ on the Zariski space $T$ which is
locally constant [def-weil-pbc-etale-sheaves], i.e. locally isomorphic to a
constant sheaf. The hypothesis on $F$ cannot be dropped: for $T=\mathbf
A^1_k$, $T_0=\{0\}$ and $F$ the skyscraper sheaf at a closed point $y\neq0$
one has $\Gamma(T,F)\neq0$ and $\Gamma(T_0,F|_{T_0})=0$.
