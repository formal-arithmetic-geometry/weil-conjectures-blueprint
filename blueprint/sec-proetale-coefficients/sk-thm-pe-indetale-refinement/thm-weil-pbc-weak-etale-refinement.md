+++
id = "thm-weil-pbc-weak-etale-refinement"
kind = "theorem"
title = "Ind-etale refinement of a weakly etale map"
order = 920
lean = ["Algebra.WeaklyEtale.indEtale_faithfullyFlat_refinement"]
uses = ["def-weil-pbc-ind-etale-algebra", "def-weil-pbc-weak-etale-refinement", "lem-weil-pbc-ind-etale-stability", "lem-weil-pbc-local-rings-ind-zariski", "lem-weil-pbc-retained-localization", "lem-weil-pbc-strict-w-cover", "lem-weil-pbc-weak-etale-field", "thm-weil-pbc-weak-etale-strict-local"]
+++
Let $A\to B$ be weakly etale [def-weil-pbc-ind-etale-algebra]. For the
construction of [def-weil-pbc-weak-etale-refinement], the map $B\to B'$ is
faithfully flat and ind-etale, and $A\to B'$ is ind-etale.
