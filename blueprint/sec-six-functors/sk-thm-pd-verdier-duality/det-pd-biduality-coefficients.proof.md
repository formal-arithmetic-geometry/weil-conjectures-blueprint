+++
kind = "proof"
of = "det-pd-biduality-coefficients"
uses = ["det-pd-biduality-finite-algclosed", "det-ctf-finite-comparison-localizing", "lem-weil-pbc-derived-cohomology-continuity", "lem-weil-duality-pairing", "lemma-weil-pbc-geometric-stalk-conservative", "det-prop-scalar-six-exceptional", "det-prop-scalar-six-tensor-hom", "det-pe-derived-nakayama-first-reduction", "det-lem-integral-models-generators", "det-lem-coefficient-finite-descent-objects", "det-lem-coefficient-finite-descent-hom"]
+++
*(i) Finite coefficients.* With finite coefficients the comparison functor
$\nu_X^*$ identifies $\Dctf(X,A)$ with its classical étale counterpart,
compatibly with pullback, direct images and compactly supported direct image
([det-ctf-finite-comparison-localizing]). Being an equivalence compatible with
$Ra_{X!}$ and with tensor products, it is also compatible with their right
adjoints $a_X^!$ and internal Hom, hence with $\mathbb D_X$, evaluation and
$\delta$. Over an algebraically closed field the claim is therefore
[det-pd-biduality-finite-algclosed]. Over a finite base field, let $X$ be of finite type over a finite field $k_0$
and let $\bar X$ be its base change to an algebraic closure $\bar k_0$. The
extension $\bar k_0/k_0$ is a filtered limit of finite étale extensions. As in
the first comparison of the geometric generic restriction, continuity of
finite-coefficient étale cohomology along this limit
([lem-weil-pbc-derived-cohomology-continuity]) commutes direct images,
exceptional restriction and internal Hom with the pullback to $\bar X$; the
comparisons are formed from evaluation, so they carry $\delta_K$ to
$\delta_{K|_{\bar X}}$ ([lem-weil-duality-pairing]). The latter is an
isomorphism by [det-pd-biduality-finite-algclosed]. Pullback to $\bar X$ is
conservative on constructible classical complexes, since every geometric point
of $X$ factors through $\bar X$ ([lemma-weil-pbc-geometric-stalk-conservative]);
so $\delta_K$ is an isomorphism.

*(ii) Integral coefficients.* For $\Lambda=\mathcal O_E$ with uniformizer
$\pi_E$, the coefficient comparisons for exceptional inverse image and internal
Hom ([det-prop-scalar-six-exceptional], [det-prop-scalar-six-tensor-hom])
identify $a_X^!$, internal Hom and their evaluations after reduction modulo
$\pi_E$. Hence the reduction of $\delta_K$ is the finite-coefficient
double-dual morphism of the reduction of $K$, an isomorphism by (i) and
[det-pd-biduality-finite-algclosed]. The cone of $\delta_K$ is derived complete
and has zero reduction modulo $\pi_E$, so it vanishes by derived Nakayama
([det-pe-derived-nakayama-first-reduction]). Taking $E=\Ql$ includes $\Zl$.

*(iii) Finite extensions of $\Ql$.* By [det-lem-integral-models-generators],
every object of $\Dbc(X,E)$ is obtained by finitely many cones and shifts from
objects $(a_!L_0)[1/\ell]$ with $a_!L_0$ integral. The coefficient comparisons
of [det-prop-scalar-six-exceptional] and [det-prop-scalar-six-tensor-hom] for
$\mathcal O_E\to E$ identify $\delta_{(a_!L_0)[1/\ell]}$ with the
rationalization of $\delta_{a_!L_0}$, an isomorphism by (ii). Since the
double-dual functor is exact, the class of $K$ for which $\delta_K$ is an
isomorphism is stable under finite cones, shifts and retracts, and so contains
all of $\Dbc(X,E)$.

*(iv) $\overline{\mathbf Q}_\ell$.* Given $K\in\Dbc(X,\overline{\mathbf Q}_\ell)$,
the object $K$, its duality maps and the identities between them descend to a
common finite coefficient field $E$
([det-lem-coefficient-finite-descent-objects],
[det-lem-coefficient-finite-descent-hom]). Extension of scalars from $E$ to
$\overline{\mathbf Q}_\ell$ carries the double-dual morphism of the model,
an isomorphism by (iii), to $\delta_K$.
