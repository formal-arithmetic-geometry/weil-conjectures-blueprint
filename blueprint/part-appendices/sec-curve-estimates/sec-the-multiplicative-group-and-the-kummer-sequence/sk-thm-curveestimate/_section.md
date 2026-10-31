+++
id = "sk-thm-curveestimate"
kind = "proposition"
title = "Smooth proper curves, torsion prime to the characteristic"
order = 913
lean = ["AlgebraicGeometry.IsConnectedCurve.sheafH_rootsOfUnitySheaf_canonical_of_isProper"]
uses = ["sk-thm-picard-main", "sk-prop-av-isogeny", "sk-def-picard-pic", "sk-prop-picard-pic-split", "sk-prop-av-tate-rank", "sk-thm-picard-rr", "sk-thm-br", "sk-cor-picard-degree", "sk-cor-jacobian-torsion", "sk-prop-sf-comparison"]
tags = ["sketch"]
+++
Let $C$ be smooth, proper and connected over an algebraically closed
field $k$, with genus $g$, and let $n\geq1$ be invertible in $k$.
There are canonical identifications

$$
\begin{aligned}
H^0(C,\mu_n)&=\mu_n(k),&
H^1(C,\mu_n)&=J(C)[n](k),\\
H^2(C,\mu_n)&=\mathbf Z/n,&
H^q(C,\mu_n)&=0\quad(q>2).
\end{aligned}
$$

The isomorphism in degree two sends the Kummer boundary of a line bundle
$L$ to $\deg L\bmod n$. These identifications commute with extension
of algebraically closed fields.
