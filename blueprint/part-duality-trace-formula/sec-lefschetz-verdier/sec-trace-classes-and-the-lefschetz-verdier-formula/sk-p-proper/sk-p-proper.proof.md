+++
kind = "proof"
of = "sk-p-proper"
uses = ["sk-d-proper-pushforward", "sk-p-pairing", "sk-thm-sf-kunneth-verdier"]
+++
We identify the map $Rc'_!A_{C'}\to P_Y$ adjoint to $u'$ with the
pushforward of the map adjoint to $u$, check that evaluation is
compatible with pushforward, and finally compare the fixed loci.
Together these steps identify the two trace classes. Since the squares
$c'_ig=fc_i$ are only required to commute, in general
$\Fix(c)\ne C\times_{C'}\Fix(c')$, and we compare the fixed loci
by means of an intermediate scheme.

We first show that pushforward is compatible with these adjoint maps and
with evaluation. Put $P_Y=K'\boxtimes \mathbb D_YK'$, and
let $\tau_f:Rf_*\omega_X\to\omega_Y$ be the counit.
By the Künneth formula for the proper map $f\times f$ and the exchange
$\mathbb D_YRf_*\simeq Rf_*\mathbb D_X$ of Verdier duality, we obtain an isomorphism

$$
\rho_f:R(f\times f)_*P_X\xrightarrow{\sim}P_Y.
$$

A cohomological correspondence $u$ defines a map
$\theta_u:Rc_!A_C\to P_X$, obtained by exceptional adjunction from the
section $A_C\to c^!P_X$. Under
$Rc'_!Rg_*\simeq R(f\times f)_*Rc_!$, the map defined by the pushforward is

$$
\theta_{u'}=
\rho_f\,R(f\times f)_*\theta_u\,
(Rc'_!Rg_*\simeq R(f\times f)_*Rc_!)\,Rc'_!\eta_g.
$$

To verify this identity, apply tensor–Hom adjunction and then the
exceptional adjunction for $c'_1$. Both sides become
$Rc'_{1!}\alpha$, followed by $Rf_*Rc_{1!}u$ and
$Rf_*\varepsilon_{c_1}$. Here the two sides use the projection formulas
for $c_1$ and for $c'_1$ in different orders, and these agree because
$c'_1g=fc_1$ and projection formulas are compatible with composition.
Evaluation is compatible with $\rho_f$, that is,

$$
e_{K'}\rho_f=
R\Delta_{Y*}\tau_f\,R(f\times f)_*e_K,
\qquad (f\times f)\Delta_X=\Delta_Yf.
$$

After restricting to the diagonal and taking tensor–Hom
adjoints, this says that Verdier duality for the proper map $f$ identifies
evaluation against $Rf_*K$ with the pushforward of evaluation against
$K$, followed by $\tau_f$. This holds because that duality is defined
by means of the counit $\tau_f$.

The fixed loci are the pullbacks of the diagonals, namely
$\Fix(c)=C\times_{X\times X}X$ and $\Fix(c')=C'\times_{Y\times Y}Y$, each defined
by its own cartesian square.
To compare them, we factor $h$ through the fibre product $C\times_{C'}\Fix(c')$:

$$
\Fix(c)\xrightarrow{i'}C\times_{C'}\Fix(c')\xrightarrow{\pi}\Fix(c'),
$$

where the closed immersion $i'$ is the pullback of $X\to X\times_YX$ and $\pi$
is the base change of $g$. We use proper base change for the
square defining $C\times_{C'}\Fix(c')$, and the exceptional counit for $i'$.
By composition of counits, the resulting integration is
$\tau_h=\tau_\pi R\pi_*\tau_{i'}$.
Applying the identity for $\theta_{u'}$ and the compatibility of
evaluation, together with these base change maps, we identify the map
$A_{C'}\to Ri_{c'*}\omega_{\Fix(c')}$ defining the left-hand trace with

$$
A_{C'}\xrightarrow{\eta_g}Rg_*A_C
\longrightarrow Rg_*Ri_{c*}\omega_{\Fix(c)}
=Ri_{c'*}Rh_*\omega_{\Fix(c)}
\xrightarrow{Ri_{c'*}\tau_h}Ri_{c'*}\omega_{\Fix(c')}.
$$

To take the $i_{c'}^*$-adjoint, we use the identity of composite units
$Rg_*\eta_{i_c}\,\eta_g=Ri_{c'*}\eta_h\,\eta_{i_{c'}}$.
This proves the first formula (compare
(SGA5, III, Theorem 4.4 and Corollary 4.7)).

For proper $X$ and $C$, we push forward to the identity correspondence on $s$, using
$f=a_X$ and $g=a_C$. The pushed cohomological correspondence is $T_c(u)$.
Lemma [sk-p-pairing] identifies its local term with its
categorical trace, and $h_*$ is integration over $\Fix(c)$. Since integration
over a disjoint union is the sum of the integrations, the second
assertion follows.
