+++
id = "prose-10-01"
kind = "hidden"
title = "Verdier and Poincaré duality"
order = 821
+++
The main estimate in the proof of the Deligne–Laumon theorem, the goal of
Part III, is an upper bound: every Frobenius eigenvalue on $H^i$ of a smooth proper variety has
absolute value at most $q^{i/2}$. The lower bound comes from Weil's axiom (c).
Suppose that the cup product pairs $H^i$ with $H^{2d-i}$ perfectly and that
Frobenius multiplies the pairing by $q^d$. Then the eigenvalues $\alpha$ in
degree $i$ correspond to the eigenvalues $q^d/\alpha$ in degree $2d-i$, so the
upper bound for $q^d/\alpha$ is a lower bound for $\alpha$
(Section [chap-Proof-of-the-Weil-conjectures]). The same relation gives the functional
equation of the zeta function (Corollary [corollary-functional-equation]). This
chapter proves axiom (c).

For the elliptic curve $y^2=x^3-x$ over $\mathbf F_3$ of the introduction,
duality says that the two eigenvalues on $H^1$ have product $3$
(Example [example-running-example-duality]), but it does not bound them
separately.

For a compact oriented manifold $M$ of dimension $n$ the model is Verdier's.
Let $a:M\to\mathrm{pt}$ be the map to a point. Then $\omega_M=a^!\mathbf Z$ is
the orientation sheaf placed in degree $-n$, and the functor
$\mathbb D=\cHom(-,\omega_M)$ is an involution on constructible complexes.
Duality is the isomorphism
$R\Gamma(M,\mathbb DK)\simeq R\!\operatorname{Hom}(R\Gamma_c(M,K),\mathbf Z)$.

We follow the same route. For a scheme $X$ with structure map
$a_X:X\to s=\operatorname{Spec}k$, put $\omega_X=a_X^!\Lambda_s$ and
$\mathbb D_X=\cHom(-,\omega_X)$
(Definition [definition-verdier-dual-evaluation]). The adjunction
$Ra_{X!}\dashv a_X^!$ gives for free a pairing of $R\Gamma_c(X,K)$ with
$R\Gamma(X,\mathbb D_XK)$, and it also gives two exchange formulas

$$
\mathbb D_YRf_!\simeq Rf_*\mathbb D_X,\qquad
f^!\mathbb D_Y\simeq\mathbb D_Xf^*
$$

(Lemma [lemma-internal-adjunction-two-exchange-formulas]). Over an algebraically
closed field the first formula, for $a_X$, is global duality,
$R\Gamma(X,\mathbb D_XK)\simeq R\!\operatorname{Hom}_\Lambda(R\Gamma_c(X,K),\Lambda)$
(Theorem [theorem-global-verdier-duality]). For smooth $X$ of pure dimension
$d$, smooth purity gives $\omega_X\simeq\Lambda_X(d)[2d]$, and global duality
becomes Poincaré duality: the pairing

$$
R\Gamma_c(X,K)\otimes^{\mathbf L}R\Gamma(X,K^\vee(d))[2d]
\longrightarrow\Lambda,\qquad K^\vee=\cHom(K,\Lambda_X),
$$

built from evaluation and the trace map, is perfect
(Theorem [theorem-poincare-duality]).

For $X$ smooth, proper and connected and $\Lambda$ a field, this will give a
perfect cup product pairing
$H^i\times H^{2d-i}\to\Lambda(-d)$ compatible with Frobenius
(Corollary [corollary-cup-product-pairing] and
Theorem [theorem-poincare-duality-frobenius] in Section [sec-Weil-complexes]).

What the adjunction does not give is that the pairing is perfect. For that we need
Verdier biduality: the map $K\to\mathbb D_X\mathbb D_XK$ is an isomorphism for every
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and every admissible $\Lambda$
(Theorem [theorem-verdier-biduality]). Then $\mathbb D_X$ is an anti-equivalence, and
applying the first two exchange formulas to $\mathbb D_XK$ gives the other two,
$\mathbb D_YRf_*\simeq Rf_!\mathbb D_X$ and $\mathbb D_Xf^!\simeq f^*\mathbb D_Y$
(Corollary [corollary-verdier-exchange-formulas]).

Biduality cannot be proved by dévissage, because dualizing a piece $t_!P$,
with $P$ locally constant on a smooth stratum $t:T\hookrightarrow X$, twice needs the exchange formula $\mathbb D_XRt_*\simeq t_!\mathbb D_T$, which
is itself a consequence of biduality (Section [sec-Verdier-biduality]). We argue
instead by induction on dimension, restricting to the geometric generic fibre of
a function, where duality commutes with restriction up to the twist $(1)[2]$
(Lemmas [lemma-restriction-geometric-generic-fibre]
and [lemma-double-dual-geometric-generic-fibre]).

Global duality was announced by Verdier and proved by Deligne
[sga4, XVIII]. Biduality for constructible complexes over a field is due to
Deligne [sga4-5, Th. finitude].

A perfect pairing of complexes induces perfect pairings of cohomology modules
over a field (Corollary [corollary-degreewise-duality-over-fields]), but not
over $\mathcal O_E$ (Remark [remark-duality-cohomology-groups-over-oe]).
For this reason we formulate the duality statements in the derived category, as perfect pairings of
perfect complexes (Definition [definition-perfect-pairing]).
