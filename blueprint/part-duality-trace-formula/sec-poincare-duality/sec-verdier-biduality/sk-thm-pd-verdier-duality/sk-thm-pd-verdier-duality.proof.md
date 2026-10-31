+++
kind = "proof"
of = "sk-thm-pd-verdier-duality"
uses = ["sk-lem-finite", "sk-lem-pd-preservation", "sk-lem-pd-generic-restriction", "sk-thm-sf-tensor-hom", "sk-prop-scalar-six", "sk-lem-pe-derived-nakayama", "sk-lem-integral-models", "sk-thm-sfb-qlbar-two-colimit", "sk-prop-reduction-to-finite"]
+++
We first treat finite coefficients $A$ over an algebraically closed
field $k$; the other coefficient rings and a finite base field are
handled at the end. For finite $A$ we argue by induction on $d=\dim X$,
simultaneously over all algebraically closed fields of characteristic
different from $\ell$, since the induction step passes to a
geometric generic fibre over $\overline{k(t)}$. In dimension
zero, by nilpotent invariance we reduce to finitely many geometric points,
where the result is Lemma [sk-lem-finite].

We may assume that $X$ is proper of dimension $d$. Indeed, the
double-dual morphism commutes with restriction to opens, because
restricting internal Hom and the exceptional adjunction to an open
identifies all its evaluation maps. Choose a compactification
$j:X\hookrightarrow\overline X$, replace the target by the closure
of $X$, which has dimension $d$, and extend $K$ by zero. Then
$j_!K$ is in $D^b_{\mathrm{ctf}}(\overline X,A)$, and the restriction of its
double-dual morphism to $X$ is $\delta_K$.

Let $Q=\Cone(\delta_K)$. It is bounded and
constructible by Lemma [sk-lem-pd-preservation]. If $x$ is a
nonclosed point of $X$, choose an affine neighbourhood $U$ of $x$ and an
algebra generator $t$ whose image in $\kappa(x)$ is
transcendental over $k$; such a generator exists because a
nonclosed point has positive transcendence degree. The induced map
to $\mathbf A^1_k$ sends $x$ to the generic point. Since every
component meeting the generic fibre drops in dimension by one, the
geometric generic fibre has dimension at most $d-1$.
Let $g$ be the projection from the geometric generic fibre of $U$. By Lemma [sk-lem-pd-generic-restriction],
$g^*Q$ is the cone of $\delta_{g^*K}$, and this vanishes by the
induction hypothesis over $\overline{k(t)}$. Since $x$ lies over the
generic point of $\mathbf A^1_k$, every geometric point above $x$
factors through the geometric generic fibre. Hence $Q$ has zero
geometric stalks above every nonclosed point of $X$.

A constructible subset of a Noetherian scheme of finite type which contains
only closed points is finite, since each positive-dimensional locally
closed piece would contain a nonclosed generic point. It follows that the finitely
many cohomology sheaves of $Q$ are supported on
a single finite set of closed points.

The exchange for proper maps in Lemma [sk-thm-sf-tensor-hom], applied to
$a_X$, identifies $R\Gamma(X,\delta_K)$ with the double-dual
morphism of the perfect complex $R\Gamma(X,K)$, which is an isomorphism by
Lemma [sk-lem-finite]. Hence
$R\Gamma(X,Q)=0$. Over an algebraically closed field, taking
global sections of a sheaf with finite support is exact, and the result is the
finite sum of its stalks. The spectral sequence for the bounded
complex $Q$ therefore shows that

$$
0=H^mR\Gamma(X,Q)
=\bigoplus_x\mathcal H^m(Q)_{\bar x}.
$$

Hence all these stalks vanish. Since the cohomology sheaves of $Q$
are supported on this finite set, $Q=0$, and this proves the
result for finite coefficients.

For a finite base field, we extend scalars to its algebraic closure. This
extension is a filtered limit of finite étale extensions, and the
same continuity and evaluation argument as in
Lemma [sk-lem-pd-generic-restriction] shows that duality commutes with this
pullback. Since the pullback is conservative on constructible classical complexes,
the result descends to the finite field.

The double-dual map $\delta:\mathrm{id}\to\mathbb D_X\mathbb D_X$ is
a natural transformation of exact functors, built from $a_X^!$, internal
Hom and evaluation, and Proposition [sk-prop-scalar-six] identifies its
extensions of scalars. Proposition [sk-prop-reduction-to-finite] therefore
extends the finite case to every admissible $\Lambda$.
