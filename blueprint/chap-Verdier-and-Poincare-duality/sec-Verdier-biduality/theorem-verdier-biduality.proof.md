+++
kind = "proof"
of = "theorem-verdier-biduality"
order = 845
uses = ["theorem-verdier-biduality--1", "theorem-verdier-biduality--2", "theorem-verdier-biduality--4", "theorem-verdier-biduality--5", "theorem-verdier-biduality--6", "lemma-perfect-complexes-geometric-point", "lemma-internal-adjunction-two-exchange-formulas", "lemma-verdier-duality-preserves-constructibility", "lemma-double-dual-geometric-generic-fibre", "lemma-restriction-geometric-generic-fibre", "theorem-nagata-s-compactification-theorem", "theorem-f-shriek-finite-coefficients", "proposition-six-operations-change-coefficients", "proposition-isomorphisms-reduce-finite-coefficients", "lemma-reduction-derived-nakayama", "lemma-integral-models", "proposition-dctf-x-qbar-2-colimit", "corollary-finite-tor-amplitude-under-comparison"]
+++
We first treat finite coefficients $A$ over an algebraically closed field $k$, and deduce the other coefficient rings and a finite base field at the end. In this main case we reduce
to proper $X$, show by induction that the cone of $\delta_K$ has zero
stalks at all nonclosed points, and compute global sections to see that
its stalks at the finitely many remaining closed points vanish. This induction is on $d=\dim X$. Since the induction step passes to a
geometric generic fibre over $\overline{k(t)}$, we run it simultaneously
over all algebraically closed fields of characteristic different from
$\ell$. In dimension
zero, $X_{\mathrm{red}}$ is a finite disjoint union of copies of
$\operatorname{Spec}k$, and by nilpotent invariance we may replace $X$ by
it. On each copy, moreover, $\omega=\Lambda$ and $\delta_K$ is the evaluation map
of a perfect complex, which is an isomorphism by
Lemma [lemma-perfect-complexes-geometric-point].

We may assume that $X$ is proper of dimension $d$; properness is used only in the last step, to compute global sections. This reduction rests on the fact that the double-dual morphism commutes with restriction to
opens. This holds because restriction to an open $j:U\to X$ commutes with
internal Hom, satisfies $j^*\omega_X=j^!\omega_X=\omega_U$, and identifies
all the evaluation maps. Given this, choose a compactification $j:X\hookrightarrow\overline X$, replace the target by the closure
of $X$, which has dimension $d$, and extend $K$ by zero. Then
$j_!K$ is in $D^b_{\mathrm{ctf}}(\overline X,A)$, and the restriction of its
double-dual morphism to $X$ is $\delta_K$.

Let $Q=\Cone(\delta_K)$. We have to show that $Q=0$. Since $Q$ is
bounded and constructible by
Lemma [lemma-verdier-duality-preserves-constructibility], it is enough
to show that all its geometric stalks vanish.

At nonclosed points the induction hypothesis applies. Let $x$ be a
nonclosed point of $X$. We choose an affine neighbourhood $U$ of $x$ and an algebra generator $t$ whose image in $\kappa(x)$ is
transcendental over $k$. Such a generator exists because a
nonclosed point has positive transcendence degree. The induced map to $\mathbf A^1_k$ then sends $x$ to the generic point. Moreover, an irreducible component of $U$ that meets the generic fibre dominates
$\mathbf A^1_k$, and its generic fibre has dimension one less than the
component. Hence the geometric generic fibre has dimension at most $d-1$,
and the induction hypothesis applies to it.
Let $g$ be the projection from the geometric generic fibre of $U$. By
Lemma [lemma-double-dual-geometric-generic-fibre],
locally on $U$ the complex $g^*Q$ is isomorphic to the cone of
$\delta_{g^*K}$. This cone vanishes by the
induction hypothesis over $\overline{k(t)}$. As $x$ lies over the
generic point of $\mathbf A^1_k$, every geometric point above $x$
factors through the geometric generic fibre. Therefore $Q$ has zero
geometric stalks above every nonclosed point of $X$.

Only finitely many closed points are left. Indeed, the support
of each cohomology sheaf of $Q$ is constructible, and by the previous
paragraph it consists of closed points.
A constructible subset of a Noetherian scheme of finite type which contains
only closed points is finite, since each positive-dimensional locally
closed piece would contain a nonclosed generic point. Thus the finitely
many cohomology sheaves of $Q$ are supported on
a single finite set of closed points.

The stalks at these closed points vanish because $X$ is proper and $Q$
has no global cohomology. To see that $R\Gamma(X,Q)=0$, we apply the
exchange for proper maps in
Lemma [lemma-internal-adjunction-two-exchange-formulas] to $a_X$. It
identifies $R\Gamma(X,\delta_K)$ with the double-dual
morphism of the perfect complex $R\Gamma(X,K)$, which is an isomorphism by
Lemma [lemma-perfect-complexes-geometric-point].
On the other hand, a sheaf $\mathcal F$ supported on a finite set $S$ of
closed points is $\bigoplus_{x\in S}x_*\mathcal F_{\bar x}$. Since each
residue field is algebraically closed, $H^0(X,\mathcal F)=\bigoplus_x
\mathcal F_{\bar x}$ and the higher cohomology vanishes. The
hypercohomology spectral sequence of the bounded
complex $Q$ therefore degenerates, and it shows that

$$
0=H^mR\Gamma(X,Q)
=\bigoplus_x\mathcal H^m(Q)_{\bar x}.
$$

All these stalks vanish. Since the cohomology sheaves of $Q$
are supported on this finite set, $Q=0$.

A finite base field reduces to its algebraic closure. This
extension is a filtered limit of finite étale extensions, and the
continuity and evaluation argument of
Lemma [lemma-restriction-geometric-generic-fibre] shows that duality commutes with
pullback along it. Hence the pullback of $\delta_K$ to the algebraic
closure is the double-dual map there, which is an isomorphism by the case
already proved. Since pullback to the algebraic closure is surjective on geometric points, it is conservative on constructible classical complexes, and the result therefore descends to the finite field.

For coefficient rings that are not finite we reduce to finite ones. Indeed, the double-dual map $\delta:\mathrm{id}\to\mathbb D_X\mathbb D_X$ is
a natural transformation of exact functors, built from $a_X^!$, internal
Hom and evaluation. Its extensions of scalars are identified by Proposition [proposition-six-operations-change-coefficients]. By
Proposition [proposition-isomorphisms-reduce-finite-coefficients] the finite case
therefore implies the theorem for every admissible $\Lambda$.
