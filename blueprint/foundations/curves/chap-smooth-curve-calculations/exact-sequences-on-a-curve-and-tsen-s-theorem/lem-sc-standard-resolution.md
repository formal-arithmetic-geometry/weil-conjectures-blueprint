+++
id = "lem-sc-standard-resolution"
kind = "lemma"
title = "The standard resolution of constructible sheaves on curves"
order = 2179
uses = ["def-sc-curves", "def-weil-pbc-etale-sheaves", "lem-sc-dim0-finite"]
+++
Let $C$ be a smooth curve over an
algebraically closed field $k$ and let $F$ be a constructible
torsion etale sheaf on $C_{\Et}$
([def-weil-pbc-etale-sheaves]). There is a dense open
$U\subseteq C$ such that $F|_U$ is locally constant, and an exact
sequence

$$
0\longrightarrow j_!\,(F|_U)\longrightarrow F\longrightarrow i_*i^*F\longrightarrow0,
$$

where $j:U\hookrightarrow C$ and $i:C\setminus U\hookrightarrow C$
are the inclusions and $C\setminus U$ is a finite set of closed
points. Consequently every constructible torsion sheaf on $C$ has
a finite filtration whose successive quotients are of the form
$j_!L$, with $L$ locally constant on a dense open
$j:U\hookrightarrow C$, or $i_*M$, with $i$ the inclusion of a
point.

## Proof

By the definition of constructibility, $C$ admits a finite
stratification into locally closed pieces on which $F$ is locally
constant; the union of the dense pieces gives a dense open $U$
with $F|_U$ locally constant, and the complement of a dense open
in the curve $C$ is a finite set of closed points
([lem-sc-dim0-finite]). The exact sequence is the standard
one: the adjunction map $j_!j^*F\to F$ is injective (it is an
isomorphism on $U$, since $j^*j_!=\mathrm{id}$), and its
cokernel is supported on the closed set $C\setminus U$, hence
equals $i_*i^*(F/j_!j^*F)=i_*i^*F$ (for a sheaf $\mathcal G$
supported on a closed set $Z$, the natural map
$\mathcal G\to i_*i^*\mathcal G$ is an isomorphism). Iterating
(this time applied to $i_*i^*F$, a finite direct sum of
skyscraper sheaves, and to the locally constant $F|_U$, to which
the same procedure applies on $U$) gives the finite filtration.
