+++
kind = "proof"
of = "lem-weil-pbc-finite-etale-graph-base-change"
+++
*The product square.* Given $a:T\to P$ and $b:T\to U_0$ with $r\circ a=t\circ b$, the $V$-component of $a$ and the $Y_0$-component of $b$ define a morphism $T\to V_0$, and together with $b$ a morphism $T\to P_0$; the projection identities show that it is compatible with $a$ and $b$. Uniqueness follows by checking components on the fibre products $P_0$ and $V_0$. Hence $(j,r_0,r,t)$ is cartesian.

*The graph square.* Let $s=(a,\mathrm{id}_U):U\to P$ and $s_0=(a_0,\mathrm{id}_{U_0}):U_0\to P_0$ be the graph sections. Comparing the two product projections gives $j\circ s_0=s\circ t$. Pasting this square with the cartesian product square gives the outer square with identities as horizontal maps, which is cartesian; by cancellation the graph square is cartesian.

*Images.* Since $q$ is etale and separated, the section $s$ of the etale projection $r$ is an open immersion. The base change of an open immersion along $j$ is the open subscheme $j^{-1}(s(U))$ of $P_0$, and by the graph square this base change is $s_0$ up to isomorphism. Hence the image of $s_0$ equals $j^{-1}$ of the image of $s$.
