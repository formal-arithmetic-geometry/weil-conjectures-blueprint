+++
kind = "proof"
of = "det-pe-condensed-point-coefficients"
+++
By [sk-def-sfb-pullback-from-point], $p_X^*$ is left adjoint to the functor
$G\mapsto(S\mapsto G(X[S]))$, which is restriction along $S\mapsto X[S]$. By
[det-pe-condensed-point-basis] this functor is $S\mapsto\Omega[S]$, and by
[det-pe-condensed-point-topology] restriction along it is an equivalence of
topoi. The left adjoint of an equivalence is its quasi-inverse, so
$(p_X^*F)(\Omega[S])\cong F(S)$, naturally in $S$; for rings the ring structures
agree because the identification is natural and compatible with finite
products.

(1) is the definition $\underline T(S)=C(S,T)$ of [sk-def-sfb-condensed-ring].
(2) For discrete $A$, a continuous map from the compact space $S$ to $A$ is
locally constant, so $C(S,A)=LC(S,A)=\varinjlim_iA^{S_i}$. On the other hand,
$\Omega[S]=\varprojlim_i\Spec\Omega^{S_i}$ is a pro-étale affine presentation with
$A_{X,\Et}(\Spec\Omega^{S_i})=A^{S_i}$, so the affine evaluation formula of
[sk-prop-pe-comparison-morphism] gives
$(\nu_X^*A_{X,\Et})(\Omega[S])=\varinjlim_iA^{S_i}$, compatibly with restriction.
Both sheaves agree on the basis, hence agree.
