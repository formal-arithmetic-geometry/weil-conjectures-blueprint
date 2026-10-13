+++
kind  = "proof"
of    = "lem-pur-divisor-class"
+++
Use the frame class of [def-pur-frame-class], independent of the local equation by [lem-pur-frame-independence], and the support boundary of [def-pur-support-cohomology] applied to the Kummer datum of [def-pur-affine-line-datum].
(a) is (def. frame class) $\operatorname{cl}(f)=\partial(\kappa(f))$.
For (b), the sum of two effective divisors $D_1,D_2$ has a frame
$(f_1,f_2)$ on an intersection of the two trivializing opens, and
$\kappa(f_1f_2)=\kappa(f_1)+\kappa(f_2)$ by
[lem-pur-kummer-additivity], so
$\operatorname{cl}(D_1)+\operatorname{cl}(D_2)$ is the class of the
frame $(f_1f_2)$. The forget-support statement is the standard
computation of the Kummer boundary of the group law of
$\operatorname{Pic}$: on a trivializing open the class
$\operatorname{cl}(D)$ is the boundary of the Kummer class of the
inverse image of the line bundle $\mathcal O_T(D)$'s unit section on
$T\setminus D$, hence its image in $H^2(T,\Lambda(1))$ is
$c_1(\mathcal O_T(D))$ of [lem-pur-kummer-additivity] (the
boundary maps in the two long exact sequences to $H^2(T,\Lambda(1))$,
and both are the image of the same class of $H^1(T,\mathbf G_m)$;
the statement is local and follows from the sheaf-theoretic
description of $c_1$ via the Kummer sequence).
