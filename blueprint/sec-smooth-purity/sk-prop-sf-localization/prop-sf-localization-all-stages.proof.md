+++
kind  = "proof"
of    = "prop-sf-localization-all-stages"
+++
*Vanishing.* For every $\Lambda$, $\operatorname{Hom}(i_*P[m],Rj_*N)=0$ for
$P\in D(Z_{\mathrm{proét}},\Lambda)$ and $N\in D(U_{\mathrm{proét}},\Lambda)$. Indeed
it is $\operatorname{Hom}(j^*i_*P[m],N)$ by $j^*\dashv Rj_*$
([def-weil-pbc-proetale-operations], [sk-def-sf-operations]), and
$j^*i_*=0$: $j^*$ is restriction to $U_{\mathrm{proét}}$, and
$(i_*M)(V)=M(V\times_XZ)=0$ for $V$ over $U$ (compare
[lem-exc-proetale-closed-essential-image]). Moreover $j^*Rj_*\cong\operatorname{id}$,
since restriction to the open $U$ is exact and preserves K-injective
complexes.

*(1).* For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$ one has $D^b_c=D^b_{ctf}$, and $Rj_*$
preserves it ([sk-thm-sf-ctf-stability]). For $\Lambda=A=A_{E,n}$, write
$G=\nu_U^*G'$ with $G'$ étale bounded constructible
([lem-sf-proetale-constructible-origin]); then $Rj_*G\cong\nu_X^*Rj_*G'$ by
[prop-weil-pbc-comparison-direct-image], and $Rj_*G'$ is bounded constructible
by [thm-fin-open-immersion] and dévissage over the finitely many cohomology
sheaves ([thm-constructible-serre]).

*(2) and (3).* The argument is the same for every $\Lambda$. Let
$K\in D^b_c(X,\Lambda)$ and let $F\to K\to Rj_*j^*K\to F[1]$ be a fibre
sequence of the open unit. By (1), $F\in D^b_c(X,\Lambda)$
([sk-def-sfb-bounded-constructible]). Since $j^*K\to j^*Rj_*j^*K$ is an
isomorphism, $j^*F=0$. The open–closed triangle
[prop-sf-open-closed-triangle-all-stages] for $F$ then shows that the unit
$F\to i_*i^*F$ is an isomorphism. Put $Q=i^*F\in D^b_c(Z,\Lambda)$. For
$P\in D^b_c(Z,\Lambda)$ the vanishing and the full faithfulness of
[prop-sf-closed-unit-all-stages] give, naturally in $P$,
$$
\operatorname{Hom}(P,Q)\cong\operatorname{Hom}(i_*P,i_*Q)
=\operatorname{Hom}(i_*P,F)\xrightarrow{\sim}\operatorname{Hom}(i_*P,K).
$$
Thus $Ri^!K:=Q$ is right adjoint to $i_*$ on $D^b_c$, with counit $F\to K$,
and the triangle of (3) is $F\to K\to Rj_*j^*K\to$. The vanishing makes
its third arrow unique and the triangle functorial. By uniqueness of right
adjoints $Ri^!$ is the restriction of the exceptional inverse image of
[sk-thm-existence] ($i_*=Ri_!$, $i$ being proper). At $\Lambda=A$ it is
also the restriction of the ambient right adjoint of
[lem-exc-proetale-closed-support], with the triangle of
[lem-exc-proetale-support-triangle], and hence the finite exceptional inverse
image of [def-weil-exceptional-inverse-image], as in
[prop-sf-closed-immersion-unit]. At $\mathcal O_E$ the coefficient
comparisons along $\mathcal O_E\to A_{E,m}$ for $Rj_*$ and for the exceptional
inverse image are isomorphisms ([sk-prop-scalar-six]). This gives
$(Rj_*G)_m\cong Rj_*G_m$ and $(Ri^!K)_m\cong Ri_m^!K_m$; integral models and
reductions enter only here, as consequences.

*Consequences.* For (4): $\operatorname{Hom}(N[m],Ri^!Rj_*G)
=\operatorname{Hom}(i_*N[m],Rj_*G)=0$ for all $N$ and $m$, so
$Ri^!Rj_*G=0$; the unit is an isomorphism by
[prop-sf-closed-unit-all-stages].

*Finite Tor amplitude.* Let $A=A_{E,n}$ and $\kappa=A/(\varpi_E)$, the
constant sheaf on each site.

*Residue criterion.* On any of the pro-étale sites, a bounded constructible
complex $K$ has Tor amplitude in $[a,b]$ if and only if $K\otimes^L_A\kappa$
has cohomology in $[a,b]$, by [lem-sf-proetale-residue-tor-test], the
pro-étale form of the étale criterion [lem-exc-residue-tor-test]; it is
applied below only to bounded constructible complexes, by (1) and (2). The pullbacks
$i^*,j^*,\nu^*$ commute with $-\otimes^L_A\kappa$, being monoidal with
$\kappa$ pulling back to $\kappa$ ([def-weil-derived-pullback-tensor-hom],
[prop-weil-pbc-proetale-constant-ring-map]); being exact they preserve
cohomological intervals. Conversely $\nu^*$ reflects them: if
$\nu^*C$ has cohomology in $[a,b]$ for $C\in\Dplus$, then
$\nu^*\tau_{>b}C=\tau_{>b}\nu^*C=0$, hence $\tau_{>b}C=0$ by
[thm-weil-pbc-site-comparison], and likewise below $a$.

