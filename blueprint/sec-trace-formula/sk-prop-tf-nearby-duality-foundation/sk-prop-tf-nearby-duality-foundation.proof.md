+++
kind = "proof"
of = "sk-prop-tf-nearby-duality-foundation"
uses = ["sk-prop-tf-nearby-external-kunneth", "sk-lem-tf-nearby-mate-coherences", "sk-lem-pd-generic-restriction"]
+++
We work on the classical étale site and use the exchanges $\chi_f$, $\nu_f$, $\beta_f$
of [sk-lem-tf-nearby-mate-coherences]; recall that $\beta_f$ is the exceptional adjoint
of $Rf_{s!}S_Vf_\eta^!\xrightarrow{\nu_f}S_WRf_{\eta!}f_\eta^!\xrightarrow{S_W\varepsilon_{f_\eta}}S_W$
and that $\nu_f=\chi_f^{-1}$ for proper $f$.

As for [sk-prop-tf-nearby-external-kunneth], global duality
kills the global sections of the cone of $\delta$ for projective $X$,
and generic slicing with induction on dimension shows that the cone has
finite support. The two compatibilities that this argument needs, of
$\delta$ with proper direct image and with generic slicing, take up most
of the proof; the slicing compatibility is where the twist $A(1)[2]$
has to be tracked on both fibres.

*Proper direct image and its normalization.*
For proper $f:X\to Y$, proper exchange and the ordinary Verdier
duality of the section on Poincaré duality identify

$$
 Rf_{s*}\delta_{X,M}\quad\text{with}\quad
 \delta_{Y,Rf_{\eta*}M}.
 \tag{2}
$$

Under proper Verdier
duality, evaluation on $Rf_{\eta*}M$ is the composite of the lax
product of $Rf_{\eta*}$, $Rf_{\eta*}\operatorname{ev}_M$, and the
trace $Rf_{\eta*}\omega_{X_\eta}\to\omega_{Y_\eta}$.
Thus, after taking tensor–Hom adjoints, both sides of
(2) are the pairing

$$
\begin{aligned}
 Rf_{s*}S_XM\otimes Rf_{s*}S_X\mathbb D M
 &\xrightarrow{\chi_f^{-1}\otimes\chi_f^{-1}}
 S_YRf_{\eta*}M\otimes S_YRf_{\eta*}\mathbb DM\xrightarrow{\mu_Y}
 S_Y(Rf_{\eta*}M\otimes Rf_{\eta*}\mathbb DM)\\
 &\longrightarrow S_YRf_{\eta*}(M\otimes \mathbb DM)
 \longrightarrow S_YRf_{\eta*}\omega_{X_\eta}
 \longrightarrow S_Y\omega_{Y_\eta}
 \xrightarrow{\theta_Y}\omega_{Y_s}.
\end{aligned}
$$

To identify the pairing obtained from $Rf_{s*}\delta_{X,M}$ with this
one, commute the lax products through proper exchange and use the identity

$$
 \theta_X=f_s^!\theta_Y\circ\beta_f(\omega_{Y_\eta})
$$

of [sk-lem-tf-nearby-mate-coherences].
The first identity follows by taking ordinary adjoints, since both
maps become the tensor product of the two generic-open counits.
The second follows by taking exceptional adjoints and composing the
two compact-support counits. This proves
(2). The same description shows that
$\delta$ restricts to its corresponding map on an open subset, because
nearby smooth exchange is an isomorphism for an open immersion and
$j^!=j^*$.

In particular, if $X$ is proper over $S$, proper exchange for $a$ and
global Verdier duality identify

$$
 R\Gamma(X_s,\delta_{X,M})
 \quad\text{with the identity of}\quad
 R\operatorname{Hom}_A(R\Gamma(X_{\bar\eta},M),A).
 \tag{3}
$$

This also follows from (2) for $a$:
nearby cycles on the trait itself are the underlying geometric-generic
complex, and their normalized pairing is ordinary evaluation.

*The duality shift in a generic slice.*
Let $b:X\to\mathbf A^1_S$ be a coordinate map and let
$S'=(\mathbf A^1_S)_{(s')}$ be the strict localization of $\mathbf A^1_S$ at a geometric
generic point $s'$ of the special fibre $\mathbf A^1_k$, the trait used in the
generic-slicing identification
$(R\Psi_{W/S}N)|_{W_s\times_{\mathbf A^1_k}s'}\simeq(R\Psi_{W'/S'}N')^P$ of the proof of
[sk-prop-tf-nearby-external-kunneth]. Put $X'=X\times_{\mathbf A^1_S}S'$,
$M'=M|_{X'_{\bar\eta'}}$, and write $g_s,g_\eta$ for the two
geometric generic-coordinate pullbacks. Let $P$ be the pro-$p$ kernel
in the generic-slicing calculation.
The group $P$ acts trivially on $A(1)[2]$: roots of unity of order prime to
the residue characteristic lift over a strictly henselian trait.
Geometric generic restriction, including internal Hom, gives

$$
 g_\eta^*\mathbb D_{X_{\bar\eta}}M\simeq \mathbb D_{X'_{\bar\eta'}}M'\otimes A(1)[2],
 \qquad
 g_s^*\mathbb D_{X_s}E\simeq \mathbb D_{X'_{s'}}(g_s^*E)\otimes A(1)[2].
 \tag{4}
