+++
id = "lem-fin-projective-curve-betti-cardinalities"
kind = "lemma"
title = "Betti cardinalities in a smooth projective curve family"
order = 1914
uses = ["def-pc-projective-morphism", "def-sbc-smooth-morphisms", "def-sc-curves", "def-sc-genus", "def-sc-mu-trivialization", "def-weil-pbc-etale-cohomology", "def-weil-pbc-scheme-conventions", "lem-fin-projective-flat-coherent-ranks", "lem-sc-cohomological-dimension", "lem-sc-global-functions", "thm-sc-proper-cohomology"]
+++
Let $S$ be Noetherian
and let $f:X\to S$ be
smooth and
projective, with geometric
fibres of pure dimension one. Fix a prime $\ell$ invertible on $S$.
Write $c_s$ for the number of connected components of the
smooth proper curve $X_{\bar s}$, and
$g_s=\sum_D g(D)$ for the sum of the
genera over its connected components.
Then the etale cohomology
cardinalities are

$$
|H^r(X_{\bar s},\mathbf F_\ell)|=
\begin{cases}
\ell^{c_s},&r=0,2,\\
\ell^{2g_s},&r=1,\\
1,&r>2,
\end{cases}
$$

and each of these functions of $s$ is constructible.