*(3') for $i^*,j^*,i_*$.* For $i^*$ and $j^*$ this is the criterion and
the commutation just stated. For $P\in D^b_{ctf}(Z,A)$ with amplitude
$[a,b]$, $j^*(i_*P\otimes^L_A\kappa)\cong j^*i_*P\otimes^L_A\kappa=0$, so
each cohomology sheaf of $i_*P\otimes^L_A\kappa$ is in the image of $i_*$
([lem-exc-proetale-closed-essential-image]) and equals
$i_*i^*\mathcal H^r(i_*P\otimes^L_A\kappa)\cong
i_*\mathcal H^r(P\otimes^L_A\kappa)$, using exactness of $i^*$ and
$i^*i_*\cong\operatorname{id}$; it vanishes outside $[a,b]$.

*(1') at the finite stage.* Let $G\in D^b_{ctf}(U,A)$ have amplitude
$[a,b]$ and write $G=\nu_U^*G'$ as in the proof of (1). Then
$\nu_U^*(G'\otimes^L_A\kappa)\cong G\otimes^L_A\kappa$ has cohomology in
$[a,b]$, hence so has $G'\otimes^L_A\kappa$. The higher direct images
$R^qj_*$ on the small étale site vanish on sheaves of $A$-modules for
$q>2d+c$: for $k$ algebraically closed this is
[lem-sf-etale-direct-image-vanishing]; in general its proof applies
verbatim, with [thm-sc-finite-type-torsion-cd] at the given $c$. By the
truncation spectral sequence [thm-sp-truncation-e2],
$Rj_*(G'\otimes^L_A\kappa)$ has cohomology in $[a,b+2d+c]$.

*Projection formula for $\kappa$.* The canonical map
$Rj_*G'\otimes^L_A\kappa\to Rj_*(G'\otimes^L_A\kappa)$ is an isomorphism.
Choose a bounded-above resolution $P\to\kappa$ by finite free $A$-modules;
tensoring with the constant complex $P$ computes $-\otimes^L_A\kappa$. For
the finite stupid truncations $\sigma_{\ge-t}P$ the comparison is an
isomorphism: it is the identity for $A$ and is preserved by finite sums,
shifts and cones. Let $G'$ and $Rj_*G'$ have cohomology in degrees $\le e$.
The quotients $\sigma_{<-t}P$ live in degrees $\le-t-1$, so
$G'\otimes\sigma_{<-t}P$ has cohomology in degrees $\le e-t-1$, and
$Rj_*$ of it in degrees $\le e-t-1+2d+c$ (the vanishing above), while
$Rj_*G'\otimes\sigma_{<-t}P$ has cohomology in degrees $\le e-t-1$.
For fixed $r$ and $t$ large, the long exact sequences of the two
triangles attached to $\sigma_{\ge-t}P\to P\to\sigma_{<-t}P$ therefore
identify both sides with the finite-free comparison in degree $r$.

Hence $Rj_*G'\otimes^L_A\kappa$ has cohomology in $[a,b+2d+c]$. Applying
$\nu_X^*$ and [prop-weil-pbc-comparison-direct-image],
$Rj_*G\otimes^L_A\kappa\cong\nu_X^*(Rj_*G'\otimes^L_A\kappa)$ has
cohomology in the same interval; with (1), the residue criterion gives
$Rj_*G\in D^b_{ctf}(X,A)$ with amplitude $[a,b+2d+c]$.

*(2') at the finite stage.* Let $K$ have amplitude $[a,b]$. Then $j^*K$
has amplitude $[a,b]$ and $Rj_*j^*K$ amplitude $[a,b+2d+c]$. Tensoring the
triangle of (3) with $\kappa$ and taking the long exact sequence,
$\mathcal H^r(i_*Ri^!K\otimes^L_A\kappa)$ lies between
$\mathcal H^{r-1}(Rj_*j^*K\otimes^L_A\kappa)$ and
$\mathcal H^r(K\otimes^L_A\kappa)$, so it vanishes outside
$[a,b+2d+c+1]$. Since $Ri^!K\cong i^*i_*Ri^!K$, the commutation of $i^*$
with $-\otimes^L_A\kappa$ and the residue criterion give amplitude
$[a,b+2d+c+1]$ for $Ri^!K$.

*Other stages.* At $\mathcal O_E$, the reductions are
$(Rj_*G)_m\cong Rj_*G_m$ and $(Ri^!K)_m\cong Ri_m^!K_m$ (shown above), and
similarly for $i^*,j^*,i_*$; the finite-stage bounds hold with intervals
depending only on the uniform interval of the reductions of $G$, resp. $K$.
At $E$ and $\Qlb$, $D^b_{ctf}=D^b_c$ ([sk-def-sf-setting]). Clauses (3') and
(4') are then (3) and (4) read inside the full subcategories $D^b_{ctf}$.

*Weil structures.* The Weil structures of $i^*,j^*,Rj_*$ come from the
exchange isomorphisms for the Frobenius automorphism squares, and the open
unit is equivariant, as in [prop-sf-open-closed-triangle-all-stages]. For a Weil complex $K$, the
fibre $F$ therefore carries a unique Weil structure making $F\to K$
equivariant (uniqueness from the vanishing), and $Ri^!K=i^*F$ inherits it;
under the adjunction bijection above this is the mate of the Weil structure
of $i_*$, so the adjunction, its counit and unit are equivariant. The third
arrow is equivariant by the uniqueness in (3).
