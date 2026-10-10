+++
id = "lem-sc-divisor-exact-sequence"
kind = "lemma"
title = "The divisor exact sequence"
order = 899
uses = ["def-sc-curves", "lem-sc-regular-dim1-dvr"]
lean = ["AlgebraicGeometry.IsCurve.exists_shortExact_divisorSequence"]
+++
Let $\overline C$ be a proper smooth
connected curve over an algebraically closed field
$k$, $S\subset\overline C$ a finite set of closed points,
$j:C:=\overline C\setminus S\hookrightarrow\overline C$ the open
immersion, and $i_P:\{P\}\hookrightarrow\overline C$ the
inclusions. There is a morphism $d$ of etale sheaves on
$\overline C_{\Et}$ such that the sequence

$$
0\longrightarrow\mathbf G_m\longrightarrow j_*\mathbf G_m
\xrightarrow{\ d\ }\bigoplus_{P\in S}i_{P*}\mathbf Z\longrightarrow0
$$

is exact, where the first map is the unit
$\mathbf G_m\to j_*j^*\mathbf G_m=j_*\mathbf G_m$ (restriction of units
to $C$).
