+++
id = "sk-thm-curveestimate"
kind = "proposition"
title = "Smooth proper curves with invertible torsion"
order = 881
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-def-curve", "sk-def-kummer", "sk-def-pic", "sk-prop-cd", "sk-prop-h1", "sk-prop-h2", "sk-prop-jacobian", "sk-thm-av-final", "sk-thm-picard-duality", "sk-thm-picard-rr", "sk-thm-br", "sk-prop-kummer-exact", "sk-cor-picard-degree", "sk-prop-av-ntorsion-etale", "sk-prop-sf-comparison"]
lean = ["AlgebraicGeometry.IsCurve.nonempty_addEquiv_sheafH_constantZMod_zero", "AlgebraicGeometry.IsCurve.nonempty_addEquiv_sheafH_constantZMod_one", "AlgebraicGeometry.IsCurve.nonempty_addEquiv_sheafH_constantZMod_two", "AlgebraicGeometry.IsCurve.subsingleton_sheafH_of_three_le"]
tags = ["sketch"]
+++
Let $C$ be smooth, proper and connected over an algebraically closed field
$k$, with genus $g$, and let $n\geq1$ be invertible in $k$. Write
$J=\operatorname{Pic}^0_{C/k}$. There are canonical identifications

$$
\begin{aligned}
H^0(C,\mu_n)&=\mu_n(k),&
H^1(C,\mu_n)&=J[n](k),\\
H^2(C,\mu_n)&=\Z/n,&
H^q(C,\mu_n)&=0\quad(q>2).
\end{aligned}
$$

The degree-two isomorphism sends the Kummer boundary of a line bundle $L$ to
$\deg L\bmod n$. These identifications commute with extension of
algebraically closed fields.
