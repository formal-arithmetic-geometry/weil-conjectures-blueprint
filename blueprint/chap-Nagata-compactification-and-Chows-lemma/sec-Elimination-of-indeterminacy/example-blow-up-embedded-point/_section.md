+++
id = "example-blow-up-embedded-point"
kind = "example"
title = "Blowing up removes an embedded point"
order = 1426
uses = ["lemma-making-open-schematically-dense"]
+++
Let $T=\operatorname{Spec}R$ with $R=k[x,y]/(xy,y^2)$, the line $y=0$
with an embedded point at the origin, and let $U=D(x)$. On $U$ the
element $y$ is zero, since $xy=0$ and $x$ is invertible, so
$U$ is not schematically dense in $T$. On the other hand, the ideal $I=(x)$ is the unit
ideal on $U$, so its blow-up is $U$-admissible. Since the ideal is principal,
the chart formula above gives $R[I/x]=R/\{b:x^nb=0\text{ for some }n\}$.
Now every element of $R$ is uniquely $f(x)+cy$ with $c\in k$, and
$x^n(f+cy)=x^nf$, so the $x$-power torsion is $ky$ and the blow-up is
$\operatorname{Spec}k[x]$. Thus the embedded point is gone, $U$ is dense, and
the boundary is the Cartier divisor $x=0$, as in
Lemma [lemma-making-open-schematically-dense].
