+++
id = "thm-constructible-serre"
kind = "theorem"
title = "Constructible sheaves form a weak Serre subcategory"
order = 1299
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.biprod", "AlgebraicGeometry.Scheme.IsConstructibleSheaf.cokernel", "AlgebraicGeometry.Scheme.IsConstructibleSheaf.kernel"]
uses = ["def-constructible-constructible", "def-weil-pbc-constructible-complexes", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "lemma-weil-pbc-geometric-stalk-conservative", "prop-constructible-pullback", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $\mathcal A=\mathrm{Mod}_\Lambda$ with $\Lambda$ a ring. The kernel and
the cokernel of a morphism between constructible sheaves on $\et X$, and
finite direct sums of constructible sheaves, are constructible. If
$\Lambda$ is finite, the middle term of a short exact sequence whose outer
terms are constructible is constructible as well; consequently, for a
finite ring $\Lambda$, the constructible sheaves form a weak Serre
subcategory of $\shv{\et X}$.
