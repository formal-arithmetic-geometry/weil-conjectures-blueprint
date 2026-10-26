+++
id = "lem-weil-pbc-etale-restriction-injectives"
kind = "lemma"
title = "Etale restriction preserves injectives"
order = 967
lean = ["AlgebraicGeometry.Etale.etaleLowerShriekUpperStarAdjunction", "AlgebraicGeometry.Etale.preservesFiniteLimits_etaleLowerShriek", "AlgebraicGeometry.Etale.injective_upperStar_obj_of_etale"]
uses = ["def-weil-pbc-etale-sum-extension", "def-weil-pbc-inverse-image", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $\Lambda$ be a commutative ring and $v:W\to X$ an etale map. On etale
sheaves of $\Lambda$-modules, the functor $v_!$
[def-weil-pbc-etale-sum-extension] is left adjoint to $v^*$
[def-weil-pbc-inverse-image] and is exact. Consequently $v^*$ sends injective
sheaves of $\Lambda$-modules to injective sheaves of $\Lambda$-modules.
