+++
id = "lem-sc-abelian-variety-characterization"
kind = "lemma"
title = "Abelian varieties are the complete group varieties"
lean = ["AlgebraicGeometry.IsAbelianVariety.geometricallyIntegral", "AlgebraicGeometry.IsAbelianVariety.irreducibleSpace"]
order = 472
uses = ["def-sc-abelian-variety", "def-sc-group-scheme"]
+++
Let $k$ be a field and $A$ a
group scheme over $k$ which is
proper, connected and smooth over $k$ (a *complete group
variety*). Then $A$ is irreducible and geometrically integral.
Consequently an *abelian variety* in the sense of
[def-sc-abelian-variety] is exactly a complete group variety.

The smoothness hypothesis cannot be dropped: for
$\operatorname{char}k=p>0$ the finite group schemes

$$
\alpha_p=\Spec k[x]/(x^p),\qquad
\mu_p=\Spec k[x]/(x^p-1)
$$

are proper and connected but not reduced, hence not smooth, over $k$.

## Proof

This is the recorded classical input of the statement, Stacks Project,
Groupoid Schemes, Definition 39.9.1
([Tag 03RO](https://stacks.math.columbia.edu/tag/03RO)) with Remark
39.9.12 ([Tag 0H2U](https://stacks.math.columbia.edu/tag/0H2U)),
Lemma 39.7.10 ([Tag 0B7Q](https://stacks.math.columbia.edu/tag/0B7Q))
and Lemma 39.9.4 ([Tag
0BFC](https://stacks.math.columbia.edu/tag/0BFC)). The argument is the standard one: $A$ is connected and locally
irreducible (being smooth), and a connected locally irreducible scheme is irreducible, the identity
component of a group scheme of finite type over a field is geometrically
irreducible, and a smooth $k$-scheme is geometrically reduced, hence
geometrically integral when connected and irreducible; since $A$ is
connected it is its own identity component. The blueprint uses
the equivalence as the bridge between [def-sc-abelian-variety] and
the classical notion of a complete group variety, so it is recorded here
rather than reproved.
