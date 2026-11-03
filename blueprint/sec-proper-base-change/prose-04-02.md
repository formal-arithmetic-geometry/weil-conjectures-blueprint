+++
id = "prose-04-02"
kind = "hidden"
title = "Proper base change (2)"
order = 171
+++
The answer is yes, and more generally pulling a proper family back to a
new base and taking its cohomology can be done in either order. For a
cartesian square with $f$ proper, $g:Y'\to Y$ arbitrary and
$X'=X\times_YY'$, the base change map

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is an isomorphism for every bounded below classical complex $K$ with
torsion cohomology sheaves (Theorem [sk-thm-properbasechange]), and taking for
$g$ a geometric point gives the stalk formula
(Corollary [sk-cor-pbc-torsion-stalk]). The theorem is due to
Artin [sga4, XII–XIII]. Beware that properness cannot be dropped: for
$j:\mathbf G_m\hookrightarrow\mathbf A^1$ and the origin
$i:\{0\}\hookrightarrow\mathbf A^1$, the sheaf $i^*j_*A$ is nonzero while
the base change of $\mathbf G_m$ to the origin is empty. Unlike smooth
base change (Section [sec-smooth-base-change]), proper base change
holds for torsion of every order, including torsion divisible by the
residue characteristics.

The proof reduces to the projective line. In degree zero the statement
is about connectedness: over a henselian pair, a proper scheme and its
closed fibre have the same sections of every étale sheaf of sets
(Theorem [sk-thm-pbc-henselian-h0]), and so the underived base change map is
an isomorphism (Proposition [sk-prop-pbc-degree-zero]). To reach higher
degrees we apply this to injective resolutions. This works as soon as
pullbacks of injective sheaves along every base change remain acyclic for
the direct image, and Theorem [sk-thm-iff] shows that this
acyclicity is equivalent to proper base change. For $\mathbf P^1_R$ over a
henselian local ring $R$, the acyclicity on the closed fibre comes from
two facts about henselian pairs: Gabber's affine analogue of proper base
change on the two standard charts, and the lifting of finite étale
covers from the closed fibre for the classes in degree one
(Lemma [sk-lem-pbc-p1-injective-fibre]). This gives proper base change for
$\mathbf P^1$ (Proposition [sk-thm-p1]), once we also know that the
cohomology of a proper curve does not change when the separably closed
ground field is enlarged (Lemma [sk-cor-curve-invariance]). The
general case is then formal. Proper base change is stable under
composition and descends along proper surjections
(Lemma [sk-lem-pbc-composition-cancellation]). Hence it holds for
$(\mathbf P^1)^n$, for $\mathbf P^n$ through the finite surjection
$(\mathbf P^1)^n\to\mathbf P^n$ that multiplies linear forms
(Lemma [sk-lem-pbc-symmetric-product]), for projective morphisms, and by
Chow's lemma (Theorem [sk-thm-chow-projective]) for every proper
morphism (Proposition [sk-thm-reduction]).

These calculations are made on the étale site, where the classical
tools are available (compare [bp]), and the comparison
theorems of Section [sec-proetale-coefficients] transport them to
classical complexes on the pro-étale site. For $\mathcal O_E$ the
theorem follows by passing to the limit over the reductions modulo
$\pi_E^n$ (Proposition [sk-prop-pbc-complete]). Here a subtlety appears: pullback need not
preserve derived completeness, so that at this stage the statement for
$\mathcal O_E$ involves the completed inverse image. Once we know that
$Rp_*$ preserves constructibility
(Proposition [sk-thm-sfb-proper-base-change]), the completion is
unnecessary and we obtain the ordinary base change isomorphism on
$D^b_{\mathrm{ctf}}$ for every admissible coefficient ring.

Proper base change is used in three places. It bounds the Tor amplitude
of $Rp_*$ with finite coefficients (Proposition [sk-prop-ctf-finite-proper]),
it shows that $Rf_!=Rp_*j_!$ does not depend on the compactification
(Proposition [sk-prop-sf-comp-coherence]), and it identifies the
stalks of $Rf_!$ with compactly supported cohomology of the fibres in the
trace formula (Corollary [sk-cor-tf-trace-function-pushforward]).
