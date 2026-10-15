+++
kind = "proof"
of = "det-proper-heart-continuity-sections"
+++
Exactness is [sk-cor-pe-wc-sections]. $W$ is quasi-compact, so $\Gamma(W,-)$ commutes with direct sums of
sheaves (Stacks, Tag 0935).

Let $F\colon I\to\Mod_A$ be any small diagram. Its colimit is the cokernel of the map

$$
\bigoplus_{(i\to j)}F(i)\xrightarrow{\ \ }\bigoplus_{i}F(i),
$$

indexed by arrows of $I$ and objects of $I$, sending the summand of $u\colon i\to j$ by $x\mapsto
\iota_jF(u)x-\iota_ix$. An additive functor that preserves direct sums and cokernels (here: exact)
carries this presentation to the corresponding presentation of the colimit of $\Gamma(W,F(-))$. Hence
$\Gamma(W,-)$ preserves all colimits. (This is also part of [sk-cor-pe-sections].)
