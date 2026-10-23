+++
kind = "proof"
of = "lem-weil-pbc-dense-open-component-modifications"
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let Z_i be the image of the component inclusion. The complement W_i of all other components is open, lies in Z_i, and contains its generic point. Finiteness makes the excluded union closed; maximality of irreducible components ensures the generic point is not on another component. The integral component has a generic point by sobriety of schemes.

Restrict the closed immersion to W_i. It is surjective into a reduced open subscheme, hence an isomorphism: locally Spec(A/I) maps onto Spec A, so I lies in the nilradical, zero because A is reduced. Intersect the dense open of the component with the preimage of W_i and transfer it through this isomorphism. This gives an open V_i of X containing the component generic point. Their union U is dense, since closure contains every component; injectivity of the image enumeration makes the V_i disjoint.

Over V_i every summand other than i has empty preimage; the i-th map is an isomorphism by restriction of the given isomorphism over its dense open and the preceding identification of the component inclusion. Thus the coproduct map restricts to an isomorphism over each V_i. The inverses glue on this open cover of U. For n=0 the covering hypothesis and the union of irreducible components imply X is empty; use U empty. ([def-weil-pbc-scheme-conventions]).
