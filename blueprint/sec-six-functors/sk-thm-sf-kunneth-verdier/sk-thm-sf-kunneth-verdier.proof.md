+++
kind = "proof"
of = "sk-thm-sf-kunneth-verdier"
uses = ["sk-lem-sf-kunneth-star", "sk-thm-pd-verdier-duality", "sk-thm-sf-ctf-stability", "sk-def-sf-kv-maps", "sk-lem-sf-flat-model", "sk-lem-sf-mate", "sk-prop-sf-closed-unit", "sk-prop-sf-dualizable-biduality", "sk-prop-sf-localization", "sk-prop-sf-open-closed-triangle", "sk-thm-regular", "sk-thm-sf-tensor-hom", "sk-thm-smooth-purity"]
+++
The geometric content is the Künneth formula for exceptional inverse images, that is,
the invertibility of the comparison map $\alpha$ below; the rest is formal. From
$\alpha$ one deduces a Künneth formula for internal Hom and hence for Verdier duals,
which gives the first isomorphism. The second isomorphism is an exceptional
tensor–Hom exchange, and the trace morphism is diagonal evaluation followed by
exceptional base change along the diagonal.

*The comparison map.* Compact-support Künneth follows from compact-support base change
and the projection formula:

$$
R\Gamma_c(U\times V,M\boxtimes N)
\simeq R\Gamma_c(U,M)\dt R\Gamma_c(V,N).
$$

Its exceptional adjoint defines, for morphisms $f_i:X_i\to Y_i$ and
$L_i\in\Dctf(Y_i,A)$, $i=1,2$, the comparison morphism in
$D((X_1\times X_2)_{\mathrm{pro\acute et}},A)$

$$
\alpha:f_1^!L_1\boxtimes f_2^!L_2\longrightarrow
(f_1\times f_2)^!(L_1\boxtimes L_2).
$$

Its invertibility is proved from smooth purity and ordinary external Künneth,
Proposition [sk-lem-sf-kunneth-star]; for the classical statements see (SGA 5, III,
(1.6.4), (1.7.3), Proposition 1.7.4 and (3.1.1)).

*Constant and lisse coefficients (routine).* For constant coefficients, smooth maps are
handled by smooth purity and its product-compatible trace. Closed immersions are
handled by the localization triangle and the identity-factor case of ordinary external
Künneth for the complementary open immersions. Affine factorization as a closed
immersion followed by a smooth projection, and Zariski localization, give the constant
case for general maps. Lisse finite flat coefficients become finite projective constant
coefficients on étale covers, so descent gives the lisse case and then bounded perfect
lisse models.

*General coefficients (routine dévissage).* Induct on the sum of the support dimensions
of $L_1,L_2$. Closed pushforward is compatible with $\alpha$ by proper base change and
the exceptional exchange of Theorem [sk-thm-pd-verdier-duality], so the closed support
may first be made the entire base. Finite constructible stratification and bounded
flat models reduce the generators to $j_{i!}F_i$ for dense open
$j_i:U_i\hookrightarrow Y_i$, with $F_i$ lisse and perfect. Since $f_i^!$ does not
commute with $j_{i!}$ in general, we pass through $Rj_{i*}$. Exceptional exchange with
$Rj_{i*}$ and ordinary external Künneth first identify the comparison on
$(Rj_{1*}F_1,Rj_{2*}F_2)$ with pushforward of the lisse comparison; here
$f^!Rj_*\simeq Rj'_*f_U^!$ is the right-adjoint mate of open base change for $Rf_!$. In
the triangles

$$
j_{i!}F_i\longrightarrow Rj_{i*}F_i\longrightarrow
i_{i*}i_i^*Rj_{i*}F_i\xrightarrow{+1},
$$

the third term remains finite-Tor constructible by Proposition [sk-thm-sf-ctf-stability]
and has smaller support dimension. Induction and two-out-of-three, in one variable and
then the other, prove $\alpha$ for $(j_{1!}F_1,j_{2!}F_2)$.

