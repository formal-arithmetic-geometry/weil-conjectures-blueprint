+++
id = "sk-def-set"
kind = "definition"
title = "The fixed setting"
order = 3424
uses = ["sk-prop-sf-open-closed-triangle", "sk-def-purity-conv", "sk-thm-existence", "sk-prop-sf-existence", "sk-prop-sf-rf-shriek-preservation", "sk-thm-sf-ctf-stability"]
lean = ["AlgebraicGeometry.PoincareDualitySetting"]
tags = ["sketch"]
+++
Work with the finite-field datum $(p,a,q,k_0,k)$, $\ell$, $E$, $\Oe$,
$\pi_E$, $\AEn=\Oe/\pi_E^n$ and the admissible coefficient rings
$\Lambda\in\{\AEn,\Oe,E,\Qlb\}$ fixed in [def-sf-setting], each
regarded as a condensed ring. For a scheme $T$ in this setting the ambient
category is $D(T_{\mathrm{pro\acute et}},\Lambda)$, the derived category of
$\Lambda_T=p_T^*\Lambda$-modules ([det-def-sfb-pulled-back-coefficients]),
and the coefficients are its full subcategories
$\Dctf(T,\Lambda)\subseteq\Dbc(T,\Lambda)$ of
[det-def-sfb-bounded-constructible]; for $\Lambda=\Oe,E,\Qlb$ the two agree.
For finite $\Lambda=\AEn$ these are equivalently the étale categories, by the
comparison of [def-sf-setting]. Let $X_0/k_0$ be smooth of relative
dimension $d$, separated of finite type and geometrically connected, put
$X=X_0\times_{k_0}k$ and $s=\Spec k$, and let $a_X:X\to s$ be the
structure morphism. No admissibility hypothesis is imposed on $a_X$: its
exceptional inverse image $Ra_X^!$ is the constructible exceptional adjoint
of [det-def-sf-operations](vi), the right adjoint of $Ra_{X!}$ on
$\Dctf$ given by [sk-thm-existence], which exists and preserves
$\Dctf$ for every admissible $\Lambda$ and every separated finite-type morphism
([thm-sf-ambient-adjoint-class], [sk-prop-sf-rf-shriek-preservation],
[sk-thm-sf-ctf-stability]); the
ambient datum of [sk-def-sf-admissible], which fails for smooth proper
curves ([sk-rem-sf-fullcd-scope]), is not used. Properness of $X_0$ is *not* part of this setting: the
duality results [sk-thm-sf-global-duality], [sk-thm-sf-identification]
and [sk-thm-derived-duality]
are formulated with compact supports and never use it. It is imposed
explicitly, and only, in [sk-def-trace-cup], [sk-cor-trace],
[sk-thm-poincare-duality] and the final clause of
[sk-thm-derived-duality], each of which needs
$Ra_{X!}\cong Ra_{X*}$.
