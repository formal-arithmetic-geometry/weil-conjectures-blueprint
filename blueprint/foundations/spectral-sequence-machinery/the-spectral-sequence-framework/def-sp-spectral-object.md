+++
id = "def-sp-spectral-object"
kind = "definition"
title = "Spectral objects"
order = 1128
uses = ["def-sp-abelian"]
+++
Let $\iota$ be a small category and $\mathcal C$ an abelian category
[def-sp-abelian]. A *spectral object* $X$ indexed by $\iota$ consists of
functors

$$
 H_n:\{\text{composable arrows }f:i\to j\text{ in }\iota\}\to\mathcal C
 \qquad(n\in\mathbb Z)
$$

and connecting maps $\delta_n(f,g):H_n(g)\to H_{n+1}(f)$ for every composable
pair $f:i\to j$, $g:j\to k$, such that for every such pair the sequence

$$
 H_n(f)\longrightarrow H_n(fg)\longrightarrow H_n(g)
 \xrightarrow{\ \delta_n(f,g)\ }H_{n+1}(f)
$$

is exact, the first arrow being $H_n$ of the map $f$ and the second $H_n$ of
the map $g$, and such that the connecting maps are natural in the pair
$(f,g)$. With the shifts this is a functorial long exact sequence for each
composable pair; this is Verdier's spectral object, which packages exact
couple data indexed by composable arrows (*reference: Verdier, Des categories
derivees des categories abeliennes, II.4; Stacks Project, Derived Categories,
Section 13.23*). The typing of the connecting map is that of the reference:
the source is $H_n$ of the *second* arrow of the pair and the target
$H_{n+1}$ of the *first*.
