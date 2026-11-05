+++
kind = "proof"
of = "theorem-smooth-purity-all-admissible-coefficients"
order = 816
uses = ["proposition-pro-etale-coverings", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "proposition-isomorphisms-reduce-finite-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-relative-dualizing-complex", "proposition-relative-dualizing-complex", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
We recall $\gamma_f$ for each kind of coefficient ring, prove the trace
normalization (1) first with finite and then with integral coefficients,
and cite (2)–(4).

*The isomorphisms $\gamma_f$.* For finite $A$ it is $\gamma_{f,A}$ of
Proposition [proposition-smooth-purity-finite-coefficients]. For $\mathcal O_E$
(and $\mathbf Z_\ell$) it is $R\varprojlim$ of the map on towers
(9.19), which is an isomorphism with target $f^!$ by
Proposition [proposition-sp-integral-adjunction]. For $E$ (and $\mathbf Q_\ell$) and for
$\overline{\mathbf Q}_\ell$ it is the inverse of the counit-preserving isomorphism of
Proposition [proposition-sp-unique-adjoint] between $f^!$ and the right adjoints
of Proposition [proposition-sp-rational] and Theorem [theorem-sp-qbar]. In
every case, therefore, $\gamma_f$ is natural in $K$.

*Property (1), finite coefficients.* Here (1) holds because the
orientation obtained from the diagonal agrees on the chart $\mathbf A^1_Y$
with the one given by the adjunction in coordinates, whose counit at the
constant sheaf is $\operatorname{Tr}_p$ (the comparison following
Proposition [proposition-relative-dualizing-complex]).

*Property (1), integral and rational coefficients.* For
$\Lambda=\mathcal O_E$ we write the left side $\phi$ of (1) as
$u\circ\operatorname{Tr}_p$ and show that $u=1$ by reducing modulo $\ell^n$.

First, the trace map $\operatorname{Tr}_p$ of
(9.1) is an isomorphism, and this is what
makes $u$ well defined. Its reduction modulo $\ell$ is the trace map with
coefficients $\mathcal O_E/\ell$, because the trace of
Proposition [proposition-ell-adic-cycle-class-diagonal] lifts the
finite ones, and this reduction is an isomorphism. Indeed, it is obtained by
extension of scalars along the free map $\mathbf Z/\ell\to\mathcal O_E/\ell$
from the trace map with coefficients $\mathbf Z/\ell$, which is an
isomorphism (Section [sec-The-trace-map-of-affine-space]). So the cone $C$ of
$\operatorname{Tr}_p$ has $C/\ell=0$, and hence
$C/\pi_E=(C/\ell)\otimes^{\mathbf L}_{\mathcal O_E/\ell}\mathcal O_E/\pi_E=0$.
Since the source and target of $\operatorname{Tr}_p$ lie in
$\Dbc(Y,\mathcal O_E)$, the complex $C$ is derived complete, and derived Nakayama
(Lemma [lemma-reduction-derived-nakayama]) gives $C=0$. Thus
$\phi=u\circ\operatorname{Tr}_p$ for a unique endomorphism $u$ of
$\mathcal O_{E,Y}$, that is, for an element
$u\in H^0(Y,\mathcal O_E)=\varprojlim_nH^0(Y,\mathcal O_E/\ell^n)$.

Next, we show that $u\equiv1$ modulo $\ell^n$ for every $n$, so that $u=1$.
The trace part of
Proposition [proposition-compatibility-purity-change-coefficients] for
$\mathcal O_E\to\mathcal O_E/\ell^n$ shows that the reduction of $\phi$
modulo $\ell^n$ is the left side of (1) with coefficients
$\mathcal O_E/\ell^n$, which by the finite case equals the trace map with
these coefficients. This is also the reduction of $\operatorname{Tr}_p$,
and that reduction is an isomorphism. Hence $u\equiv1$ modulo $\ell^n$.
For $E$ and $\overline{\mathbf Q}_\ell$ both sides are obtained from the integral ones by inverting
$\ell$ and extending scalars.

*Properties (2)–(4).* These are
Propositions [proposition-compatibility-purity-base-change],
[proposition-compatibility-purity-composition]
and [proposition-compatibility-purity-change-coefficients].
