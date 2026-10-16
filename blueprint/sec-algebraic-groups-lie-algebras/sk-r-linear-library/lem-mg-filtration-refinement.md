+++
id = "lem-mg-filtration-refinement"
kind = "lemma"
title = "Refining a finite filtration"
lean = ["Representation.HasGradedPieces.trans", "Representation.CompositionSeries.exists_equiv_sigma_of_monotone", "Representation.ConstituentsLE", "Representation.ConstituentsLE.of_chain"]
order = 2888
uses = ["def-mg-weil-composition-series", "lem-mg-composition-series-exists", "lem-mg-jordan-holder"]
+++
Let $0=M_0\subseteq M_1\subseteq\cdots\subseteq M_s=M$ be a finite
filtration by Weil subrepresentations. In the terminology of
[def-mg-weil-composition-series], the composition-factor multiset of
$M$ is the disjoint union of the composition-factor multisets of the
quotients $M_i/M_{i-1}$.
