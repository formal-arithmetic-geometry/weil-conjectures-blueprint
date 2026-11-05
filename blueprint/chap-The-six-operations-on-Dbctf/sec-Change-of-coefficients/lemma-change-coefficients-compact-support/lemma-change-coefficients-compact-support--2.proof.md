+++
kind = "proof"
of = "lemma-change-coefficients-compact-support--2"
order = 637004
uses = ["definition-change-of-coefficients-maps", "proposition-construction-independence-rf-shriek", "lemma-schematic-closure-uniqueness", "proposition-dense-compactifications-form-cofiltered-category"]
+++
First consider a refinement $h:Z\to Z_1$ with $hj=j_1$.
The restriction comparison $j_!\to h^*j_{1!}$ is obtained by adjunction
from the pullback composition isomorphism. Compatibility of the
pullback comparisons with composition, and compatibility with
$j_!\dashv j^*$, show that this restriction comparison commutes with
the coefficient comparisons. For a proper cartesian refinement it is
invertible. Compose its inverse with the unit of $h^*\dashv Rh_*$ to
obtain compatibility of $j_{1!}\to Rh_*j_!$.

The direct-image composition isomorphism $Rp_{1*}Rh_*\simeq R(p_1h)_*$
is the adjoint of the pullback composition isomorphism. It therefore
also commutes with the coefficient comparisons. Whiskering the
preceding refinement comparison by $Rp_{1*}$ and composing with this
isomorphism proves compatibility for the refinement isomorphisms of
Proposition [proposition-construction-independence-rf-shriek].

Choose a common refinement of $c_1$ and $c_2$. Compose compatibility
for its map to $c_1$ with the inverse of compatibility for its map to
$c_2$. This is precisely the asserted identity for the independence
isomorphisms.
