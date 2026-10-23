+++
kind  = "proof"
of    = "det-def-localizing-closure-existence"
+++
(1) The category of $\Lambda_X$-modules is Grothendieck abelian
([det-prop-sfb-module-category]), so direct sums exist and are exact. In the homotopy
category $K(\Lambda_X)$ the termwise direct sum of complexes is the coproduct, and the
termwise direct sum of mapping-cone triangles is the mapping-cone triangle of the direct
sum. By exactness of direct sums, the acyclic complexes form a localizing subcategory of
$K(\Lambda_X)$; for a Verdier quotient by a subcategory closed under coproducts, the quotient
functor preserves coproducts (Neeman, *Triangulated categories*, Lemma 3.2.10). So
$D(X_{\mathrm{proét}},\Lambda)$ has direct sums, computed termwise; in particular direct sums of
distinguished triangles are distinguished, which is used in (2).

(2) Each condition (containing $0$ and $\mathcal S$, closure under isomorphisms, under shifts
in both directions, under cones of morphisms between members, and under direct sums of
families of members) is preserved by arbitrary intersections. The whole category is one
such subcategory, so the intersection is over a non-empty collection.

(3) Eilenberg swindle: let $K=K_1\oplus K_2\in\Loc(\mathcal S)$ and
$K^{(\mathbf N)}=\bigoplus_{\mathbf N}K\in\Loc(\mathcal S)$. Regrouping summands gives
$K_1\oplus K^{(\mathbf N)}=K_1\oplus(K_2\oplus K_1)^{(\mathbf N)}\cong(K_1\oplus K_2)^{(\mathbf N)}=K^{(\mathbf N)}$.
The split triangle $K^{(\mathbf N)}\to K_1\oplus K^{(\mathbf N)}\to K_1\xrightarrow{0}K^{(\mathbf N)}[1]$
exhibits $K_1$ as a cone of a morphism between members, so $K_1\in\Loc(\mathcal S)$. For the
last assertion: $\Loc(\mathcal S')$ is localizing and contains $\mathcal S$, so it contains
$\Loc(\mathcal S)$; conversely $\Loc(\mathcal S)$ is localizing and contains $\mathcal S'$.
