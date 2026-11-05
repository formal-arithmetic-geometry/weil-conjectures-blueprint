+++
kind = "proof"
of = "theorem-proper-pushforward-lefschetz-verdier"
order = 927
uses = ["theorem-comparison-direct-images", "definition-pro-etale-base-change-map", "definition-projection-formula-map", "proposition-proper-direct-image-constructible-complexes", "lemma-change-coefficients", "proposition-ordinary-external-kunneth", "definition-verdier-dual-evaluation", "proposition-properties-trace", "lemma-external-duality-trace-morphism", "definition-trace-morphism", "lemma-local-terms-point", "lemma-passing-schematic-closure"]
+++
The trace class of $u$ is built in three steps: $u$ becomes a map into
$P_X=K\boxtimes\mathbb D_XK$, evaluation maps $P_X$ to the
dualizing complex on the diagonal, and $c^!$ moves the result to
the fixed locus. We check that each step commutes with pushforward. For the first two steps this means identifying the map adjoint to $u'$ with the
pushforward of the map adjoint to $u$, and evaluation for $K'$ with the
pushforward of evaluation for $K$. The third step needs more care. The squares $c'_ig=fc_i$ are only required to commute, so in general $\Fix(c)\ne C\times_{C'}\Fix(c')$, and we compare the two fixed loci through an intermediate scheme.

*Maps into $P$.* Put $P_Y=K'\boxtimes \mathbb D_YK'$, and
let $\tau_f:Rf_*\omega_X\to\omega_Y$ be the counit.
By the Künneth formula for the proper map $f\times f$ and the exchange
$\mathbb D_YRf_*\simeq Rf_*\mathbb D_X$ of Verdier duality, we obtain an isomorphism

$$
\rho_f:R(f\times f)_*P_X\xrightarrow{\sim}P_Y.
$$

A cohomological correspondence $u$ defines a map
$\theta_u:Rc_!A_C\to P_X$, obtained by exceptional adjunction from the
section $A_C\to c^!P_X$. Under
$Rc'_!Rg_*\simeq R(f\times f)_*Rc_!$, the map defined by the pushforward $u'$ is

$$
\theta_{u'}=
\rho_f\,R(f\times f)_*\theta_u\,
(Rc'_!Rg_*\simeq R(f\times f)_*Rc_!)\,Rc'_!\eta_g.
$$

To verify this identity, we apply tensor–Hom adjunction and then the
exceptional adjunction for $c'_1$. After this both sides become
$Rc'_{1!}\alpha$, followed by $Rf_*Rc_{1!}u$ and
$Rf_*\varepsilon_{c_1}$. The two sides use the projection formulas
for $c_1$ and for $c'_1$ in different orders, but they agree because
$c'_1g=fc_1$ and projection formulas are compatible with composition.

*Evaluation.* Evaluation is compatible with $\rho_f$, in the sense that

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

*Fixed loci.* The two maps into $P_Y$ and the two evaluations therefore
match. The trace classes, however, live on two different fixed loci, and we
must see that passing from $\Fix(c)$ to $\Fix(c')$
is the map $h_*$ of Definition [definition-pushforward-correspondence].
Recall that the fixed loci are the pullbacks of the diagonals,
$\Fix(c)=C\times_{X\times X}X$ and $\Fix(c')=C'\times_{Y\times Y}Y$.
To compare them, we factor $h$ through the fibre product $C\times_{C'}\Fix(c')$:

$$
\Fix(c)\xrightarrow{i'}C\times_{C'}\Fix(c')\xrightarrow{\pi}\Fix(c'),
$$

where the closed immersion $i'$ is the pullback of $X\to X\times_YX$ and $\pi$
is the base change of $g$. We use proper base change for the
square defining $C\times_{C'}\Fix(c')$, and the exceptional counit for $i'$.
Since counits are compatible with composition, the integration map for $h$ is
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

Taking the $i_{c'}^*$-adjoint by means of the identity of composite units
$Rg_*\eta_{i_c}\,\eta_g=Ri_{c'*}\eta_h\,\eta_{i_{c'}}$, we obtain the
first formula (compare
[sga5, III, Theorem 4.4 and Corollary 4.7]).

*The trace formula.* For proper $X$ and $C$, we push forward to the identity correspondence on $s$, using
$f=a_X$ and $g=a_C$. Then the pushed cohomological correspondence is $T_c(u)$.
Indeed, for $g=a_C$ the map $\alpha$ is the pullback
$R\Gamma(X,K)\to R\Gamma(C,c_2^*K)$ and $\beta$ is the counit of
$c_1$ after $R\Gamma$, and these are the outer arrows in the definition of
$T_c(u)$. Moreover, the fixed locus of the identity correspondence of $s$ is $s$ itself. Hence the left side of the first formula is the local term of
$T_c(u)$ on $s$, which by Lemma [lemma-local-terms-point] is the
trace of $T_c(u)$. On the right, $h_*$ is integration over $\Fix(c)$, and since integration over a disjoint union is the sum of the integrations, this
gives the second assertion.
