+++
id = "sbc-lem-strict-henselian-constant-cohomology"
kind = "lemma"
title = "Constant-sheaf cohomology of a strictly henselian local scheme"
order = 5233
lean = ["AlgebraicGeometry.Etale.cohomology_constant_of_strictlyHenselian"]
+++
Let $(R,\mathfrak m)$ be a strictly henselian local ring, let
$X=\operatorname{Spec}R$, and let $A$ be a finite constant sheaf of order
invertible in $R$. Then
$$
H^q(X_{\Et},A)=\begin{cases}A,&q=0,\\0,&q>0.\end{cases}
$$

## Proof

A finite étale cover of $\operatorname{Spec}R$ is trivial: $R$ being
strictly henselian, every finite étale $R$-algebra is a finite product of
copies of $R$ (the Hensel property and connectedness of
$\operatorname{Spec}R$). Hence the étale site of $X$ is contractible for
finite coefficients of order invertible in $R$, and the constant sheaf $A$
is the pullback of the constant sheaf on a point:
$H^q(X_{\Et},A)=H^q(\mathrm{pt},A)$, zero for $q>0$ and $A$ for $q=0$
(*reference: Stacks Project, Étale Cohomology: the cohomology of a constant
sheaf on a strictly henselian local scheme*).

Unresolved dependencies: def:weil-pbc-etale-cohomology
