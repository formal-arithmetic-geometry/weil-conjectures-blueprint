+++
kind = "proof"
of = "sk-thm-tf-contracting-local-term"
uses = ["sk-lem-tf-contracting-fixed-geometry", "sk-cor-tf-sp-fixed-constant", "sk-thm-tf-sp-zero-section", "sk-lem-tf-contracting-cone-geometry", "sk-prop-tf-trace-specialization", "sk-i-additivity", "sk-p-proper", "sk-rem-tf-contracting-neighbourhood"]
+++
By Remark [sk-rem-tf-contracting-neighbourhood], restricting $C$ to $W$
and removing the other connected components of $\Fix(c)$ does not change the trace
class on $F_0$. Therefore we may assume that $\Fix(c)=F_0$ and that the
ideal inclusions hold on $C$.

The restricted morphism $u_Z$ is obtained by base change along the
first leg. Write $i:Z_{\mathrm{red}}\hookrightarrow X$ and
$i':C_Z\hookrightarrow C$. The square formed by $i'$, $i$, $c_1$ and
$c_{Z,1}$ is cartesian up to reduction, and hence invariance under
nilpotent thickenings and base change for direct image with compact
support show that

$$
i^*Rc_{1!}\simeq Rc_{Z,1!}i'^*.
$$

Since $I_2\subset I_1$, the second leg maps $C_Z$ into $Z_{\mathrm{red}}$,
and hence $i'^*c_2^*K\simeq c_{Z,2}^*i^*K$. Therefore the adjoint
$\widehat u:Rc_{1!}c_2^*K\to K$ of $u$ under $Rc_{1!}\dashv c_1^!$
induces

$$
Rc_{Z,1!}c_{Z,2}^*i^*K
\simeq i^*Rc_{1!}c_2^*K
\xrightarrow{i^*\widehat u}i^*K.
$$

We define $u_Z$ as its adjoint under $Rc_{Z,1!}\dashv c_{Z,1}^!$.
Equivalently, $u_Z$ is $i'^*u$ followed by the base change map
$i'^*c_1^!K\to c_{Z,1}^!i^*K$, which in general is not an
isomorphism.

By Lemma [sk-lem-tf-contracting-fixed-geometry], the common map
$\Fix(c)\to X$ maps set-theoretically into $Z$, and after base change from
$T$ to $S$ the reduction of the fixed scheme of the deformed
correspondence is $(\Fix(c)\times S)_{\mathrm{red}}$. This is the
hypothesis of Corollary [sk-cor-tf-sp-fixed-constant], which we use below.

Suppose first that $i^*K=0$. Verdier's theorem on the zero section
(Theorem [sk-thm-tf-sp-zero-section]) identifies the restriction of
$\operatorname{Sp}_{X,Z}(K)$ to the zero section with the restriction
of $K$ to $Z$. Together with invariance under the nilpotent
thickening $Z_{\mathrm{red}}\to Z$, it shows that

$$
\operatorname{Sp}_{X,Z}(K)|_Z=0.
$$

By Lemma [sk-lem-tf-contracting-cone-geometry](2), the leg $\gamma_2$ of
the correspondence on the special fibre, along which we take ordinary pullback, maps
set-theoretically into the zero section, and by invariance under
nilpotent thickenings we get $\gamma_2^*\operatorname{Sp}_{X,Z}(K)=0$.
Thus the specialized morphism has zero source and zero trace.
The generic fibre of the deformed correspondence is $c$ over $\eta$,
so Proposition [sk-prop-tf-trace-specialization] says that this trace is
the specialization of the pullback of $\operatorname{Tr}_c(u)$ to the
generic fibre. By Corollary [sk-cor-tf-sp-fixed-constant], specialization
is the identity under the identifications for constant families, which
carry that pullback to $\operatorname{Tr}_c(u)$. Therefore
$\operatorname{Tr}_c(u)=0$.

For general $K$, we apply Proposition [sk-i-additivity]
to the triangle

$$
j_!j^*K\longrightarrow K\longrightarrow Ri_*i^*K,
\qquad j:X\setminus Z_{\mathrm{red}}\hookrightarrow X.
$$

The ideal inclusions imply that
$c_1^{-1}(Z_{\mathrm{red}})\subset c_2^{-1}(Z_{\mathrm{red}})$,
which is the hypothesis of that proposition.
By the case just treated, the open piece has zero trace. By the
construction in that proposition, the closed graded piece is the
proper pushforward of the restricted morphism $u_Z$, and
Theorem [sk-p-proper] identifies its trace with the
pushforward of the trace class on $c_Z$.
Lemma [sk-lem-tf-contracting-fixed-geometry] describes $h_{F_0}$ after
reduction, and this proves the displayed formula. If $F_0$ is proper,
then so is $F_{0,Z}$, since $h_{F_0}$ is an isomorphism after
reduction. Pushing both sides forward to $\operatorname{Spec}k$ and
composing with the trace map, we obtain the equality of local terms
(Definition [sk-d-trace-class]).
