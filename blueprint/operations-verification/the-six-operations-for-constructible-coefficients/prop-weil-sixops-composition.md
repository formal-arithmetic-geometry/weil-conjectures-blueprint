+++
id = "prop-weil-sixops-composition"
kind = "theorem"
title = "Composition, properness, and recollement"
order = 3967
tags = ["latex:proposition"]
uses = ["def-compact-support-direct-image-detailed", "def-weil-open-closed-recollement", "def-weil-scheme-morphism-properties", "prop-functor-package"]
+++
In the setting of [prop-functor-package], for composable
separated finite-type morphisms $X\xrightarrow{f}Y\xrightarrow{g}Z$ of
finite-type $k$-schemes, $R(g\circ f)_!\xrightarrow{\sim}Rg_!Rf_!$
with the identity compatibility and the associativity pentagon; if
$f$ is proper, $Rf_!\xrightarrow{\sim}Rf_*$; and for a closed
immersion $i:Z\hookrightarrow X$ with open complement $j$, there is
the functorial recollement triangle

$$
R(fj)_!j^*K\longrightarrow Rf_!K\longrightarrow
R(fi)_!i^*K\longrightarrow R(fj)_!j^*K[1].
$$

## Proof

The assertion is item (3) of [prop-functor-package] of the terminal assembly, on exactly the domains stated there.
