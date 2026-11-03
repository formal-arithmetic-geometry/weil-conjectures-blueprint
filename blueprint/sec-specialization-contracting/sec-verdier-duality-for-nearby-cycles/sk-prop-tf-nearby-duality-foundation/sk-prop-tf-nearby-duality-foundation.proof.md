+++
kind = "proof"
of = "sk-prop-tf-nearby-duality-foundation"
uses = ["sk-prop-tf-nearby-external-kunneth", "sk-lem-tf-nearby-mate-coherences", "sk-lem-pd-generic-restriction"]
+++
The argument is the one used for Proposition [sk-prop-tf-nearby-external-kunneth]:
on a projective $X$, global duality shows that the cone of $\delta$ has
zero cohomology on $X_s$, and (E.2) with induction on
dimension shows that it has finite support. We therefore need two
compatibilities of $\delta$, with proper direct image and with restriction
to the generic point of a coordinate line, and in the second we keep track of the twist $A(1)[2]$ on both
fibres.

*Proper direct image.*
For proper $f:X\to Y$, the isomorphism $\chi_f$ and the ordinary
Verdier duality of Section [sec-poincare-duality] identify

$$
Rf_{s*}\delta_{X,M}\quad\text{with}\quad
\delta_{Y,Rf_{\eta*}M}.
\tag{E.14}
$$

Under Verdier duality for the proper map $f_\eta$, evaluation on
$Rf_{\eta*}M$ is the composite of the lax monoidal map of $Rf_{\eta*}$,
the map $Rf_{\eta*}\operatorname{ev}_M$, and the
trace $Rf_{\eta*}\omega_{X_\eta}\to\omega_{Y_\eta}$.
Thus, after taking tensor–Hom adjoints, both sides of
(E.14) are the pairing

$$
\begin{split}
Rf_{s*}\Psi_XM\otimes Rf_{s*}\Psi_X\mathbb D M
&\xrightarrow{\chi_f^{-1}\otimes\chi_f^{-1}}
\Psi_YRf_{\eta*}M\otimes \Psi_YRf_{\eta*}\mathbb DM\xrightarrow{\mu_Y}
\Psi_Y(Rf_{\eta*}M\otimes Rf_{\eta*}\mathbb DM)\\
&\longrightarrow \Psi_YRf_{\eta*}(M\otimes \mathbb DM)
\longrightarrow \Psi_YRf_{\eta*}\omega_{X_\eta}
\longrightarrow \Psi_Y\omega_{Y_\eta}
\xrightarrow{\theta_Y}\omega_{Y_s}.
\end{split}
$$

To identify the pairing obtained from $Rf_{s*}\delta_{X,M}$ with this
one, we move the lax monoidal maps past the base change maps for proper
morphisms, and we use the identity
$\theta_X=f_s^!\theta_Y\circ\beta_f(\omega_{Y_\eta})$ of
(E.9).
The compatibility of the lax monoidal maps with the base change maps
follows by taking ordinary adjoints, since both maps become the tensor
product of the two counits for the open immersions of the generic
fibres. This proves (E.14).

The same description shows that the restriction of $\delta$ to an open subset is the
corresponding map there, because the base change map of nearby cycles for
smooth pullback is an isomorphism for an open immersion and $j^!=j^*$.

In particular, suppose that $X$ is proper over $S$, and apply
(E.14) to the structure morphism $a$. On
the trait, $\Psi_S$ takes the stalk at the geometric generic point and the
pairing (E.13) is ordinary evaluation.
Together with global Verdier duality on both fibres, this identifies

$$
R\Gamma(X_s,\delta_{X,M})
\quad\text{with the identity of}\quad
R\operatorname{Hom}_A(R\Gamma(X_{\bar\eta},M),A).
\tag{E.15}
$$

*Duality and restriction to the generic point of a line.*
Let $b:X\to\mathbf A^1_S$ be a coordinate map and let
$S'=(\mathbf A^1_S)_{(s')}$ be the trait at the generic point of the
special fibre used in (E.2). Set
$X'=X\times_{\mathbf A^1_S}S'$, $M'=M|_{X'_{\bar\eta'}}$, and write
$g_s,g_\eta$ for the two pullbacks to the geometric generic point of
the coordinate line. Let $P$ be the pro-$p$ kernel in
(E.2), and let $L\in D^b_{\mathrm{ctf}}(X_s,A)$.
Restriction to the geometric generic point of the
coordinate line, which is compatible with internal Hom, yields

$$
g_\eta^*\mathbb D_{X_{\bar\eta}}M\simeq \mathbb D_{X'_{\bar\eta'}}M'\otimes A(1)[2],
\qquad
g_s^*\mathbb D_{X_s}L\simeq \mathbb D_{X'_{s'}}(g_s^*L)\otimes A(1)[2].
\tag{E.16}
$$

This is Lemma [sk-lem-pd-generic-restriction] applied on each geometric
fibre. One can also see locally where the twist comes from, using a
closed embedding over $\mathbf A^1$ into $\mathbf A^r_{\mathbf A^1}$:
smooth purity gives $A(r+1)[2r+2]$ before generic restriction
and $A(r)[2r]$ after it, and the comparison of the complexes with
closed support for the embedding preserves evaluation.
In particular, on $\mathbf A^r_{\mathbf A^1_S}$ the identifications of
the dualizing complexes before and after slicing differ by $A(1)[2]$ on
both fibres. Since $P$ acts trivially on $A(1)[2]$ (roots of unity of
order prime to the residue characteristic lift over a strictly
henselian trait), the twist commutes with taking $P$-invariants.

