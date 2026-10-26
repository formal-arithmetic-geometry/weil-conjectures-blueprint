+++
id = "lem-weil-pbc-fiber-degree-split-cofan"
kind = "lemma"
title = "Fibre degree of a finite coproduct of copies of the base"
uses = ["def-pc-finite-locally-free", "def-pc-scheme", "pqf-def-affine-morphism"]
lean = ["AlgebraicGeometry.Scheme.Hom.fiberDegree_eq_nat_card_of_split_cofan"]
order = 1735
+++
Let $p:Z\to U$ be an affine morphism of schemes [def-pc-scheme], [pqf-def-affine-morphism], let $J$ be a finite set, and let $D_j$ be schemes with maps $i_j:D_j\to Z$ exhibiting $Z$ as the coproduct $\coprod_{j\in J}D_j$. Suppose each composite $p\circ i_j:D_j\to U$ is an isomorphism. For every point $x\in U$, the scheme-theoretic fibre $Z_x$ has $\dim_{\kappa(x)}\Gamma(Z_x,\mathcal O_{Z_x})=|J|$, where $\kappa(x)$ is the residue field. This dimension is the fibre degree used in [def-pc-finite-locally-free]. The empty set $J$ is allowed.
