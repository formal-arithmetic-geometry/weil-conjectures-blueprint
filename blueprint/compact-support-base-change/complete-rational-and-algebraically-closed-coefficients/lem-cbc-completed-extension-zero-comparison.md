+++
id = "lem-cbc-completed-extension-zero-comparison"
kind = "lemma"
title = "Completed extension-by-zero base change"
order = 6623
lean = ["AlgebraicGeometry.Proetale.completedPullback_extensionByZero"]
uses = ["def-weil-pbc-completed-pullback", "def-cbc-open-immersion-square", "def-cbc-extension-by-zero", "lem-cbc-proetale-extension-zero", "lem-cbc-proetale-extension-zero-base-change", "lem-cbc-exact-functor-rlim"]
+++
Let $(A,I)$ be an adic coefficient datum, let
$$
 \begin{array}{ccc}
 U'&\xrightarrow{g_U}&U\\
 j'\downarrow&&\downarrow j\\
 X'&\xrightarrow{g}&X
 \end{array}
$$
be an open-immersion square ([def-cbc-open-immersion-square]), and let
$K\in D(U_{\Proet},A)$ be derived $I$-complete. Then the canonical map
$$
 Lg^*_{\mathrm{comp}}j_!K\xrightarrow{\ \sim\ }j'_!Lg_{U,\mathrm{comp}}^*K
$$
is an isomorphism, natural in $K$.

## Proof

The functor $j_!$ is exact ([def-cbc-extension-by-zero] on the pro-etale
site, [lem-cbc-proetale-extension-zero]), so the reduction tower of $j_!K$ is
$j_!K_\bullet$ (reductions commute with $j_!$ by exactness). By the definition
of the completed pullback its reduction maps are $Lg_n^*j_!K_n$, which
[lem-cbc-proetale-extension-zero-base-change] identifies with
$j'_!Lg_{U,n}^*K_n$, the reductions of $j'_!Lg_{U,\mathrm{comp}}^*K$ (with the
reduction compatibilities of the completed pullback for the map $g_U$).
Applying the exactness of $j'_!$ and [lem-cbc-exact-functor-rlim] to the
defining derived limits of the completed pullback gives the asserted
isomorphism (the countable-product hypothesis of [lem-cbc-exact-functor-rlim]
holds for $j'_!$: extension by zero for an open immersion is exact and, being
the stalk- and sectionwise extension by the zero functor
$V\mapsto V\cap U'$, it is computed levelwise and preserves the countable
products of the derived-product representation).

Unresolved dependencies: def:weil-pbc-adic-coefficient-datum, lem:weil-pbc-completed-pullback-reduction
