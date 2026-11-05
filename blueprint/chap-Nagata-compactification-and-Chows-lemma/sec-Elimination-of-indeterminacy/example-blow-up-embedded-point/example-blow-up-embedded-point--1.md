+++
id = "example-blow-up-embedded-point--1"
kind = "example"
title = "Blowing up removes an embedded point (1)"
name_showing = false
order = 1426001
aliases = ["bp-r443-1"]
+++
Let $T=\operatorname{Spec}R$ with $R=k[x,y]/(xy,y^2)$, the line $y=0$
with an embedded point at the origin, and let $U=D(x)$. On $U$ the
element $y$ is zero, since $xy=0$ and $x$ is invertible, so
$U$ is not schematically dense in $T$. The ideal $I=(x)$ is the unit
ideal on $U$, so its blow-up is $U$-admissible. For a principal ideal
the chart formula above gives $R[I/x]=R/\{b:x^nb=0\text{ for some }n\}$.
Every element of $R$ is uniquely $f(x)+cy$ with $c\in k$, and
$x^n(f+cy)=x^nf$, so the $x$-power torsion is $ky$ and the blow-up is
$\operatorname{Spec}k[x]$. The embedded point is gone, $U$ is dense, and
the boundary is the Cartier divisor $x=0$, as in
Lemma [lemma-making-open-schematically-dense].