For a bounded constructible complex $L$ of finite Tor dimension with
continuous $P$-action on a fixed special fibre, there is a natural
comparison isomorphism

$$
(\mathbb DL)^P\xrightarrow{\sim}\mathbb D(L^P).
\tag{E.17}
$$

To see this, note that for a finite quotient $G$ of $P$, which is a
$p$-group, the order $|G|$ is invertible in $A$, and the invariants
are the image of the idempotent
$e=|G|^{-1}\sum_{g\in G}g$. Verdier duality sends this idempotent to
the same averaging idempotent for the contragredient action, since
inversion permutes the summands. Therefore its image is the dual of
$\operatorname{im}e$. By exactness of invariants and continuity, we
get the assertion for the pro-$p$ group $P$. The resulting pairing
is the restriction of evaluation to the two direct summands of
invariants.

Under the identifications (E.2) and
(E.16), the restriction of $\delta$
is

$$
g_s^*\delta_{X,M}
\ =\ (\delta_{X',M'})^P\otimes A(1)[2],
\tag{E.18}
$$

where the target is identified using
(E.17). Since the slicing calculation is
obtained by factoring the inclusion of the geometric generic point and
composing the adjunctions for the direct images, it takes
the lax monoidal map and the evaluation in
(E.13) to the corresponding pairing on
the slice, restricted to $P$-invariants.

It remains to treat the last arrow $\theta_X$ of the pairing. We claim
that under (E.2) and
(E.16), the map $g_s^*\theta_X$
corresponds to $(\theta_{X'})^P\otimes A(1)[2]$. We check
this on a smooth ambient space, where $\theta$ is the identity by smooth
purity, and descend along a closed embedding. Since the claim is
local, we may embed $X$ over $\mathbf A^1_S$ as a closed subscheme
$i:X\hookrightarrow\mathbf A^r_{\mathbf A^1_S}$. On
$\mathbf A^r_{\mathbf A^1_S}$ and on its slice, smooth purity and the base change isomorphism of nearby cycles for
smooth pullback identify $\theta$ with
the identity of the dualizing complex of a smooth scheme, and these
identifications differ by $A(1)[2]$, as we have just seen. For $X$, the
identity (E.9) for $i$ gives
$\theta_X=i_s^!\theta_{\mathbf A^r}\circ\beta_i(\omega_{\mathbf A^r_\eta})$,
writing $\mathbf A^r$ for $\mathbf A^r_{\mathbf A^1_S}$. By
(E.6), $\theta_X$ is therefore the adjoint, for
$Ri_{s*}\dashv i_s^!$, of $\nu_i$, followed by $\Psi$ of the exceptional counit
$Ri_{\eta*}i_\eta^!\to1$ and by $\theta_{\mathbf A^r}$. The base change map $\nu_i$ for the proper map $i$
and the factorization used for slicing commute with this counit,
because their ordinary adjoints are the same composite of the counit
for the open immersion of the generic fibre and the counit for $i$.
Since generic restriction is compatible with $i^!$ and with evaluation,
the claim for $\mathbf A^r_{\mathbf A^1_S}$ gives it for $X$ before
taking invariants. For a finite quotient $G$ of $P$, the additive
functor $i_{s'}^!$ commutes with the action of $G$, and hence preserves
the image of the averaging idempotent. Therefore $i_{s'}^!$ commutes
with $(-)^P$, the same descent works after taking $P$-invariants, and
the claim follows. Together with the self-duality of the averaging
idempotent, this proves (E.18). Since
the shift $[2]$ is even, no additional Koszul sign appears.

*Induction on dimension.*
We argue by induction on $n=\dim X_{\bar\eta}$, simultaneously for all
traits $S$ as above. Since the assertion is local and compatible with
restriction to opens, we may pass to a projective compactification and
extend $M$ by zero on its generic fibre. Using the compatibility with
proper direct image for the closure of that generic fibre, and
invariance under nilpotent thickenings, we may assume that $X$ is
projective, reduced, and flat over $S$. These reductions do not
increase $n$. Put $Q=\Cone(\delta_{X,M})$. It is bounded and
constructible by the finiteness theorem for nearby cycles and ordinary
Verdier duality, and by (E.15) we have
$R\Gamma(X_s,Q)=0$.

The support of $Q$ is finite by the argument in the proof of
Proposition [sk-prop-tf-nearby-external-kunneth], with one factor: on a
neighbourhood with a quasi-finite coordinate map $X\to\mathbf A^q_S$,
$q\leq n$, the restriction to the generic point of each coordinate line has generic fibre of
dimension at most $q-1<n$, so the induction hypothesis and
(E.18) show that $Q$ vanishes over the
generic point of each coordinate line of the special fibre. Hence the
support lies over finitely many closed points of each coordinate line,
and it is finite because the coordinate map is quasi-finite; finitely
many such neighbourhoods cover $X_s$. This also covers $n=0$. As there, a
complex with finite support is detected by its global sections, so
$R\Gamma(X_s,Q)=0$ implies $Q=0$.
Finally, the comparison for constructible
complexes with finite coefficients transports both the pairing and
this isomorphism to the small pro-étale site.
