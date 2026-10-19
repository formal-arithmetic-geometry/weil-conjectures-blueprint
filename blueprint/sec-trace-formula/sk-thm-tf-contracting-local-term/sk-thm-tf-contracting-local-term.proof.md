+++
kind = "proof"
of = "sk-thm-tf-contracting-local-term"
uses = ["sk-lem-tf-contracting-fixed-geometry", "sk-cor-tf-sp-fixed-constant", "sk-thm-tf-sp-zero-section", "sk-lem-tf-contracting-cone-geometry", "sk-prop-tf-trace-specialization", "sk-i-additivity", "sk-p-proper"]
+++
By Remark [sk-rem-tf-contracting-neighbourhood], restricting $C$ to $W$
and removing the other fixed components does not change the trace
class on $\beta$. We may therefore assume $F_c=\beta$ and that the
ideal inclusions hold on $C$.

The restricted morphism $u_Z$ comes from base change along the
first leg. Write $i:Z_{\mathrm{red}}\hookrightarrow X$ and
$e:C_Z\hookrightarrow C$. The square formed by $e$, $i$, $c_1$ and
$c_{Z,1}$ is Cartesian up to reduction, so nilpotent invariance and
compact-support base change give

$$
 i^*Rc_{1!}\simeq Rc_{Z,1!}e^*.
$$

Since $L\subset J$, the second leg maps $C_Z$ into $Z_{\mathrm{red}}$,
so $e^*c_2^*K\simeq c_{Z,2}^*i^*K$. The adjoint
$\widehat u:Rc_{1!}c_2^*K\to K$ of $u$ under $Rc_{1!}\dashv c_1^!$
therefore induces

$$
 Rc_{Z,1!}c_{Z,2}^*i^*K
    \simeq i^*Rc_{1!}c_2^*K
    \xrightarrow{i^*\widehat u}i^*K.
$$

Define $u_Z$ as its adjoint under $Rc_{Z,1!}\dashv c_{Z,1}^!$.
Equivalently, $u_Z$ is $e^*u$ followed by the base-change mate
$e^*c_1^!K\to c_{Z,1}^!i^*K$; this mate is in general not an
isomorphism.

By Lemma [sk-lem-tf-contracting-fixed-geometry], the common map
$F_c\to X$ lands set-theoretically in $Z$, and after base change from
$T$ to $S$ the fixed scheme of the deformed correspondence has
reduction $(F_c\times S)_{\mathrm{red}}$. This is the hypothesis of
Corollary [sk-cor-tf-sp-fixed-constant], used below.

Suppose first that $i^*K=0$. Verdier's zero-section theorem
(Theorem [sk-thm-tf-sp-zero-section]) identifies the restriction of
$\operatorname{Sp}_{X,Z}(K)$ to the zero section with the restriction
of $K$ to $Z$; with nilpotent invariance for $Z_{\mathrm{red}}\to Z$
it gives

$$
 \operatorname{Sp}_{X,Z}(K)|_Z=0.
$$

By Lemma [sk-lem-tf-contracting-cone-geometry] (2), the ordinary-pullback
leg $\gamma_2$ of the special correspondence maps set-theoretically
into the zero section, and nilpotent invariance gives
$\gamma_2^*\operatorname{Sp}_{X,Z}(K)=0$.
The specialized morphism therefore has zero source and zero trace.
By Proposition [sk-prop-tf-trace-specialization], this trace is the
specialization of $\operatorname{Tr}_c(u)$ along the fixed scheme of
the deformed correspondence. Corollary [sk-cor-tf-sp-fixed-constant]
identifies this specialization with the identity, so it is injective
and $\operatorname{Tr}_c(u)=0$.

For general $K$, apply Proposition [sk-i-additivity]
to the triangle

$$
 j_!j^*K\longrightarrow K\longrightarrow Ri_*i^*K,
 \qquad j:X\setminus Z_{\mathrm{red}}\hookrightarrow X.
$$

The ideal inclusions give
$c_1^{-1}(Z_{\mathrm{red}})\subset c_2^{-1}(Z_{\mathrm{red}})$,
which is the hypothesis of that proposition.
The open piece has zero trace by the case just treated. By the
construction in that proposition, the closed graded piece is the
proper pushforward of the restricted correspondence, which is $u_Z$,
and
Theorem [sk-p-proper] identifies its trace with the
pushforward of the trace class on $c_Z$.
Lemma [sk-lem-tf-contracting-fixed-geometry] identifies $h_\beta$ after
reduction, which proves the displayed formula. Integrating and
composing exceptional counits gives the equality of local terms.
