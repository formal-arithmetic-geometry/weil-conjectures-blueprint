+++
kind = "proof"
of = "theorem-proper-pushforward-lefschetz-verdier"
order = 927
uses = ["lemma-integral-models", "lemma-naturality-pasting-comparison", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "definition-kunneth-map", "proposition-ordinary-external-kunneth", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "proposition-properties-trace", "lemma-external-duality-trace-morphism", "definition-trace-morphism", "lemma-local-terms-point", "lemma-kunneth-formula-compact-supports", "theorem-nagata-s-compactification-theorem", "lemma-passing-schematic-closure"]
+++
The [trace class](@definition-trace-class-local-terms) of $u$ is built in three steps: $u$ becomes a map into
$P_X=K\boxtimes\mathbb D_XK$, evaluation maps [$P_X$](@lemma-external-duality-trace-morphism) to the
[dualizing complex](@definition-verdier-dual-evaluation) on the diagonal, and [$c^!$](@theorem-existence-exceptional-inverse-image) moves the result to
the [fixed locus](@definition-correspondence). We check that each step commutes with [pushforward](@definition-pushforward-correspondence). For the first two steps this means identifying the map adjoint to $u'$ with the
pushforward of the map adjoint to $u$, and evaluation for $K'$ with the
pushforward of evaluation for $K$. The third step needs more care. The squares $c'_ig=fc_i$ are only required to commute, so in general $\Fix(c)\ne C\times_{C'}\Fix(c')$, and we compare the two [fixed loci](@definition-correspondence) through an intermediate scheme.

*Maps into $P$.* Put $P_Y=K'\boxtimes \mathbb D_YK'$, and
let $\tau_f:Rf_*\omega_X\to\omega_Y$ be the counit.
By the [Künneth formula](@proposition-ordinary-external-kunneth) for the proper map $f\times f$ and the exchange
$\mathbb D_YRf_*\simeq Rf_*\mathbb D_X$ of [Verdier duality](@lemma-internal-adjunction-two-exchange-formulas), we obtain an isomorphism

$$
\rho_f:R(f\times f)_*P_X\xrightarrow{\sim}P_Y.
$$

A [cohomological correspondence](@definition-correspondence) $u$ defines a map
$\theta_u:Rc_!A_C\to P_X$, obtained by exceptional adjunction from the
section $A_C\to c^!P_X$. Under
$Rc'_!Rg_*\simeq R(f\times f)_*Rc_!$, the map defined by the [pushforward](@definition-pushforward-correspondence) $u'$ is

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
adjoints, this says that [Verdier duality](@lemma-internal-adjunction-two-exchange-formulas) for the proper map $f$ identifies
evaluation against $Rf_*K$ with the pushforward of evaluation against
$K$, followed by $\tau_f$. This holds because that duality is defined
by means of the counit $\tau_f$.

*[Fixed loci](@definition-correspondence).* The two maps into $P_Y$ and the two evaluations therefore
match. The [trace classes](@definition-trace-class-local-terms), however, live on two different [fixed loci](@definition-correspondence), and we
must see that passing from [$\Fix(c)$](@definition-correspondence) to [$\Fix(c')$](@definition-correspondence)
is the map $h_*$ of Definition [definition-pushforward-correspondence].
Recall that the [fixed loci](@definition-correspondence) are the pullbacks of the diagonals,
$\Fix(c)=C\times_{X\times X}X$ and $\Fix(c')=C'\times_{Y\times Y}Y$.
To compare them, we factor $h$ through the fibre product $C\times_{C'}\Fix(c')$:

$$
\Fix(c)\xrightarrow{i'}C\times_{C'}\Fix(c')\xrightarrow{\pi}\Fix(c'),
$$

where the closed immersion $i'$ is the pullback of $X\to X\times_YX$ and $\pi$
is the base change of $g$. We use [proper base change](@theorem-proper-base-change-classical-pro) for the
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

*The trace formula.* For proper $X$ and $C$, we push forward to the identity [correspondence](@definition-correspondence) on $s$, using
$f=a_X$ and $g=a_C$. Then the pushed [cohomological correspondence](@definition-correspondence) is [$T_c(u)$](@definition-action-correspondence).
Indeed, for $g=a_C$ the map $\alpha$ is the pullback
$R\Gamma(X,K)\to R\Gamma(C,c_2^*K)$ and $\beta$ is the counit of
$c_1$ after $R\Gamma$, and these are the outer arrows in the definition of
[$T_c(u)$](@definition-action-correspondence). Moreover, the [fixed locus](@definition-correspondence) of the identity [correspondence](@definition-correspondence) of $s$ is $s$ itself. Hence the left side of the first formula is the [local term](@definition-trace-class-local-terms) of
[$T_c(u)$](@definition-action-correspondence) on $s$, which by Lemma [lemma-local-terms-point] is the
trace of [$T_c(u)$](@definition-action-correspondence). On the right, [$h_*$](@definition-pushforward-correspondence) is [integration](@definition-trace-class-local-terms) over [$\Fix(c)$](@definition-correspondence), and since [integration](@definition-trace-class-local-terms) over a disjoint union is the sum of the [integrations](@definition-trace-class-local-terms), this
gives the second assertion.
