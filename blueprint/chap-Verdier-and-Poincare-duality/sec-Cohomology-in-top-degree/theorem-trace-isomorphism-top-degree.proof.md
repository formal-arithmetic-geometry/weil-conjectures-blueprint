+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree"
order = 866
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-affines-form-basis", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-forgetting-supports-composition", "corollary-degreewise-duality-over-fields", "lemma-class-of-point", "theorem-nagata-s-compactification-theorem", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
We read off the top degree from Poincaré duality in degree zero
over $\mathbf Z/\ell^n$, and then change coefficients: to a finite
$A$ by extension of scalars, to $\mathcal O_E$ by a limit, and to the
fields by inverting $\ell$.

With finite coefficients, étale cohomology of a $d$-dimensional
scheme of finite type over an algebraically closed field vanishes above
degree $2d$, that is, $\operatorname{cd}_\ell(X)\le2d$ in the
notation of Definition [definition-cohomological-dimension] [sga4, X, Cor. 4.3].
This gives the vanishing outside $[0,2d]$, and $H^0=\Lambda$ because $X$ is connected.

Now let $\Lambda=\mathbf Z/\ell^n$. Since this ring is injective as a module over
itself,
$R\!\operatorname{Hom}_{\mathbf Z/\ell^n}(-,\mathbf Z/\ell^n)$ has cohomology equal to
the ordinary dual of the opposite cohomology. Hence Poincaré
duality (Theorem [theorem-poincare-duality]) in degree zero identifies $H^{2d}(X,\mathbf Z/\ell^n(d))$
with $\Hom(H^0(X,\mathbf Z/\ell^n),\mathbf Z/\ell^n)=\mathbf Z/\ell^n$.
By Theorem [theorem-poincare-duality] this identification is given by
pairing with $H^0$ and applying the trace map, so it is
$\operatorname{tr}_X(d)$.

A general finite ring $A$ need not be injective over itself, so we reach it by extension of scalars instead. Every finite $A$ is an algebra over some $\mathbf Z/\ell^n$, and by
Proposition [proposition-six-operations-change-coefficients] the complexes with constant coefficients
and their traces over $A$ are obtained by derived extension of
scalars from $\mathbf Z/\ell^n$. For a complex $P$ with cohomology in degrees $\le2d$, right exactness of the tensor product gives
$H^{2d}(P\otimes^{\mathbf L}A)=H^{2d}(P)\otimes A$. The top cohomology is therefore
$\mathbf Z/\ell^n\otimes A=A$, and the trace is an isomorphism. Since
derived extension of scalars does not raise the top degree, the same
upper bound holds.

For $\mathcal O_E$, we write $R\Gamma(X,\mathcal O_{E,X}(d))$ as the
derived inverse limit of the complexes $R\Gamma(X,(\mathcal O_E/\pi_E^n)_X(d))$.
Its cohomology fits into the Milnor sequence
$0\to\lim^1_nH^{i-1}\to H^i\to\lim_nH^i\to0$. Since the cohomology groups at each level are finite, they satisfy the Mittag–Leffler condition and there is no $\lim^1$
contribution to the top group. The traces in top degree are
compatible, so we get $H^{2d}(X,\mathcal O_{E,X}(d))=\mathcal O_E$, with the same
vanishing bounds. The lower bound and $H^0$ also follow directly from ordinary sheaf cohomology and
connectedness. Finally, inverting $\ell$ and then extending scalars along
finite extensions of $E$, we obtain the cases $\mathbf Q_\ell$, $E$ and $\overline{\mathbf Q}_\ell$.
