+++
id = "def-kun-bc-property"
kind = "definition"
title = "The base-change property $BC(f,n,q_0)$"
order = 2008
uses = ["def-kun-cd", "def-kun-unbounded-exchange", "def-weil-pbc-scheme-conventions", "sbc-def-base-change-map", "sbc-def-base-change-property"]
+++
Let $f:X\to S$ be a morphism of schemes, $n\ge1$, and
$q_0\ge0$. Say *$BC(f,n,q_0)$ holds* if for every
commutative diagram

$$
\begin{array}{ccccc}
X&\longleftarrow&X'&\longleftarrow&Y\\
\Big\downarrow{\scriptstyle f}&&\Big\downarrow{\scriptstyle f'}&\Big\downarrow{\scriptstyle e}\\
S&\longleftarrow&S'&\longleftarrow&T
\end{array}
$$

with $X'=X\times_SS'$, $Y=X'\times_{S'}T$, $g:T\to S'$
quasi-compact and
quasi-separated, $X'\to T$ (resp. $h:Y\to X'$) the resulting
projection, $\Lambda=\kunZn$ coefficients, and every abelian sheaf
$F$ on $T_{\Et}$ annihilated by $n$, the exchange morphism of
[def-kun-unbounded-exchange] is an
isomorphism on $q$-th cohomology sheaves for all $q\le q_0$. Here $n$ is not required to be invertible on $S$.
