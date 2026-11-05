+++
kind = "proof"
of = "proposition-compactifying-union-two-opens--1"
order = 1458002
uses = ["lemma-schematic-closure-uniqueness", "definition-admissible-blow-up", "lemma-gluing-after-admissible-blow-ups", "lemma-extending-graph-from-compactification", "lemma-separation-closures", "lemma-extending-isomorphism-over-closure-closed", "definition-strict-transform"]
+++
The copy of $M_i$ is dense in $X_i\setminus B_{i,j}$, so the copy
of $M$ is dense in $W_i$. Density is preserved by the common
modification, by [lemma-gluing-after-admissible-blow-ups]. Since $D$
is dense in $M$, the composite $D\to M\to W$ is dominant. This is
`AlgebraicGeometry.TwoOpenPreparation.FinalModification.isDominant`.
Moreover, $M$ and its open $D$ are Noetherian, so $D\to W$ is
quasi-compact.

Let $R$ be a valuation ring with fraction field $K$, and consider
an $S$-map $\operatorname{Spec}(K)\to D$ over a given map
$\operatorname{Spec}(R)\to S$. Properness of the $X_i$ gives extensions
$g_i:\operatorname{Spec}(R)\to X_i$. The pair $(g_1,g_2)$ factors
through $X_{12}$: it does so on $\operatorname{Spec}(K)$, and a map
from the spectrum of a domain that factors generically through a
closed subscheme factors through that closed subscheme. The assumed
disjointness shows that at least one $g_i$ sends the closed point
outside $B_{i,j}$. An open of a local scheme containing its closed
point is the whole scheme, so this $g_i$ factors through
$X_i\setminus B_{i,j}$ and hence through $W_i$. These are the steps
of `AlgebraicGeometry.TwoOpenSide.exists_comparisonFst_comparisonSnd`
and `AlgebraicGeometry.TwoOpenSide.KeyDisjoint.avoids`.

The generic point already lifts to the copy of $M$ in $W_i'$.
Properness of the admissible blow-up $W_i'\to W_i$ therefore gives a
lift of $\operatorname{Spec}(R)$ to $W_i'$, and then to $W$.
Separatedness of $W\to S$ makes this lift unique. Thus the valuative
criterion holds relative to $D\to W$, as expressed by
`AlgebraicGeometry.TwoOpenPreparation.FinalModification.valuativeCriterion_relativeTo`.
Apply the dense-source valuative criterion
`AlgebraicGeometry.UniversallyClosed.of_valuativeCriterion_of_isDominant`
to the quasi-compact dominant map $D\to W$. It follows that $W\to S$
is universally closed. It is already separated and of finite type,
so it is proper. The common modification supplies the open immersion
$M\to W$ over $S$, giving the asserted compactification.

To obtain the data of this proposition from two compactifiable opens
covering a separated $M$, Lean first chooses dense compactifications,
extends their graphs by [lemma-extending-graph-from-compactification],
and separates the boundary closures by [lemma-separation-closures].
It improves the first comparison projection using
[lemma-extending-isomorphism-over-closure-closed]. The new comparison
space embeds as a closed subscheme of the strict transform of the old
one; injectivity near the boundary and density give the required
disjointness. This is the construction in
`AlgebraicGeometry.nonempty_twoOpenPreparation`.

For separatedness of $W_i$, let $X_i^\circ=X_i\setminus B_{i,j}$.
The graph of $\psi_i$ in $M\times_S X_i$ is proper, and the image
of the overlap $M_i\to M\times_S X_i^\circ$ is exactly the inverse
image of that closed graph. Indeed, a graph point outside $B_{i,j}$
must lie above $M_i$, where $\psi_i$ is the specified isomorphism.
The overlap is an immersion with closed image, hence a closed
immersion. This is
`AlgebraicGeometry.TwoOpenSide.isClosedImmersion_intermediateGraph`.
The two separated charts therefore glue to a separated $W_i$.
They also show that $W_i$ is of finite type and Noetherian, so
[lemma-gluing-after-admissible-blow-ups] supplies the common
modification used above. This is
`AlgebraicGeometry.TwoOpenPreparation.nonempty_finalModification`.
