+++
kind = "proof"
of = "corollary-plancherel--1"
order = 1238003
uses = ["prose-16-08", "theorem-grothendieck-lefschetz-trace-formula", "proposition-function-sheaf-dictionary", "lemma-artin-schreier-character-sheaf"]
+++
Identify the rational points of $\mathbf A^r$ with
$\mathbf F_{q^n}^r$. The Fourier trace formula (16.3) in [prose-16-08],
formalized as
`AlgebraicGeometry.WeilComplex.traceFunction_affineSpaceFourierTransform`,
identifies the trace function of the transform with $(-1)^r$ times
the classical Fourier transform of $t_{K,n}$. The sign has absolute
value one, so it disappears after taking squared absolute values.

Apply the classical Plancherel identity
`FiniteField.sum_norm_sq_fourierTransformPi`. Its proof expands each
squared absolute value into a double sum. Character values have
absolute value one, and conjugation inverts them
(`FiniteField.conj_ringHom_compTrace`), so the inner sum is

$$
\sum_y\iota\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}
\langle x-z,y\rangle\bigr).
$$

The orthogonality relation
`FiniteField.sum_compTrace_sum_sub_mul` computes this as
$\#\mathbf F_{q^n}^{\,r}$ if $x=z$ and zero otherwise: write the sum
as a product of the one-dimensional character sums, one for each
coordinate. Thus only the diagonal terms survive. Finally,
$\#\mathbf F_{q^n}=q^n$ gives the factor $q^{nr}$.
