+++
id = "sk-ex-tf-trace-example"
kind = "remark"
title = "A trace not determined by cohomology"
order = 545
tags = ["sketch", "latex:example"]
+++
Let $A=\mathbf Z/\ell^2$ and let $P=[A\xrightarrow{\ell}A]$, with the
terms in degrees $0$ and $1$. This is the perfect complex from
Section [sec-n-constructible] whose cohomology modules
$H^0(P)=\ell A$ and $H^1(P)=A/\ell A$ are not perfect. The chain maps
$1_P=(1,1)$ and $v=(1+\ell,1)$ commute with the differential, since
$\ell(1+\ell)=\ell$ in $A$, and both induce the identity on $H^0(P)$
and on $H^1(P)$. By the chain formula of
Proposition [sk-p-trace],

$$
\operatorname{tr}_A(1_P\mid P)=1-1=0,
\qquad
\operatorname{tr}_A(v\mid P)=(1+\ell)-1=\ell\neq0.
$$

Thus, over a finite ring, the trace of an endomorphism of a perfect
complex is not determined by the maps it induces on cohomology, and
the trace formula has to be stated for the operator on the complex.
Over a field, the trace is the alternating sum of the traces on
cohomology (Proposition [sk-p-trace]), and this distinction
disappears.
