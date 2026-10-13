+++
kind  = "proof"
of    = "lem-cbc-completed-extension-zero-comparison"
+++
The functor $j_!$ is exact
([def-weil-pbc-extension-by-zero] on the pro-etale site,
[lem-cbc-proetale-extension-zero]), so the reduction tower of
$j_!K$ is $j_!K_\bullet$ (reductions commute with $j_!$ by
exactness and [def-weil-pbc-adic-coefficient-datum]). By
[def-weil-pbc-completed-pullback] its reduction maps are
$Lg_n^*j_!K_n$, which
[lem-cbc-proetale-extension-zero-base-change] identifies
with $j'_!Lg_{U,n}^*K_n$, the reductions of
$j'_!Lg_{U,\mathrm{comp}}^*K$ (with the reduction compatibilities of
[lemma-weil-pbc-completed-pullback-reduction] for the map
$g_U$). Applying the exactness of $j'_!$ and
[lem-cbc-exact-functor-rlim] to the defining derived limits of
[def-weil-pbc-completed-pullback] gives the asserted
isomorphism (the countable-product hypothesis of
[lem-cbc-exact-functor-rlim] holds for $j'_!$: extension by
zero for an open immersion is exact and, being the stalk- and
sectionwise extension by the zero functor
$V\mapsto V\cap U'$, it is computed levelwise and preserves the
countable products of the derived-product representation).
