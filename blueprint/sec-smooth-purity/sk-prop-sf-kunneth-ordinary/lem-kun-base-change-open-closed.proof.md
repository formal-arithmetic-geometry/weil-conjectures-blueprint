+++
kind  = "proof"
of    = "lem-kun-base-change-open-closed"
+++
Fix a geometric point $\bar y$ of $Y$ with image $\bar x=g(\bar y)$. If $x\in U$, the stalk of $g^{-1}j_*F$ at $\bar y$ is
$F_{\bar x}$, the universal property of the pullback in the
cartesian square identifying the inverse images along $g\circ j$
with $F_{\bar x}$; the same holds for $h_*p^{-1}F$. If $x\notin U$, then $X\setminus U$ is an open neighbourhood of $x$ because
$j$ is a closed immersion, and every etale source $W\to X$ with a
lift of $\bar x$ has $W\times_XU$ empty over that component, so
both stalks are zero: $j_*F$ has zero sections over an open
neighbourhood of $x$, and $p^{-1}F$ similarly. The map is an
isomorphism on all stalks, hence an isomorphism by
lem:weil-pbc-geometric-stalk-conservative.
