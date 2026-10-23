+++
id = "lem-weil-pbc-geometric-stalks-detect-mono"
kind = "lemma"
title = "Monomorphisms of etale sheaves are detected on a covering family of geometric stalks"
order = 1597
uses = ["def-pc-scheme", "def-pc-separably-closed", "def-weil-geometric-point", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Scheme.isConservative_pointSmallEtale", "CategoryTheory.ObjectProperty.IsConservativeFamilyOfPoints.jointlyReflectMonomorphisms", "CategoryTheory.JointlyReflectMonomorphisms.mono_iff", "AddCommGrpCat.mono_iff_injective"]
tags = ["mathlib", "stacks-03PU"]
+++
Let $S$ be a scheme [def-pc-scheme], let $(\Omega_i)_{i\in I}$ be a family of separably closed fields [def-pc-separably-closed] and $(\bar s_i:\operatorname{Spec}\Omega_i\to S)_{i\in I}$ a family of morphisms of schemes whose images cover $S$ (every point of $S$ is the image of the point of some $\operatorname{Spec}\Omega_i$; for instance a family of geometric points [def-weil-geometric-point] covering $S$), and let $\varphi:F\to G$ be a morphism in the category $\Ab(S_{\Et})$ of abelian sheaves on the small etale site [def-weil-pbc-abelian-etale-sheaves]. Then $\varphi$ is a monomorphism if and only if for every $i\in I$ the induced map of stalks [def-weil-pbc-geometric-stalks] $\varphi_{\bar s_i}:F_{\bar s_i}\to G_{\bar s_i}$ is injective.
