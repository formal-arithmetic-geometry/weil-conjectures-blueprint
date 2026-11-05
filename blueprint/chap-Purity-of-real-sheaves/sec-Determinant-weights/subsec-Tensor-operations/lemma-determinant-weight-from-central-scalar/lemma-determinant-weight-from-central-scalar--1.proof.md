+++
kind = "proof"
of = "lemma-determinant-weight-from-central-scalar--1"
order = 1142002
uses = ["lemma-normality-geometric-monodromy", "proposition-central-element-arithmetic-monodromy-group", "corollary-determinant-weights"]
+++
The inclusion $H\subseteq G$ is part of
[lemma-normality-geometric-monodromy]. Every element of $G(k)$ preserves
$U$ and $S$, since preservation of a subspace is a closed condition.
It therefore acts on $Q$.

Choose a basis of $Q$, lift its vectors to $S$, and extend its coordinate
forms to $k^n$. The determinant of the matrix obtained by applying these
forms to the images of the lifts is a polynomial $p$ on $\GL(k^n)$.
For any matrix preserving $U$ and $S$, its value is the determinant of
the induced endomorphism of $Q$. This is
`Matrix.GeneralLinearGroup.exists_evalAlgHom_eq_det_of_mk_eq`.

Let $A=\delta_Q(P)\subseteq k^\times$, a finite subgroup by hypothesis.
The polynomial $\prod_{a\in A}(p-a)$ vanishes on $\rho(P)$, hence on
$H$. Thus $p(h)\in A$, by
`Matrix.GeneralLinearGroup.evalAlgHom_mem_of_mem_zeroLocus_vanishingIdeal`.
Choose $u\in P$ with $p(h)=\delta_Q(u)$. Taking determinants in
$z=h\rho(s)^N$, and using the scalar action on $Q$, gives

$$
c_Q^{\dim_k Q}=\delta_Q(u)\delta_Q(s)^N.
$$

Since $\delta_Q(u)$ has finite order, $\lambda(\delta_Q(u))=0$;
this is `Representation.toAdd_apply_detCharacter_eq_zero`.
Applying $\lambda$ to the equality and dividing by
$N\dim_k Q>0$ proves the formula.

For a representation on an arbitrary finite-dimensional vector space,
choose a basis and transport its subquotients to $k^n$. The determinant
character and dimension are preserved, giving
`AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.detWeight_eq_of_isPositiveCentralPair_of_basis`.
In the tensor and exterior-power applications, Lean first transports
the positive central pair along the corresponding polynomial
representation, using the transport in
[proposition-central-element-arithmetic-monodromy-group], and applies
this formula to the resulting datum. For the Weil representations here,
take $k=\overline{\mathbf Q}_\ell$ and $\lambda=\lambda_\iota$;
the finite geometric determinant is supplied by
[corollary-determinant-weights].
