+++
id = "prop-trf-trace-class-additivity"
kind = "theorem"
title = "Additivity of trace classes"
order = 2492
uses = ["def-trf-fixed-scheme", "def-trf-integration", "def-trf-local-term", "def-weil-scheme-morphism-properties", "lem-trf-integration-linear", "lem-trf-trace-triangle-compatibility"]
+++
Let

$$
K'\longrightarrow K\longrightarrow K''\longrightarrow K'[1]
$$

be a distinguished triangle in $D^b_{ctf}(X,A)$ with an induced
morphism $(u',u,u'')$ of the corresponding triangles of the functors
$Lc_2^*$ and $Rc_1^!$. Then

$$
\operatorname{Tr}_c(u)=
\operatorname{Tr}_c(u')+\operatorname{Tr}_c(u'')
$$

in $\operatorname{Hom}_{D(F,A)}(A_F,\omega_{F,A})$; if $F$ is
proper over $s$ with
finitely many components in the sense of
[def-trf-fixed-scheme], the same identity holds for the
local terms.

## Proof

The first assertion is exactly
[lem-trf-trace-triangle-compatibility]. For the second, suppose
$F$ proper over $s$ with finitely many open-and-closed components
$\beta\in\pi_0(F)$; the local terms of
[def-trf-local-term] are the integrals
$\operatorname{LT}_\beta(u)=\int_\beta\operatorname{Tr}_c(u)|_\beta$
of [def-trf-integration], and integration is $A$-linear by
[lem-trf-integration-linear], so
additivity of the classes gives
$\operatorname{LT}_\beta(u)=\operatorname{LT}_\beta(u')+ \operatorname{LT}_\beta(u'')$ for every $\beta$.
