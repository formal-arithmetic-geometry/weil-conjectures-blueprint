+++
id = "sk-lem-sf-ctf-generation"
kind = "section"
title = "Finite/open generation of $\\Dctf$"
order = 2345
uses = ["sk-lem-sf-determination", "sk-prop-sf-open-closed-triangle", "sk-thm-sf-ctf-stability"]
+++
*Lemma (sketch).*

On a separated finite-type $k$-scheme, $\Dctf(-,\Lambda)$ is generated as a
thick subcategory by the objects $Rg_*j_!\Lambda_U$, where $U$ is an open
stratum of a stratification, $j:U\hookrightarrow\overline U$ is the open
immersion into its closure and $g:\overline U\to X$ is that closure's finite
map to the ambient scheme.

## Proof

An object of $\Dctf$ has finitely many cohomology sheaves, each
constructible, so its truncation triangles and [sk-lem-sf-determination]
reduce the claim to a single constructible sheaf $F$. Choose a
stratification on which $F$ is lisse. For a stratum $U$ with closure
$\overline U$, the sheaf $F$ sits in an exact sequence with $g_*j_!(F|_U)$ and
a sheaf supported on the complement — the constant open–closed triangle
[sk-prop-sf-open-closed-triangle] in the relevant twisted form — so induction on the
number of strata reduces to $g_*j_!L$ with $L$ lisse on $U$. A lisse $L$ is a
successive extension of the composition factors of its generic stalk, viewed
as a module over the fundamental group of $U$ with coefficients in the finite
ring $\Lambda$; a simple constructible sheaf is $i_*M$ for a closed immersion
of an irreducible closed subset and a simple $\Lambda$-module $M$, obtained by
taking the maximal irreducible closed subset on which the sheaf is nonzero.
Each such factor is a direct summand of $Rg_*j_!\Lambda_U$ for a suitable
finite étale $g$, hence lies in the thick closure. That the generators and
the intermediate objects stay in $\Dctf$ is [sk-thm-sf-ctf-stability].

Uses: `\Cref{lem:sf-determination}`, `\Cref{prop:sf-open-closed-triangle}`, `\Cref{thm:sf-ctf-stability}`
