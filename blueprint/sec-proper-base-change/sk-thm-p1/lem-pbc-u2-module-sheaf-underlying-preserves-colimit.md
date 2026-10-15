+++
id = "lem-pbc-u2-module-sheaf-underlying-preserves-colimit"
kind = "lemma"
title = "Underlying sheaf forgetful functor preserves module-sheaf colimits"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.moduleSheaf_underlying_preserves_colimit"]
+++
For a scheme X, a commutative ring Λ, and a small diagram D of Λ-module sheaves on the small etale site of X, the sheafCompose functor induced by ModuleCat Λ → AddCommGrpCat preserves colimits of D.
