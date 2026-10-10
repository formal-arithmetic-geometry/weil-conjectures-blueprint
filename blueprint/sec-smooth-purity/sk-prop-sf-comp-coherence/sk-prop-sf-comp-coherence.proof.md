+++
kind  = "proof"
of    = "sk-prop-sf-comp-coherence"
+++
*The comparison.* Write $u:\overline X_1\to\overline X_2$, proper, with
$u j_1=j_2$, and identify $X$ with the open $j_2(X)\subseteq\overline X_2$.
Test $\alpha_u$ at geometric points of $\overline X_2$. Over that open: the
restriction $u':u^{-1}(j_2(X))\to X$ is proper and admits $j_1$ as an open
section, so $j_1(X)$ is open *and closed* in $u^{-1}(j_2(X))$ — an
open section of a separated morphism is a clopen immersion — whence
$u^{-1}(j_2(X))=j_1(X)\amalg W$ with $j_{1!}K$ vanishing on $W$. Hence
$Ru'_*(j_{1!}K)=K$ and $\alpha_u$ is the identity of $K$ there. Outside
$j_2(X)$: if
$\bar y\notin j_2(X)$ then $u^{-1}(\bar y)$ misses $j_1(X)$, since
$u j_1=j_2$; so $j_{1!}K$ restricts to zero on the fibre and proper base change
([sk-thm-properbasechange]) makes $(Ru_*j_{1!}K)_{\bar y}=0$, as is
$(j_{2!}K)_{\bar y}$. Geometric stalks are conservative, so $\alpha_u$ is an
isomorphism. Identity and transitivity follow because both sides are computed
from the same clopen decomposition, and the section identifications agree for a
composite proper map.

*Coherence.* Composition of derived direct images gives
$R\bar f_{1*}\cong R\bar f_{2*}Ru_*$; composing with
$R\bar f_{2*}(\alpha_u^{-1})$ gives the comparison of candidates, and
transports its identity and transitivity. For independence, let $d$ and $d'$
be two common refinements of $c_1,c_2$, with comparisons
$t_i:Rf_!^{d}\to Rf_!^{c_i}$ and $t_i'$ likewise. By
[sk-prop-nagata-sketch-comp-category] (i) choose a refinement mapping to
both $d$ and $d'$; by (iii) the two resulting maps to each $c_i$ agree after a
further refinement. Transitivity then gives $t_2t_1^{-1}=t_2'{t_1'}^{-1}$.
For three compactifications, one common refinement of all three gives
$(t_3t_2^{-1})(t_2t_1^{-1})=t_3t_1^{-1}$, the cocycle condition.
