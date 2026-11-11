+++
kind = "proof"
of = "lemma-reciprocal-roots-zeta--1"
order = 1389003
uses = ["theorem-poincare-duality-frobenius", "theorem-trace-isomorphism-top-degree--8", "theorem-grothendieck-lefschetz-trace-formula--5", "theorem-trace-formula-euler-product--6", "corollary-point-counting-zeta-function--2", "corollary-point-counting-zeta-function--6", "corollary-purity-cohomology-smooth-proper-variety--1", "lemma-hankel-rank-rationality--1", "lemma-hankel-rank-rationality--2", "lemma-reduced-fractions-integer-coefficients--1"]
+++
The identity (19.2) holds because both sides
are reduced fractions for $Z(X_0,T)$ over $\mathbf Q_\ell$. By
Corollary [corollary-purity-cohomology-smooth-proper-variety], the
reciprocal roots of $P_{i,\ell}$ have absolute value $q^{i/2}$ under
every embedding $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$. Since $q>1$,
distinct degrees give distinct absolute values, and so the polynomials
$P_{i,\ell}$ are pairwise coprime. Their products over odd and over
even degrees are therefore coprime, and they have constant coefficients
one. By (19.1) their quotient is
$Z(X_0,T)$. On the other hand, $A$ and $B$ remain coprime in
$\mathbf Q_\ell[T]$, since a Bézout relation over $\mathbf Q$ remains
valid over $\mathbf Q_\ell$. The two reduced fractions agree by the
uniqueness argument in the proof of
Lemma [lemma-reduced-fractions-integer-coefficients], which works
over any field.

*Source:* the proof of Lemma [lemma-reciprocal-roots-zeta].
