+++
id = "prop-weil-milnor-triangle"
kind = "theorem"
title = "Milnor triangle"
order = 3061
tags = ["latex:proposition"]
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-complete-integral-detailed", "def-weil-pbc-proetale-site", "lem-weil-pbc-mittag-leffler", "prop-weil-pbc-roos-triangle"]
+++
For a strict tower of complexes $C=(C_n)$ in
$\operatorname{Tow}_E(Y)$ of
[def-weil-derived-complete-integral-detailed], there is a functorial
Milnor triangle

$$
R\varprojlim_nC_n\longrightarrow
\prod_{n\geq1}C_n\xrightarrow{1-\mathrm{shift}}
\prod_{n\geq1}C_n\longrightarrow(R\varprojlim_nC_n)[1],
$$

functorial in $C$. (Source: the classical Milnor exact sequence for
derived inverse limits; its Stacks Project form is More on Algebra,
Section 15.88, namely Lemma 15.88.9,
[Tag 07KX](https://stacks.math.columbia.edu/tag/07KX), the
canonical distinguished triangle
$R\varprojlim K\to\prod_nK_n^\bullet\to\prod_nK_n^\bullet\to R\varprojlim K[1]$, and Lemma 15.88.10,
[Tag 07KY](https://stacks.math.columbia.edu/tag/07KY), the
associated short exact sequences
$0\to R^1\varprojlim_nH^{p-1}(K_n^\bullet)\to H^p(R\varprojlim K)\to\varprojlim_nH^p(K_n^\bullet)\to0$.)

## Proof

This is the decomposed form of the classical input of the source note:
the Milnor triangle for derived inverse limits is proved in full in
the ambient-foundations chapter as [prop-weil-pbc-roos-triangle], with the Milnor map
comparison of lem:weil-pbc-mittag-leffler.
