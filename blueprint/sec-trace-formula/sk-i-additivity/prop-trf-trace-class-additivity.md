+++
id = "prop-trf-trace-class-additivity"
kind = "theorem"
title = "Additivity of trace classes"
order = 2354
uses = ["d-curve-pieces", "def-trf-fixed-scheme", "def-trf-integration", "def-trf-local-term", "def-weil-scheme-morphism-properties", "lem-trf-integration-linear", "lem-trf-trace-triangle-compatibility", "prop-functor-package", "prop-sf-open-closed-triangle-all-stages", "prop-weil-open-closed-recollement-adjunctions", "thm-trf-frobenius-fixed-points"]
+++
1. Let $i:Z\hookrightarrow X$ be a closed subscheme with open complement
$j:U\hookrightarrow X$ which is $c$-invariant, $c_2(c_1^{-1}(Z))\subset Z$,
let
$$
K'=j_!j^*K\longrightarrow K\longrightarrow K''=Ri_*i^*K\longrightarrow K'[1]
$$
be its open–closed triangle, and let $(u',u,u'')$ be the induced morphism
of the corresponding triangles of the functors $Lc_2^*$ and $Rc_1^!$, with
$u'=[j]_!(u|_U)$ and $u''=[i]_!(u|_Z)$ the induced coefficient morphisms of
[lem-trf-trace-triangle-compatibility] (an arbitrary morphism of
distinguished triangles is not enough, see there). Then
$$
\operatorname{Tr}_c(u)=
\operatorname{Tr}_c(u')+\operatorname{Tr}_c(u'')
$$
in $\operatorname{Hom}_{D(F,A)}(A_F,\omega_{F,A})$; if $F$ is
proper over $s$ with
finitely many components in the sense of
[def-trf-fixed-scheme], the same identity holds for the
local terms.
1. *(Curve pieces.)* In the setting of [d-curve-pieces] ($m\geq1$,
$x\in X_0(\mathbf F_{q^m})$, $c=(\operatorname{id}_X,\Phi_m)$ the
graph correspondence), let $v:\Phi_m^*K\to K$ be the scheme-Frobenius
map $\varphi_m$ or an arbitrary Frobenius coefficient morphism, with
pieces $u^Z,u^U$. Then $(u^U,v,u^Z)$ is a morphism of the
open–closed triangles $K^U\to K\to K^Z\to K^U[1]$ under
$L\Phi_m^*$ and $Rc_1^!=\operatorname{id}$, and hence
$$
\operatorname{Tr}_c(v)=\operatorname{Tr}_c(u^Z)+\operatorname{Tr}_c(u^U),
\qquad
\operatorname{LT}_\beta(v)=\operatorname{LT}_\beta(u^Z)+\operatorname{LT}_\beta(u^U)
$$
for every component $\beta$ of $F=\operatorname{Fix}(\Phi_m)$.
Invertibility of $v$ is not required.
