+++
kind  = "proof"
of    = "lem-cbc-open-closed-recollement"
+++
The closed immersion $i$ is finite, so $i_*$ is exact and $Ri_*=i_*$ by
[lemma-weil-pbc-finite-direct-image-exact].

*Sheaves.* The composite of the two maps vanishes, since $j^{-1}i_*=0$ and so
$\operatorname{Hom}(j_!j^{-1}F,i_*i^{-1}F)=\operatorname{Hom}(j^{-1}F,j^{-1}i_*i^{-1}F)=0$.
The pair $(i^{-1},j^{-1})$ jointly reflects isomorphisms, hence exactness. After
$j^{-1}$ the sequence becomes $0\to j^{-1}F\to j^{-1}F\to0\to0$, the first map
being an isomorphism by the identity $j^{-1}j_!\cong\operatorname{id}$ of
[prop-weil-open-closed-recollement-adjunctions]. After $i^{-1}$ it becomes
$0\to0\to i^{-1}F\to i^{-1}i_*i^{-1}F\to0$, using the stalkwise description of
[def-weil-pbc-extension-by-zero] for $i^{-1}j_!=0$ and the counit isomorphism
$i^{-1}i_*\cong\operatorname{id}$ for the last map. Both are short exact, so the
original sequence is short exact.

*Complexes.* Complete the counit $j_!j^{-1}K\to K$ to a distinguished triangle
$j_!j^{-1}K\to K\xrightarrow{g}C\to$. Applying $j^{-1}$ kills $C$, since the counit
becomes invertible; applying $i^{-1}$ makes $g$ invertible, since
$i^{-1}j_!=0$. Hence the unit $C\to Ri_*i^{-1}C$ is an isomorphism: after
$j^{-1}$ both sides vanish ($j^{-1}Ri_*=0$), and after $i^{-1}$ it is inverse
to the counit of $i^{-1}\dashv Ri_*$, invertible because $Ri_*$ is fully
faithful; joint conservativity of $(i^{-1},j^{-1})$ concludes. By naturality
of the unit, $g$ followed by $C\cong Ri_*i^{-1}C\cong Ri_*i^{-1}K$ is the unit at
$K$, which gives the triangle (see also [def-weil-open-closed-recollement]).
