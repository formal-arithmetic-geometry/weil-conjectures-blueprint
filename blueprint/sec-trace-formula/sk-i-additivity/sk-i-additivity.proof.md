+++
kind  = "proof"
of    = "sk-i-additivity"
uses  = ["sk-d-integral", "sk-thm-sf-kunneth-verdier"]
+++
For the filtered assertion we lift each step of the trace morphism to filtered
complexes and read off its weight-zero graded piece; this gives the identity of
trace classes before integration. For the open–closed assertion we construct
the filtered correspondence from the localization triangle and identify its
graded pieces.

*Filtered operations (routine).* Use finite decreasing filtrations, the
convolution filtration on tensor products, and the internal-Hom filtration

$$
F^r\mathcal Hom(\mathcal M,\mathcal N)
=\{v:v(F^a\mathcal M)\subset F^{a+r}\mathcal N
\text{ for every }a\}.
$$

Derive these operations using filtered flat and filtered injective
resolutions. For finite filtrations such resolutions can be built successively
on the graded pieces by mapping cylinders. The resulting identities are

$$
\begin{aligned}
\operatorname{gr}^rR\mathcal Hom_F(\mathcal M,\mathcal N)
&\simeq\bigoplus_aR\mathcal Hom(M_a,N_{a+r}),\\
\operatorname{gr}^r\mathbb D_F\mathcal K&\simeq \mathbb D_XK_{-r},\\
\operatorname{gr}^r(\mathcal M\otimes_F\mathcal N)
&\simeq\bigoplus_{a+b=r}M_a\dt N_b.
\end{aligned}
$$

Give $\omega_X$ its filtration concentrated in weight zero. The evaluation
$\mathcal K\otimes_F\mathbb D_F\mathcal K\to\omega_X$ on the weight-zero summand
$K_a\dt \mathbb D_XK_a$ is ordinary evaluation, because evaluation is the
tensor–Hom adjoint of $\operatorname{id}_{\mathcal K}$, whose graded map is
$\operatorname{id}_{K_a}$. The Koszul signs are those of the underlying
complexes; the filtration weights contribute no signs.

*The filtered trace morphism.* The four defining steps of the trace morphism
lift to filtered complexes:

$$
R\mathcal Hom_F(c_2^*\mathcal K,c_1^!\mathcal K)
\simeq c^!(\mathcal K\boxtimes_F\mathbb D_F\mathcal K)
\longrightarrow Ri_{c*}\omega_{F_c}[\text{weight }0].
$$

These steps are exceptional tensor–Hom adjunction, external duality, the
diagonal adjoint of evaluation, and exceptional proper base change for the
closed diagonal. Each is defined by filtered units, counits and tensor
evaluation, and taking graded pieces gives their unfiltered versions. In
particular the filtered external-duality comparison is an isomorphism: each of
its graded maps is a finite sum of the isomorphisms in
Lemma [sk-thm-sf-kunneth-verdier], and graded pieces detect isomorphisms of
finite filtered complexes. Forgetting the filtration gives exactly the trace
morphism already defined.

Its weight-zero map has source

$$
\bigoplus_aR\mathcal Hom(c_2^*K_a,c_1^!K_a),
$$

and its restriction to summand $a$ is $\operatorname{Tr}_{c,K_a}$. The
internal-Hom and external-duality steps preserve the two indices, while
diagonal evaluation on the equal pair of indices is the evaluation just
checked. The section defined by $\tilde u$ comes from the unit in weight zero,
hence lands in $F^0$ of the source. The trace map on $F^1$ is zero, since its
target is pure weight zero. Its restriction to $F^0$ therefore factors through
$\operatorname{gr}^0$, where the section is the tuple $(u_a)_a$. This
factorization holds on filtered dg models, hence survives localization, and it
proves the stated sum in $H^0(F_c,\omega_{F_c})$.

*The open–closed filtration.* Let
$L=Rc_{1!}c_2^*:\Dctf(X,A)\to\Dctf(X,A)$, and let $v:LK\to K$ be the
exceptional adjoint of $u$. Invariance and ordinary inverse-image base change
for $!$ imply

$$
i^*LK_U=0,\qquad
R\operatorname{Hom}_X(LK_U,K_Z)
\simeq R\operatorname{Hom}_Z(i^*LK_U,i^*K)=0.
$$

The second vanishing is that of the whole mapping complex, including all
shifts. Consequently $LK_U\to LK\xrightarrow vK$ factors through $K_U\to K$
with a contractible space of choices, and the coherent cofiber of this
factorization gives a morphism of two-step filtered objects

$$
\begin{array}{ccccc}
LK_U&\longrightarrow&LK&\longrightarrow&LK_Z\\
\downarrow&&\downarrow v&&\downarrow\\
K_U&\longrightarrow&K&\longrightarrow&K_Z.
\end{array}
$$

Since it includes the homotopy, it is a morphism of filtered objects in the
sense required by the filtered assertion.

*The two graded maps.* Let $C_U=c_2^{-1}(U)$ and
$C_Z=(c_1^{-1}(Z))_{\mathrm{red}}$. By the invariance hypothesis, both legs of
$C_U$ land in $U$ and both legs of $C_Z$ land in $Z$. Base change and
composition give

$$
LK_U\simeq j_!Rc_{1U!}c_{2U}^*j^*K,
\qquad i^*LK\simeq Rc_{1Z!}c_{2Z}^*i^*K.
$$

The open graded map is $j_!$ of the adjoint restriction of $LK_U\to K$. The
restricted closed map is exactly

$$
Rc_{1Z!}c_{2Z}^*i^*K\simeq i^*LK
\xrightarrow{i^*v}i^*K.
$$

Nilpotent invariance justifies using the reduced fiber in this base-change
identity. Let $q:C_Z\hookrightarrow C$ be the closed immersion and
$M=i^*K\in\Dctf(Z,A)$. The proper pushforward along $(i,q)$ of the
correspondence on $(Z,M)$ adjoint to this map has ordinary half

$$
c_2^*Ri_*M\xrightarrow{\eta_q}
Rq_*q^*c_2^*Ri_*M
=Rq_*c_{2Z}^*i^*Ri_*M
\xrightarrow{Rq_*c_{2Z}^*\varepsilon_i}Rq_*c_{2Z}^*M
$$

and exceptional half $Rq_*c_{1Z}^!M\to c_1^!Ri_*M$ adjoint to

$$
Rc_{1!}Rq_*c_{1Z}^!M
=Ri_*Rc_{1Z!}c_{1Z}^!M\xrightarrow{Ri_*\varepsilon_{c_{1Z}}}Ri_*M.
$$

Taking $i^*$, using $i^*LK_U=0$ and then the displayed base-change identity
turns these halves into the closed graded map above, and adjunction
$i^*\dashv Ri_*$ characterizes the map so obtained. Applying the filtered
assertion proves the open–closed formula. Restricting the formula to a proper
open-and-closed fixed component and integrating gives additivity of its local
term.

*Complement (graph correspondences).* The three coefficient morphisms form a
morphism of the distinguished triangle attached to the open–closed
decomposition, compatibly with the two functors $Lc_2^*$ and $Rc_1^!$.
Triangle compatibility of the trace class then gives the identity for the
classes themselves, in the group of maps $A_F\to\omega_F$ on the fixed scheme.
Since the fixed scheme is proper with finitely many clopen components and
integration is $A$-linear by [sk-d-integral], the identity descends to the
local terms component by component. No invertibility of the coefficient
morphisms is used: only exactness and the formal laws of the trace enter.
