+++
id = "prop-compactification-coherence-detailed"
kind = "theorem"
title = "Compactification coherence"
order = 1827
tags = ["latex:proposition"]
uses = ["def-weil-compact-support-candidate", "def-weil-compactifications-refinements", "def-weil-extension-by-zero", "def-weil-finite-torsion-constructibility", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-weil-derived-direct-image-composition", "lem-weil-pbc-proper-open-comparison-proetale", "prop-compactification-refinement"]
+++
Let $K_0$ be a field, let $X,Y$ be
finite-type $K_0$-schemes, and let
$f:X\to Y$ be a
separated finite-type
$K_0$-morphism. Fix a prime $\ell$, write $\Ql=\mathbf Q_\ell$, and
require that its image in $K_0$ is invertible. Choose a finite extension
$E/\Ql$, an integer $n\in\mathbf Z_{\geq1}$,
and put $A=A_{E,n}$. The coefficient $A$ is used with the
finite-torsion
constructibility condition. For objects
$c_i=(j_i,\bar f_i)\in\operatorname{Comp}(f)$ in the
compactification category
and a refinement
$u:c_1\to c_2$, the canonical transformation between the
compact-support candidates

$$
R\bar f_{1*,n}j_{1!}
\xrightarrow{\sim}
R\bar f_{2*,n}j_{2!}
$$

is the composite of the proper-composition isomorphism with the isomorphism

$$
Ru_*j_{1!}\xrightarrow{\sim}j_{2!}
$$

on the ambient derived category. These transformations are identities for
identity refinements and are transitive under composition. For any two
compactifications $c_1,c_2$, comparison through a common refinement gives
a natural isomorphism

$$
Rf_{!,n}^{c_1}\xrightarrow{\sim}Rf_{!,n}^{c_2}.
$$

Here $R\bar f_{i*,n}$ and $j_{i!}$ are respectively the
derived direct image and
extension-by-zero functors. A common
refinement may be chosen for any finite collection of
compactifications; the resulting comparison is independent of that choice
and satisfies the cocycle condition for triples of compactifications.
The comparison is asserted on the domain declared in
[def-weil-compact-support-candidate]: the complexes of the pro-etale
site that come from the etale site with an
etale-origin witness.
