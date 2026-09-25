+++
id = "sbc-cor-classical-form"
kind = "theorem"
title = "Classical form: base change along a smooth morphism"
order = 1448
tags = ["latex:corollary"]
uses = ["def-sbc-smooth-morphisms", "def-weil-pbc-scheme-conventions", "sbc-def-base-change-map", "sbc-def-base-change-square", "sbc-thm-smooth-base-change"]
+++
Consider a Cartesian diagram

$$
\begin{array}{ccc}
X' & \xrightarrow{\;v\;} & X\\
f'\big\downarrow & & \big\downarrow f\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
\qquad(X'=X\times_YY')
$$

where $g$ is smooth and $f$ is
quasi-compact and
quasi-separated. Then

$$
g^{-1}R^qf_*\mathcal F=R^qf'_*v^{-1}\mathcal F
$$

for any $q$ and any abelian sheaf $\mathcal F$ on $X_{\Et}$ all of
whose stalks at geometric points are torsion of orders invertible on
$Y$.

## Proof

The displayed diagram is a
base-change square of
[sbc-def-base-change-square] with base $S=Y$, vertical side
$g:Y'\to Y$ (smooth), and horizontal side $f:X\to Y$ (quasi-compact and
quasi-separated), the projections being $f'$ and $v$; the claim is
[sbc-thm-smooth-base-change] applied to these letters, and the
isomorphism is the base-change map of [sbc-def-base-change-map].
