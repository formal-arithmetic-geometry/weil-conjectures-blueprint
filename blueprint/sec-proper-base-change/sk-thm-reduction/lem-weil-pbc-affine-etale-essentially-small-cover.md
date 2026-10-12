+++
id = "lem-weil-pbc-affine-etale-essentially-small-cover"
kind = "lemma"
title = "A set of affine etale schemes covers every object of the small etale site"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.AffineEtale.instEssentiallySmall"]
tags = ["sheaf-dag", "mathlib", "stacks-021A"]
+++
Let $T$ be a scheme [def-pc-scheme] and $T_{\Et}$ its small etale site [def-weil-pbc-etale-site]. There is a set $\mathcal S$ of objects of $T_{\Et}$, each of the form $\mathrm{Spec}(A)\to T$ with $A$ a ring (affine schemes etale over $T$), such that every object $U\to T$ of $T_{\Et}$ with $U$ affine is isomorphic in $T_{\Et}$ to a member of $\mathcal S$; consequently every object $V$ of $T_{\Et}$ has a covering $\{U_k\to V\}_{k\in K}$ in $T_{\Et}$ with every $U_k\in\mathcal S$ (refine an affine open covering of $V$). In other words the full subcategory $T_{\mathrm{aff},\Et}$ of affine objects is essentially small and cover-dense in $T_{\Et}$.
