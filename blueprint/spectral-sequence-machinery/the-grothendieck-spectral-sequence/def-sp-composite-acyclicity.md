+++
id = "def-sp-composite-acyclicity"
kind = "definition"
title = "Composable pairs with an acyclicity condition"
order = 1736
lean = ["CategoryTheory.ComposablePair", "CategoryTheory.ComposablePair.SendsInjectivesToAcyclics"]
uses = ["def-sp-left-exact-additive", "def-sp-grothendieck-abelian", "def-sp-acyclic", "def-sp-injective-resolutions"]
+++
A *composable pair* $(F,G)$ consists of left exact additive
[def-sp-left-exact-additive] functors

$$
 \mathcal A\xrightarrow{\ F\ }\mathcal B\xrightarrow{\ G\ }\mathcal C
$$

between Grothendieck abelian categories
[def-sp-grothendieck-abelian]. $F$ *sends injectives to $G$-acyclics* if
$F(I)$ is $G$-acyclic [def-sp-acyclic] for every injective
[def-sp-injective-resolutions] object $I\in\mathcal A$.