$$

This is Lemma [sk-lem-pd-generic-restriction] applied on each geometric
fibre. Its origin can also be seen locally by a closed embedding over
$\mathbf A^1$ into $\mathbf A^r_{\mathbf A^1}$: smooth purity gives
$A(r+1)[2r+2]$ before generic restriction and $A(r)[2r]$ after it;
the closed-support comparison for the embedding preserves evaluation.
Thus the factor $A(1)[2]$ occurs on both fibres, and the comparison below
keeps it on both.

For a bounded constructible complex $E$ of finite Tor dimension with continuous
$P$-action on a fixed special fibre there is a natural comparison

$$
 (\mathbb DE)^P\xrightarrow{\sim}\mathbb D(E^P).
 \tag{5}
$$

For a finite $p$-group quotient, invariants are the image of the
idempotent $e=|P|^{-1}\sum_{h\in P}h$. Verdier duality sends this
idempotent to the same averaging idempotent on the contragredient
action, since inversion permutes the summands. Its image is therefore
the dual of $\operatorname{im}e$. Exactness of invariants and
continuity give the assertion for a pro-$p$ group. The resulting
pairing is the restriction of evaluation to the two invariant direct
summands.

Under the generic-slicing identifications and
(4), the restriction of $\delta$
is

$$
 g_s^*\delta_{X,M}
 \ =\ (\delta_{X',M'})^P\otimes A(1)[2],
 \tag{6}
$$

where the target is identified using
(5). The slicing calculation is obtained
by factoring the geometric-generic inclusion and composing its
direct-image adjunctions. It therefore takes the lax product and
evaluation in (1) to the corresponding
pairing on the slice, restricted to $P$-invariants. The dualizing
map $\theta$ has the same compatibility. To check this, embed $X$, locally over
$\mathbf A^1_S$, as a closed subscheme of
$\mathbf A^r_{\mathbf A^1_S}$. On $\mathbf A^r_{\mathbf A^1_S}$ and its slice, smooth purity
and smooth nearby exchange identify $\theta$ with the identity of
the smooth dualizing complex. Their identifications differ by $A(1)[2]$
as just calculated. For the closed embedding $i:X\hookrightarrow\mathbf A^r_{\mathbf A^1_S}$,
the definition of $\beta_i$ says that $\theta_X$ is uniquely specified
by the pairing obtained after $Ri_{s*}$ and the exceptional counit
$Ri_{s*}i_s^!\to1$. Proper nearby exchange and the slicing
factorization commute with this counit: their ordinary adjoints are
the same composite of the generic-open counit and the counit for $i$.
The evaluation-compatible generic restriction for $i^!$ then gives the
assertion on $X$. The exceptional pullback $i_{s'}^!$ commutes with
$R\Gamma(P,-)$, since both preserve limits; equivalently it preserves
the averaging direct summand. Thus the same closed-embedding check
applies after taking $P$-invariants.
This gives the compatibility of $\theta$. Together with the
self-duality of the averaging projector, it proves
(6). The even shift $[2]$ introduces
no additional Koszul sign.

*Dimension induction.*
Induct, for all traits $S$ as above, on
$n=\dim X_{\bar\eta}$. Open locality allows a projective
compactification and extension of $M$ by zero on its generic fibre.
Proper compatibility for the closure of that generic fibre, and
nilpotent invariance, allow us to assume that $X$ is projective,
reduced, and flat over $S$. These reductions do not increase $n$.
Let $C$ be the cone of $\delta_{X,M}$. It is bounded constructible
by the finiteness theorem for nearby cycles and ordinary Verdier duality, and
(3) gives $R\Gamma(X_s,C)=0$.

As in the proof of [sk-prop-tf-nearby-external-kunneth], work on neighbourhoods with a
quasi-finite relative coordinate map $X\to\mathbf A^q_S$, where
$q\leq n$. For $q>0$ take the generic slice in any one coordinate.
Its generic-fibre dimension is at most $q-1<n$, so induction and
(6) show that $C$ restricts to
zero over that generic special-fibre coordinate. Its constructible
support therefore projects to only finitely many closed points of
that coordinate line. Repeat for all $q$ coordinates. The support
is contained in the inverse image of a finite product of finite
sets, hence is finite because the coordinate map is quasi-finite.
If $q=0$, that finiteness already holds. A finite cover proves that
$C$ has finite support on $X_s$.

This also supplies the base case $n=0$. A bounded constructible
complex supported on finitely many closed geometric points is the
closed direct image of its stalk complexes; global sections are
their finite direct sum and detect vanishing. Thus
$R\Gamma(X_s,C)=0$ forces $C=0$. This closes the induction and
proves the proposition. Finally the finite constructible comparison
transports both the pairing and this isomorphism to the small
pro-étale site.
