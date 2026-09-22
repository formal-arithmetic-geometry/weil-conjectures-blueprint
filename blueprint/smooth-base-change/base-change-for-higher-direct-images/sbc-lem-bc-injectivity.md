+++
id = "sbc-lem-bc-injectivity"
kind = "lemma"
title = "Injectivity of the critical map and its cokernel"
order = 5126
lean = ["AlgebraicGeometry.baseChangeMap_injective_of_lower_degree"]
uses = ["sbc-def-base-change-map", "sbc-def-base-change-property"]
+++
With $f:X\to S$ and $n$ as in [sbc-def-base-change-property], assume for
some $q\geq1$ that $\mathrm{BC}(f,n,q-1)$ holds. Then for every such
diagram, every abelian sheaf $\mathcal F$ on $T_{\Et}$ annihilated by $n$
and every $q$:

1. the base-change map
   $f'^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ is injective;
2. if $\mathcal F\subset\mathcal G$ with $\mathcal G$ annihilated by $n$,
   then
   $$
   \operatorname{Coker}\bigl(f'^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F\bigr)
   \subset\operatorname{Coker}\bigl(f'^{-1}R^qg_*\mathcal G\to R^qh_*e^{-1}\mathcal G\bigr);
   $$
3. if in (2) the sheaf $\mathcal G$ is an injective sheaf of
   $\mathbf Z/n\mathbf Z$-modules, then
   $$
   \operatorname{Coker}\bigl(f'^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F\bigr)
   \subset R^qh_*e^{-1}\mathcal G.
   $$

(*Stacks Project, Lemma 59.88.2, [Tag
0F03](https://stacks.math.columbia.edu/tag/0F03).*)

## Proof

Choose a short exact sequence
$0\to\mathcal F\to\mathcal I\to\mathcal Q\to0$ with $\mathcal I$ an
injective sheaf of $\mathbf Z/n\mathbf Z$-modules on $T_{\Et}$. The
injective-acyclicity input gives $R^qg_*\mathcal I=0$ for $q>0$, so the two
long exact sequences of higher direct images (the distinguished triangle of
the short exact sequence) and the naturality of the base-change maps of
[sbc-def-base-change-map] give the diagram with exact rows of the statement.

In that diagram the left two vertical arrows are isomorphisms by
$\mathrm{BC}(f,n,q-1)$ and the top right entry is zero, hence the middle
vertical arrow is injective, which is (1); the same diagram gives the
inclusion of the cokernel into $R^qh_*e^{-1}\mathcal I$, which is (3); and
for (2), with $\mathcal F\subset\mathcal G\subset\mathcal I$, the same
diagram applied to $\mathcal F\subset\mathcal G$ gives the inclusion of the
cokernels.

Unresolved dependencies: lem:weil-pbc-leray-acyclicity, def:weil-pbc-inverse-image, def:weil-pbc-direct-image, def:weil-pbc-derived-categories, lem:weil-pbc-five-lemma-transfer
