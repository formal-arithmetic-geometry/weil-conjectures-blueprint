+++
kind  = "proof"
of    = "sk-p-proper"
uses  = ["sk-d-proper-pushforward", "sk-p-pairing", "sk-thm-sf-kunneth-verdier"]
+++
The squares $b_ig=fc_i$ are only required to commute, so in general
$F_c\ne C\times_DF_b$; this is why the proof compares the fixed loci through an
intermediate scheme.

The proof identifies the kernel class of $u'$ with the pushforward of the
kernel class of $u$, checks that evaluation is compatible with pushforward, and
finally compares the fixed loci; together these identify the two trace
classes.

Trace compatibility is a calculation on the diagonal. Let $P_X=K\boxtimes\mathbb D_XK$
and $e_K:P_X\to R\Delta_{X*}\omega_X$ be as in [sk-thm-sf-kunneth-verdier]. Put $q=f\times f$,
$P_Y=K'\boxtimes \mathbb D_YK'$ and let $\tau_f:Rf_*\omega_X\to\omega_Y$ be the
counit. Proper Verdier duality and proper Künneth identify

$$
\rho_f:Rq_*P_X\xrightarrow{\sim}P_Y.
$$

A cohomological correspondence $u$ has a kernel class $[u]_P:Rc_!A_C\to P_X$,
obtained by exceptional adjunction from the section $A_C\to c^!P_X$. Under
$Rb_!Rg_*\simeq Rq_*Rc_!$, the class of the pushforward is

$$
[u']_P=
\rho_f\,Rq_*[u]_P\,
(Rb_!Rg_*\simeq Rq_*Rc_!)\,Rb_!\eta_g.
$$

To verify this identity, apply tensor–Hom adjunction and then the exceptional
adjunction for $b_1$. Both sides become $Rb_{1!}\gamma$, followed by
$Rf_*Rc_{1!}u$ and $Rf_*\varepsilon_{c_1}$; the projection formulas combine by
their composition compatibility. Evaluation is compatible with $\rho_f$:

$$
e_{K'}\rho_f=
R\Delta_{Y*}\tau_f\,Rq_*e_K,
\qquad q\Delta_X=\Delta_Yf.
$$

After restricting to the diagonal and taking tensor–Hom adjoints, this asserts
that proper Verdier duality identifies evaluation against $Rf_*K$ with
pushforward of evaluation against $K$, followed by $\tau_f$; this is the
defining counit normalization of that duality.

The fixed loci are the separate Cartesian diagonal pullbacks
$F_c=C\times_{X\times X}X$ and $F_b=D\times_{Y\times Y}Y$. For their comparison
put $E=C\times_DF_b$. The map $h$ factors as

$$
F_c\xrightarrow{a}E\xrightarrow{\pi}F_b,
$$

where $a$ is the closed pullback of $X\to X\times_YX$ and $\pi$ is the proper
base change of $g$. Use proper base change for the square defining $E$, and the
exceptional counit for $a$. Composition of counits identifies the resulting
integration with $\tau_h=\tau_\pi R\pi_*\tau_a$. Applying the two kernel
identities with these specified exchanges identifies the map
$A_D\to Ri_{b*}\omega_{F_b}$ defining the left-hand trace with

$$
A_D\xrightarrow{\eta_g}Rg_*A_C
\longrightarrow Rg_*Ri_{c*}\omega_{F_c}
=Ri_{b*}Rh_*\omega_{F_c}
\xrightarrow{Ri_{b*}\tau_h}Ri_{b*}\omega_{F_b}.
$$

In taking the $i_b^*$-adjoint, use the composite-unit identity
$Rg_*\eta_{i_c}\,\eta_g=Ri_{b*}\eta_h\,\eta_{i_b}$. This proves the first
formula; compare (SGA 5, III, Theorem 4.4 and Corollary 4.7).

For proper $X,C$ push to the point correspondence on $s$, using $f=a_X$ and
$g=a_C$. The pushed cohomological correspondence is $T_c(u)$.
Lemma [sk-p-pairing] identifies its local term with its categorical trace, and
$h_*$ is integration over $F_c$. Integration over a disjoint union is the sum
of integrations, proving the second assertion.
