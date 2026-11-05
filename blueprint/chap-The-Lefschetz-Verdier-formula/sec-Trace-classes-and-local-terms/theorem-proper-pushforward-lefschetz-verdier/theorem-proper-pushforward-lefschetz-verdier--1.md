+++
id = "theorem-proper-pushforward-lefschetz-verdier--1"
kind = "theorem"
title = "Proper pushforward of the trace class"
name_showing = false
order = 925001
aliases = ["bp-r281-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.traceClassPushforward_eq"]
uses = ["definition-correspondence", "definition-pushforward-correspondence", "definition-trace-class-local-terms"]
+++
Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be prime,
and put $A=\Qbarl$. Let $X,Y,C,C'$ be separated $k$-schemes of finite
type, let $K\in\Dbc(X,A)$, and let $u:c_2^*K\to c_1^!K$ be a
cohomological correspondence on $(X,K)$. Suppose that $f:X\to Y$ and
$g:C\to C'$ are proper and that $c'_ig=fc_i$ for $i=1,2$.

Set $K'=Rf_*K$, and let $u'$ be the pushforward of $u$ of
Definition [definition-pushforward-correspondence]. For fixed loci
$F=\Fix(c)$ and $F'=\Fix(c')$, the induced proper map $h:F\to F'$
satisfies

$$
h_*\operatorname{Tr}_c(u)=\operatorname{Tr}_{c'}(u')
$$

as morphisms $A_{F'}\to\omega_{F'}$. The leg squares need only commute;
they need not be cartesian, and the schemes need not be proper over $k$.
