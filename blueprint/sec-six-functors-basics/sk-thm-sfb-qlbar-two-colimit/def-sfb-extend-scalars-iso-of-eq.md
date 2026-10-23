+++
id = "def-sfb-extend-scalars-iso-of-eq"
kind = "definition"
title = "Extension of scalars along equal morphisms"
order = 2166
uses = ["det-def-sfb-change-of-scalars"]
lean = ["CategoryTheory.Mod.extendScalarsIsoOfEq"]
+++
Let $\mathcal C$ be a braided monoidal category with coequalizers in which tensoring on either
side preserves colimits, $R$ a commutative monoid object and $\varphi,\psi\colon R\to S$ morphisms
of monoid objects with $\varphi=\psi$. The natural isomorphism
$\operatorname{Ext}_\varphi\cong\operatorname{Ext}_\psi$ ([det-def-sfb-change-of-scalars]) is the
one given by uniqueness of left adjoints, both functors being left adjoint to the equal
restrictions of scalars $\operatorname{Res}_\varphi=\operatorname{Res}_\psi$.
