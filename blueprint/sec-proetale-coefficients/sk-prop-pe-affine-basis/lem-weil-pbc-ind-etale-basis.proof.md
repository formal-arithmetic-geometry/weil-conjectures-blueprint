+++
kind  = "proof"
of    = "lem-weil-pbc-ind-etale-basis"
+++
Cover $X$ by affine opens $X_0$, and an object over $X_0$ by affine opens.
On each of them apply the ind-etale refinement theorem over the affine base
$X_0$. Its faithfully flat affine refinement is a covering in the small
pro-etale site; it is a limit of affine schemes etale over $X_0$, hence over
$X$, so it belongs to [def-weil-pbc-ind-etale-basis]. For a covering of an
affine basis object, the definition of a pro-etale covering first selects
finitely many affine pieces of its members, whose images cover the object.
Apply the same refinement theorem over that basis object to these pieces.
Their composites with $X$ are again pro-etale affine, by the stability lemma
for ind-etale algebras. The relative-map and base-change assertions of that
lemma prove stability under the required fibre products.

For completeness, the extension of a sheaf on this basis is explicit: a
section on an arbitrary object is a compatible family of sections on a basis
covering, with equality imposed on basis coverings of the pairwise
intersections. Two choices are compared on a common refinement, which exists
by the preceding covering and fibre-product assertions. The basis sheaf axiom
makes this comparison independent of refinements and permits gluing. This
constructs a sheaf on the full site inverse to restriction, on objects and
morphisms. It also proves the asserted detection of isomorphisms.
