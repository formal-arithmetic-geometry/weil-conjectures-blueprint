+++
kind = "proof"
of = "lemma-finite-morphisms-cohomology--3"
order = 1594006
uses = ["lemma-finite-morphisms-cohomology--1"]
+++
By [lemma-finite-morphisms-cohomology--1], $h_*$ is exact, and $h^*$
is exact as well. The category of abelian étale sheaves on $Y$ has
enough injectives. The adjunction $h^*\dashv h_*$ therefore induces
a bijection

$$
\Ext^q(\mathbf Z_C,h_*G)
\longrightarrow \Ext^q(h^*\mathbf Z_C,G).
$$

This is `CategoryTheory.Adjunction.mapExtCounit_bijective`. In degree
zero it is the adjunction bijection. In higher degrees its proof
embeds $G$ into an injective sheaf and uses the two long exact
$\Ext$ sequences and induction; exactness of $h_*$ and preservation
of injectives give the required comparison.

The canonical isomorphism $h^*\mathbf Z_C\simeq\mathbf Z_Y$ gives a
second bijection by precomposition. The composite is the displayed
pullback followed by the counit, by
`AlgebraicGeometry.Etale.map_counit_cohomologyMap`. Hence the edge
map is bijective.
