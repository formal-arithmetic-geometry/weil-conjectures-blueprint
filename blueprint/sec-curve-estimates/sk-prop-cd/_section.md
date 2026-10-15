+++
id = "sk-prop-cd"
kind = "proposition"
title = "Vanishing in high degrees"
order = 995
uses = ["sk-def-av-pic", "sk-def-br", "sk-def-curve", "sk-prop-hilbert90", "sk-prop-kummer-exact", "sk-prop-tsen"]
lean = ["AlgebraicGeometry.IsCurve.subsingleton_sheafH_of_three_le"]
tags = ["sketch"]
+++
For $C$ as in [sk-def-curve], $n$ prime to $\operatorname{char}k$,
and every sheaf $F$ of $\Z/n$-modules on $C_{\Et}$ (more generally
every torsion sheaf whose torsion is prime to $\operatorname{char}k$):
$H^q(C,F)=0$ for $q\ge3$ (the étale cohomological dimension of a
curve over an algebraically closed field is $\le2$; the sharper
bound $\le1$ for $C$ affine is [sk-prop-cd-affine], and the
$p$-primary bound in characteristic $p$ goes through the
Artin–Schreier sequence). Consequently, for a complex $F$ in
$D^b(C_{\Et},\Z/n)$ with $\mathcal H^i(F)=0$ for $i>b$, one has
$H^q(C,F)=0$ for $q>b+2$; the shift cannot be dropped, since
$F=(\Z/2)[-3]$ on $\Pone$ has $H^3(\Pone,F)=H^0(\Pone,\Z/2)\neq0$.
