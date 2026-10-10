+++
id = "lemma-nagata-immersion-into-proper"
kind = "lemma"
title = "The immersion construction is a compactification"
order = 80
lean = ["AlgebraicGeometry.HasCompactification.of_isImmersion"]
uses = ["def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-immersion-compactification", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-open-immersion-qc-over-separated-target"]
+++
Let $g\colon X\to Y$ be an immersion over $S$ with $Y\to S$ proper, and
assume the composite $X\to S$ is quasi-compact. Then $X\to S$ is
compactifiable: $g$ is quasi-compact, and the constructed factorization
$\mathsf C(g)$ is a compactification of $X\to S$.

## Proof

Write $f\colon X\to S$ for the composite. Since $Y\to S$ is proper, it is
separated, hence quasi-separated; as $f$ is quasi-compact,
[lemma-nagata-open-immersion-qc-over-separated-target] applied to the
triangle $X\xrightarrow{g}Y\to S$ shows that $g$ is quasi-compact. Thus $g$
is a quasi-compact immersion and $\mathsf C(g)$ is defined
([def-nagata-immersion-compactification]). Its first map $g^{\mathrm{im}}$
is a (quasi-compact) open immersion by
[lemma-nagata-immersion-open-in-scheme-image]. The second map is the
composite of the closed immersion $g_{\mathrm{im}}$ with the proper map
$Y\to S$, hence is proper. The factorization equality gives the required
structural equality:

$$
g^{\mathrm{im}};g_{\mathrm{im}};(Y\to S)
=g;(Y\to S)=f.
$$

So $\mathsf C(g)$ is a compactification of $f$ in the sense of
[def-nagata-compactification], and $f$ is compactifiable
([def-nagata-compactifiable]).
