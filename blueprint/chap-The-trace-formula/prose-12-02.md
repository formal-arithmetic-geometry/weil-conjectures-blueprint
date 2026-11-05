+++
id = "prose-12-02"
kind = "hidden"
title = "The trace formula (2)"
order = 949
+++
For constant coefficients the local term at a transverse fixed point is $1$, so on a
proper $X$ transversality would be enough. Two
things stand in the way in general. First, $X$ need not be proper. If we
compactify, the new fixed points at the boundary have zero stalk for $j_!K$, and
we need their local terms to vanish. Second, a local term is computed from
$\cHom(c_2^*K,c_1^!K)$ near the fixed point, where $c_1,c_2$ are the two projections
of the graph of Frobenius to $X$ (Definition [definition-correspondence]). The
stalk $K_{\bar y}$ does not determine this complex
(Remark [remark-locality-warning]), so the vanishing of the local term at a
point where the stalk vanishes is a real statement, which transversality alone
does not give.

One computation on a curve settles both problems: Proposition [proposition-frobenius-local-term-curve] says that for any morphism
$\psi:(\Phi_X^m)^*K\to K$ on a smooth curve, the local term at a rational point $y$
is $\operatorname{tr}(\psi_{\bar y}\mid K_{\bar y})$. The proof, which is Grothendieck's [sga5, XV, §3], uses $d\Phi_X=0$ a second time: the graph $v=u^{q^m}$ is tangent to the axis $v=0$ and the diagonal is not, so blowing up
$(y,y)$ separates them, and near the exceptional divisor the local term becomes a
restriction map that vanishes when $K_{\bar y}=0$
(Remark [remark-outline-local-computation]). Since both sides of the formula
are additive along an open subscheme and its complement
(Lemma [lemma-additivity-open-subscheme-complement]) and compatible with
$Rf_!$ (Lemma [lemma-comparison-via-relative-frobenius]), we never need to
compactify anything but $\mathbf A^1\subset\mathbf P^1$.

The answer is Theorem [theorem-grothendieck-lefschetz-trace-formula]: for every
Weil complex $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ (Section [sec-Weil-complexes]), where
$\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$ and $A$ is a finite commutative
$\ell$-primary ring, and for every $m\geq1$, we have in $\Lambda$

$$
\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{X,K}^m\mid
R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{y,m}\mid
K_{\bar y}\bigr).
$$

Here $\operatorname{tr}_\Lambda$ is the trace of an endomorphism of a perfect complex
(Definition [definition-categorical-trace]), and $\operatorname{Frob}_{y,m}$ is the
$m$-th iterate of the Weil structure on the stalk at the fixed point $\bar y$. For
$K=\Lambda_X$ and $\Lambda$ a field the formula is Weil's axiom (b), and it
gives the rationality of the zeta
function (Corollary [corollary-point-counting-zeta-function]).

Purity, however, needs the formula for general $K$. For $\Lambda\in\{\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$, in the
form of an Euler product (Theorem [theorem-trace-formula-euler-product]), it reads

$$
\prod_{x\in|X_0|}\det\bigl(1-T^{\deg x}\operatorname{Frob}_x\mid K_{\bar x}\bigr)^{-1}
=\prod_i\det\bigl(1-T\operatorname{Frob}_{X,K}\mid H^i_c(X,K)\bigr)^{(-1)^{i+1}},
$$

which relates the local eigenvalues of $K$ to the eigenvalues on cohomology.

The conventions of Section [chap-The-Lefschetz-Verdier-formula] remain in force.
