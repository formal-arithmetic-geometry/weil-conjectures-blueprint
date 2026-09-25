+++
id = "lem-sc-av-commutative"
kind = "lemma"
title = "Abelian varieties are commutative"
order = 495
uses = ["def-sc-abelian-variety", "lem-sc-rigidity"]
+++
Let $A$ be an abelian variety
over a field $k$. Then $A$ is commutative: the multiplication
satisfies $m\circ s=m$, where $s$ swaps the factors. In
particular $A(k)$ is an abelian group for every field $k$.

## Proof

The commutator map $c:A\times A\to A$,
$(x,y)\mapsto xyx^{-1}y^{-1}$, satisfies
$c(A\times\{e\})=\{e\}$; by the rigidity lemma
([lem-sc-rigidity]) applied with $X=A$, $Y=A$,
$y_0=e$, $Z=A$, it factors through the second projection, so
$c(x,y)=c(e,y)=e$ for all $x,y$, i.e. $A$ is commutative.
(An alternative reference: Stacks Project, Groupoid Schemes, Lemma
39.9.5, [Tag 0BFD](https://stacks.math.columbia.edu/tag/0BFD), whose proof replaces the rigidity lemma by More on
Morphisms, Lemma 37.44.3, [Tag 0AH8](https://stacks.math.columbia.edu/tag/0AH8).)
