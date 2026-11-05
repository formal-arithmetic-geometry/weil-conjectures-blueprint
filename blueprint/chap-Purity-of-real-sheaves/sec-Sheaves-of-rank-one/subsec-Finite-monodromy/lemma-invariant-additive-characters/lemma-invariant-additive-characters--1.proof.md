+++
kind = "proof"
of = "lemma-invariant-additive-characters--1"
order = 1101002
uses = ["proposition-no-fixed-class-degree-one"]
+++
First suppose that $a$ takes values in $\mathbf Z_\ell$. Conjugation by
an element of $\pi_1(U)$ does not change an additive homomorphism, and
invariance under $s$ implies invariance under every power of $s$.
Since every element of $W$ is a product of a geometric element and a
power of $s$, the character is invariant under conjugation by every
element of $W$. This is
`AlgebraicGeometry.WeilGroup.conj_invariant_of_conj_invariant_frobeniusLift`.
It ensures that the character transported to the chosen fundamental
group is fixed by the Frobenius action in the identification above.

Reduce $a$ modulo $\ell^n$. These reductions form a compatible system
of continuous characters with values in $\mathbf Z/\ell^n$, by
`PadicInt.continuousMonoidHomEquiv`. Each is the monodromy character of
a finite étale $\mathbf Z/\ell^n$-torsor $T_n$, by
`AlgebraicGeometry.Scheme.EtaleTorsor.exists_monodromy_eq`.
Transport by geometric Frobenius precomposes monodromy with the
Frobenius action on the fundamental group
(`AlgebraicGeometry.Scheme.EtaleTorsor.monodromy_mapIso`). Thus the
transported torsor has the same monodromy as $T_n$, and is isomorphic
to it by `AlgebraicGeometry.Scheme.EtaleTorsor.isIsomorphic_of_monodromy_eq`.

Apply Proposition [proposition-no-fixed-class-degree-one] to this
compatible system of Frobenius-fixed torsors. Its Lean form,
`AlgebraicGeometry.Scheme.EtaleTorsor.exists_section_of_isIsomorphic_mapIso`,
gives a section of each $T_n$. A torsor with a section has zero
monodromy, by
`AlgebraicGeometry.Scheme.EtaleTorsor.monodromy_eq_one_of_section`.
Hence every reduction of $a$ is zero, and $a=0$ because an element of
$\mathbf Z_\ell$ is determined by its reductions. Transport back
along the identification with the geometric subgroup to obtain the
integral assertion.

For $a$ with values in $\mathbf Q_\ell$, compactness of $\pi_1(U)$
implies that its image is bounded. Choose $m\ge0$ so that
$\ell^m a$ takes values in $\mathbf Z_\ell$. It is continuous and
invariant under conjugation by $s$, so the integral assertion gives
$\ell^m a=0$. Since $\ell^m\ne0$ in $\mathbf Q_\ell$, this gives
$a=0$.
