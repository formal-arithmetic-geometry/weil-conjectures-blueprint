+++
kind = "proof"
of = "lemma-identity-component--1"
order = 1133002
uses = ["lemma-stable-subspaces-center", "proposition-lie-algebras-faithful-semisimple-representation", "proposition-cartier-s-theorem", "lemma-connected-components-images-homomorphisms", "definition-monodromy-groups", "lemma-restriction-normal-subgroup", "lemma-normality-geometric-monodromy"]
+++
Put $T=Z(G^\circ)^\circ$ and $\mathfrak g=\operatorname{Lie}(G^\circ)$.
By Lemma [lemma-stable-subspaces-center], the $G^\circ$-stable and
$\mathfrak g$-stable subspaces of $k^n$ agree. Thus $k^n$ is a faithful
semisimple $\mathfrak g$-module, and Proposition
[proposition-lie-algebras-faithful-semisimple-representation] gives

$$
\mathfrak g=Z(\mathfrak g)+[\mathfrak g,\mathfrak g].
$$

The center comparison in Lemma [lemma-stable-subspaces-center] identifies
$Z(\mathfrak g)$ with $\operatorname{Lie}(T)$. For $X,Y\in\mathfrak g$,
the commutator of $1+\varepsilon X$ and $1+\eta Y$ is
$1+\varepsilon\eta[X,Y]$. It lies in $H(R)$ by hypothesis. Restricting
its equations to the subring $k[\varepsilon\eta]\subset R$ shows that
$[X,Y]\in\operatorname{Lie}(H)$. By Proposition
[proposition-cartier-s-theorem], $H$ and $H^\circ$ have the same Lie
algebra. Consequently

$$
\mathfrak g=\operatorname{Lie}(T)+\operatorname{Lie}(H^\circ).
$$

Since $T$ centralizes $H^\circ$, the set $K=T(k)H^\circ(k)$ is a subgroup
of $G^\circ(k)$. Its Zariski closure contains $T$ and $H^\circ$, so its
Lie algebra contains both summands above. It is therefore all of
$G^\circ$, by Lemma [lemma-connected-components-images-homomorphisms](3).

To pass from this closure to $K$ itself, consider the image $Y$ of the
multiplication morphism $T\times H^\circ\to G^\circ$. Chevalley's theorem
makes $Y$ constructible. Its $k$-points are exactly $K$: a nonempty fiber
over a $k$-point has a $k$-point because $k$ is algebraically closed.
The closure of $Y$ is $G^\circ$, so $Y$ contains a dense open subset $U$
of $G^\circ$. For $x\in G^\circ(k)$, irreducibility gives a $k$-point
$z\in U\cap xU^{-1}$. Both $z$ and $z^{-1}x$ lie in $K$, whence
$x=z(z^{-1}x)\in K$. This proves the asserted factorization.

For the monodromy groups of [definition-monodromy-groups], semisimplicity
passes from the Weil representation to $G(k)$ because the stable
subspaces agree, and then to its normal subgroup $G^\circ(k)$ by Lemma
[lemma-restriction-normal-subgroup]. The commutator containment of Lemma
[lemma-normality-geometric-monodromy] holds over every $k$-algebra in
Lean, so it supplies the hypothesis over $R$. The same argument applies
to any semisimple representation of a group with a surjective degree map
to $\mathbf Z$ and a chosen element of degree one, taking $H$ to be the
Zariski closure of the image of the degree-zero subgroup.