*Internal Hom and Verdier duals.* For $E_i,L_i\in\Dctf(X_i,A)$ the external comparison
$\cHom_A(E_1,L_1)\boxtimes\cHom_A(E_2,L_2)\to
\cHom_A(E_1\boxtimes E_2,L_1\boxtimes L_2)$ is an isomorphism. It suffices to check it
on generators $E_i=Rh_{i!}F_i$, with $h_i$ the inclusion of a stratum and $F_i$ lisse
perfect, for which

$$
\cHom_A(Rh_{i!}F_i,L_i)
\simeq Rh_{i*}(F_i^\vee\dt h_i^!L_i);
$$

ordinary Künneth and $\alpha$ identify the exterior product of these expressions with
internal Hom on the product, and dévissage extends this to all $E_i$. Taking
$L_i=\omega_{X_i}$ and using $\alpha$ for the structure maps gives, for
$M_i\in\Dctf(X_i,A)$,

$$
\mathbb D_{X_1\times X_2}(M_1\boxtimes M_2)
\simeq \mathbb D_{X_1}M_1\boxtimes \mathbb D_{X_2}M_2.
$$

*The two isomorphisms.* For $M\in\Dctf(U,A)$, $N\in\Dctf(V,A)$ and the projections
$p_U,p_V$ of $V\times U$, Verdier exchange and biduality rewrite
$\cHom_A(p_U^*M,p_V^!N)$ as $\mathbb D_{V\times U}(\mathbb D_VN\boxtimes M)$, and the
formula for duals of exterior products identifies it with $N\boxtimes \mathbb D_UM$.
Taking $M=N=K$, with the product factors ordered as above, gives the first
isomorphism. The second follows from the canonical exceptional tensor–Hom exchange,
for $P,Q\in\Dctf(X\times X,A)$,

$$
c^!\cHom_A(P,Q)\simeq\cHom_A(c^*P,c^!Q),
$$

applied to $P=p_2^*K$ and $Q=p_1^!K$. The exchange is proved by testing against an
object $M$ of $D(C_{\mathrm{pro\acute et}},A)$ and applying $c_!\dashv c^!$, the
projection formula for $c_!$, and the tensor–Hom adjunction, in that order.

*The trace morphism.* Let $e_K:P_X\to R\Delta_{X*}\omega_X$ be adjoint to the evaluation
$\Delta_X^*P_X=K\dt \mathbb D_XK\to\omega_X$. Apply $c^!$ and the exceptional proper
base-change isomorphism for $\Delta_X$:

$$
c^!P_X\xrightarrow{c^!e_K}c^!R\Delta_{X*}\omega_X
\xrightarrow{\sim}Ri_{c*}d_c^!\omega_X
\simeq Ri_{c*}\omega_{F_c}.
$$

The final isomorphism is composition of exceptional inverse images.

*General form.* The three maps of [sk-def-sf-kv-maps] are treated in turn.

