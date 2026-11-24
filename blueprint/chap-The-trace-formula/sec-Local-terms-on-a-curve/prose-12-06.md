+++
id = "prose-12-06"
kind = "hidden"
title = "Local terms on a curve (1)"
order = 958
+++
The [local terms](@definition-trace-class-local-terms) of the [trace formula](@theorem-trace-formula-frobenius-correspondence) live on the [fixed point scheme](@definition-correspondence)
$\Fix(\href{@definition-frobenius-correspondences-their-operators}{\Phi_X^m})=\Fix(c_m)$ of the graph $c_m$. More precisely, a [local term](@definition-trace-class-local-terms) is defined on each open and closed part of this scheme that is proper over $k$. The next lemma
shows that the [fixed scheme](@definition-correspondence) is a finite reduced set of points, one for each
$\mathbf F_{q^m}$-rational point of $X_0$, so every such point has its own
[local term](@definition-trace-class-local-terms). For Frobenius on a smooth curve we then show that this [local term](@definition-trace-class-local-terms) is
the trace on the stalk.

On $\mathbf A^1$ the [fixed scheme](@definition-correspondence) of [$\Phi^m$](@definition-frobenius-correspondences-their-operators) is
$\operatorname{Spec}k[t]/(t^{q^m}-t)$. Its $q^m$ points are reduced
because $t^{q^m}-t$ has derivative $-1$. This is the algebraic form
of the transversality seen at the start of
Chapter [chap-The-trace-formula]. Reducedness alone does not determine the
[local term](@definition-trace-class-local-terms), because the stalk does not determine $\cHom(c_2^*K,\href{@theorem-existence-exceptional-inverse-image}{c_1^!K})$ near the
fixed point (Remark [remark-locality-warning] below).
