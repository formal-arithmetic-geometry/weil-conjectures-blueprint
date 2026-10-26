+++
id = "def-exc-continuous-cohomology"
kind = "definition"
title = "Discrete modules and continuous group cohomology"
order = 1359
lean = ["Action.IsDiscreteModule", "DiscreteModule", "DiscreteModule.invariants", "DiscreteModule.H"]
uses = ["def-weil-abstract-derived-category"]
+++
Let $G$ be a topological group (in the applications $G$ is profinite).
A *discrete $G$-module* is an abelian group $M$ with an action of $G$
by additive automorphisms such that every element of $M$ has an open
stabilizer. With $G$-equivariant homomorphisms, discrete $G$-modules
form a full subcategory of the category of $G$-representations on
abelian groups; it is an abelian category with enough injectives. Its
invariant functor sends $M$ to
$M^G=\{m:gm=m\text{ for all }g\in G\}$.
The continuous cohomology of $M$ is

$$
H^q(G,M)=\operatorname{Ext}^q(\mathbf Z,M)\qquad(q\geq0),
$$

the Ext groups in this abelian category, computed in its derived
category, from the trivial module $\mathbf Z$; these are the right
derived functors of the invariant functor, and $H^0(G,M)=M^G$.
A discrete $A$-module with continuous $G$-action, for a ring $A$ and a
$G$-action by $A$-linear automorphisms with open stabilizers, is in
particular a discrete $G$-module.