*The map $\alpha$.* Take first a constant auxiliary coefficient. For
smooth $f_i$ of relative dimension $d_i$, [sk-thm-smooth-purity] identifies
$Rf_i^!$ with $Lf_i^*(d_i)[2d_i]$, and its compatibility with base change and
with composition identifies the smooth product comparison with the ordinary
pullback–tensor comparison and the sum of the twists; the smooth trace is the
exceptional counit under this orientation, and its base-change square is the
adjoint of the same purity comparison, using the adjunction coherence of
fix-prop-adjunctions and the mate calculus [sk-lem-sf-mate]. Closed immersions are handled by supported
localization [sk-prop-sf-localization] together with the closed-immersion unit
[sk-prop-sf-closed-unit] and the case $Q=\Lambda_Z$ of
[sk-lem-sf-kunneth-star]; the regular case carries the fundamental class of
[sk-thm-regular]. An affine factorization of a general $f_i$ into a closed
immersion followed by a smooth projection gives the map locally. This
settles constant coefficients $L_i=\Lambda_{Y_i}$, hence, by additivity,
finite free ones. For $L_i$ lisse with flat stalks the invertibility of
$\alpha$ is étale-local on $Y_1\times Y_2$ — $Rf^!$ commutes with étale
pullback (for étale $u$, $Ru^!=Lu^*$, and the composition isomorphism of
[sk-lem-sf-mate]), compatibly with $\alpha$ — and on a finite étale cover
trivializing the $L_i$ they become finite free, the case just treated; this
is a local reduction, not a dévissage (the lisse coefficients cannot be
replaced by constant ones globally, [sk-lem-sf-flat-model]). For
general $L_i\in\Dctf(Y_i,\Lambda)$ argue by induction on
$\delta=\dim\operatorname{supp}L_1+\dim\operatorname{supp}L_2$; the claim is
trivial if some $L_i=0$, and both sides of $\alpha$ are exact in each $L_i$,
so two-out-of-three applies to triangles in either variable.
*Closed pushforward.* For a closed immersion $g_1:Z_1\hookrightarrow
Y_1$, with $g_1':X_1\times_{Y_1}Z_1\hookrightarrow X_1$ and
$f_1':X_1\times_{Y_1}Z_1\to Z_1$ the projections, the dual base change
$Rf_1^!Rg_{1*}\cong Rg'_{1*}Rf_1'^!$ (the mate of $\operatorname{Ex}_!$ under
[sk-lem-sf-mate]) and $Rg_{1*}M_1\boxtimes L_2\cong
R(g_1\times\mathrm{id})_*(M_1\boxtimes L_2)$ ([sk-lem-sf-kunneth-star])
identify $\alpha_f(Rg_{1*}M_1,L_2)$ with
$R(g_1'\times\mathrm{id})_*\,\alpha_{f_1'\times f_2}(M_1,L_2)$, compatibly
with the definition of $\alpha$ as an exceptional adjoint (a mate-calculus
check, [sk-lem-sf-mate]); likewise in the second variable. Since
$L_i\cong Rg_{i*}g_i^*L_i$ for $Z_i=\operatorname{supp}L_i$
([sk-prop-sf-open-closed-triangle], as $L_i$ vanishes on the complement),
we may assume $\dim Y_i=\dim\operatorname{supp}L_i$. Then by the generation
[sk-lem-sf-flat-model] on $Y_i$ it suffices to treat the generators
$L_i=Rg_{i*}j_{i!}F_i$ with $F_i$ lisse with flat stalks on a stratum $U_i$
dense in $\overline U_i$, $\dim\overline U_i\le\dim Y_i$, and by the closed
pushforward just described we may take $\overline U_i=Y_i$, $L_i=j_{i!}F_i$.
*Open localization.* $Rf^!$ does not commute with $j_!$, so pass
through $Rj_*$: for the open immersion $j=j_1\times j_2$ with base changes
$j'$ and $f'$, the dual base change $Rf^!Rj_*\cong Rj'_*Rf'^!$ (the mate of
the base change for $j_!$) and [sk-lem-sf-kunneth-star], which gives
$Rj_{1*}F_1\boxtimes Rj_{2*}F_2\cong Rj_*(F_1\boxtimes F_2)$ and
$Rj'_{1*}Rf_1'^!F_1\boxtimes Rj'_{2*}Rf_2'^!F_2\cong
Rj'_*(Rf_1'^!F_1\boxtimes Rf_2'^!F_2)$, identify
$\alpha_f(Rj_{1*}F_1,Rj_{2*}F_2)$ with $Rj'_*\,\alpha_{f'}(F_1,F_2)$,
compatibly with $\alpha$ as before; the latter is the lisse case already
treated, so $\alpha$ is invertible on $(Rj_{1*}F_1,Rj_{2*}F_2)$. The
open–closed triangle [sk-prop-sf-open-closed-triangle] for
$M=Rj_{i*}F_i$ reads
$j_{i!}F_i\to Rj_{i*}F_i\to T_i\xrightarrow{+1}$ with
$T_i=i_{i*}i_i^*Rj_{i*}F_i\in\Dctf(Y_i,\Lambda)$
([sk-thm-sf-ctf-stability]), a general object of $\Dctf$ supported on the
boundary $Z_i=Y_i\setminus U_i$, of dimension $<\dim Y_i$. By the induction
hypothesis $\alpha$ is invertible on $(T_1,j_{2!}F_2)$ and on
$(Rj_{1*}F_1,T_2)$, the support dimensions having dropped; two-out-of-three
in the second variable gives $(Rj_{1*}F_1,j_{2!}F_2)$, and then in the first
variable $(j_{1!}F_1,j_{2!}F_2)$. Hence $\alpha$ is invertible.

