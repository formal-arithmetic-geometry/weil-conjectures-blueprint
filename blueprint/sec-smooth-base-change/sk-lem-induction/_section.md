+++
id = "sk-lem-induction"
kind = "section"
title = "The induction step in relative dimension one"
order = 1414
uses = ["sk-def-bc", "sk-lem-universal-datum", "sk-thm-vanishing"]
lean = ["AlgebraicGeometry.Etale.BaseChangeProperty.of_sub_one"]
+++
*Lemma (sketch).*

Let $f:X\to S$ be affine smooth of relative dimension one with $X$
affine and $n$ invertible on $S$. If $\mathrm{BC}(f,n,q-1)$ holds
for some $q\ge1$, then $\mathrm{BC}(f,n,q)$ holds.

## Proof

*Contradiction.* Suppose $\mathrm{BC}(f,n,q)$ fails. By
[sk-lem-universal-datum] there is a universal curve-test datum with
$R^qh_*(\Z/d\Z)\neq0$ for some $d\mid n$ (after base change and
normalization: $d$ is invertible on the new base because $n$ is
invertible on $S$ and on all its base changes). But
[sk-thm-vanishing] applies to that datum and gives
$R^qh_*(\Z/d\Z)=0$. Contradiction.

Uses: [sk-def-bc], [sk-lem-universal-datum], [sk-thm-vanishing]
