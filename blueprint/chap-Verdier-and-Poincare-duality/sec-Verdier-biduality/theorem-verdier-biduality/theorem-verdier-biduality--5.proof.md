+++
kind = "proof"
of = "theorem-verdier-biduality--5"
order = 844012
uses = ["lemma-verdier-duality-preserves-constructibility"]
+++
The derived internal Hom into a fixed object commutes with shifts and is triangulated on the opposite derived category. Lean proves this as `DerivedCategory.exists_commShift_isTriangulated_bifunctorRHom`, using the hom-complex functor on K-injective representatives. Apply it to the internal Hom bifunctor of Weil sheaves and $\omega_X$. Since the resulting objects are again Weil complexes, restrict to the full triangulated subcategory. The inclusion transports the shift compatibility and detects distinguished triangles; this is the final use of `CategoryTheory.ObjectProperty.isTriangulated_lift`.