*The map $\beta$.* Both sides are exact in each $E_i$, so dévissage in
both $E_i$, by [sk-lem-sf-flat-model], reduces to $E_i=Rh_{i!}F_i$ with
$h_i=g_ij_i$, $g_i$ finite and $j_i$ open, and $F_i$ lisse on $U_i$ with flat
stalks. Such an $F_i$ is dualizable: its stalks are finite flat, hence free,
over the local ring $\Lambda$, so $F_i$ is locally finite free and
[sk-prop-sf-dualizable-biduality] gives $\RHom(F_i,-)\simeq
F_i^\vee\otimes^L-$. Tensor–Hom and the exceptional adjunction then give
$\RHom(E_i,L_i)\simeq Rh_{i*}\RHom(F_i,Rh_i^!L_i)\simeq
Rh_{i*}\bigl(F_i^\vee\otimes^LRh_i^!L_i\bigr)$ ([sk-thm-sf-tensor-hom]).
With $h=h_1\times h_2$ and $F=F_1\boxtimes F_2$, so that
$F^\vee\simeq F_1^\vee\boxtimes F_2^\vee$ and $E_1\boxtimes E_2\simeq Rh_!F$
($\mathrm{Ku}_!$), the comparison becomes

$$
 Rh_{1*}\bigl(F_1^\vee\otimes^LRh_1^!L_1\bigr)\boxtimes
 Rh_{2*}\bigl(F_2^\vee\otimes^LRh_2^!L_2\bigr)
 \xrightarrow[\text{twice}]{\ \mathrm{Ku}_*\ }
 Rh_*\bigl(F^\vee\otimes^L(Rh_1^!L_1\boxtimes Rh_2^!L_2)\bigr)
 \xrightarrow{\ Rh_*(1\otimes\alpha)\ }
 Rh_*\bigl(F^\vee\otimes^LRh^!(L_1\boxtimes L_2)\bigr),
$$

the first arrow being [sk-lem-sf-kunneth-star] in each factor (after the
symmetry of $\otimes^L$) and the second the $\alpha$ just proved; by the same
identifications the target is $\RHom(E_1\boxtimes E_2,L_1\boxtimes L_2)$.
Taking ordinary and then exceptional adjoints identifies this composite with
the specified $\beta$: both paths become the tensor product of the two
evaluation maps after the projection formula. Hence $\beta$ is invertible.

*The map $\kappa$.* Apply $\beta$ to the pairs $(\Lambda_X,M)$ and
$(N,\omega_Y)$, then $\RHom(1,\alpha)$ for the identification
$M\boxtimes\omega_Y\simeq Rp_X^!M$, which is $\alpha$ for
$\operatorname{id}_X\times a_Y$. Their composite is $\kappa_{M,N}$ by
[sk-def-sf-kv-maps] (iv), and both factors have just been shown invertible.
