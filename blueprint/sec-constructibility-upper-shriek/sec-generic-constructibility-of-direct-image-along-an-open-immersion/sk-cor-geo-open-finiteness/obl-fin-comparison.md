+++
id = "obl-fin-comparison"
kind = "theorem"
title = "The comparison and finitude of proper direct images"
lean = ["AlgebraicGeometry.Etale.isIso_homology_derivedBaseChangeMapPlus_of_isProper"]
order = 2670
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "fin4-lem-fibrewise-cohomological-dimension", "lemma-weil-pbc-geometric-stalk-conservative", "sbc-def-coefficient-conventions", "thm-fin-proper-constructibility-complete"]
+++
Let $k$ be a field of characteristic prime to $N$, let $\Lambda$ be
the finite commutative ring annihilated by $N$ of
[sbc-def-coefficient-conventions], let $S$ be of finite type over
$k$, let $f:X\to S$ be a
proper morphism whose
geometric fibres have
dimension at most $d\in\mathbf Z_{\geq0}$, and let $F$ be a
constructible
$\Lambda$-sheaf on $X_{{\mathrm{et}}}$. Then:

1. **(i)** (*the comparison*) For every $q\geq0$ and every
geometric point
$\bar s$ of $S$, the comparison map of
[cor-weil-pbc-geometric-fiber-finite]
$$
(R^qf_*F)_{\bar s}\xrightarrow{\ \sim\ }
H^q\bigl(X_{\bar s},F|_{X_{\bar s}}\bigr)
$$
is an isomorphism; each fibre-cohomology group
$H^q(X_{\bar s},F|_{X_{\bar s}})$ is a finite $\Lambda$-module;
and these groups vanish for $q>2d$.
1. **(ii)** (*the finitude*) The higher direct images
$R^qf_*F$ of [def-weil-pbc-direct-image] are
constructible
on $S_{{\mathrm{et}}}$ for every $q\geq0$, and
$R^qf_*F=0$ for $q>2d$.
