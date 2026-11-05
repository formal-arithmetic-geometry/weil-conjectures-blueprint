+++
kind = "proof"
of = "proposition-determinant-weights-tensor-operations--2"
order = 1145006
uses = ["proposition-central-element-arithmetic-monodromy-group", "lemma-determinant-weight-from-central-scalar", "corollary-determinant-weights"]
+++
If $\deg=0$, all the determinant weights vanish. The nonzero subquotient
$Q$ forces $r\le\dim V$, so take $T$ to consist of $r$ zeros. Otherwise
replace $\deg$ by a surjective degree map with the same kernel and write
$\gamma=u\delta^m$ with $u$ in the kernel and $\delta$ of degree one.
It suffices to prove the assertion at $\delta$ and multiply the selected
weights by $m$.

Choose a basis of $V$ adapted to the direct sum. By
[proposition-central-element-arithmetic-monodromy-group] there is a positive
central pair $(N,z)$; on $A_a$, its action is multiplication by a scalar
$c_a$. By [lemma-determinant-weight-from-central-scalar], the determinant
weight of $A_a$ at $\delta$ is $\chi(c_a)/N$.

Transport the central pair along the exterior-power representation. In the
exterior basis, its eigenvalues are the products of $r$ distinct basis
scalars. Schur's lemma makes its action on $Q$ scalar, and that scalar is
an eigenvalue on $\bigwedge^rV$. It is therefore one of these products.
The central-scalar weight formula on $Q$ turns this product into a sum of
$r$ entries of the multiset of the weights at $\delta$. A summand $A_a$
contributes at most $\dim A_a$ entries. Mapping this submultiset by
$x\mapsto mx$ gives the required $T$.

For Weil representations the required finiteness follows from
[corollary-determinant-weights]. In the purity proof, Lean takes
$V=\bigoplus_a A_a$ to be the semisimplification of the original
representation and uses its characteristic polynomials; it does not
transfer the constituents of exterior powers from a nonsemisimple
representation.
