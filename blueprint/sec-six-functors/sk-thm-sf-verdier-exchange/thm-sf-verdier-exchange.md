+++
id = "thm-sf-verdier-exchange"
kind = "theorem"
title = "Verdier-duality exchange"
order = 2171
uses = ["def-sf-datum", "def-sf-pf", "fix-cor-verdier-exchange", "lem-sf-mate", "lem-sf-tensor-hom", "thm-sf-comp-composition"]
+++
In the setting of [def-sf-datum], assume that $f:X\to Y$ and the
structure morphisms are exceptional-adjoint admissible. Then for
$M\in D^b_{ctf}(X,\Lambda)$ there is a canonical isomorphism

$$
D_Y(Rf_!M)\xrightarrow{\ \sim\ }Rf_*D_X(M),
$$

natural in $M$, compatible with finite reduction, scalar extension, and
shifts. ([fix-cor-verdier-exchange]; the difference from
the compiled chapter is that the proof below uses only
[lem-sf-tensor-hom] and never the duality chapter, which removes the
cycle recorded in [rem-sf-yoga].)

## Proof

The operations are those of the six-functor datum of [def-sf-datum],
its projection transformation is [def-sf-pf], and the mate calculus
is that of [lem-sf-mate]; the formal core is
[fix-cor-verdier-exchange].
Step 1: $Rf^!\omega_Y\cong\omega_X$. By axiom (A4) and
[lem-sf-mate], the mate of the composition law [thm-sf-comp-composition]
$R(a_Y\circ f)_!\cong Ra_{Y!}Rf_!$ is the isomorphism
$Rf^!Ra_Y^!\cong Ra_X^!$, i.e. $Rf^!\omega_Y\cong\omega_X$. Step 2: apply
[lem-sf-tensor-hom] with $N=\omega_Y$ (an object of
$D^b_{ctf}(Y,\Lambda)$) and substitute Step 1:

$$
D_Y(Rf_!M)=R\mathcal H om_Y(Rf_!M,\omega_Y)
\cong Rf_*R\mathcal H om_X(M,f^!\omega_Y)
\cong Rf_*R\mathcal H om_X(M,\omega_X)=Rf_*D_X(M).
$$

Step 3: naturality and the compatibilities are those of
[lem-sf-tensor-hom] and of the mate construction of
[lem-sf-mate].
