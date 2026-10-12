+++
kind = "proof"
of = "lem-weil-pbc-constant-pullback-unit-continuous-map"
uses = ["lemma-constructible-pullback-constant"]
+++
Use the already proved continuous-map model of the constant abelian sheaf in WeilConjectures.Mathlib.AlgebraicGeometry.Sites.ConstantSheaf (constantSheafIsoContinuousMapSheaf and toSheafify_constantSheafToContinuousMapSheaf). Define κ on g by precomposing its continuous-map representative with pr1. It is additive by pointwise addition. Naturality follows from the base-change square, Hom.etale_map_left_comp_fst.

Compose the constant-sheaf adjunction on Y with i^* ⊣ i_* and the terminal-object comparison for pushforward. The constant-sheaf comparison is the uniqueness isomorphism between this adjunction and the constant-sheaf adjunction on Y₀. Mathlib Adjunction.homEquiv_leftAdjointUniq_hom_app and homEquiv_naturality_right identify the adjunct of c followed by the continuous-map comparison with the adjunct of the continuous-map comparison on Y₀. ([lemma-constructible-pullback-constant]).

The adjunct of κ, followed by the terminal-object comparison, sends m to the constant function m, because toSheafify_constantSheafToContinuousMapSheaf sends the presheaf unit to the constant function. The same holds on Y₀, and restrictions preserve constant functions, including on empty objects. Equality follows by evaluation at m and at a point of the terminal scheme. Cancel the terminal comparison isomorphism and use injectivity of the constant-sheaf adjunction Hom equivalence to identify κ with the adjunct of c followed by the continuous-map comparison. Evaluate this identity at W and g and expand homEquiv_unit to obtain the formula.
