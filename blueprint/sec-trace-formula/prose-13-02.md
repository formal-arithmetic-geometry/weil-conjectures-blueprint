+++
id = "prose-13-02"
kind = "hidden"
title = "The Grothendieck–Lefschetz trace formula (2)"
order = 569
+++
It does, for every Weil complex $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$
(Section [sec-frobenius]), where $\Lambda\in\{A,\Zl,\mathcal O_E,\Ql,E,\overline{\mathbf Q}_\ell\}$
and $A$ is a finite commutative $\ell$-primary ring: for every $m\geq1$,
in $\Lambda$,

$$
\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{X,K}^m\mid
R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{y,m}\mid
K_{\bar y}\bigr)
$$

(Theorem [sk-thm-tf-uniform-formula]). Here $\operatorname{tr}_\Lambda$ is
the trace of an endomorphism of a perfect complex
(Definition [sk-d-trace]),
and $\operatorname{Frob}_{y,m}$ is the $m$-th iterate of the Weil
structure on the stalk at the fixed point $\bar y$. For $K=\Lambda_X$ and
$\Lambda$ a field this is Weil's axiom (b), which gives rationality of the
zeta function and, with duality, its functional equation
(Corollaries [sk-cor-tf-point-counting] and [sk-cor-tf-functional-equation]).
For the elliptic curve $y^2=x^3-x$ over $\mathbf F_3$ it reads
$N_m=1-\operatorname{Tr}(F^m\mid H^1)+3^m$; from $N_1=4$ and
$\det(F\mid H^1)=3$ we get $Z(C_0,T)=(1+3T^2)/((1-T)(1-3T))$, which
predicts $N_2=16$ and $N_3=28$ (Example [sk-ex-ex-run-trace]).

General $K$ is needed for the weights. In the form of an Euler product,

$$
\prod_{x\in|X_0|}\det\bigl(1-T^{\deg x}\operatorname{Frob}_x\mid K_{\bar x}\bigr)^{-1}
=\prod_i\det\bigl(1-T\operatorname{Frob}_{X,K}\mid H^i_c(X,K)\bigr)^{(-1)^{i+1}}
$$

(Theorem [sk-thm-trace-transport]), the formula relates the local
eigenvalues of $K$ to the eigenvalues on cohomology. The proof of
purity fibres $X_0$ in curves, and Rankin's argument
(Section [sec-purity-real-sheaves]) and the Fourier transform
(Section [sec-fourier-transform]) apply the formula to tensor powers of
lisse sheaves and to Fourier transforms. Its relative form, that the
trace function of $Rf_!K$ is the sum of the trace function of $K$ over
the fibres (Corollary [sk-cor-tf-trace-function-pushforward]), is the
entry of Grothendieck's dictionary in Section [sec-n-dictionary] on which these
arguments rest.

Following [sga5, III], we apply the Lefschetz–Verdier formula
(Theorem [sk-p-proper]) to the graph of Frobenius, and two
problems arise. The first is that the formula requires $X$ to be
proper. If we compactify, the new fixed points at the boundary have
zero stalk for $j_!K$, and we must show that their local terms vanish.
The second is that a local term is computed from
$\cHom(c_2^*K,c_1^!K)$ near the fixed point, and the stalk $K_{\bar y}$
does not determine it. This is not a technicality. For
$j:\mathbf G_m\hookrightarrow\mathbf A^1$ and $K=j_!A$ the stalk at the
origin is zero, but $\cHom(j_!A,j_!A)\simeq Rj_*A$ has stalk $A$ there
(Remark [sk-rem-tf-locality-warning]). For constant coefficients and a
transverse fixed point the local term is $1$ (and at a tangent one it is
the intersection multiplicity; we use this only as motivation). For
coefficients such as $j_!A$, however, transversality is not enough, and
the proof uses more: since $d\Phi_X=0$, the graph of Frobenius is
tangent to a coordinate axis.

Both problems are settled by one computation, on a curve: for any
morphism $\psi:(\Phi_X^m)^*K\to K$ on a smooth curve, the local term at
a rational point $y$ is $\operatorname{tr}_A(\psi_{\bar y}\mid K_{\bar y})$
(Proposition [sk-p-frob]). Additivity reduces it to the
point, where it is Lemma [sk-p-pairing], and to the case
$K_{\bar y}=0$. In that case the local term is a restriction map from
cohomology supported on the graph to cohomology supported at $y$
(Lemma [sk-lem-tf-curve-supported-pairing]). Since $d\Phi_X=0$, the graph
is tangent to a coordinate axis at $(y,y)$ while the diagonal is not, so
blowing up $(y,y)$ separates them, and after a cover of degree prime to
$\ell$ that makes the monodromy an $\ell$-group one shows that the
restriction is zero as a morphism in $D(A)$
(Lemma [sk-lem-tf-curve-restriction-zero]). The rest is dévissage: both
sides are additive along an open subscheme and its complement
(Lemma [sk-i-global-additivity]) and compatible with $Rf_!$
(Lemma [sk-i-relative-frob]), which reduces finite coefficients
to $\mathbf A^1\subset\mathbf P^1$
(Theorem [sk-thm-tf-coefficient-morphism-formula]). This is
Grothendieck's argument, as in [sga5, XV, §3] and
[tfbp]. Appendix [sec-specialization-contracting] computes the
local terms of contracting correspondences in another way, by
specialization to the normal cone, following [varshavsky05].

The other coefficient rings follow by reduction modulo $\pi_E^n$,
inverting $\ell$ and finite extensions of $E$. Since an integral model of
a rational Weil complex need not carry an invertible integral Weil
structure (Lemma [sk-lem-tf-rational-model] and the remark after it), the
formula with finite coefficients is proved for arbitrary Frobenius
correspondences $\psi:\Phi_X^*K\to K$, not necessarily invertible.

The conventions of Section [sec-lefschetz-verdier] remain in force.
