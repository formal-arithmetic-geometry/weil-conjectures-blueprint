+++
id = "sk-cor-picard-degree-g"
kind = "section"
title = "The degree of the dictionary"
order = 750
+++
*Corollary (sketch).*

Let $X$ be a smooth projective curve of genus $g$ and $\cL$ a line
bundle on $X_K$ ($K/k$ any field extension) with $h^0(X_K,\cL)=1$
and $H^q(X_K,\cL)=0$ for $q>0$. Then

$$
\deg(\cL)=\chi(\cL)-\chi(\cO_{X_K})=1-(1-g)=g.
$$

This is the exact instance of Riemann–Roch used in the
zero-scheme dictionary ([sk-lem-picard-zero-dictionary]).

## Proof

The vanishing gives $\chi=h^0=1$, and [sk-thm-picard-rr] (RR) gives
$\chi(\cO_{X_K})=1-g$ and $\chi(\cL)=\deg\cL+\chi(\cO_{X_K})$;
hence $\deg\cL=g$.
