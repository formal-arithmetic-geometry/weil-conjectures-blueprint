+++
id = "lem-weil-pbc-fpqc-descend-separated"
kind = "lemma"
title = "Separatedness descends along flat surjective quasi-compact morphisms (Stacks 02KU)"
uses = ["def-pc-scheme", "def-weil-finite-type-morphism"]
lean = ["AlgebraicGeometry.isSeparated_of_flat_surjective_baseChange"]
order = 1793
+++
Let $g:S'\to S$ be a morphism of schemes [def-pc-scheme] which is flat, surjective and quasi-compact [def-weil-finite-type-morphism]. Let $f:X\to S$ be a morphism of schemes and let $f':X\times_SS'\to S'$ be the second projection of the fibre product. If $f'$ is separated (its diagonal $X\times_SS'\to(X\times_SS')\times_{S'}(X\times_SS')$ is a closed immersion), then $f$ is separated.
