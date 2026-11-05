+++
kind = "proof"
of = "theorem-weil-conjectures-smooth-proper-schemes"
order = 1389
uses = ["theorem-trace-isomorphism-top-degree", "corollary-cup-product-pairing", "corollary-point-counting-zeta-function", "corollary-functional-equation", "corollary-purity-cohomology-smooth-proper-variety", "lemma-hankel-rank-rationality", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
For (1) and (2), we define $P_i$ using only the reduced fraction $A/B$
of Lemma [lemma-reduced-fractions-integer-coefficients], by sorting
the reciprocal roots of $A$ and $B$ by absolute value, and then we
compare $P_i$ with $P_{i,\ell}$ by Lemma [lemma-reciprocal-roots-zeta].

For odd $i$, let $R_i$ be the submultiset of the reciprocal roots of $A$
whose absolute value under every complex embedding is $q^{i/2}$, and
for even $i$ define $R_i$ in the same way using the reciprocal roots of
$B$. By Lemma [lemma-reciprocal-roots-zeta], every reciprocal root
of $A$ or $B$ lies in exactly one $R_i$. The multisets of reciprocal
roots of $A$ and $B$ are Galois-stable, with multiplicities. The
condition on all complex embeddings is Galois-invariant, and so each
$R_i$ is Galois-stable. Put

$$
P_i(T)=\prod_{a\in R_i}(1-aT).
$$

The coefficients of $P_i$ are integers, being rational by Galois
invariance and algebraic integers because the roots satisfy monic
integral equations.

Now let $\ell\nmid q$ be any prime and
$\theta:\overline{\mathbf Q}\hookrightarrow\overline{\mathbf Q}_\ell$ an embedding. By
(19.2) and
Lemma [lemma-reciprocal-roots-zeta], the embedding $\theta$ maps
$R_i$ onto the multiset of Frobenius eigenvalues on $H^i_\ell$. Since
both polynomials have constant coefficient one, $P_i=P_{i,\ell}$ in
$\overline{\mathbf Q}_\ell[T]$, hence in $\mathbf Q_\ell[T]$. As $\ell$ was arbitrary,
this proves the existence in (1), and uniqueness follows by comparing with
a single $P_{i,\ell}$. The product formula for $Z(X_0,T)$ in (1) is then
(19.1), and assertion (2) is
Lemma [lemma-reciprocal-roots-zeta].

The remaining assertions follow from Poincaré duality and the
functional equation of Chapter [chap-The-trace-formula]. For (3), since
$P_i=P_{i,\ell}$, we have $b_i=\deg P_i=\dim_{\mathbf Q_\ell}H^i_\ell$, which does not
depend on $\ell$, and $b_i=b_{2d-i}$ by
Corollary [corollary-functional-equation].

For the second part of (3), assume that $X_0$ is geometrically
connected, so that $X$ is connected. By Theorem [theorem-trace-isomorphism-top-degree],
$H^0(X,\mathbf Q_\ell)=\mathbf Q_\ell$, with Frobenius acting as the identity, and the trace
map $\operatorname{tr}_X$ identifies $H^{2d}(X,\mathbf Q_\ell)$ with $\mathbf Q_\ell(-d)$, on
which Frobenius acts by $q^d$. So $b_0=b_{2d}=1$, $P_0=1-T$ and
$P_{2d}=1-q^dT$.

For (4), Poincaré duality pairs the eigenvalues on $H^i_\ell$ with
those on $H^{2d-i}_\ell$ by $\alpha\mapsto q^d/\alpha$. Substituting
$T\mapsto1/(q^dT)$ in the product formula therefore exchanges the
corresponding factors up to a monomial, and
Corollary [corollary-functional-equation] carries out this computation
and gives (4) in $\mathbf Q_\ell(T)$. Since the zeta function is rational over
$\mathbf Q$, and the scalar $\varepsilon q^{d\chi/2}$ is a rational
number, the identity holds in $\mathbf Q(T)$.
