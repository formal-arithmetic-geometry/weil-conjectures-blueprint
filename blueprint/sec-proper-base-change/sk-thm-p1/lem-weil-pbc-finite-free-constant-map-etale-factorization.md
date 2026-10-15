+++
id = "lem-weil-pbc-finite-free-constant-map-etale-factorization"
kind = "lemma"
title = "Étale-local factorization of a finite free constant map"
uses = ["def-constructible-constant", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.exists_etale_factorization_of_finite_free_constant_map"]
+++
Let X be a scheme, Λ a commutative ring, F and G sheaves of Λ-modules on the small etale site, and φ : F → G any morphism. For a finite free constant source Q_X = Λ^(Fin n)_X and a map α : Q_X → G, suppose a map l on the algebraic-closure geometric stalk at x satisfies l φ_x = α_x. Then there is an etale morphism V → X whose image contains x and a map β : Q_V → F|_V with β (φ|_V) = α|_V. No monomorphism hypothesis on φ is required. Schemes, the site, constants, and stalks are as in [def-weil-pbc-scheme-conventions], [def-weil-pbc-etale-site], [def-constructible-constant], and [def-weil-pbc-geometric-stalks].
