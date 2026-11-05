+++
kind = "proof"
of = "lemma-acyclicity-closed-fibre--1"
order = 372002
uses = ["definition-underived-base-change-map", "definition-torsion-sheaves", "theorem-gabber-affine-proper-base-change", "lemma-finiteness-small-etale-topoi", "theorem-finite-etale-covers-proper-henselian", "lemma-finite-morphisms", "lemma-cohomology-modules-underlying-abelian"]
+++
*Degrees $q\geq2$.* On an affine open $W=\operatorname{Spec}B$ of
$\mathbf P^1_R$, put $J=\mathfrak mB$. Henselizing $(B,J)$, applying
[theorem-gabber-affine-proper-base-change], and using continuity of étale
cohomology identifies $H^q(W_0,I_0|_{W_0})$ with the filtered colimit of
$H^q(\operatorname{Spec}B',I|_{\operatorname{Spec}B'})$, where $B'$ runs
through the étale neighbourhoods of $B/J$ in $B$. The sheaf $I$ is torsion
in the sense of [definition-torsion-sheaves]. Its restriction to each étale
neighbourhood is injective, since étale restriction has an exact left
adjoint, extension by zero. The underlying abelian sheaf is therefore
acyclic, as in [lemma-cohomology-modules-underlying-abelian], so the colimit
vanishes for $q>0$. The same holds on the intersection of the two standard
affine charts. Mayer–Vietoris gives the desired vanishing for $q\geq2$;
this is the two-chart case of the finite affine cover bound used in Lean.

*Representing a class in degree one.* By
[lemma-finiteness-small-etale-topoi](1), a class
$\xi\in H^1(\mathbf P^1_\kappa,I_0)$ comes from a class of $G_0$ for a
constructible sheaf $G$ with a map $G\to I$. Part (2) gives a monomorphism
$G\hookrightarrow P=\bigoplus_{a=1}^N(h_a)_*\underline{M_a}$, where each
$h_a:Y_a\to\mathbf P^1_R$ is finite and finitely presented and each $M_a$
is a finite $\mathbf F_\ell$-module. Injectivity extends $G\to I$ to
$P\to I$. Taking the components of the resulting class of $P_0$ writes

$$
\xi=\sum_{a=1}^N H^1(\psi_{a,0})(x_a),\qquad
\psi_a:(h_a)_*\underline{M_a}\longrightarrow I,\qquad
x_a\in H^1(\mathbf P^1_\kappa,((h_a)_*\underline{M_a})_0).
$$

*Lifting and vanishing.* The finite base change isomorphism
([definition-underived-base-change-map], [lemma-finite-morphisms]) and the
Leray edge isomorphisms identify, up to an automorphism, the restriction
map for $(h_a)_*\underline{M_a}$ with that for $\underline{M_a}$ on $Y_a$
and its closed fibre. Since $Y_a$ is proper over $R$,
[theorem-finite-etale-covers-proper-henselian] makes the latter map
bijective in degree one. Thus $x_a$ lifts to a class
$z_a\in H^1(\mathbf P^1_R,(h_a)_*\underline{M_a})$. Its image under
$\psi_a$ is zero in $H^1(\mathbf P^1_R,I)$ by injective acyclicity.
Naturality of restriction then gives $H^1(\psi_{a,0})(x_a)=0$ for every
$a$, hence $\xi=0$. These comparisons commute with forgetting the module
structure, so they compute the underlying abelian cohomology throughout.
