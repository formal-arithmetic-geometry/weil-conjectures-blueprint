+++
kind = "proof"
of = "lem-weil-pbc-integral-idempotent-annihilating-polynomial"
+++
*$z=b^2-b$ lies in $IB$.* The kernel of the quotient map $B\to B/IB$ is $IB$. The image $\bar b$ of $b$ is idempotent, so the image of $z=b^2-b$ is $\bar b^2-\bar b=0$, i.e. $z\in IB$.

Apply Mathlib Polynomial.exists_monic_aeval_eq_zero_forall_mem_of_mem_map to z = b^2 - b to obtain monic g with g(z) = 0 and every non-leading coefficient in I. Coefficientwise reduction gives g.map (Ideal.Quotient.mk I) = X^g.natDegree. Set h = X*g and d = g.natDegree + 1, so d is positive and h is monic, h(z) = 0, and h reduces to X^d. This also handles degree-zero g without a separate case. (`Polynomial.exists_monic_aeval_eq_zero_forall_mem_of_mem_map` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Ideal.lean))).

For nontrivial A, put q = X*(X-1) and f = (X*g).comp q. The product q is monic with positive degree; Polynomial.Monic.comp makes f monic. Polynomial.aeval_comp and q(b) = b^2-b show f(b) = 0. Polynomial.map_comp and the reduction of g show f modulo I equals q^d = X^d*(X-1)^d. If A is the zero ring, B is also the zero ring via its algebra map; choose d = 1 and f = 1, and all equalities follow from subsingleton elimination.
