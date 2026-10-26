+++
id = "lem-weil-pbc-finite-etale-graph-clopen"
kind = "lemma"
title = "Morphisms correspond to clopen graphs projecting isomorphically"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Scheme.finiteEtale_graph_clopen"]
order = 1753
+++
Let $p:U\to Y$ be a morphism of schemes [def-pc-scheme] and $q:V\to Y$ a finite etale morphism. Put $P=V\times_Y U$ with projection $r:P\to U$. There exists a bijection from the set of morphisms $a:U\to V$ satisfying $q\circ a=p$ to the set of open subsets $W\subseteq P$ that are also closed and for which $r|_W$ is an isomorphism. The underlying subset assigned to $a$ is the image of its graph $(a,\mathrm{id}_U):U\to P$.
