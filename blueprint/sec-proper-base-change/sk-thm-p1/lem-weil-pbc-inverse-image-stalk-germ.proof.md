+++
kind = "proof"
of = "lem-weil-pbc-inverse-image-stalk-germ"
uses = ["def-weil-pbc-geometric-stalks", "def-weil-pbc-inverse-image", "lemma-openclosed-stalk-upperstar"]
+++
Choose c = AlgebraicGeometry.Etale.upperStarCompSheafFiberIso AddCommGrpCat f y [lemma-openclosed-stalk-upperstar]. It is already a natural isomorphism in G. Its definition is the composite of the constructed/abstract pullback comparison, the inverse of Point.sheafFiberComapIso, and Point.sheafFiberIso for pointSmallEtaleComapIso f y. This uses the general-site route explicitly cited by Stacks 03Q1 (3), via Sites 05V1.

For G, U and a lift ū, compose the desired equality with c.inv. Expand the three factors of c.inv. Point.toPresheafFiber_sheafFiberIso_inv_app transports the germ to the lift (pointSmallEtaleFiberEtaleIso f y).inv.app U ū. Point.toPresheafFiber_sheafFiberComapIso_hom_app then rewrites it as the unit of the abstract sheaf pullback followed by the germ at that lift and the stalk of the abstract/constructed pullback comparison. These two rewrite lemmas are proved in WeilConjectures.Mathlib.CategoryTheory.Sites.Point.Category and .Comap, respectively; they describe the factors of the isomorphism in the preceding step. ([lemma-openclosed-stalk-upperstar], [def-weil-pbc-geometric-stalks]).

Use Point.toPresheafFiber_naturality to move the pullback comparison before the germ. Adjunction.unit_leftAdjointUniq_hom_app, evaluated on U, identifies the abstract unit followed by that comparison with the unit of Etale.upperStarLowerStarAdjunction [def-weil-pbc-inverse-image]. This proves the required germ equality by associativity. The transported lift agrees definitionally with the lift in the statement. No extra hypothesis on f or on G is used. ([def-weil-pbc-geometric-stalks]).
