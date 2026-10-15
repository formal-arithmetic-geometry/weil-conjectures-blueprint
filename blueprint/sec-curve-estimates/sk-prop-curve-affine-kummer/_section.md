+++
id = "sk-prop-curve-affine-kummer"
kind = "proposition"
title = "Cohomology of a smooth affine curve"
order = 885
uses = ["sk-def-curve", "sk-def-kummer", "sk-def-pic", "sk-thm-curveestimate"]
tags = ["sketch"]
+++
Let $\overline C$ be a smooth proper connected curve of genus $g$ over an
algebraically closed field. Let $U=\overline C\setminus D$, where $D$
consists of $r\geq1$ closed points, and let $n$ be invertible. There is a
natural exact sequence (the *residue sequence*)

$$
0\longrightarrow H^1(\overline C,\mu_n)
\longrightarrow H^1(U,\mu_n)
\xrightarrow{\ \partial\ }(\Z/n)^D
\xrightarrow{\ \sum\ }\Z/n\longrightarrow0.
$$

Moreover $H^0(U,\mu_n)=\mu_n(k)$ and $H^q(U,\mu_n)=0$ for $q>1$. The group
$H^1(U,\mu_n)$ is noncanonically $(\Z/n)^{2g+r-1}$, and the pullback maps on
all these groups are isomorphisms under algebraically closed extension.

