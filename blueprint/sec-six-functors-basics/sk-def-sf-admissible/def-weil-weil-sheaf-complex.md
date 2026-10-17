+++
id = "def-weil-weil-sheaf-complex"
kind = "definition"
title = "Weil sheaf and Weil complex"
lean = ["AlgebraicGeometry.WeilSheaf", "AlgebraicGeometry.WeilComplex"]
order = 1866
uses = ["def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-scheme-morphism-properties", "def-weil-pbc-proetale-site", "sk-def-sfb-condensed-ring", "sk-def-sfb-qlbar-condensed", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-derived-categories", "sk-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "sk-cor-coefficient-heart-ii", "sk-thm-sfb-qlbar-two-colimit"]
+++
Fix the finite-field datum [def-weil-finite-field-fiber] $p,a,q,k_0,k$, where
$q=p^a$, and a prime $\ell\neq p$. Choose an algebraic closure $\Qlb$ of
$\Ql$ and a finite extension $E/\Ql$ contained in $\Qlb$, and let
$\Lambda\in\{\underline E,\underline{\Qlb}\}$ be the corresponding condensed
ring ([sk-def-sfb-condensed-ring], [sk-def-sfb-qlbar-condensed]); we write
$\Lambda\in\{E,\Qlb\}$. Let $Y_0$ be a finite-type
[def-weil-scheme-morphism-properties] $k_0$-scheme, put $Y=Y_0\times_{k_0}k$,
and let $g_Y:Y\to Y$ be the geometric-Frobenius automorphism of
[def-weil-frobenius-detailed]. On the small pro-étale site
[def-weil-pbc-proetale-site] put $\Lambda_Y=p_Y^*\Lambda$
([sk-def-sfb-pulled-back-coefficients]). Since $g_Y$ is an automorphism of
schemes and $p_Y\circ g_Y=p_Y$, the inverse image $g_Y^*$ is an exact
autoequivalence of $\Mod(Y_{\mathrm{proét}},\Lambda)$, with a canonical
isomorphism $g_Y^*\Lambda_Y\cong\Lambda_Y$; being exact it needs no deriving
([sk-def-sfb-derived-categories]), and we also write $Lg_Y^*=g_Y^*$ on
$D(Y_{\mathrm{proét}},\Lambda)$. It preserves constructible sheaves and hence the
triangulated subcategory $\Dbc(Y,\Lambda)$ ([sk-def-sfb-bounded-constructible],
[sk-cor-coefficient-heart-ii]).

**Weil sheaves.** Write
$\Sh_c(Y,\Lambda)=\Cons(Y,\Lambda)$ for the abelian category of constructible
$\Lambda_Y$-modules ([sk-lem-coefficient-heart] (1)); it is the heart of the
standard $t$-structure on $\Dbc(Y,\Lambda)$. A *Weil $\Lambda_Y$-module* is a pair
$(M,\theta)$ with $M\in\Mod(Y_{\mathrm{proét}},\Lambda)$ and an isomorphism

$$
 \theta:g_Y^*M\xrightarrow{\sim}M;
$$

morphisms are module maps commuting with $\theta$. Since $g_Y^*$ is exact,
these form an abelian category $\Mod_{\mathrm W}(Y,\Lambda)$ in which kernels,
cokernels and extensions are computed on the underlying modules. A
*constructible Weil sheaf* (a *Weil sheaf* for short) is a Weil module with
$M\in\Sh_c(Y,\Lambda)$. By [sk-lem-coefficient-heart] (1), Weil sheaves form a
full abelian subcategory $\Sh_{c,\mathrm W}(Y,\Lambda)$ of
$\Mod_{\mathrm W}(Y,\Lambda)$, closed under kernels, cokernels and extensions.

**Weil complexes.** Let $D^b_{c,\mathrm W}(Y,\Lambda)$ be the full subcategory
of the derived category $D(\Mod_{\mathrm W}(Y,\Lambda))$
([sk-def-sfb-derived-categories]) of bounded complexes all of whose
cohomology objects are Weil sheaves. It is a triangulated subcategory: in a
triangle $K\to L\to C\to K[1]$ the object $H^i(C)$ is an extension of
$\ker(H^{i+1}K\to H^{i+1}L)$ by $\operatorname{coker}(H^iK\to H^iL)$, and both
are Weil sheaves by the closure properties above. The standard truncations of
complexes of Weil modules preserve it, so the standard $t$-structure
restricts to $D^b_{c,\mathrm W}(Y,\Lambda)$, with heart
$\Sh_{c,\mathrm W}(Y,\Lambda)$. Its objects are called *Weil complexes*.

**Forgetful functor and Frobenius.** The forgetful functor
$\Mod_{\mathrm W}(Y,\Lambda)\to\Mod(Y_{\mathrm{proét}},\Lambda)$ is exact, so it
induces a $t$-exact triangulated functor

$$
 \operatorname{For}:D^b_{c,\mathrm W}(Y,\Lambda)
 \longrightarrow \Dbc(Y,\Lambda).
$$

If $K$ is represented by a complex $(M^\bullet,\theta^\bullet)$ of Weil
modules, the termwise isomorphisms $\theta^m$ form an isomorphism of complexes
$g_Y^*M^\bullet\to M^\bullet$, and hence the derived Frobenius isomorphism

$$
 \theta_K:Lg_Y^*\operatorname{For}(K)
 \xrightarrow{\sim}\operatorname{For}(K)
 \quad\text{in }\Dbc(Y,\Lambda),
$$

natural in $K$ and compatible with shifts and distinguished triangles. Thus
every Weil complex gives a pair $(\operatorname{For}(K),\theta_K)$ consisting
of an object of the condensed category $\Dbc(Y,\Lambda)$ and an isomorphism
$Lg_Y^*\operatorname{For}(K)\cong\operatorname{For}(K)$. Where only such a pair
is used (traces of Frobenius on stalks and on cohomology, weights, equivariant
maps), a pair $(K,\theta)$ with $K\in\Dbc(Y,\Lambda)$ and
$\theta:Lg_Y^*K\xrightarrow{\sim}K$ is also called a Weil complex. For $K$ in
the heart the two notions agree: a pair $(\mathcal F,\theta)$ with
$\mathcal F\in\Sh_c(Y,\Lambda)$ is exactly a Weil sheaf, since morphisms in
the heart are morphisms of sheaves.

**Descent to a finite field of coefficients** (a consequence, not part of the
definition). Let $\Lambda=\Qlb$ and let $(K,\theta)$ be a pair as above. By
[sk-thm-sfb-qlbar-two-colimit] (3) there are a finite $E\subset\Qlb$ and
$K_E\in\Dbc(Y,E)$ with $K\cong(K_E)_{\Qlb}$. The pullback $g_Y^*$ is monoidal
and fixes the coefficients, so it commutes with extension of scalars, and
$\theta$ and $\theta^{-1}$ are morphisms between objects defined over $E$. By
[sk-thm-sfb-qlbar-two-colimit] (2) with $r=0$ they come from morphisms
$\theta_F,\theta'_F$ over some finite $F\supset E$, and after enlarging $F$ the
identities $\theta_F\theta'_F=\mathrm{id}$ and $\theta'_F\theta_F=\mathrm{id}$
hold over $F$. Hence every pair $(K,\theta)$ over $\Qlb$, for instance a Weil
sheaf or the pair $(\operatorname{For}(K),\theta_K)$ of a Weil complex, is the
extension of scalars of a pair $(K_F,\theta_F)$ defined over some finite $F$,
and morphisms of pairs descend in the same way.
