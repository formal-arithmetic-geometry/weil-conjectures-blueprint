+++
kind = "proof"
of = "corollary-determinant-weights--2"
uses = ["corollary-determinant-weights--1"]
+++
The finite subgroup $\det\rho(\ker\deg)$ consists of elements of finite
order. If $\det\rho(u)^n=1$ with $n>0$, applying $\lambda$ gives
$n\lambda(\det\rho(u))=0$, and hence $\lambda(\det\rho(u))=0$
(`Representation.toAdd_apply_detCharacter_eq_zero`). Expanding the
determinant character and $\lambda$ on $us$ therefore leaves the
numerator unchanged, and division by $r$ gives the identity.

For the Weil representation, [corollary-determinant-weights--1] supplies
the finite geometric determinant. The real character is
$\lambda_\iota(c)=2\log_q|\iota(c)|$; its determinant weight is the
quotient in [definition-determinant-weight]
(`AlgebraicGeometry.WeilGroup.detWeight_weightCharacter`). If $s'$ is
another degree-one lift, put $u=s's^{-1}$, which has degree zero, and
apply the identity to $s'=us$.
