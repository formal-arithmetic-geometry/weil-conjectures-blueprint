+++
kind  = "proof"
of    = "sk-thm-p1"
+++
Write $p:\Pone_S\to S$, and for a base change $g:T\to S$ let
$p':\Pone_T\to T$ and $g':\Pone_T\to\Pone_S$ be the other two sides of the
cartesian square. Higher direct images and cohomology of a sheaf of
$\Lambda$-modules agree with those of its underlying abelian sheaf, and a
sheaf of $\Lambda$-modules is torsion when its underlying abelian sheaf is, so
the torsion-sheaf statements below apply to sheaves of $\Lambda$-modules. We
first prove that for every torsion sheaf $F$ of $\Lambda$-modules on
$\Pone_{S,\Et}$ and every $q$ the exchange morphism
$g^{-1}R^qp_*F\to R^qp'_*g'^{-1}F$ is an isomorphism (steps (i)–(iii)), and
then pass to complexes (step (iv)). The proof depends on the *curve
calculations*, which we now exhibit.

*(i) The curve calculations.* For $C$ separated of finite type
over an algebraically closed $k$ with $\dim C\le1$ and $F$ torsion,
they are the eight assertions on
$(C_1)\ H^q(C_{\Et},F)=0\ (q>2);$\
$(C_2)\ C\ \text{affine}\ \Rightarrow\ H^q=0\ (q>1);$\
$(C_3)\ \operatorname{char}k=p,\ F\ p\text{-primary}\ \Rightarrow\ H^q=0\ (q>1);$\
$(C_4)\ F\ \text{constructible, prime to }p\ \Rightarrow\ H^q(C,F)\ \text{finite};$\
$(C_5)\ C\ \text{proper},\ F\ \text{constructible}\ \Rightarrow\ H^q(C,F)\ \text{finite};$\
$(C_6)\ k\subset k'\ \text{algebraically closed},\ F\ \text{prime to }p \Rightarrow\ H^q(C,F)\cong H^q(C_{k'},F);$\
$(C_7)\ C\ \text{proper}\ \Rightarrow\ H^q(C,F)\cong H^q(C_{k'},F) \text{ for all torsion }F;$\
$(C_8)\ a:U\hookrightarrow C\ \text{open}\ \Rightarrow\ a^*:H^2(C,F)\twoheadrightarrow H^2(U,a^{-1}F).$
For the constant sheaf
$\Fq=\Z/n$ of order $n$ prime to $\operatorname{char}k$ on a smooth
proper connected curve $C$ of genus $g$ these are explicit
computations (the ``Kummer route'': a primitive $n$-th root of unity
identifies $\Z/n\simeq\mu_n$, and the Kummer sequence reads $H^1$ and
$H^2$ off $\Pic(C)$): $H^0(C,\Z/n)=\Z/n$,
$H^1(C,\Z/n)=\Pic(C)[n]\simeq(\Z/n)^{2g}$,
$H^2(C,\Z/n)=\Pic(C)/n\simeq\Z/n$ (via the degree), and
$H^q(C,\Z/n)=0$ for $q\ge3$; this is [sk-thm-curveestimate]. For
an affine open $j:U\hookrightarrow C$ one has $H^q(U,\Z/n)=0$ for
$q\ge2$ (the étale cohomological dimension of an *affine*
curve is $1$; that of the proper $C$ is $2$), and $H^q(C,j_!\Z/n)=0$
for $q\ge3$ with $H^2(C,j_!\Z/n)\to H^2(C,\Z/n)$ surjective (its
cokernel injects into $H^2$ of the finite set $C\setminus U$, which
is $0$); these are $(C_2)$ and $(C_8)$ for the constant sheaf. In
characteristic $p$ the analogues for $\Fp$ come from the
Artin–Schreier sequence
$0\to\Fp\to\mathcal O_C\xrightarrow{F-1}\mathcal O_C\to0$:
$H^0(C,\Fp)=\Fp$, $H^1(C,\Fp)=\ker(F-1\mid H^1(C,\mathcal O_C))$ is
finite of $\Fp$-dimension the $p$-rank of $C$ (at most $g$, not
$2g$), $H^2(C,\Fp)=\operatorname{coker}(F-1\mid H^1(C,\mathcal O_C))=0$
($F-1$ is surjective on a finite-dimensional vector space over the
algebraically closed $k$), and $H^q(C,\Fp)=0$ for $q\ge3$; on an
affine $U$ one has $H^q(U,\Fp)=0$ for $q\ge2$ because $\mathcal O_U$
has no higher cohomology.\
From these,
by finiteness of the normalization, constructible and dense-open
reduction
($0\to j_!j^{-1}F\to F\to i_*i^{-1}F\to0$), locally constant
reduction (finite $r$-group filtration + trace splitting) and
dévissage, $(C_1)$–$(C_8)$ hold for every torsion $F$ and every
such $C$. In particular $(C_6)$/$(C_7)$ give the *invariance*
$H^q(C,F)\cong H^q(C_{k'},F)$ under algebraically closed extension
of the base field, and hence — passing to algebraic closures and
using that universal homeomorphisms do not change the étale site
— under *separably closed* extension $k\subset k'$.

*(ii) Strictly henselian base.* For $A$ strictly henselian
with closed point $s$, the degree-zero comparison
$\Gamma(Z,F)\cong\Gamma(Z_s,F|_{Z_s})$ ($Z$ proper over $A$; Stein's
connectedness), applied through the Mayer–Vietoris sequence to the
two affine opens of $\Pone_A$, kills $H^q$ of an injective for
$q\ge2$; the remaining class in $H^1$ is killed by the
constructible/finite-étale machinery (Gabber's affine comparison +
torsor lifting over a proper henselian pair). Hence
$H^q(\Pone_A,F)\cong H^q(\Pone_s,F|)$ for every torsion $F$. (This
comparison is where the curve calculations of (i) enter for the
constant sheaf on the closed fibre $\Pone_s$.)

*(iii) Arbitrary $S$, one sheaf.* Let $F$ be a torsion sheaf of
$\Lambda$-modules on $\Pone_{S,\Et}$. The stalk of
$g^{-1}R^qp_*F\to R^qp'_*g'^{-1}F$ at a geometric point $\bar t\to T$
(over $\bar s\to S$) is, by (ii) applied over the strict henselizations of
$S$ at $\bar s$ and of $T$ at $\bar t$, the canonical pullback
$H^q(\Pone_{\kappa(\bar s)},F|)\to H^q(\Pone_{\kappa(\bar t)},F|)$ between
separably closed fields, an isomorphism by the invariance obtained in (i).
Geometric stalks are conservative, so the exchange morphism is an
isomorphism on every cohomology sheaf of $F$ placed in degree $0$; that is,
the exchange morphism $\Ex_{\square,F}$ is an isomorphism in
$\Dplus(T_{\Et},\Lambda)$. In particular, if $I$ is a torsion injective
sheaf of $\Lambda$-modules, then $R^qp_*I=0$ for $q>0$, hence
$R^qp'_*g'^{-1}I\cong g^{-1}R^qp_*I=0$: the projection satisfies
$\mathrm{IA}_\Lambda$ of [sk-def-ia].

*(iv) Complexes.* Let $K\in\Dplus(\Pone_{S,\Et},\Lambda)$ have torsion
cohomology sheaves and fix $m\in\mathbf Z$; we show that
$H^m(\Ex_{\square,K})$ is an isomorphism. The functors $g^{-1}Rp_*$ and
$Rp'_*g'^{-1}$ are triangulated, $\Ex_\square$ is a morphism of triangulated
functors, and both functors carry $D^{\geq m+1}$ into $D^{\geq m+1}$ ($g^{-1}$
and $g'^{-1}$ are exact, $p_*$ and $p'_*$ left exact). Applied to the
triangle $\tau_{\leq m}K\to K\to\tau_{>m}K\to$, this shows that $H^m$ of
either functor at $K$ equals $H^m$ at $\tau_{\leq m}K$, compatibly with
$\Ex_\square$. Since $K$ is bounded below, $\tau_{\leq m}K$ is bounded, and
by induction on the number of its nonzero cohomology sheaves, using the
triangles $\tau_{\leq n-1}K\to\tau_{\leq n}K\to H^n(K)[-n]\to$ and the five
lemma on the long exact cohomology sequences, it suffices that
$\Ex_{\square,H^n(K)[-n]}$ is an isomorphism. This is (iii) for the torsion
sheaf $H^n(K)$, shifted. Hence $\Ex_{\square,K}$ is an isomorphism, which is
$\mathrm{PBC}_\Lambda$ for the projection. (For a torsion ring $\Lambda$ the
same conclusion also follows from $\mathrm{IA}_\Lambda$ by [sk-thm-iff].)
