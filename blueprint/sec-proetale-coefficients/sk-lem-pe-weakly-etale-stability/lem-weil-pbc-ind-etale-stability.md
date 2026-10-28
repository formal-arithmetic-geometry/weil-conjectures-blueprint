+++
id = "lem-weil-pbc-ind-etale-stability"
kind = "lemma"
title = "Stability and diagonal of an ind-etale algebra"
order = 904
lean = ["RingHom.IndEtale.isStableUnderBaseChange", "RingHom.IndEtale.comp", "RingHom.IndEtale.of_isColimit", "RingHom.IndZariski.comp", "RingHom.IndZariski.of_isColimit", "RingHom.IndZariski.indEtale", "RingHom.IndEtale.weaklyEtale", "RingHom.IndEtale.of_comp", "Algebra.WeaklyEtale.trans", "RingHom.WeaklyEtale.comp", "Algebra.WeaklyEtale"]
uses = ["def-weil-pbc-ind-etale-algebra", "lem-weil-pbc-etale-finite-data-descent"]
+++
The class of ind-etale [def-weil-pbc-ind-etale-algebra] maps is stable
under base change, composition, and filtered colimits. The class of
ind-Zariski maps is stable under composition and filtered colimits, and every
ind-Zariski map is ind-etale. An ind-etale map is weakly etale. If $B,C$ are
ind-etale over $A$, every $A$-algebra map $B\to C$ is ind-etale. Weakly etale
maps are stable under composition and base change.
