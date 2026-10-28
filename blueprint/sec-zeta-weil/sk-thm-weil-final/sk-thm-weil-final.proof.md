+++
kind  = "proof"
of    = "sk-thm-weil-final"
+++
For (1) and (2), we identify the odd and even products of the $P_{i,\ell}$
with the polynomials $A$ and $B$ of the reduced expression $Z=A/B$ of
[sk-lem-wweil-integer-rationality], show that each root of these integral
polynomials has absolute value $q^{i/2}$ under every complex embedding, and
then regroup the roots by this absolute value.

Fix a prime $\ell\nmid q$. By [sk-input-weights], the reciprocal roots of
$P_{i,\ell}$ have $\iota$-modulus $q^{i/2}$. Since distinct degrees
give distinct moduli, the polynomials $P_{i,\ell}$ are pairwise
coprime. In particular, the products of the $P_{i,\ell}$ over odd and
over even degrees form a reduced fraction with constant coefficients
one. Let $Z(X_0,T)=A/B$ with coprime $A,B\in\mathbf Z[T]$ and
$A(0)=B(0)=1$, as fixed in [sk-lem-wweil-integer-rationality]. By the
determinant identity of [sk-cor-tf-point-counting] and the uniqueness of
reduced fractions over $\mathbf Q_\ell$, we get

$$
 A=\prod_{i\ \mathrm{odd}}P_{i,\ell},\qquad
 B=\prod_{i\ \mathrm{even}}P_{i,\ell}
 \quad\hbox{in }\mathbf Q_\ell[T].
$$

Write $A(T)=\prod_a(1-aT)$ and $B(T)=\prod_b(1-bT)$ over
$\overline{\mathbf Q}$. The reciprocal roots $a$ and $b$ are roots of the
monic integral polynomials $U^{\deg A}A(U^{-1})$ and $U^{\deg B}B(U^{-1})$,
and hence they are nonzero algebraic integers. Choose an embedding
$\theta:\overline{\mathbf Q}\hookrightarrow\Qlb$. By the last display and
the pairwise coprimality of the $P_{i,\ell}$, for every reciprocal root $a$
of $A$ or $B$ there is exactly one $i$ such that $\theta(a)$ is a Frobenius
eigenvalue on $H^i_\ell$.

*Absolute values.* Let $\tau:\mathbf Q(a)\hookrightarrow\mathbf C$
be any embedding. We
claim that $\tau\circ\theta^{-1}$, defined on $\theta(\mathbf Q(a))$,
extends to a field isomorphism $\iota':\Qlb\xrightarrow{\sim}\mathbf C$.
This holds because both are algebraically closed fields of
characteristic zero with transcendence degree $2^{\aleph_0}$ over
$\mathbf Q$. Since $\iota'(\theta(a))=\tau(a)$, applying
[sk-input-weights] with this $\iota'$ to the
eigenvalue $\theta(a)$ on $H^i_\ell$, we find

$$
 |\tau(a)|=q^{i/2}.
$$

Thus $a$ has absolute value $q^{i/2}$ under every complex embedding,
and since $q>1$ this determines $i$.

*The factors.* For odd $i$, let $R_i$ be the submultiset of the
reciprocal roots of $A$
whose absolute value under every complex embedding is $q^{i/2}$, and
for even $i$ define $R_i$ in the same way using the reciprocal roots of $B$.
These multisets are Galois-stable, with
multiplicities, and the condition on all complex embeddings is
Galois-invariant. Hence each $R_i$ is Galois-stable. Put

$$
 P_i(T)=\prod_{a\in R_i}(1-aT).
$$

The coefficients of $P_i$ are rational by Galois invariance, and they
are algebraic integers because the roots satisfy monic integral
equations. Hence they are integers. For the chosen $\ell$, the root
multiset of $P_i$ is exactly that of $P_{i,\ell}$, and since both have
constant coefficient one, $P_i=P_{i,\ell}$. For any other prime, the
same argument identifies the factor in degree $i$ with the same
submultiset of the reciprocal roots of $A$ or $B$, so $P_i$ does not depend
on the prime. Comparing with a single $P_{i,\ell}$ also proves
uniqueness, and the product formula for $Z(X_0,T)$ in (1) is the
determinant identity above.

The remaining assertions follow from Poincaré duality and the
functional equation of [sk-cor-tf-functional-equation]. For (3), since
$P_i=P_{i,\ell}$, we have $b_i=\deg P_i=\dim_{\Ql}H^i_\ell$, which does not
depend on $\ell$, and $b_i=b_{2d-i}$ by
[sk-cor-tf-functional-equation].

For the second part of (3), since $X_0$ is geometrically connected, $X$ is
connected. By [sk-cor-trace], $H^0(X,\Ql)=\Ql$, with Frobenius acting as the
identity, and the trace map $\operatorname{tr}_X$ identifies
$H^{2d}(X,\Ql)$ with $\Ql(-d)$, on which Frobenius acts by $q^d$. Hence
$b_0=b_{2d}=1$, $P_0=1-T$ and $P_{2d}=1-q^dT$.

[sk-cor-tf-functional-equation] gives (4) in $\Ql(T)$.
This is an identity in $\mathbf Q(T)$, because the
zeta function is rational over $\mathbf Q$ and the scalar
$\varepsilon q^{d\chi/2}$ is a rational number.
