+++
id = "thm-pur-with-support-exactness"
kind = "theorem"
title = "Long exact sequence for cohomology with support"
order = 2928
uses = ["def-pur-support-cohomology", "def-weil-open-closed-recollement", "def-weil-pbc-derived-categories", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions", "thm-weil-pbc-site-comparison"]
+++
Let $X$ be a scheme, let
$i:Z\hookrightarrow X$ be a closed subscheme with open complement
$j:U\hookrightarrow X$, and let $F$ be a
torsion etale sheaf on the
small etale site of $X$. In the
notation of [def-pur-support-cohomology], there is a long exact
sequence

$$
\cdots\longrightarrow H^q_Z(X,F)\longrightarrow H^q(X,F)
\longrightarrow H^q(U,F)\longrightarrow H^{q+1}_Z(X,F)\longrightarrow\cdots,
$$

functorial in the pair $(X,X\setminus Z)$ and in $F$. The same
statement holds for bounded-below complexes with torsion cohomology in the
derived category of [def-weil-pbc-derived-categories], and on the
pro-etale site of $X$ for finite-torsion coefficients, by the comparison
[thm-weil-pbc-site-comparison].
