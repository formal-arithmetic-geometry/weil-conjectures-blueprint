+++
id = "lem-weil-pbc-curve-dense-open-localization"
kind = "lemma"
title = "Dense-open localization"
order = 1171
uses = ["def-constructible-constructible", "def-constructible-stratification", "def-weil-pbc-curve-setting", "def-weil-pbc-eight-curve-assertions", "def-weil-pbc-etale-sheaves", "lem-weil-pbc-zero-dimensional-cohomology", "lem-weil-pbc-zero-dimensional-field-extension", "lemma-weil-pbc-eight-curve-devissage", "prop-constructible-generic-constancy", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $C$ be a reduced curve and $F$ a constructible $\mathbf F_r$-sheaf. There
is a dense open $j:U\hookrightarrow C$, a finite disjoint union of irreducible
curves, on which $F$ is finite locally constant. For $i:Z=C\setminus
U\hookrightarrow C$ there is a natural exact sequence

$$
 0\to j_!j^{-1}F\to F\to i_*i^{-1}F\to0,
$$

and $Z$ is zero-dimensional. Write $U=\coprod_aU_a$ and let
$j_a:U_a\hookrightarrow C$ be the composite open immersion. Then

$$
 \mathcal C(C,F)\quad\Longleftrightarrow\quad
 \mathcal C(C,j_{a,!}(F|_{U_a}))\text{ for every }a.
$$
