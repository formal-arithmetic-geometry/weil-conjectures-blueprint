+++
id = "def-constructible-finite"
kind = "definition"
title = "Finite sheaves"
order = 1493
lean = ["AlgebraicGeometry.Scheme.IsFiniteSheaf"]
uses = ["def-pc-separably-closed"]
+++
A sheaf $\mathcal F\in\shv{\et X}$ (with $\mathcal A$ concrete) is
*finite* if for every geometric point $\bar x$ of $X$ the stalk
$\mathcal F_{\bar x}$ is finitely generated: for sheaves of $\Lambda$-modules
a finitely generated $\Lambda$-module, for sheaves of sets a finite set.
Over a finite ring $\Lambda$ this says that all stalks are finite.
