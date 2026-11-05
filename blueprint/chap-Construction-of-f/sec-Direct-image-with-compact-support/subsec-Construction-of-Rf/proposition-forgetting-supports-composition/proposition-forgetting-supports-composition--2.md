+++
id = "proposition-forgetting-supports-composition--2"
kind = "proposition"
title = "Forgetting supports and composition (2)"
name_showing = false
order = 519002
aliases = ["bp-r158-2"]
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationIso_hom_app_comp_toLowerStar"]
uses = ["proposition-forgetting-supports-composition--1", "proposition-construction-independence-rf-shriek"]
+++
The unrestricted composition square is bypassed by the Lean route; its
composition compatibility is the proper case in
[proposition-forgetting-supports-composition--3].

Let $\Lambda$ be a finite commutative ring, let $f:X\to Y$ be
quasi-compact, and let $c,d$ be compactifications of $f$.
On $D(\et{X},\Lambda)$, write
$\kappa_{c,d}:Rf_!^{\,c}\xrightarrow{\sim}Rf_!^{\,d}$ for the
comparison isomorphism of
[proposition-construction-independence-rf-shriek]. Then, for every
$K\in D(\et{X},\Lambda)$,

$$
\eta_f^{\,d}(K)\circ\kappa_{c,d}(K)=\eta_f^{\,c}(K),
$$

where the maps $\eta_f^{\,c}$ and $\eta_f^{\,d}$ are those of
[proposition-forgetting-supports-composition--1]. Thus the forget-supports
map is independent of the compactification under these comparisons.
