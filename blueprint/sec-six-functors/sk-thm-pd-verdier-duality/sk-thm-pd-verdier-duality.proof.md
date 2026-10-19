+++
kind = "proof"
of = "sk-thm-pd-verdier-duality"
uses = ["sk-lem-finite", "sk-lem-pd-preservation", "sk-lem-pd-generic-restriction", "sk-thm-sf-tensor-hom", "sk-prop-scalar-six", "sk-lem-pe-derived-nakayama", "sk-lem-integral-models", "sk-thm-sfb-qlbar-two-colimit"]
+++
The key case is finite $A$ over an algebraically closed field; the
other coefficient rings and the finite base field follow by formal
reductions at the end. In the key case induct on $d=\dim X$,
simultaneously over all algebraically closed fields of characteristic
different from $\ell$, since the induction step passes to a
geometric generic fibre over $\overline{k(t)}$. In dimension
zero, nilpotent invariance reduces to finitely many geometric points;
[sk-lem-finite] proves the result.

The double-dual morphism commutes with restriction to opens: restriction of
internal Hom to an open slice and restriction of the exceptional
adjunction identify all its evaluation maps. Choose a compactification
$j:X\hookrightarrow\overline X$, replace the target by the closure
of $X$, and extend $K$ by zero. The target has dimension
$d$, and $j_!K$ is in $\Dctf(\overline X,A)$.
Restriction of its double-dual morphism is $\delta_K$. It
therefore suffices to treat proper $X$ of dimension $d$.

Let $\Delta=\operatorname{Cone}(\delta_K)$. It is bounded
constructible by [sk-lem-pd-preservation]. If $x$ is a
nonclosed point of $X$, choose an affine neighbourhood and an
algebra generator $t$ whose image in $\kappa(x)$ is
transcendental over $k$. Such a generator exists since a
nonclosed point has positive transcendence degree. The induced map
to $\mathbf A^1_k$ sends $x$ to its generic point. Every
component meeting that generic fibre loses one dimension, so the
geometric generic fibre has dimension at most $d-1$.
[sk-lem-pd-generic-restriction] and induction over
$\overline{k(t)}$ show that $\Delta$ has zero geometric
stalk above $x$. Every nonclosed point is treated this way.

A constructible subset of a finite-type Noetherian scheme containing
only closed points is finite: each positive-dimensional locally
closed piece would contain a nonclosed generic point. The finitely
many cohomology sheaves of $\Delta$ therefore have support in
one finite set of closed points. These two paragraphs are
[det-pd-biduality-finite-support].

Proper exchange in [sk-thm-sf-tensor-hom], applied to
$a_X$, identifies $R\Gamma(X,\delta_K)$ with the double-dual
morphism of the perfect complex $R\Gamma(X,K)$, an isomorphism by
[sk-lem-finite]. Hence
$R\Gamma(X,\Delta)=0$. A finite-support sheaf over an
algebraically closed field has exact global sections, equal to the
finite sum of its stalks. The bounded cohomology spectral sequence
thus gives

$$
 0=H^mR\Gamma(X,\Delta)
   =\bigoplus_x\mathcal H^m(\Delta)_{\bar x}.
$$

All these stalks vanish, proving the finite-coefficient result
([det-pd-biduality-finite-algclosed]).

For a finite base field, extend to its algebraic closure. This
extension is a filtered limit of finite étale extensions; the
same continuity and evaluation calculation as in
[sk-lem-pd-generic-restriction] commutes duality with that
pullback. It is conservative on constructible classical complexes,
so the finite result descends.

For $\mathcal O_E$, [sk-prop-scalar-six] identifies
the reduction of $\delta_K$ modulo a uniformizer with the
finite-coefficient double-dual morphism, because it identifies
$a_X^!$, internal Hom and their evaluations. Its cone belongs
to the derived-complete constructible category and has zero residue
reduction. Derived Nakayama, [sk-lem-pe-derived-nakayama], makes
the cone zero. Taking $E=\Ql$ includes $\Zl$.

For $E$, [sk-lem-integral-models](4) builds every object
of $\Dbc(X,E)$ by finitely many cones and shifts from objects
$(a_!L_0)[1/\ell]$ with $a_!L_0$ integral. Together with
[sk-prop-scalar-six], this reduces the claim for $\delta$
to the integral result. The assertion is stable under finite cones, shifts
and retracts, since the double-dual functor is exact.
Finally $K$, its duality maps and their identities descend to a
common finite coefficient field by [sk-thm-sfb-qlbar-two-colimit];
extension of scalars proves the $\overline{\mathbf Q}_\ell$-case.
The coefficient reductions are [det-pd-biduality-coefficients].
