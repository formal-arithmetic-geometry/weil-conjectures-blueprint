+++
id = "prop-compactification-coherence"
kind = "theorem"
title = "Compactification coherence"
order = 46
tags = ["latex:proposition"]
uses = ["def-compact-support-candidate", "def-finite-derived-extension-by-zero", "def-weil-finite-coefficient-datum", "prop-compactification-refinement", "prop-finite-extension-by-zero-properties", "prop-finite-proper-base-change"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, a separated finite-type morphism
$f:X\to Y$, and $n\geq1$. For every refinement
$u:c_1\to c_2$ in $\operatorname{Comp}(f)$ and every
$K\in D^b_c(X,\mathcal O_E/\varpi_E^n)$, the canonical map

$$
R\bar f_{1*,n}j_{1!,n}K
\xrightarrow{\sim}
R\bar f_{2*,n}j_{2!,n}K
$$

is the composite of the proper-composition isomorphism with the isomorphism

$$
Ru_{*,n}j_{1!,n}K\xrightarrow{\sim}j_{2!,n}K.
$$

The latter isomorphism is in
$D^b_c(\overline X_2,\mathcal O_E/\varpi_E^n)$ and is checked after
pullback to every geometric point: proper base change
(Proposition [prop-finite-proper-base-change]) identifies its stalk with
the cohomology of the proper geometric fiber, and the sectionwise
description of $j_{!,n}$ makes that fiber the identity over $X$ and zero
over its complement. These transformations are identities for
identity refinements and are transitive under composition. For any two
compactifications $c_1,c_2$, comparison through a common refinement gives
a natural isomorphism

$$
Rf_{!,n}^{c_1}|_{D^b_c}
\xrightarrow{\sim}Rf_{!,n}^{c_2}|_{D^b_c}.
$$

It is independent of the common refinement and satisfies the cocycle
condition for triples of compactifications.
