+++
id = "def-weil-pbc-bounded-constructible-complete"
kind = "definition"
title = "Bounded constructible complete category"
order = 1360
uses = ["def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-intrinsic-completion", "def-weil-pbc-adic-coefficient-datum", "sk-def-sfb-bounded-constructible"]
+++
Assume $T$ is noetherian of finite dimension and the torsion orders are
invertible on $T$. Define $\Dbc(T_{\Proet},A)$ to be the full subcategory of
derived $I$-complete objects, in the sense of the intrinsic completion,
whose reduction tower has compatible etale origins
[def-weil-pbc-etale-origin-witness] and is uniformly bounded constructible
in the sense of the bounded constructible tower.

For the $\ell$-adic coefficient data, $(A,I)=(\mathcal O_E,(\varpi))$ with $E/\Ql$ finite and
$P_n=A_{E,n}$, the ring $A_T$ is the condensed coefficient ring $\mathcal O_{E,T}$
([def-weil-pbc-adic-coefficient-datum]). In that case $\Dbc(T_{\Proet},\mathcal O_E)$ is *by
definition* the condensed bounded constructible category of
[sk-def-sfb-bounded-constructible]: the bounded complexes of $\mathcal O_{E,T}$-modules
with constructible cohomology sheaves. The conditions above then characterize it: an
object of $D(T_{\Proet},\mathcal O_E)$ is bounded with constructible cohomology sheaves if
and only if it is derived $\varpi$-complete and its reduction tower is uniformly bounded
constructible with compatible etale origins. For a general adic datum the conditions
above serve as the definition.
