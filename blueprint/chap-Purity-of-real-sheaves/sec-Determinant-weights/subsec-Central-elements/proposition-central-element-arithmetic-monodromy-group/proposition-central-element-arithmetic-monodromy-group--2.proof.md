+++
kind = "proof"
of = "proposition-central-element-arithmetic-monodromy-group--2"
order = 1138004
uses = ["definition-monodromy-groups"]
+++
Pulling back equations along $\varphi$ shows that $r$ sends $G(k)$ into
$G'(k)$ and $H(k)$ into $H'(k)$. This is
`Matrix.GeneralLinearGroup.map_mem_zeroLocus_vanishingIdeal`.
Since $z$ commutes with $\rho(W)$, the element $r(z)$ commutes with
$\rho'(W)$. The commutator equations are closed, so it commutes with
$G'(k)$, by
`Matrix.GeneralLinearGroup.commute_of_mem_zeroLocus_vanishingIdeal`.
Finally, writing $z=h\rho(s)^N$ and applying $r$ gives the required
coset relation with the same positive integer $N$.

For preservation, the stabilizer of a subspace $S\subseteq k^m$ is cut
out by the equations $\lambda(gx)=0$ for $x\in S$ and linear forms
$\lambda$ vanishing on $S$. If $S$ is stable under $\rho'(W)$, those
equations vanish on its Zariski closure $G'$. Thus every element of
$G'(k)$ preserves $S$, and an element preserving both $U$ and $S$
induces an endomorphism of $S/(S\cap U)$.

For the last assertion, restrict $f$ to $S$ and pass to the quotient.
The commutation hypothesis makes the induced map an endomorphism of the
$W$-representation. Schur's lemma over the algebraically closed field
$k$ identifies it with multiplication by some $c\in k$. Lifting the
equality back to $S$ gives $f(x)-cx\in U$.

In the weight arguments Lean applies this to the exterior-power and
Kronecker-square homomorphisms. The transported positive central pair
supplies membership in $G'(k)$ and commutation with $\rho'(W)$ through
`IsPositiveCentralPair.mem_zeroLocus_arithmeticMonodromy` and
`IsPositiveCentralPair.commute`. The version in an arbitrary basis is
`AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.toLin_apply_mem_of_mem_zeroLocus_arithmeticMonodromy`.
