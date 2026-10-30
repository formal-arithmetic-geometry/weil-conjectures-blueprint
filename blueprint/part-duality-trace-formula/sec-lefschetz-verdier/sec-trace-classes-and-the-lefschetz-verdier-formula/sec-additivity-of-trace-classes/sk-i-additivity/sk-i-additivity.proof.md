+++
kind = "proof"
of = "sk-i-additivity"
uses = ["sk-d-integral", "sk-thm-sf-kunneth-verdier", "sk-d-proper-pushforward"]
+++
For the filtered assertion we lift each step of the trace morphism to
filtered complexes and read off its graded piece of weight zero. This
gives the identity of trace classes before integration. For the
assertion on open and closed pieces we construct the filtered correspondence from
the localization triangle and identify its graded pieces.

*Filtered operations.*
We use finite decreasing
filtrations, the convolution filtration on tensor products, and
the filtration on internal Hom given by

$$
F^r\mathcal Hom(\mathcal M,\mathcal N)
=\{v:v(F^a\mathcal M)\subset F^{a+r}\mathcal N
\text{ for every }a\}.
$$

These operations are derived using filtered flat and filtered injective
resolutions; for finite filtrations, such resolutions can be built
successively on the graded pieces by mapping cylinders. This gives the
identities

$$
\begin{aligned}
\operatorname{gr}^r\cHom_F(\mathcal M,\mathcal N)
&\simeq\bigoplus_a\cHom(M_a,N_{a+r}),\\
\operatorname{gr}^r\mathbb D_F\mathcal K&\simeq \mathbb D_XK_{-r},\\
\operatorname{gr}^r(\mathcal M\otimes_F\mathcal N)
&\simeq\bigoplus_{a+b=r}M_a\otimes^{\mathbf L} N_b.
\end{aligned}
$$

Give $\omega_X$ its filtration concentrated in weight zero.
The evaluation
$\mathcal K\otimes_F\mathbb D_F\mathcal K\to\omega_X$ on the
weight-zero summand $K_a\otimes^{\mathbf L} \mathbb D_XK_a$ is ordinary evaluation,
because evaluation is the tensor–Hom adjoint of
$\operatorname{id}_{\mathcal K}$, whose graded map is
$\operatorname{id}_{K_a}$. The Koszul signs are those of the
underlying complexes, and the filtration weights contribute no signs.

*The trace morphism on filtered complexes.*
The four steps defining
the trace morphism lift to filtered complexes:

$$
\cHom_F(c_2^*\mathcal K,c_1^!\mathcal K)
\simeq c^!(\mathcal K\boxtimes_F\mathbb D_F\mathcal K)
\longrightarrow Ri_{c*}\omega_{\Fix(c)}[\text{weight }0].
$$

These steps are the exceptional tensor–Hom adjunction, external
duality, the adjoint of evaluation along the diagonal, and exceptional
proper base change for the closed diagonal. Each is defined by
filtered units, counits and tensor evaluation, and on
graded pieces we recover their unfiltered versions. In particular, the
filtered comparison for external duality is an isomorphism, because each of its
graded maps is a finite sum of the isomorphisms in
Lemma [sk-thm-sf-kunneth-verdier], and graded pieces detect
isomorphisms of finite filtered complexes. Forgetting the
filtration, we recover exactly the trace morphism defined before.

Its map in weight zero has source

$$
\bigoplus_a\cHom(c_2^*K_a,c_1^!K_a),
$$

and its restriction to summand $a$ is
$\operatorname{Tr}_{c,K_a}$. Indeed, the steps for internal Hom and
external duality preserve the two indices, while evaluation along the
diagonal on a pair of equal indices is the evaluation checked above. The section
defined by $\tilde u$ comes from the unit in weight zero, and hence
lands in $F^0$ of the source. The trace map on $F^1$ is zero,
since its target is pure of weight zero. Therefore its restriction to $F^0$
factors through $\operatorname{gr}^0$, where the
section is the tuple $(u_a)_a$. This factorization holds
on filtered dg models, so it survives localization, and it proves
the stated sum in $H^0(\Fix(c),\omega_{\Fix(c)})$.

