+++
id = "cor-sf-continuity-fullcd"
kind = "theorem"
title = "Continuity for arbitrary sheaves gives the full cohomological-dimension bound"
order = 3735
tags = ["latex:corollary"]
uses = ["def-weil-full-cohomological-dimension", "def-weil-pbc-etale-site", "def-weil-pbc-ind-etale-algebra", "def-weil-pbc-pointed-etale-neighbourhoods-detailed", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-pbc-strict-henselization-limit-detailed", "def-weil-scheme-morphism-properties", "lem-sf-etale-direct-image-vanishing", "lem-sf-fullcd-detection-equivalence", "lem-sf-stalk-limit-acyclic", "lem-weil-pbc-affine-neighbourhood-cofinal", "lem-weil-pbc-ind-etale-basis", "lem-weil-pbc-proetale-restriction-injectives", "rem-sf-fullcd-general-form", "thm-sf-continuity-arbitrary-sheaves-vanishing", "thm-sp-grothendieck", "thm-weil-pbc-weak-etale-refinement"]
+++
Fix $d\geq0$ and assume the following continuity statement.

1. **$(\mathrm{Co})$** For every cofiltered inverse system $(Z_i)_{i\in I}$ of
finite-type $k$-schemes with $\dim Z_i\leq d$ and affine transition maps,
with limit $Z$, every sheaf $\mathcal G$ of $A$-modules on
$Z_{\Proet}$ and every $q\geq1$, the canonical comparison map
$$
\varinjlim_iH^q\bigl(Z_{i,\Proet},\mathcal G|_{Z_i}\bigr)
\longrightarrow H^q\bigl(Z_{\Proet},\mathcal G\bigr)
$$
is an isomorphism.

Then:

1. **(i)** $H^r(V_{\Proet},\mathcal F)=0$ for every finite-type $k$-scheme
$V$ with $\dim V\leq d$, every sheaf $\mathcal F$ of $A$-modules on
$V_{\Proet}$ and every $r>2d$, and also
$R^q\nu_{V,*}\mathcal F=0$ for every $q\geq1$, the comparison morphism
being the $\nu_V$ of [def-weil-pbc-site-comparison-morphism]; that is,
$(\mathrm{G})$ holds at $V$ with the bound $M=0$;
1. **(ii)** the same vanishing $H^r(Z_{\Proet},\mathcal G)=0$ for $r>2d$
holds for every limit $Z$ of such a system;
1. **(iii)** consequently the vanishing required by
[def-weil-full-cohomological-dimension] holds with the bound $c=2d$:
for every proper finite-type
$p:\overline X\to Y$ with $\dim\overline X\leq d$, every base change
$V\to Y$ of $Y_{\Proet}$ and every sheaf $\mathcal F$ of $A$-modules on
$\overline X_{\Proet}$, one has
$R^q(p_V)_*(\mathcal F|_{\overline X\times_YV})=0$ for $q>2d$; that is,
$\operatorname{FullCD}(p,A;2d)$ holds for $p$.

Thus, under the continuity hypothesis $(\mathrm{Co})$ for arbitrary sheaves,
the statement $(\mathrm{G})$ of [rem-sf-fullcd-general-form] holds with
the bound $M=0$, and the full-cohomological-dimension condition is a theorem
with the bound $2d$ instead of an interface.

## Proof

*(i).* Let $V$ be finite type over $k$ with $\dim V\leq d$ and let
$\mathcal F$ be a sheaf of $A$-modules on $V_{\Proet}$, in the sense of
[def-weil-pbc-proetale-modules] on the site of
[def-weil-pbc-proetale-site]. For a geometric
point $\bar v\to V$, the pointed étale neighbourhoods $(U,\bar u)$ with
$U$ affine form a cofinal subsystem of the system of
[def-weil-pbc-pointed-etale-neighbourhoods-detailed], by
[lem-weil-pbc-affine-neighbourhood-cofinal]; each $U$ is a finite-type
$k$-scheme with $\dim U\leq d$ (an étale morphism is weakly étale, and a
weakly étale morphism induces isomorphisms of the strict henselizations of
the local rings, Stacks Project, More on Morphisms, Lemma 37.64.11,
[Tag 094Z](https://stacks.math.columbia.edu/tag/094Z), so that
$\dim U\leq\dim V$), and the affine pointed neighbourhoods are the finite
type models of the limit $\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{V,\bar v}$ of
[def-weil-pbc-strict-henselization-limit-detailed]. The continuity hypothesis
$(\mathrm{Co})$ therefore applies to this system, whose transition maps are
affine because the neighbourhoods are affine, and, together with
[lem-sf-stalk-limit-acyclic](iii), gives that every cohomology class on an
étale neighbourhood of $\bar v$ dies after refinement, that is,
$(\mathrm{C}_q)$ of
[thm-sf-continuity-arbitrary-sheaves-vanishing] at $V$ for every
$q\geq1$. By that theorem $R^q\nu_{V,*}\mathcal F=0$ for every $q\geq1$
and every $\mathcal F$.

The Leray spectral sequence of the composite $\Gamma(V_{\Proet},-)= \Gamma(V_{\Et},-)\circ\nu_{V,*}$, which is [thm-sp-grothendieck], reads

$$
E_2^{p,q}=H^p\bigl(V_{\Et},R^q\nu_{V,*}\mathcal F\bigr)
\Longrightarrow H^{p+q}\bigl(V_{\Proet},\mathcal F\bigr),
$$

and its $q>0$ row now vanishes, so that
$H^r(V_{\Proet},\mathcal F)=H^r(V_{\Et},\nu_{V,*}\mathcal F)$ for every
$r$. The sheaf $\nu_{V,*}\mathcal F$ is a sheaf of $A$-modules on
$V_{\Et}$, hence a torsion sheaf of abelian groups, $A$ being finite; the
structure morphism $V\to\operatorname{Spec}k$ is finite type and $k$ is
algebraically closed, so [lem-sf-etale-direct-image-vanishing] applied to
it and to the Leray spectral sequence over $\operatorname{Spec}k$, whose
higher etale cohomology vanishes because $k$ is separably closed, gives
$H^r(V_{\Et},\nu_{V,*}\mathcal F)=0$ for $r>2d$. This is (i). The same
argument in the form used in [rem-sf-fullcd-general-form] for finite-type
sources is the one recalled here.

*(ii).* Let $Z=\varprojlim_iZ_i$ be as in the hypothesis. Evaluating
the continuity hypothesis at $q=r>2d$ and applying (i) to each finite-type
model $Z_i$ gives

$$
H^r(Z_{\Proet},\mathcal F)
=\varinjlim_iH^r\bigl(Z_{i,\Proet},\mathcal F|_{Z_i}\bigr)=0
\qquad(r>2d),
$$

the terms vanishing by (i) because $\dim Z_i\leq d$.

*(iii).* Let $p:\overline X\to Y$, $V\to Y$ and $\mathcal F$ be as
in the statement. By the detection equivalence
[lem-sf-fullcd-detection-equivalence] the vanishing required by
[def-weil-full-cohomological-dimension] with the bound $c$ is
equivalent to
$H^r((\overline X\times_YV)_{\Proet},\mathcal F|)=0$ for all $r>c$ and all
base changes $V\to Y$ of $Y_{\Proet}$, so it suffices to obtain that
vanishing with $c=2d$. Let $V\to Y$ be a base change. The site
$V_{\Proet}$ has a basis of affine objects ind-etale over $Y$
([lem-weil-pbc-ind-etale-basis], over an affine open of $Y$; the
definition of an ind-etale algebra is a filtered colimit of etale algebras,
[def-weil-pbc-ind-etale-algebra]), and every weakly etale $V\to Y$ is
covered by such objects by [thm-weil-pbc-weak-etale-refinement]. For
such an object $W=\varprojlim_mW_m$, with $W_m$ affine and etale over
$Y$, the base-changed source
$\overline X\times_YW$ is the limit of the finite-type $k$-schemes
$Z_m=\overline X\times_YW_m$ with affine transition maps (fibre products
commute with this inverse limit, the transition maps $W_{m'}\to W_m$ being
affine, so the identification is checked on affine charts), and each $Z_m$
has dimension at most $\dim\overline X\leq d$, the projection
$Z_m\to\overline X$ being etale and hence of relative dimension zero; so
(ii) applies and gives

$$
H^r\bigl((\overline X\times_YW)_{\Proet},\mathcal F|\bigr)=0\qquad(r>2d).
$$

The sheaf $R^q(p_V)_*(\mathcal F|_{\overline X\times_YV})$ is a sheaf on
$V_{\Proet}$, so it vanishes if and only if its restrictions to the members
of a covering of $V$ vanish; restricting the slice to $W$ identifies the
site $(\overline X\times_YV)_{\Proet}$ over $W$ with
$(\overline X\times_YW)_{\Proet}$ and the derived evaluation accordingly,
by [lem-weil-pbc-proetale-restriction-injectives], so it suffices to
know that $R^q(p_W)_*(\mathcal F|_{\overline X\times_YW})=0$ for every $W$
of the basis. That is the relative clause of the detection equivalence
[lem-sf-fullcd-detection-equivalence] applied to the base-changed proper
morphism $p_W:\overline X\times_YW\to W$, whose source vanishing is exactly
the display above. Hence
$R^q(p_V)_*(\mathcal F|_{\overline X\times_YV})=0$ for $q>2d$, uniformly in
$V$. This is (iii).
