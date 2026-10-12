+++
id = "sk-thm-iff"
kind = "theorem"
title = "PBC $\\Leftrightarrow$ IA"
order = 1067
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_iff_hasInjectiveAcyclicity"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-ia", "sk-def-pbc", "sk-thm-acyclicity"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring which is torsion as an additive group
(e.g. $\Lambda=\mathbf Z/n\mathbf Z$), and let $f$ be a proper morphism of
schemes. Then $\mathrm{PBC}_\Lambda(f)$ in the sense of [sk-def-pbc] holds if
and only if $\mathrm{IA}_\Lambda(f)$ in the sense of [sk-def-ia] holds.
