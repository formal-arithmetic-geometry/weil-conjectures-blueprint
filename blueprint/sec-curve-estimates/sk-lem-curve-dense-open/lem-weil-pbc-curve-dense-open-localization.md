+++
id = "lem-weil-pbc-curve-dense-open-localization"
kind = "lemma"
title = "Dense-open localization"
lean = ["AlgebraicGeometry.IsCurve.exists_dense_assertions_iff_forall_lowerShriek"]
order = 1500
uses = ["def-constructible-constructible", "def-constructible-stratification", "def-weil-pbc-curve-setting", "def-weil-pbc-eight-curve-assertions", "def-weil-pbc-etale-sheaves", "lem-weil-pbc-zero-dimensional-cohomology", "lem-weil-pbc-zero-dimensional-field-extension", "lemma-weil-pbc-curve-dense-open-reduction", "lemma-weil-pbc-eight-curve-devissage", "prop-constructible-generic-constancy", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $C$ be a reduced curve over an algebraically closed field $k$, let
$\Lambda$ be a finite ring, $r$ a prime, and $F$ a constructible sheaf of
$\Lambda$-modules on $C_{\Et}$ with $rF=0$. There are finitely many pairwise
disjoint irreducible opens $U_1,\dots,U_m\subseteq C$ whose union $U$ is
dense, whose complement $Z=C\setminus U$ is zero-dimensional, and on each of
which $F$ is finite locally constant, such that, writing
$j_a:U_a\hookrightarrow C$ for the inclusions,

$$
 \mathcal C(C,F)\quad\Longleftrightarrow\quad
 \mathcal C(C,j_{a,!}(F|_{U_a}))\text{ for every }a,
$$

where $\mathcal C$ denotes the eight assertions of
[def-weil-pbc-eight-curve-assertions].
