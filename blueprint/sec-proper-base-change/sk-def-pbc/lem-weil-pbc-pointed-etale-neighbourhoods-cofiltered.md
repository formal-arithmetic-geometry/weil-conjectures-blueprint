+++
id = "lem-weil-pbc-pointed-etale-neighbourhoods-cofiltered"
kind = "lemma"
title = "Pointed etale neighbourhoods of a geometric point form a cofiltered category"
order = 1079
uses = ["def-pc-scheme", "def-weil-geometric-point", "def-weil-etale-morphism", "def-weil-pbc-pointed-etale-neighbourhoods"]
lean = ["AlgebraicGeometry.Scheme.instIsCofilteredElementsEtaleCompOverForgetObjOppositeFunctorTypeCoyonedaOpMk"]
tags = ["mathlib", "stacks-03PQ"]
+++
Let $S$ be a scheme [def-pc-scheme], $\Omega$ a field and $\bar s:\operatorname{Spec}\Omega\to S$ a morphism of schemes (for instance a geometric point [def-weil-geometric-point]). Let $\mathcal N^{\mathrm{all}}_{\bar s}$ be the category whose objects are pairs $(V,\bar v)$ with $V\to S$ an etale morphism [def-weil-etale-morphism] and $\bar v:\operatorname{Spec}\Omega\to V$ a morphism over $S$ (i.e. $(V\to S)\circ\bar v=\bar s$), and whose morphisms $(V',\bar v')\to(V,\bar v)$ are the $S$-morphisms $h:V'\to V$ with $h\circ\bar v'=\bar v$ (this is the category of pointed etale neighbourhoods of [def-weil-pbc-pointed-etale-neighbourhoods]). Then $\mathcal N^{\mathrm{all}}_{\bar s}$ is cofiltered: it is nonempty ($(S,\bar s)$ is an object); for two objects $(V_1,\bar v_1),(V_2,\bar v_2)$ the fibre product $(V_1\times_SV_2,(\bar v_1,\bar v_2))$ is an object mapping to both by the projections; and for two morphisms $h_1,h_2:(V,\bar v)\to(V',\bar v')$ there is a morphism $h:(V'',\bar v'')\to(V,\bar v)$ with $h_1\circ h=h_2\circ h$.
