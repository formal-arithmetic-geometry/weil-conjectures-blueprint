+++
id = "def-weil-weil-sheaf-complex"
kind = "definition"
title = "Weil sheaf and Weil complex"
lean = ["AlgebraicGeometry.WeilSheaf", "AlgebraicGeometry.WeilComplex"]
order = 2410
uses = ["def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-scheme-morphism-properties", "def-weil-pbc-proetale-site", "det-def-sfb-condensed-ring", "det-def-sfb-qlbar-condensed", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-derived-categories", "det-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "sk-cor-coefficient-heart-ii"]
+++
Fix the finite-field datum [def-weil-finite-field-fiber] $p,a,q,k_0,k$, where
$q=p^a$, and a prime $\ell\neq p$. Choose an algebraic closure $\Qlb$ of
$\Ql$ and a finite extension $E/\Ql$ contained in $\Qlb$, and let
$\Lambda\in\{\underline E,\underline{\Qlb}\}$ be the corresponding condensed
ring ([det-def-sfb-condensed-ring], [det-def-sfb-qlbar-condensed]); we write
$\Lambda\in\{E,\Qlb\}$. Let $Y_0$ be a finite-type
[def-weil-scheme-morphism-properties] $k_0$-scheme, put $Y=Y_0\times_{k_0}k$,
and let $g_Y:Y\to Y$ be the geometric-Frobenius automorphism of
[def-weil-frobenius-detailed]. On the small pro-étale site
[def-weil-pbc-proetale-site] put $\Lambda_Y=p_Y^*\Lambda$
([det-def-sfb-pulled-back-coefficients]). Since $g_Y$ is an automorphism of
schemes and $p_Y\circ g_Y=p_Y$, the inverse image $g_Y^*$ is an exact
autoequivalence of $\Mod(Y_{\mathrm{proét}},\Lambda)$, with a canonical
isomorphism $g_Y^*\Lambda_Y\cong\Lambda_Y$; being exact it needs no deriving
([det-def-sfb-derived-categories]), and we also write $Lg_Y^*=g_Y^*$ on
$D(Y_{\mathrm{proét}},\Lambda)$. It preserves constructible sheaves and hence the
triangulated subcategory $\Dbc(Y,\Lambda)$ ([det-def-sfb-bounded-constructible],
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
([det-def-sfb-derived-categories]) of bounded complexes all of whose
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
$Lg_Y^*\operatorname{For}(K)\cong\operatorname{For}(K)$.

**Strict Weil complexes.** A pair $(K,\theta)$ with $K\in\Dbc(Y,\Lambda)$ and
$\theta:Lg_Y^*K\xrightarrow{\sim}K$ is a *strict Weil complex*; a morphism
$(K,\theta)\to(L,\theta')$ is a morphism $h:K\to L$ of $\Dbc(Y,\Lambda)$ with
$h\circ\theta=\theta'\circ Lg_Y^*(h)$. Where only such a pair is used (traces of
Frobenius on stalks and on cohomology, weights, equivariant maps), a strict
Weil complex is also called a Weil complex. Strict Weil complexes form a
category of pairs over $\Dbc(Y,\Lambda)$, which is not triangulated, and
$K\mapsto(\operatorname{For}(K),\theta_K)$ is a functor from
$D^b_{c,\mathrm W}(Y,\Lambda)$ to it. On the hearts it is an equivalence: a pair
$(\mathcal F,\theta)$ with $\mathcal F\in\Sh_c(Y,\Lambda)$ is exactly a Weil
sheaf, since morphisms in the heart are morphisms of sheaves. It is not
faithful: on $Y=\operatorname{Spec}k$ a nonsplit Frobenius extension of
$\Lambda$ by $\Lambda$ (a Jordan block) is a nonzero morphism
$\Lambda\to\Lambda[1]$ of $D^b_{c,\mathrm W}(Y,\Lambda)$, while
$\Hom_{\Dbc(Y,\Lambda)}(\Lambda_Y,\Lambda_Y[1])=0$.

**Descent to a finite field of coefficients** (a consequence, not part of the
definition). For finite extensions $E\subset F$ inside $\Qlb$, extension of
scalars $M\mapsto M_F=F_Y\otimes_{E_Y}M$, and likewise $M\mapsto M_{\Qlb}$, is
exact and commutes with $g_Y^*$, so it carries Weil modules to Weil modules and
induces triangulated functors
$D^b_{c,\mathrm W}(Y,E)\to D^b_{c,\mathrm W}(Y,F)\to D^b_{c,\mathrm W}(Y,\Qlb)$
compatible with $\operatorname{For}$. Then:

1. every strict Weil complex $(K,\theta)$ over $\Qlb$, for instance a Weil
   sheaf or the pair $(\operatorname{For}(K),\theta_K)$ of a Weil complex, is
   isomorphic to the extension of scalars of a strict Weil complex
   $(K_F,\theta_F)$ over some finite $F$, with $K_F$ a sheaf when $K$ is one,
   and morphisms of strict Weil complexes descend in the same way;
2. for $K,L\in D^b_{c,\mathrm W}(Y,E)$ and every integer $r$, extension of
   scalars induces an isomorphism
   $$
   \varinjlim_{F\supset E}\Hom_{D^b_{c,\mathrm W}(Y,F)}(K_F,L_F[r])
   \xrightarrow{\ \sim\ }
   \Hom_{D^b_{c,\mathrm W}(Y,\Qlb)}(K_{\Qlb},L_{\Qlb}[r]),
   $$
   the colimit running over finite extensions $F$ of $E$ in $\Qlb$;
3. every Weil complex over $\Qlb$ is isomorphic to $K_{\Qlb}$ for some finite
   $E\subset\Qlb$ and some $K\in D^b_{c,\mathrm W}(Y,E)$.
