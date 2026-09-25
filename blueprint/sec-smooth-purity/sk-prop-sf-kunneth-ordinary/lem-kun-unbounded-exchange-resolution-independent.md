+++
id = "lem-kun-unbounded-exchange-resolution-independent"
kind = "lemma"
title = "The unbounded exchange morphism is independent of the K-injective models"
order = 1705
uses = ["def-kun-unbounded-exchange", "def-weil-pbc-kinjective-resolutions", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let $\square=(f,f',g,g',\alpha)$ be a cartesian square, $\Lambda$ a
commutative ring and $K\in D(X_{\Et},\Lambda)$. Then
$\Ex_{\square,K}$ of [def-kun-unbounded-exchange] is unchanged,
in the derived category, by the replacement of a
K-injective resolution
of $K$ (or of $g'^{-1}K$ on $X'$) by another one.

## Proof

Two K-injective resolutions of $K$ are chain-homotopy equivalent by
[prop-weil-pbc-kinjective-resolutions-exist], and a comparison
between them over $K$ is a homotopy equivalence; applying
$g'^{-1}$ gives again a homotopy equivalence, and homotopic
comparisons induce homotopic maps between the mates defining
$\Ex_{\square,K}$ in [def-kun-unbounded-exchange]. Hence the
class of $\Ex_{\square,K}$ in the derived category is independent of
the chosen K-injective resolutions,
[def-weil-pbc-kinjective-resolutions].
