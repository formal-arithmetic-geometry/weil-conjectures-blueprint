+++
id = "lem-weil-pbc-pointed-etale-neighbourhood-affine-shrink"
kind = "lemma"
title = "Shrinking a pointed etale neighbourhood to an affine open around the point"
uses = ["def-pc-scheme", "def-weil-etale-morphism", "def-weil-open-immersion", "def-weil-affine-spectrum", "def-weil-pbc-pointed-etale-neighbourhoods"]
refines = "proof/lem-weil-pbc-etale-local-ring-triples"
lean = ["AlgebraicGeometry.Scheme.exists_affine_mem_range_and_range_subset, AlgebraicGeometry.IsOpenImmersion.lift, AlgebraicGeometry.IsOpenImmersion.lift_fac, AlgebraicGeometry.IsOpenImmersion.lift_uniq"]
tags = ["sheaf-dag", "mathlib", "stacks-04HX"]
+++
Let $S$ be a scheme [def-pc-scheme], $f:V\to S$ an etale morphism [def-weil-etale-morphism], $\Omega$ a field and $\bar v:\operatorname{Spec}\Omega\to V$ a morphism of schemes whose image is the point $v\in V$, and let $W\subset V$ be an open subset containing $v$. Then there are a commutative ring $R$ and an open immersion [def-weil-open-immersion] $j:\operatorname{Spec}R\to V$ [def-weil-affine-spectrum] with $v\in j(\operatorname{Spec}R)\subset W$; the composite $f\circ j$ is etale; and there is exactly one morphism $\bar v_0:\operatorname{Spec}\Omega\to\operatorname{Spec}R$ with $j\circ\bar v_0=\bar v$. In particular $(\operatorname{Spec}R,\bar v_0)$ is an affine pointed etale neighbourhood of $f\circ\bar v$ [def-weil-pbc-pointed-etale-neighbourhoods] and $j$ is a morphism of pointed etale neighbourhoods $(\operatorname{Spec}R,\bar v_0)\to(V,\bar v)$.
