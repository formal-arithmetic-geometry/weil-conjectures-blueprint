+++
kind = "proof"
of = "lemma-connected-components-images-homomorphisms--1"
order = 1720005
uses = []
+++
The underlying space of $G$ is Noetherian. It has finitely many
irreducible components, each contained in a connected component, so
there are finitely many connected components. Each is closed, and
its complement is a finite union of closed components; thus it is
also open.

Take $G^\circ$ to be the open subscheme on the component of $1$.
It is geometrically connected, since it is connected and has the
rational point $1$. The fibres of $X\times G^\circ\to X$ are
therefore connected. If a morphism from this product maps the slice
$X\times\{1\}$ into an open and closed subset, it maps the whole
product into that subset. Applying this to multiplication and to
conjugation shows that they take values in $G^\circ$; inversion
does so by connectedness and preservation of $1$. The operations
lift to $G^\circ$, and their identities follow by composing with
the monomorphism $G^\circ\to G$. This gives the subgroup structure
and normality.

For irreducibility, Lean uses the fact that a connected group scheme
locally of finite type over any field is irreducible. Over an
algebraically closed field, a Noetherian affine open contains a closed
point lying on a single irreducible component. Translations carry this
property to every closed point. Specialization to closed points then
gives the same property at every point. Each point has an irreducible
open neighbourhood, so connectedness implies irreducibility. Over a
general field, the identity section gives geometric connectedness;
base change to an algebraic closure and descend irreducibility along
the surjective projection. Apply this to $G^\circ$.

Finally, translation by $g$ is an isomorphism, so its homeomorphism
carries the component of $1$ onto the component of $g$. Over an
algebraically closed field each component contains a closed, hence
rational, point. Choosing one in each component gives the asserted
cosets, as in `AlgebraicGeometry.GrpObj.range_identityComponentTranslate`.
The main theorem uses these component results; the normality result
is present in the source but is not needed on its dependency path.