*The filtration by the open and the closed piece.*
Let $\Theta=Rc_{1!}c_2^*:D^b_{\mathrm{ctf}}(X,A)\to D^b_{\mathrm{ctf}}(X,A)$, and let
$\widehat u:\Theta K\to K$ be the exceptional adjoint of $u$. By the hypothesis
$c_1^{-1}(Z)\subset c_2^{-1}(Z)$, base change of $Rc_{1!}$ along $i$,
and the adjunction $i^*\dashv Ri_*$, we have

$$
i^*\Theta K_U=0,\qquad
R\operatorname{Hom}_X(\Theta K_U,K_Z)
\simeq R\operatorname{Hom}_Z(i^*\Theta K_U,i^*K)=0.
$$

The second vanishing is that of the whole mapping complex, including
all shifts. Consequently, $\Theta K_U\to \Theta K\xrightarrow{\widehat u}K$ factors through
$K_U\to K$, with a contractible space of choices, and the coherent
cofibre of this factorization is a morphism of two-step filtered objects

$$
\begin{array}{ccccc}
\Theta K_U&\longrightarrow&\Theta K&\longrightarrow&\Theta K_Z\\
\downarrow&&\downarrow \widehat u&&\downarrow\\
K_U&\longrightarrow&K&\longrightarrow&K_Z.
\end{array}
$$

Since it includes the homotopy, it is a morphism of filtered objects
in the sense required by the filtered assertion.

*The two graded maps.*
Let
$C_U=c_2^{-1}(U)$ and $C_Z=(c_1^{-1}(Z))_{\mathrm{red}}$.
By the invariance hypothesis, both legs of $C_U$ land in $U$ and
both legs of $C_Z$ land in $Z$.
By base change, composition and nilpotent invariance (which lets us use
the reduced fibre $C_Z$),

$$
\Theta K_U\simeq j_!Rc_{1U!}c_{2U}^*j^*K,
\qquad i^*\Theta K\simeq Rc_{1Z!}c_{2Z}^*i^*K.
$$

The graded map on the open piece is $j_!$ of the map adjoint to the restriction of
$\Theta K_U\to K$. The graded map on the closed piece, restricted to $Z$, is exactly

$$
Rc_{1Z!}c_{2Z}^*i^*K\simeq i^*\Theta K
\xrightarrow{i^*\widehat u}i^*K.
$$

Let $i':C_Z\hookrightarrow C$ be the closed immersion and
$M=i^*K\in D^b_{\mathrm{ctf}}(Z,A)$. The proper pushforward along $(i,i')$ of the
correspondence on $(Z,M)$ adjoint to this map is built from the maps $\alpha$
and $\beta$ of Definition [sk-d-proper-pushforward], which here are

$$
c_2^*Ri_*M\xrightarrow{\eta_{i'}}
Ri'_*i'^*c_2^*Ri_*M
=Ri'_*c_{2Z}^*i^*Ri_*M
\xrightarrow{Ri'_*c_{2Z}^*\varepsilon_i}Ri'_*c_{2Z}^*M
$$

and $Ri'_*c_{1Z}^!M\to c_1^!Ri_*M$ adjoint to

$$
Rc_{1!}Ri'_*c_{1Z}^!M
=Ri_*Rc_{1Z!}c_{1Z}^!M\xrightarrow{Ri_*\varepsilon_{c_{1Z}}}Ri_*M.
$$

After taking $i^*$ and using $i^*\Theta K_U=0$ and the displayed base change
identity, these two maps give the graded map on the closed piece above. Since a
map into $Ri_*M$ is determined by its adjoint under $i^*\dashv Ri_*$, the
pushforward of this correspondence is the induced correspondence $u_Z$ on
$K_Z$.
The filtered assertion now gives the formula for the open and
the closed piece. Restricting the formula to a proper open and closed part of the
fixed locus, and integrating, we get additivity of its local term.
