+++
id = "proposition-composition-base-change-rf-shriek--6"
kind = "proposition"
title = "Pasting of base-change comparisons"
order = 516007
aliases = ["bp-r157-6"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekBaseChange_padicAlgCl_paste_horiz", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekBaseChange_padicAlgCl_paste_vert"]
uses = ["proposition-composition-base-change-rf-shriek--1", "proposition-composition-base-change-rf-shriek--4"]
+++
For $\Lambda=\Qbarl$ in the shared context, the base change maps of
[proposition-composition-base-change-rf-shriek--4] satisfy both pasting laws.
For successive changes of base $Y''\xrightarrow{v_1}Y'\xrightarrow{v_2}Y$,
with induced maps $X''\xrightarrow{u_1}X'\xrightarrow{u_2}X$, the map for
the outer cartesian rectangle is
$$
(v_2v_1)^*Rf_!\simeq v_1^*v_2^*Rf_!
\xrightarrow{v_1^*\Ex_!}v_1^*Rf'_!u_2^*
\xrightarrow{\Ex_!u_2^*}Rf''_!u_1^*u_2^*
\simeq Rf''_!(u_2u_1)^*.
$$
For $X\xrightarrow fY\xrightarrow gZ$ and its base change
$X'\xrightarrow{f'}Y'\xrightarrow{g'}Z'$, write $u$, $v$ and $w$ for the
maps to $X$, $Y$ and $Z$. The map for the outer rectangle is
$$
w^*R(gf)_!\xrightarrow{w^*C_{f,g}}w^*Rg_!Rf_!
\xrightarrow{\Ex_!Rf_!}Rg'_!v^*Rf_!
\xrightarrow{Rg'_!\Ex_!}Rg'_!Rf'_!u^*
\xrightarrow{C_{f',g'}^{-1}u^*}R(g'f')_!u^*.
$$
Thus base change is compatible with the composition isomorphisms of
[proposition-composition-base-change-rf-shriek--1].
