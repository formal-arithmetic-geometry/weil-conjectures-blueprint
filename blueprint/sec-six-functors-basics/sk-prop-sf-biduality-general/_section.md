+++
id = "sk-prop-sf-biduality-general"
kind = "proposition"
title = "General Verdier biduality"
order = 1711
uses = ["sk-def-sf-operations", "sk-prop-sf-rf-shriek-preservation"]
lean = ["AlgebraicGeometry.Etale.constructibleFiniteTor_verdierDual", "AlgebraicGeometry.Etale.nonempty_iso_verdierDual_verdierDual"]
tags = ["sketch"]
+++
Let $Y$ be a separated finite-type $k$-scheme and let $\Lambda$ be a
coefficient stage; let $Ra_Y^!$ be the constructible exceptional adjoint of
the structure morphism ([sk-def-sf-operations](vi); no admissibility datum
is assumed, cf.\ [sk-def-sf-admissible]). Then
$\mathbb D_Y=\RHom_\Lambda(-,\omega_{Y,\Lambda})$
with $\omega_{Y,\Lambda}=Ra_Y^!\Lambda\in\Dctf(Y,\Lambda)$
([sk-prop-sf-rf-shriek-preservation]) is a contravariant exact
anti-equivalence of $\Dctf(Y,\Lambda)$ with $\mathbb D_Y\mathbb D_Y\cong \mathrm{id}$: the double-dual morphism $\delta_K$ is an isomorphism for every
$K$.
