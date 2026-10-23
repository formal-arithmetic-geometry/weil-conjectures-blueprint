+++
id = "def-weil-pbc-retained-localization"
kind = "definition"
title = "Retaining a closed subset"
order = 940
lean = ["Ideal.WLocalization", "WLocalization.Generalization"]
uses = ["def-weil-pbc-w-localization"]
+++
Let $R$ be a ring, $J\subset R$ an ideal, and $R^w$ the w-localization of
[def-weil-pbc-w-localization]. Define $R_{[J]}$ to be the localization of
$R^w$ at the multiplicative set of elements whose image in $R^w/JR^w$ is a
unit, i.e. of the elements lying in no prime of $R^w$ that contains $JR^w$.
It retains the points of $\operatorname{Spec}R^w$ that generalize a point of
$V(JR^w)$.
