+++
id = "prose-21-01"
kind = "hidden"
title = "Proof of the Weil conjectures"
order = 788
+++
Deligne's theorem bounds weights from above, and Poincaré duality
turns an upper bound into a lower one. For a curve this is already the
whole argument. If $X_0$ is a smooth projective curve and $\alpha$ is a
Frobenius eigenvalue on $H^1(X,\overline{\mathbf Q}_\ell)$, then
Theorem [sk-cor-dl-general-complex], applied to the constant sheaf,
gives $|\iota(\alpha)|\le q^{1/2}$. The cup product pairing
$H^1\times H^1\to H^2=\overline{\mathbf Q}_\ell(-1)$ is perfect and Frobenius multiplies it
by $q$, so $q/\alpha$ is also an eigenvalue, and the same bound for it
gives $|\iota(\alpha)|\ge q^{1/2}$. In general, let $X_0$ be smooth and
proper of pure dimension $d$. Every eigenvalue $\alpha$ on
$H^i(X,\overline{\mathbf Q}_\ell)$ satisfies $|\iota(\alpha)|\le q^{i/2}$, duality pairs it
with the eigenvalue $q^d/\alpha$ on $H^{2d-i}$, which satisfies
$|\iota(q^d/\alpha)|\le q^{(2d-i)/2}$, and so $|\iota(\alpha)|=q^{i/2}$
(Corollary [sk-input-weights]). We prove this in the relative
form, for $R^if_*$ of a pure lisse sheaf along a smooth proper morphism
(Theorem [sk-prop-smooth-proper-purity]), since the proof is the same.
This is Weil's axiom (d), and with it the Riemann hypothesis.

What remains is to pass from $\ell$-adic statements about one embedding
$\iota$ to the statements of Weil, which are about integers and all
complex embeddings. First, the reciprocal roots of
$P_{i,\ell}=\det(1-TF\mid H^i(X,\Ql))$ have absolute value $q^{i/2}$
under every complex embedding, and not only under those of the form
$\iota$: any embedding of a number field into $\mathbf C$ extends to an
isomorphism $\overline{\mathbf Q}_\ell\simeq\mathbf C$, to which
Corollary [sk-input-weights] applies. Next comes the zeta
function, which does not mention $\ell$. It is a rational function with
integer coefficients, so it has a unique reduced form $Z(X_0,T)=A/B$
with $A,B\in\mathbf Z[T]$ coprime and $A(0)=B(0)=1$
(Lemma [sk-lem-wweil-integer-rationality]). By the trace formula it is also
the alternating product of the polynomials $P_{i,\ell}$. Polynomials of
different degrees $i$ have no common root, by purity, so the odd and the
even products are already reduced, and they equal $A$ and $B$. Grouping
the reciprocal roots of $A$ and $B$ by absolute value recovers each
$P_{i,\ell}$ from $Z(X_0,T)$ alone. Hence $P_{i,\ell}$ has integer
coefficients and does not depend on $\ell$
(Theorem [sk-thm-weil-final]).

This regrouping needs purity. Without it the factors of the
zeta function can cancel, and the zeta function does not determine the
cohomology. For example, $X_0=\mathbf G_m\sqcup\operatorname{Spec}\mathbf F_q$
has $q^m$ points over $\mathbf F_{q^m}$, as many as $\mathbf A^1$, so
$Z(X_0,T)=1/(1-qT)$. Yet $H^0_c$ and $H^1_c$ are both one-dimensional
with eigenvalue $1$, and the factor $1-T$ cancels between them. For
smooth proper $X_0$ this cannot happen, because eigenvalues in different
degrees have different absolute values.

The section ends with the classical consequences: Hasse's theorem for
elliptic curves, the running example over $\mathbf F_3$
(Example [sk-ex-ex-run-end]), and the estimate
$|\#X_0(\mathbf F_{q^m})-(1+q^{dm})|\le\sum_{i=1}^{2d-1}b_iq^{mi/2}$ for a
smooth proper geometrically connected $X_0$, which for a curve of genus
$g$ is Weil's bound $2gq^{m/2}$ (Corollary [sk-cor-hasse]).
