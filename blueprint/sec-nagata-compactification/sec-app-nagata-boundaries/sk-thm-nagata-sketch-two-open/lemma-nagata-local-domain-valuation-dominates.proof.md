+++
kind  = "proof"
of    = "lemma-nagata-local-domain-valuation-dominates"
+++
Consider the set of subrings of $L$ containing $B$ and whose units avoid the
maximal ideal of $B$, ordered by inclusion. The union of a chain has the
same property, so Zorn's lemma gives a maximal such ring $C$. For any
$x\in L^\times$, if neither $x$ nor $x^{-1}$ belonged to $C$, adjoining one
of them and localizing at the complement of the maximal ideal would produce
a strictly larger ring with the same property, contradicting maximality.
Thus $C$ is a valuation ring. Its unique maximal ideal contracts to the
maximal ideal of $B$ because $B$ is local and every element outside that
ideal is a unit in $C$.
