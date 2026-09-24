+++
id = "lem-weil-pbc-constructible-finite-pushforward"
kind = "lemma"
title = "Embedding a constructible sheaf in finite pushforwards"
order = 1748
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-constructible-finite-pushforward-approximation"]
+++
If $U$ is quasi-compact and quasi-separated and $C$ is constructible torsion
on $U_{\Et}$, there is a monomorphism

$$
 C\hookrightarrow\bigoplus_{i=1}^m(h_i)_*\underline{M_i},
$$

where every $h_i:V_i\to U$ is finite and finitely presented and every $M_i$ is
a finite abelian group.

## Proof

Apply [lem-weil-pbc-constructible-finite-pushforward-approximation] to $U$ and
$C$. The finite maps obtained there are finite over the Noetherian
approximation and therefore of finite presentation; their pullbacks remain
finite and finitely presented. Exactness of inverse image and
finite-base-change compatibility of direct image preserve the monomorphism,
giving the displayed map on $U$. This is precisely the descent argument in
Stacks Project, Lemma 59.74.4 (Tag
[09Z7](https://stacks.math.columbia.edu/tag/09Z7)); no composition with a
locally closed stratum is used.
