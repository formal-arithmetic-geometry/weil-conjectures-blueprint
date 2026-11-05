+++
kind = "proof"
of = "theorem-pure-lisse-sheaves-over-relative"
order = 1346
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "theorem-grothendieck-lefschetz-trace-formula", "theorem-trace-formula-euler-product", "lemma-bounding-weights-mixed-sheaf", "proposition-weights-under-usual-operations", "lemma-degree-zero-top-cohomology", "lemma-boundary-stalk", "lemma-point-count-bound", "lemma-extreme-degrees-affine-curve", "lemma-cohomological-range-curve", "proposition-twisting-weight-zero-adding-dual", "lemma-unramified-at-infinity-no-linear-characters", "corollary-h-1-c-stalk-fourier", "proposition-exactness-fixed-pure-weight", "lemma-finite-quasi-finite-direct-images", "theorem-real-constructible-sheaves-are-mixed"]
+++
We bound the stalks of $R^ih_!F$ by the curve case, we show that these
sheaves are mixed by twisting to weight zero and adding the dual, and
we combine the two facts using
Lemma [lemma-bounding-weights-mixed-sheaf].

*The stalks.* Fix a closed point $y$ of $Y_0$. Base change for
direct images with compact support
(Proposition [proposition-composition-base-change-rf-shriek]) gives
an identification

$$
(R^ih_!F)_{\bar y}=H_c^i(U_{\bar y},F)
$$

compatible with the local Frobenius operators. The restriction of $F$ to
the fibre is again pure of weight $w$, because a residue extension
raises both an eigenvalue and the residue cardinality to the same
power. The fibre is a smooth affine curve over $\kappa(y)$, so
Theorem [theorem-weight-bound-curve] shows that $H_c^i(U_{\bar y},F)$ has
weights at most $w+i$. After a finite extension of $\kappa(y)$ the
components of the fibre are geometrically connected.
Lemma [lemma-extreme-degrees-affine-curve], applied to each of them
with $j$ the identity, shows that these groups vanish outside degrees
$1$ and $2$.

*Mixedness.* We prove that $R^ih_!F$ is mixed. This is trivial
for $F=0$, so we may assume $F\ne0$. Let $G=F^0\oplus(F^0)^\vee$, with
$F^0=F\otimes\mathcal B_b$, be the sheaf of
Proposition [proposition-twisting-weight-zero-adding-dual]. It is
lisse, real and pure of weight zero. At a closed point $y$
write

$$
P_{i,y}(T)=\det(1-T\operatorname{Frob}_y\mid H_c^i(U_{\bar y},G)).
$$

Applying Lemma [lemma-extreme-degrees-affine-curve] to the components of the
fibre after a finite extension of $\kappa(y)$, as above, we see that
$P_{0,y}=1$ and that every reciprocal root of $P_{2,y}$ has modulus
$q_y$. By the bound just proved, every reciprocal root of $P_{1,y}$
has modulus at most $q_y^{1/2}$.

We claim that $\iota P_{1,y}$ and $\iota P_{2,y}$ have real
coefficients. By the Euler product and the determinant identity of
Theorem [theorem-trace-formula-euler-product], after applying $\iota$ we have

$$
L_\iota(U_y,G,T)=\frac{\iota P_{1,y}(T)}{\iota P_{2,y}(T)}.
$$

Since the Euler factors are real, this rational function has real
Taylor coefficients. Both it and its complex conjugate are regular at
zero, so they are equal as rational functions. Moreover, the numerator and the
denominator are coprime: a common root would give an eigenvalue having
both permitted moduli, whereas $q_y^{1/2}<q_y$. Since a reduced fraction whose
numerator and denominator have constant coefficient one is unique,
comparing it with its conjugate we find
$\iota P_{1,y},\iota P_{2,y}\in\mathbf R[T]$, which proves the claim.
Without the curve case this step would fail, because a common factor of
numerator and denominator could cancel, and we would only know that the
quotient is real, not each polynomial.

The sheaves $R^ih_!G$ are constructible by the finiteness theorems,
and we have shown that they are real at every closed point. By
Theorem [theorem-real-constructible-sheaves-are-mixed] each of them
has a finite mixed filtration.

To return from $G$ to $F$, note that by additivity $R^ih_!F^0$ is a
direct summand of $R^ih_!G$. A direct summand is a Weil subsheaf, and
so it is mixed by
Proposition [proposition-weights-under-usual-operations]. By the
projection formula for the constant twist, it is isomorphic to
$R^ih_!F\otimes\mathcal B_b$. Removing the twist preserves the finite
Weil filtration and shifts the weight of every pure quotient by $w$.
Hence $R^ih_!F$ is mixed.

*Conclusion.* The sheaf $R^ih_!F$ is mixed, and by the bound on the
stalks all its local eigenvalues have modulus at most $q_y^{(w+i)/2}$.
Lemma [lemma-bounding-weights-mixed-sheaf], with
$w+i$ in place of $w$, shows that every nonzero quotient in the
filtration has weight at most $w+i$.
